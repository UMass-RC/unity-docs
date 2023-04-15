### Email

Slurm can send you emails based on the status of your job via the <red>`--mail-type`</red> argument.

Common mail types are `BEGIN, END, FAIL, INVALID_DEPEND, and REQUEUE`. See the [sbatch man page](https://slurm.schedmd.com/sbatch.html#OPT_mail-type)

Example:
```sh
srun --mail-type=BEGIN hostname
```
or:
```sh
#!/bin/bash
#SBATCH --mail-type=BEGIN
hostname
```

There is also the <red>`--mail-user`</red> argument, but this is optional. Our mail server knows the email you used to register your Unity account.

#### Time Limit Email - Preventing Loss of Work

When your job reaches its time limit, it will be killed, even if it's 99% of the way through its task. Without [checkpointing](https://en.wikipedia.org/wiki/Application_checkpointing), all those CPU hours will be for nothing and you will have to schedule the job all over again.

One way to prevent this is to check on your job's output as it approaches its time limit. You can specify <red>`--mail-type=TIME_LIMIT_80`</red>, and Slurm will email you if 80% of the time limit has passed and your job is still running. Then you can check on the job's output and determine if it will finish in time. If you think that your job will not finish in time, you can email us at [hpc@umass.edu](mailto:hpc@umass.edu) and we can extend your job's time limit.
