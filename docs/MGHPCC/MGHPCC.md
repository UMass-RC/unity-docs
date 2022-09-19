# MGHPCC Transitions #
Latest updates on MGHPCC transitions available [here.](https://www.umass.edu/it/researchcomputing/mghpcc-transitions)

*** Moving from MGHPCC to Unity ***

The Unity cluster uses Slurm, an open-source batch system.

Slurm offers the same basic functionalities as LSF: you can use it to submit jobs, monitor their progress, and kill them if necessary. As in LSF, a job can be a single command, a parallel program using MPI or openMP, or a complex script. Slurm also supports GPUs and advanced features like job arrays.  Slurm works in the same way as LSF in that: you only need to specify the resources needed by your job, such as number of cores and GPUs (if applicable), memory, run-time, etc. Slurm will analyse your job's requirements and will automatically send it to the right partition. (Slurm uses partitions instead of queues, but the idea is the same.)

The LSF commands that you use today to submit and monitor jobs — ``` bsub, bjobs ``` — and their various options will need to be replaced with their Slurm equivalent, which can be found [here](https://scicomp.ethz.ch/wiki/LSF_to_Slurm_quick_reference).

A full list of Slurm commands and their equivalents can be found [here](https://slurm.schedmd.com/rosetta.pdf).