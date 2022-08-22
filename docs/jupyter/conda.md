# Conda Environments within JupyterLab #

!!! note
    Currently, there is no GUI implementation within JupyterLab of the below processes. This is a planned feature for the future.

## Introduction ##
It is possible to create unlimited custom conda environments and use them within JupyterLab. Some CLI commands are required, but they can all be done through the JupyterLab interface.

The Conda package manager does not require any compiling during package install, which is why it is favorable in a cluster environment where users don't have admin right to install dependent libraries.

## Environment Setup ##

!!! note
    This guide uses the `conda` command often. Thie command needs to be loaded before using it using the command `module load miniconda`. This guide assumes you have done this.

### Creating an Environment ###
Create an environment using this command. You can create as many discrete environment as you want.
```
conda create --name testName python=3.7
```
!!! note
    Replace `testName` with the name of your choice for the environment, and replace `3.7` with whatever python version you want.

### Activating an Environment ###
Use this command to activate your environment. This step is required any time you'd like to modify that specific environment.
```
conda activate testName
```
!!! note
    Your currently active conda environment will appear left of your prompt in the format `(testName)`.

### Adding Packages to your Environment ###
Install Conda packages of your choosing. We are using numpy as an example.
``` bash
conda install numpy
```
The install will ask you to confirm installing numpy as well as any other additional required packages, you will need to repond with a `y` then press enter.

## Adding your Environment to JupyterLab ##
**Make sure your environment is active.**  
The `ipykernel` package has to be installed within your environment for JupyterLab to be able to talk to it. Other kernels are supported, since conda can run languages other than python.
``` bash
conda install ipykernel
```
Add a kernelspec (Kernel Specification) to your JupyterLab.
``` bash
python -m ipykernel install --user --name testName --display-name="Display Name Within JupyterLab"
```
If the above was done within JupyterLab, your JupyterLab instance must be restarted.

## Other Operations ##
### List Available Environments ###
``` bash
conda env list
```

### List Packages Currently Installed in the Activated Environment ###
``` bash
conda list
```

### Deleteing an Environment ###
``` bash
conda remove --name testName --all
```
You may also need to remove the kernelspec within JupyterLab seperately.
``` bash
rm -rf ~/.local/share/jupyter/kernels/testName
```