# Using Environment Modules

Modules are easy to use. You can <red>`load`</red> and <red>`unload`</red> them as you please, enabling and disabling different software. You can list currently active modules with <red>`module list`</red>, search for modules with <red>`module avail`</red>, and unload all active modules with <red>`module purge`</red>.

While the modules work on the login nodes, the login nodes have strict CPU and memory limits. Jobs that do heavy lifting should always be [scheduled through Slurm](../slurm/index.md).

### List All Available Modules ###
These all do the same thing:
```
module available
module avail
module av
ml av
```

This will return an output that looks something like this:
```
------------------------------------------------- /modules/modulefiles -------------------------------------------------
   R/3.6.2             cuda/10.1.243 (D)    gcc/9.2.0               julia/1.1.1         openmpi/4.0.4
   cmake/3.7.2         cuda/11.0.1          glxgears/1.0            jupyter/3.6.8       python/2.7.16
   cmake/3.15.0 (D)    fd3dspher/1.0        gmsh/4.4.1              mathematica/12.0    python/3.7.4  (D)
   cuda/8.0.61         gcc/5.5.0            gpu-burn/default        mesa/19.0.8         qt/5.13.1
   cuda/9.0.176        gcc/6.5.0            gromacs/2020.2C         miniconda/3.7       stress/1.0.4
   cuda/9.2.148        gcc/7.4.0     (D)    gromacs/2020.2G  (D)    opencl/2.2.11       vtk/8.2.0
```
!!! note
    The module list is rapidly growing. To see the full list, use this command in your terminal.

### Search for Modules ###
```
module avail gcc
```
This filters the output of <red>`module avail`</red> for just the `gcc` modules.

### Loading Modules ###
```
module load gcc/9.2.0
```
!!! note
    Not all modules are shown by default in `module avail`. See [module hierarchy](module-hierarchy.md).

### Unloading Modules ###
```
module unload gcc
```

### Unloading All Modules ###
```
module purge
```

### List Currently Loaded Modules ###
```
module list
```
