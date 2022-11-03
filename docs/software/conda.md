# Using Conda Environments #

## Introduction ##

The conda package manager allows users to compile software easily and without admin privileges. Conda environments can be created for any software set, and can be enabled/disabled dynamically not unlike modules.

A conda environment is not to be confused with [the environment of your login shell](module-intro.md). The package tied to an environment module is compiled by hand by the Unity admins, where **conda packages can be installed by any user with a simple command**. A conda environment can contain any number of packages, where a module usually only contains one. Modules and conda environments can be used together.

On Unity we use Miniconda, as opposed to Anaconda. From a user's perspective they can be considered to be the same thing.

!!! note
    When working on a conda environment, **make sure you activate it!** Without a currently active environment, conda will attempt to modify the global Unity environment, and you will get `permission denied`.

### Setup ###
The <red>`conda`</red> command is not available unless the `miniconda` module is loaded.

If you see this:
```
conda: Command not found
```
Do this:
```
module load miniconda
```

## Creating an Environment ##
You can create as many conda environments as you desire, limited only by our [disk quotas](../technical/storage.html).
```
conda create --name testName python=3.7
```
This creates an environment in your home folder, specifically `/home/$USER/.conda/envs/<name>`.

You can also create environments in other directories, such as your PI's work directory.
```
mkdir -p /work/pi_name/$USER-conda/envs
conda create --prefix /work/pi_name/$USER-conda/envs/testName python=3.7

# OPTIONAL, make a symlink (shortcut) to home directory
ln -s /work/pi_name/$USER-conda/envs/testName ~/testName
```

Replace `testName` with the name of your choice, and replace `3.7` with your Python version of choice.

!!! note
    The `$USER` environment variable evaluates to your username.

## Activating an Environment ##
Environment created with `--name`:
```
conda activate testName
```
Environment created with `--prefix`:
```
conda activate /work/pi_name/$USER-conda/envs/testName
# OR
cd /work/pi_name/$USER-conda/envs/
conda activate ./testName
```

Your currently active conda environment will appear in parentheses to the left of your command line prompt:
```
user@login2:~$
conda activate ./testName
(testName) user@login2:~$
```

## Adding Packages to your Environment ##
```
conda install numpy
```
The install will ask you to confirm installing numpy as well as any other additional required packages.

## List Available Environments ##
```
conda env list
```

## List Packages Installed in the Current Environment ##
```
conda list
```

## Delete an Environment ##
```
conda remove --name testName --all
```
If your environment was added to JupyterHub, you will have to remove it manually.
```
rm -rf ~/.local/share/jupyter/kernels/testName
```

# Conda Environments and Jupyter

You can create many custom conda environments and use them within JupyterHub. This must be done in the command line, but JupyterHub provides a command line interface in it's 'Terminal' app.

### Adding your Environment to JupyterHub ###
!!! note
    **make sure your environment is activated first.** Without a currently active environment, conda will attempt to modify the main default environment, and you will get permission denied.
```
conda install ipykernel
```
Add a kernelspec (Kernel Specification) to your JupyterHub.
```
python -m ipykernel install --user --name testName --display-name="Display Name Within JupyterHub"
```
If the above was done within JupyterHub, reload the page. If that doesn't work, restart your JupyterHub server.

## Learn more ##
[Conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)