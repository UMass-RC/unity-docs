# Using SRUN to Submit Jobs #

!!! note 
    Usually, if you have to run a single application multiple times, or if you are trying to run a non-interactive application, you should use [sbatch](sbatch.md) instead of srun, since sbatch allows you to specify parameters in the file, and is *non-blocking* (see below).

SRUN is a so-called *blocking* command, as in it will not let you execute other commands until this command is finished (not necessarily the job, just the allocation). For example, if you run `srun /bin/hostname` and resources are available right away, the job will be sent out and the result saved into a file. If resources are not available, you will be stuck in the command while you are pending in the queue.

Please note that like sbatch, you can run a batch file using srun.

The command syntax is `srun <options> [executable] <args>`

Options is where you can specify the resources you want for the executable, or define. The following are some of the options available; to see all available parameters run `man srun`.

* `-c <num>` Number of CPUs (threads) to allocate to the job per task
* `-n <num>` The number of tasks to allocate (for MPI)
* `-G <num>` Number of GPUs to allocate to the job
* `--mem <num>` Memory to allocate to the job (in MB by default)
* `-p <partition>` Partition to submit the job to

To run an interacitve job (in this case a bash prompt), the command might look like this (`--pty` is the important option):
```
srun -c 6 -p cpu --pty bash
```
To run an application on the cluster that uses a GUI, you **must** use an interactive job, in addition to the `--x11` argument:
```
srun -c 6 -p cpu --pty --x11 xclock
```
!!! note
    You cannot run an interactive/gui job using the `sbatch` command, you must use `srun`.