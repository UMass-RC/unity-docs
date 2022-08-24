# Introduction to Slurm: The Job Scheduler #
Slurm is the job scheduler we use in our cluster. More info about what a job scheduler is can be found in the [introduction](../index.md). Here we will go more into depth about some elements of the scheduler. There are many more features of Slurm that go beyond the scope of this guide, but all that you as a user needs to know should be available.

!!! note
    Doing work on the login nodes can cause Unity to become sluggish for the entire user base.
    We have disincentivized this by setting limits on cpu and memory.
    Learn how to use `srun` interactive sessions to switch from a login node to a compute node.


## Partitions / Queues ##
Our cluster has a number of slurm **partitions** defined, also known as a **queue**. As you may have guessed, you as the user request to use a specific partition based on what resources your job needs. Find out which partition is best for your job [here](../technical/partitionlist.md)

## Jobs ##
A job is an operation which the user submits to the cluster to run under allocated resources.
There are two commands for this, `srun` and `sbatch`. `srun` is tied to your current session, and can allow you to interact with your job. `sbatch` is not tied to your current session, so you can start it and walk away. If you want to interact with your job **and** be able to walk away, you can use `tmux` to make a detachable session. (see below)

#### SRUN ####
An `srun` job is tied to your ssh session. If you break (ctrl+C) or close your ssh session during an `srun` job, **the job will be killed**.

You can also make an **interactive** job, which will allow your job to take input from your keyboard. You can run `bash` in an interactive job to resume your work on a compute node just as you would on a login node. **This is highly recommended.**

See [SRUN Jobs](../slurm/srun.md) for more information.

#### SBATCH ####
An `sbatch` job is submitted to the cluster with no information returned to the user other than a Job ID. An `sbatch` job will try to create a file in your current working directory that contains the results of your job.

See [SBATCH Jobs](../slurm/sbatch.md) for more information.

#### TMUX SRUN ####
```
tmux
# tmux session opens
srun --pty -c 1 bash
# interactive job on compute node opens with one cpu core
sleep 3600; echo "done"
# interactive job will have blinking cursor for an hour
# > ctrl+b
# tmux keyboard-shortcut command mode opens
# > d
# tmux session detaches, back to login node
# at this point you can log off and log back in without killing the job
tmux ls
# print list of tmux sessions
# first number on the left (call it X) is needed to re-attach the session
tmux attach-session -t X
# back to interactive job
```