# Custom Conda Environments within JupyterLab #
!!! note
    Currently, there is no GUI implementation within JupyterLab of the below processes. This is a planned feature for the future.

## Introduction ##
It is possible to create unlimited custom conda environments and use them within JupyterLab. Some CLI commands are required, but they can all be done through the JupyterLab interface.

The Conda package manager does not require any compiling during package install, which is why it is favorable in a cluster environment where users don't have admin right to install dependent libraries.

## Creating/Activating an Environment ##
1. Open a Terminal from within JupyterLab (or use SSH access)
1. Load the miniconda environment module in order to have access to the `conda` command. 
   ```
   module load miniconda
   ```
1. Create an environment, name it whatever you wish. Use the necessary python version. You only have to run this once, this command is not necessary to reactivate your environment in the future.  
   ```
   conda create --name testName python=3.7
   ```  
   !!! note
       Replace `testName` with a name of your choosing. You can also change the python version to something other than `3.7`.
1. Activate the environment
   ```
   conda activate testName
   ```
   !!! tip
       Your currently active conda environment will appear left of your prompt in the format `(testName)`.

## Adding Packages to your Environment ##
1. Install Conda packages, numpy as an example
   ```
   conda install numpy
   ```
   !!! note
       The install will ask you to confirm installing numpy as well as any other additional required packages, you will need to repond with a `y` then press enter.
1. Add any other required packages using step #5.

## Adding your Environment to JupyterLab ##
1. Make sure your environment is active.
1. The `ipykernel` package has to be installed within your environment for JupyterLab to be able to talk to it. Other kernels are supported.
   ```
   conda install ipykernel
   ```
1. Add a kernelspec (Kernel Specification) to your JupyterLab
   ```
   python -m ipykernel install --user --name testName --display-name="Display Name Within JupyterLab"
   ```
1. Step #3 was done within JupyterLab, your JupyterLab instance must be restarted.

## Other Operations ##
### List Available Environments ###
```
conda env list
```

### List Packages Currently Installed in the Activated Environment ###
```
conda list
```

### Deleteing an Environment ###
```
conda remove --name testName --all
```
You may also need to remove the kernelspec within JupyterLab seperately.
```
rm -rf ~/.local/share/jupyter/kernels/testName
```