---
title: Array Batch Jobs
---

# Array Batch jobs #

It is often the case that you need to run the same set of commands over either different sets of data, or the same data with different parameters. Array jobs help you submit several jobs at once with the same batch script, and provide a relative index (via environment variable `$SLURM_ARRAY_TASK_ID`) that can be used by the script or program to select what to do .

### Syntax
To submit an array job, specify
```shell
--array=<indexes>
```
where `<indexes>` can be any combination of ranges and lists. For example, `1-100,200` would submit 101 jobs. Ranges support skip counting with a `:`, so `0-15:4` is the same as `0,4,8,12`.

When submitting a large array it may be useful to limit the number of jobs in the array running at one time (see the [partition list]({{< relref "partition-list" >}}) for per-user and per-account limits). For this,you can use the `%` syntax. For example, this will limit to 10 concurrent jobs:
```shell
--array=1-100%10
```
This value can be updated later with `scontrol`:

```shell
scontrol update jobid=.... arraytaskthrottle=15
```
!!! note
    Decreasing the number of concurrent jobs will not kill job. A new job will not start until the running tasks dips below the new threshold.

Jobs submitted as an array will be listed using the `<jobid>_<arrayid>` syntax in `squeue` and `sacct` output, and default output file name will be `slurm-%A_%a.out` to match this.

### Selecting data or parameters with SLURM_ARRAY_TASK_ID
Each job in the job array will have a unique value from the set of indexes provided. Here are some examples of how to make use of that value.

#### Selecting a dataset
Depending on how your data is structured, choosing which set to work on mean selecting a directory or file name to work on. Best practice here would be to generate a list ahead of time, and then select an item from that list:
```BashSession
login$ ls -1 *.fasta > input.txt
login$ wc -l input.txt
23
login$ sbatch --array=1-23 search.sh
```
Then in the batch script, use `$SLURM_ARRAY_TASK_ID` to select a line
```bash
#!/bin/bash
#$BATCH -N 1 -c 12
INPUT_FILE=$(sed -n "${SLURM_ARRAY_TASK_ID}p" input.txt)
module load blast-plus/2.12.0
blastx -query "${INPUT_FILE}" -db nr -num_threads "${SLURM_CPUS_ON_NODE}"
```
!!! note
    Do not use the `ls` command directly in the batch script, as changes to the contents of the directory during the run may affect the order of the output, leading to missed or double-processed files.

#### Selecting a parameter set
The environment variable can also be used directly in your code. For example:
```python
import os
# Define the set of parameters
parameters = [
    {'x': 1, 'y': 1},
    {'x': 2, 'y': 1},
]
def model(x, y):
    pass
if __name__ == "__main__":
    # Note: use zero-based indexing on submit: --array=0-1
    DATA_SET = int(os.getenv("SLURM_ARRAY_TASK_ID"))
    model(**parameters[DATA_SET])
```

#### Using as random number generator seed
For some applications the only change in the code might be a seed for a random number generator. This should work the same as the previous example:
```python
import os
import random
SEED = int(os.getenv("SLURM_ARRAY_TASK_ID"))
random.seed(SEED)
# Remember the value somewhere so you can reproduce
print(f"Using RNG Seed: {SEED}")
```

### Email from Job arrays
By default emails for jobs BEGIN/END/FAIL apply to the array as a whole. For small arrays you might consider `--mail-type=ARRAY_TASKS,FAIL` to be notified of each task failure, if any.

### Canceling an array job
You can cancel either a specific array index, or an entire array (running and pending), depending on how you specify the job id:

```shell
scancel jobid_arrayid  # cancel a specific instance
scancel jobid  # will cancel any running or pending items in the array
```
### Job dependencies
If your array jobs also have multiple steps with different resource requirements, you can submit multiple job arrays where the next step depends only on the corresponding ID of the last array. To do this you need to submit each job sequentially, and use `--dependency=aftercorr:` to specify it on the next job. For example, if you have a job that requires a lot of resources to compute, but only a single core to post-process, you can use the following commands (either on the command line or in another bash script).
```shell
mainjob=$(sbatch -P --array=0-12%6 -G 1 -p gpu main_job.sh)
sbatch --array=0-12%6 --dependency=aftercorr:$mainjob post_process.sh
```
