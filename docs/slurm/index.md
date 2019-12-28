# Instruction to Slurm: The Job Scheduler #
Slurm is the job scheduler we use in our cluster. More info about what a job scheduler is can be found in the [introduction](../index.md). Here we will go more into depth about some elements of the scheduler. There are many more features of Slurm that go beyond the scope of this guide, but all that you as a user needs to know should be available.

### Partitions / Queues ###
Our cluster has a number of slurm **partitions** defined, each of which corresponds to a job **queue**:
* cpu-short
* cpu-long
* gpu

As you may have guessed, you as the user request to use a specific partition based on what resources your job needs. *cpu-short* has a 4 hour runtime limit to facilitate more efficient queuing for those wishing to run shorter jobs. The other partitions have no runtime limit.

To view all available partitions in Slurm, you can run the command `sinfo`.

For those that purchase hardware for Unity and choose to have priority/sole access to a partition, that parition will be listed but if you are not a member of that group you will not be able to use it.

### Jobs ###
A job is an operation which the user submits to the cluster to run under allocated resources.

When submitting a job to the cluster, you will have a few options. The first is to use `srun`, which will simply run the command you specify in the srun command with any parameters specified.

The other option is an **interactive** job. This job will allocate resources and start the job interactively, so that you can view what is happening live and interact with the prompt. If you leave this prompt **the job will be cancelled**. For example, you can use this feature together with the `bash` command to open an interactive bash shell with allocated resources.