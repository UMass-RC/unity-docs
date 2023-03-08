
# Using a Jupyter notebook

Start by accessing JupyterLab using the Unity OnDemand interface:

[https://ood.unity.rc.umass.edu/pun/sys/dashboard/batch_connect/sys/jupyterlab/session_contexts/new](https://ood.unity.rc.umass.edu/pun/sys/dashboard/batch_connect/sys/jupyterlab/session_contexts/new)

Click on the JupyterLab interactive app and fill out the following fields:

1. For `Partition` choose one of the following: gpu, gpu-long, uri-gpu, gpu-preempt
2. `Maximum job duration`: 1:00:00
3. `Memory (in GB)`: 50
4. `GPU count`: 1
5. `Modules`: cudnn/cuda11-8.4.1.50 cuda/11.4.0

The fields `CPU thread count` and `Extra arguments for Slurm` can be left blank.

Inside JupyterLab:

* Open the ColabFold.ipynb notebook
* Choose Python (colabfold) for the kernel
* Insert your protein sequence next to query_sequence and execute the code in the cell (press SHIFT+ENTER or press the play button in the toolbar above).
* Run the code in the remaining cells in order to predict the protein structure with the default parameters (see below) and output plots and a visualization of the 3D structure.
* The output directory containing the results will be located in the folder where you put the ColabFold.ipynb notebook.

#### Notes:
* Default parameters:
    * No templates
    * Number of models: 5
    * Stop predictions at score 100
    * Msa mode: mmseqs2_uniref_env
    * Model type: alphafold2_ptm
* Running ColabFold on the terminal through SBATCH should be favored with a large number of input protein sequences.


# Using an SBATCH script

## ColabFold on Unity has 3 main components:

* A script **colabfold_search** that searches the ColabFold databases of proteins using MMseqs2 to build diverse multiple sequence alignments in A3M format.
* A script **colabfold_batch** designed to predict protein structures.
* A set of protein databases:
    * **UniRef30**: database containing 30% sequence identity clustered proteins based on UniRef100 non-redundant protein sequence database. 
    * **Environmental database** (also called ColabFoldDB): combination of** **the** **Big Fantastic Database (BFD) and the MGnify database with redundancy reduced in addition to metagenomic protein catalogs containing eukaryotic proteins, phage catalogs and an updated version of MetaClust.
    * **Templates database** (PDB70): database containing 70% sequence identity clustered proteins from the** **Protein Data Bank (PDB) database.

## Getting started
### Search against the ColabFold databases

Finding homologous proteins using MMSeqs2 can be done by running a batch script using the SBATCH command: `sbatch <path to batch script file>`

The code below is an example of a batch script to run MMSeqs2. The top of the script contains the instruction to use bash to execute the commands (`#!/bin/bash`) and the SBATCH parameters (`#SBATCH <parameter>`) followed by the different modules required to run MMSeqs2 through ColabFold.


```
#!/bin/bash
#SBATCH --partition=cpu
#SBATCH --nodes=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=200G
#SBATCH -t 05:00:00
#SBATCH -o slurm-%j.out
#SBATCH -e slurm-%j.err

module load uri
module load MMseqs2/14-7e284-gompi-2021b
module load miniconda
source ~/.bashrc
conda activate colabfold
```


The command colabfold_search shown below is added after activating the conda environment `colabfold-v1.5.0`. In this case, protein sequences contained in a fasta file are aligned against the UniRef30 (`--db1 uniref30_2202/uniref30_2202_db`) and environmental (`--db3 colabfold_envdb_202108/colabfold_envdb_202108_db`) databases. UniRef30 is the default database used to search proteins. In order to use the environmental database, the parameter `--use-env `has to be set to 1 in addition to providing the path (`--db3 colabfold_envdb_202108/colabfold_envdb_202108_db`).


```
colabfold_search <path to fasta file> /datasets/bio/colabfold <path to output directory> --db1 uniref30_2202/uniref30_2202_db --db3 colabfold_envdb_202108/colabfold_envdb_202108_db --use-env 1 --use-templates 0
```


To use the PDB70 templates database, the parameter `--use-templates` should be set to 1 and the path to the database should be provided with `--db2 pdb`.

#### Notes:
* `<path to fasta file>` is the full path to a fasta file containing protein sequence(s) of interest.
* `<path to output directory>` is the full path to an existing directory used to store the multiple sequence alignments (MSAs).
* It is recommended to request at least 200G using `#SBATCH --mem=200G` in order to load the protein databases.
* Running colabfold_search with 1,762 proteins, the UniRef30 and environmental databases and the highest mmseqs sensitivity (s = 8) on a gpu A100 node with 64 threads takes approximately 3h.

### Train models and make predictions

The code below provides an example on how to make predictions using `colabfold_batch` in a batch script:

The parameter --stop-at-score is used to stop generating models until the predicted confidence metric (pLDDT or predicted local distance difference test) is reached.


```
#!/bin/bash
#SBATCH --partition=uri-gpu
#SBATCH --nodes=1
#SBATCH --cpus-per-gpu=16
#SBATCH -mem-per-gpu=80
#SBATCH -t 05:00:00
#SBATCH -o slurm-%j.out
#SBATCH -e slurm-%j.err

module load cudnn/cuda11-8.4.1.50
module load cuda/11.4.0
module load miniconda
source ~/.bashrc

conda activate colabfold

colabfold_batch <path to directory containing MSAs> <path to output directory> --stop-at-score 85 --msa-mode 'MMseqs2 (UniRef+Environmental)'
```

The `colabfold_batch` command above will create the following files in the provided output directory for each input protein sequence:

* `{*}_PAE.png` → 2D plot of the Predicted Aligned Error (PAE) for each of the 5 trained models.

* `{*}_coverage.png` → plot of the coverage of protein sequences to the query protein.

* `{*}_plddt.png` → plot of the pLDDT (predicted local distance difference test) scores for each residue and the 5 trained models.

* `{*}_predicted_aligned_error_v1.json` → raw data with PAE for all residue pairs for each of the 5 trained models.

The next 2 files are generated for the 5 trained models:

* `{*}_unrelaxed_rank_1_model_1.pdb` → PDB format text file containing the predicted structure obtained from model 1.
* `{*}_unrelaxed_rank_1_model_1_scores.json` → raw data with the pLDDT scores for each residue of the protein structure obtained from model 1.


#### Notes:
* `<path to directory containing MSAs>` is the same as `<path to the output directory>` used with the `colabfold_search` command.
* `<path to output directory>` is the full path to an existing directory used to store the results.
* Predictions on proteins longer than 1000bp should be run on a GPU node with at least 40GB VRAM.
* Predictions can be expedited on a large set of input protein sequences by submitting the batch script as an array job.

# Full list of parameters for colabfold_search and colabfold_batch

```
colabfold_search [-h] [-s S] [--db1 DB1] [--db2 DB2] [--db3 DB3]
                        [--use-env {0,1}] [--use-templates {0,1}]
                        [--filter {0,1}] [--mmseqs MMSEQS]
                        [--expand-eval EXPAND_EVAL] [--align-eval ALIGN_EVAL]
                        [--diff DIFF] [--qsc QSC] [--max-accept MAX_ACCEPT]
                        [--db-load-mode DB_LOAD_MODE] [--threads THREADS]
                        query dbbase base
   
  query                 fasta files with the queries.
  dbbase                The path to the database and indices you downloaded
                        and created with setup_databases.sh
  base                  Directory for the results (and intermediate files)
  -s S                  mmseqs sensitivity (1-8). Lowering this will result in a
                        much faster search but possibly sparser msas → default = 8
  --db1 DB1             path to a UniRef database on Unity
  --db2 DB2             path to the Templates database on Unity
  --db3 DB3             path to the Environmental database on Unity
  --use-env {0,1}
  --use-templates {0,1}
  --filter {0,1}
  --mmseqs MMSEQS       Location of the mmseqs binary
  --expand-eval EXPAND_EVAL
  --align-eval ALIGN_EVAL
  --diff DIFF
  --qsc QSC
  --max-accept MAX_ACCEPT
  --db-load-mode DB_LOAD_MODE → default = 0 (batch searches)
  --threads THREADS
```

```
colabfold_batch [-h]   [--stop-at-score STOP_AT_SCORE]
                       [--stop-at-score-below STOP_AT_SCORE_BELOW]
                       [--num-recycle NUM_RECYCLE]
                       [--num-ensemble NUM_ENSEMBLE]
                       [--random-seed RANDOM_SEED] [--num-models {1,2,3,4,5}]
                       [--recompile-padding RECOMPILE_PADDING]
                       [--model-order MODEL_ORDER] [--host-url HOST_URL]
                       [--data DATA]
                       [--msa-mode {MMseqs2 UniRef+Environmental),MMseqs2 (UniRef only,single_sequence}]
                       [--model-type {auto,AlphaFold2-ptm,AlphaFold2-multimer-v1,AlphaFold2-multimer-v2}]
                       [--amber] [--templates]
                       [--custom-template-path CUSTOM_TEMPLATE_PATH] [--env]
                       [--cpu] [--rank {auto,plddt,ptmscore,multimer}]
                       [--pair-mode {unpaired,paired,unpaired+paired}]
                       [--recompile-all-models]
                       [--sort-queries-by {none,length,random}]
                       [--save-single-representations]
                       [--save-pair-representations] [--training]
                       [--max-msa           {512:5120,512:1024,256:512,128:256,64:128,32:64,16:32}]
                       [--zip] [--use-gpu-relax]
                       [--overwrite-existing-results]
                       input results

--stop-at-score STOP_AT_SCORE
                        Compute models until plddt (single chain) or ptmscore
                        (complex) > threshold is reached. This can make
                        colabfold much faster by only running the first model
                        for easy queries.
--stop-at-score-below STOP_AT_SCORE_BELOW → default = 0
                        Stop to compute structures if plddt (single chain) or
                        ptmscore (complex) < threshold. This can make
                        colabfold much faster by skipping sequences that do
                        not generate good scores.
--num-recycle NUM_RECYCLE <strong>→ default = 3</strong>
                        Number of prediction cycles.Increasing recycles can
                        improve the quality but slows down the prediction.
--num-ensemble NUM_ENSEMBLE <strong>→ default = 1</strong>
                        Number of ensembles.The trunk of the network is run
                        multiple times with different random choices for the
                        MSA cluster centers.
--random-seed RANDOM_SEED <strong>→ default = 0</strong>
                        Changing the seed for the random number generator can
                        result in different structure predictions.
--num-models {1,2,3,4,5} <strong>→ default = 5</strong>
--recompile-padding RECOMPILE_PADDING <strong>→ default = 1.1</strong>
                        Whenever the input length changes, the model needs to
                        be recompiled, which is slow. We pad sequences by this
                        factor, so we can e.g. compute sequence from length
                        100 to 110 without recompiling. The prediction will
                        become marginally slower for the longer input, but
                        overall performance increases due to not recompiling.
                        Set to 1 to disable.
--model-order MODEL_ORDER
--host-url HOST_URL <strong>→ default = https://api.colabfold.com</strong>
--data DATA
--msa-mode {MMseqs2 (UniRef+Environmental),MMseqs2 (UniRef only),single_sequence}
                        Using an a3m file as input overwrites this option
--model-type {auto,AlphaFold2-ptm,AlphaFold2-multimer-v1,AlphaFold2-multimer-v2}
                        predict structure/complex using the following
                        model.Auto will pick "AlphaFold2" (ptm) for structure
                        predictions and "AlphaFold2-multimer-v2" for
                        Complexes. <strong>→ default = AlphaFold2-ptm</strong>
--amber               Use amber for structure refinement
--templates           Use templates from pdb
--custom-template-path CUSTOM_TEMPLATE_PATH
                        Directory with pdb files to be used as input</code>
--env
--cpu                 Allow running on the cpu, which is very slow
--rank {auto,plddt,ptmscore,multimer} → default = plddt
                        rank models by auto, plddt or ptmscore
--pair-mode {unpaired,paired,unpaired+paired} → default =  unpaired+paired
                        rank models by auto, unpaired, paired, unpaired+paired
--recompile-all-models → default = false
                        recompile all models instead of just model 1 and 3
--sort-queries-by {none,length,random}
                        sort queries by: none, length, random
--save-single-representations
                        saves the single representation embeddings of all
                        models
--save-pair-representations
                        saves the pair representation embeddings of all models
--training            turn on training mode of the model to activate drop
                        Outs → default = false
--max-msa {512:5120,512:1024,256:512,128:256,64:128,32:64,16:32} → default = null
                        defines: `max_msa_clusters:max_extra_msa` number of
                        sequences to use
--zip                 zip all results into one <jobname>.result.zip and
                        delete the original files
--use-gpu-relax       run amber on GPU instead of CPU
--overwrite-existing-results → default = false
```

