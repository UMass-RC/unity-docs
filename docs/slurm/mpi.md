# Running Jobs on Multple Nodes Using MPI

#### This is the (simplified) sanity check that the Unity admins used to verify that MPI is working: ####
!!! note
    We recommend when running quick jobs that you put your job
    in a `preempt` partition for a shorter wait time.

    `srun -p cpu-preempt ...`
#### srun ####
```
module load openmpi
mpicc /modules/admin-resources/mpi_testing/mpi_array.c -o mpi_array
srun --pty -N 2 mpi_array
```
#### sbatch ####
```
module load openmpi
mpicc /modules/admin-resources/mpi_testing/mpi_array.c -o mpi_array
sbatch -N 2 mpi_script
```
Where `mpi_script` is a file containing the following:
```
#!/bin/bash
srun mpi_array
```


## Frequently Asked Questions ##

### Why can't I use <red>`mpirun`</red>/<red>`mpiexec`</red>? ###
```
This version of Spack (openmpi ~legacylaunchers schedulers=slurm)
is installed without the mpiexec/mpirun commands to prevent
unintended performance issues. See https://github.com/spack/spack/pull/10340
for more details.
If you understand the potential consequences of a misconfigured mpirun, you can
use spack to install 'openmpi+legacylaunchers' to restore the executables.
Otherwise, use srun to launch your MPI executables.
```
The community of HPC admins at Spack have agreed that using <red>`mpirun`</red> with slurm is a bad idea.
<red>`srun`</red> is capable of doing all that <red>`mpirun`</red> is, and having the two fight over control
is reported to cause poor performance.
We currently have a module called `openmpi+mpirun`, which was installed in Spack with `+legacylaunchers`, enabling you to use the wrappers as you please.

### Why do I get multiple outputs from my mpi aware binaries? ###
This is because message passing is not working.
You are running duplicates of your job in parallel, which are unaware of each other.
If using <red>`srun`</red>, you should make sure that you have the pseudo-terminal enabled `--pty`.
This should not occur with <red>`sbatch`</red>.

### Why do I keep getting `PMIX ERROR: NO-PERMISSIONS in file`? ###
openmpi is dependent on pmix.
Our current system slurm installation was not configured with pmix support.
This is evident by <red>`srun --mpi=list`</red>.
pmix_v2 and pmix_v3 should be there, but they aren't.
We will likely recompile slurm to accommodate this.

### Why do I keep getting this OpenFabrics warning?
```
"No OpenFabrics connection schemes reported that they were able to be
used on a specific port.  As such, the openib BTL (OpenFabrics
support) will be disabled for this port."
```
We do not currently have Infiniband hardware in our network, and openmpi would like us to.
You can simply add `-mca btl ^ofi` to your <red>`mpirun`</red> command and disable the Infiniband feature. We will likely recompile openmpi to disable this site-wide.
```
mpirun -mca btl ^ofi ...
```
