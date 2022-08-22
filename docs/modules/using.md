# Using Modulefiles #
Using modulefiles is very simple. Keep in mind that the below commands will work anywhere on the cluster, so you can load/unload modules within your slurm submission scripts or during interactive jobs. This is what they are intended for.

### List All Available Modules ###
``` bash
module av
```
which will return an output that looks something like this:
``` bash
------------------------------------------------- /modules/modulefiles -------------------------------------------------
   R/3.6.2             cuda/10.1.243 (D)    gcc/9.2.0               julia/1.1.1         openmpi/4.0.4
   cmake/3.7.2         cuda/11.0.1          glxgears/1.0            jupyter/3.6.8       python/2.7.16
   cmake/3.15.0 (D)    fd3dspher/1.0        gmsh/4.4.1              mathematica/12.0    python/3.7.4  (D)
   cuda/8.0.61         gcc/5.5.0            gpu-burn/default        mesa/19.0.8         qt/5.13.1
   cuda/9.0.176        gcc/6.5.0            gromacs/2020.2C         miniconda/3.7       stress/1.0.4
   cuda/9.2.148        gcc/7.4.0     (D)    gromacs/2020.2G  (D)    opencl/2.2.11       vtk/8.2.0
```
!!! note
    The output above is subject to change.

### Searching for Modules ###
``` bash
module av gcc
```
That will only show you the available gcc modules.

### Loading Modules ###
``` bash
module load gcc/9.2.0
```
!!! note
    The convention is `<app name>/<app version>`.

After loading a module, you can test is out by running `whereis gcc`, which will show you which `gcc` will be executed.

### Unloading Modules ###
``` bash
module unload gcc
```

### Unloading All Modules ###
``` bash
module purge
```

### List Currently Loaded Modules ###
``` bash
module list
```