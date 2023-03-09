### Email ###

Slurm can send you emails based on the status of your job via the <red>`--mail-type`</red> argument.

Common mail types are `BEGIN, END, FAIL, INVALID_DEPEND, REQUEUE, and STAGE_OUT`. See the [sbatch man page](https://slurm.schedmd.com/sbatch.html#OPT_mail-type)

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
