# Using SBATCH to Submit Jobs #

SBATCH is a *non-blocking* command, meaning there is not a circumstance where running the command will cause it to hold. Even if the resources requested are not available, the job will be thrown into the queue and will start to run once resources become available. The status of a job can be seen using `squeue`.
```
squeue -u $USER
squeue -j YOUR_JOBID
```

SBATCH is based around running a single file. That being said, you shouldn't need to specify any parameters in the command other than `sbatch <batch file>`, because you can specify all parameters in the command inside the file itself.

The following is an example of a batch script. Please note that the top of the script **must** start with `#!/bin/bash` (or whatever interpreter you need, if you don't know, use bash), and then immediately follow with `#SBATCH <param>` parameters. An example of common SBATCH parameters and a simple script is below, this script will allocate 4 CPUs and one GPU in the GPU partition.

```
#!/bin/bash
#SBATCH -c 4  # Number of Cores per Task
#SBATCH --mem=8192  # Requested Memory
#SBATCH -p gpu  # Partition
#SBATCH -G 1  # Number of GPUs
#SBATCH -t 01:00:00  # Job time limit
#SBATCH -o slurm-%j.out  # %j = job ID

module load cuda/10
/modules/apps/cuda/10.1.243/samples/bin/x86_64/linux/release/deviceQuery
```
This script should query the available GPUs, and print only one device to the specified file. Feel free to remove/modify any of the parameters in the script to suit your needs.