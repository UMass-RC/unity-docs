# Unity GPU Documentation

Graphics Processing Units (GPUs) provide a powerful tool to run code in
parallel at a larger scale than traditional CPU parallel workload. This comes
at the tradeoff with slower communication times. It is important to note that
using one or more GPUs does not guarantee that code will run faster, however
many popular software packages have been modified to incorporate GPUs for
better performance.

## Available GPU Resources

| Device | Arch | Caps | VRAM | Constraint(s) |
| --- | --- | --- | --- | --- |
| NVIDIA GeForce GTX TITAN X | Maxwell | sm_52 | vram8 vram11 vram12 | titanx |
| Tesla M40 24GB | Maxwell | sm_52 | vram8 vram11 vram12 vram16 vram23 | m40 |
| NVIDIA GeForce GTX 1080 Ti | Pascal | sm_52 sm_61 | vram8 vram11 | 1080ti |
| Tesla V100-PCIE-16GB | Volta | sm_52 sm_61 sm_70 | vram8 vram11 vram12 vram16 | v100 |
| Tesla V100-SXM2-16GB | Volta | sm_52 sm_61 sm_70 | vram8 vram11 vram12 vram16 | v100 |
| Tesla V100-SXM2-32GB | Volta | sm_52 sm_61 sm_70 | vram8 vram11 vram12 vram16 vram23 vram32 | v100 |
| NVIDIA GeForce RTX 2080 | Turing | sm_52 sm_61 sm_70 sm_75 | vram8 | 2080 |
| NVIDIA GeForce RTX 2080 Ti |  Turing |sm_52 sm_61 sm_70 sm_75 | vram8 vram11 | 2080ti |
| Quadro RTX 8000 | Turing | sm_52 sm_61 sm_70 sm_75 | vram8 vram11 vram12 vram16 vram23 vram32 vram40 vram48 | rtx8000 |
| NVIDIA A100-PCIE-40GB | Ampere | sm_52 sm_61 sm_70 sm_75 sm_80 | vram8 vram11 vram12 vram16 vram23 vram32 vram40 | a100, a100-40g |
| NVIDIA A100-SXM4-80GB | Ampere | sm_52 sm_61 sm_70 sm_75 sm_80 | vram8 vram11 vram12 vram16 vram23 vram32 vram40 vram48 vram80 | a100, a100-80g |

## Requesting GPU Resources

Requesting GPU access on Unity can be done via Slurm either for an interactive session or using a batch script.
Below are a minimal example of both interactive and batch jobs.

!!! note
    Not all software is able to use GPUs, and some software will require
    special options, dependencies, or alternate versions to be able to run with
    GPUs. Please ensure your software supports GPU use before requesting these
    resources.

---

**Interactive**
```bash
srun -p gpu-preempt -t 02:00:00 --gpus=1 --pty /bin/bash
```


 **Batch Script**
```bash
#!/bin/bash

#SBATCH -p gpu-preempt # Submit job to to gpu-preempt partition
#SBATCH -t 02:00:00    # Set max job time for 2 hours
#SBATCH --gpus=1       # Request access to 1 GPU
$SBATCH --constraint=2080ti # Request access to a 2080ti GPU

./myscript.sh
```

Specific GPUs can also be selected by using the --constraint flags with Slurm,
or by adding the gpu type to --gpus. The available constraints are listed
below.

!!! note
    Using `--constraint` allows you to select multiple possible GPUs that fulfil the requirements. You can either use `--constraint=[2080|2080ti]` or `--constraint=sm_70&vram12`. It is better to use the first form if you are using GPUs across more than one node to ensure the same model is used across all entire job.

- 2080ti
- 1080ti
- 2080
- titanx
- m40
- rtx8000
- v100
- a100


 **Batch Script with Specific GPU**
```bash
#!/bin/bash

#SBATCH -p gpu-preempt # Submit job to to gpu-preempt partition
#SBATCH -t 02:00:00    # Set max job time for 2 hours
#SBATCH --gpus=2080ti:1       # Request access to 1 2080tiGPU

./myscript.sh
```

 **Batch Script with Constraint**
```bash
#!/bin/bash

#SBATCH -p gpu-preempt # Submit job to to gpu-preempt partition
#SBATCH -t 02:00:00    # Set max job time for 2 hours
#SBATCH --gpus=1       # Request access to 1 2080tiGPU
#SBATCH --constraint=2080ti

./myscript.sh
```

 **Batch Script with Constraint specifying multiple options**
```bash
#!/bin/bash

#SBATCH -p gpu-preempt # Submit job to to gpu-preempt partition
#SBATCH -t 02:00:00    # Set max job time for 2 hours
#SBATCH --gpus=1       # Request access to 1 2080tiGPU
#SBATCH --constraint=2080ti|1080ti|2080

./myscript.sh
```

---


## GPU-Enabled Software

**CUDA**: NVIDIA's parallel computing platform. A version of this will typically be required to be loaded for most GPU jobs, as this allows access to this NVIDIA compiler suite (nvcc, nvfortran) as well as the NVIDIA GPU profiling tool (nsys).

**cuDNN**: Cuda Deep Neural Network library, often used to accelerate deep learning frameworks in Keras, PyTorch, TensorFlow, and others.

**OpenMPI**: The OpenMPI compilers for MPI compiled against the cuda compilers. This is necessary to use if software that uses both MPI and GPU acceleration.

**Note: be sure to check which version(s) of cuda are compatible with the software that is being used.**


| Software Name | Available Verions |
| --- | --- |
| cuda 11 | 11.8.0, 11.5.0, 11.4.0, 11.3.1, 11.0.3, 11.0.1 |
| cuda 10 | 10.2.89, 10.1.243, 10.0.130 |
| cuda legacy versions (<10.0) | 9.2, 9.2.88, 9.0, 8.0.61, 8.0, 7.5.18, 7.0, 6.5.14, 6.0 |
| cudnn | cuda11-8.4.1.50, cuda10-7.5.0.56, 8.2.4.15-11.4 |
| openmpi | 4.1.3+cuda11.6.2-mpirun, 4.1.3+cuda11.6.2 |

In addition to these, many programming languages are able to use one or more GPUs.

- Python
- Matlab
- Julia
- C++ (using Cuda or OpenACC)
- Fortran (using Cuda or OpenACC)
- C (using Cuda or OpenACC)



### Setting up a TensorFlow GPU Environment

Some software, especially with python, requires setting up the environment in a specific way.

For python programs that can use GPU, such as TensorFlow, this is best done using a conda environment.

The steps to set up a conda environment for TensorFlow is shown below:

---

1. request an interactive session with a GPU node

```bash
srun -t 01:00:00 -p gpu-preempt --gpus=1 --mem=16G --pty /bin/bash
```

2. load modules

```bash
module load miniconda/22.11.1-1
module load cuda/11.4.0
module load cudnn/cuda11-8.4.1.50
```

3. create the environment

```bash
conda create --name TensorFlow-env python=3.9
```

Note: TensorFlow 2 requires a python version of at least 3.9

```bash
conda activate TensorFlow-env
pip install TensorFlow
pip install tensorrt
conda install ipykernel
```
Note: if you do not request enough memory, TensorRT will fail to install

4. Add environment to Jupyter
```bash
python -m ipykernel install --user --name TensorFlow-env --display-name="TensorFlow-Env"
```

---

After completing these steps, a new kernel with the name "TensorFlow-Env" will be shown with new Open OnDemand sessions


## Troubleshooting with GPUs

To view ongoing GPU processes, the `nvidia-smi pmon` command can be used.

If you are getting error messages, please be sure to add the following command
to your scripts in order to know which GPU is being used.

```bash
nvidia-smi -L
```

If there is a CUDA_ERROR_OUT_OF_MEMORY, a GPU with more available VRAM may be
necessary, or the code being run should be modified to reduce the memory usage.
