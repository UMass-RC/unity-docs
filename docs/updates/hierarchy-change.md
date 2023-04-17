# The Module Hierarchy Change (Coming soon!) #

As a Unity user, you have access to many modules built with various software stacks. As Unity grows and more modules are installed with more stacks, it can become difficult to effectively manage them all. The hierarchy change is to combat module bloat, simplify module names, and (most importantly) prevent conflicts. For many users, nothing will change, but some will have to take a few extra steps when loading modules going forward.

The <red>`module`</red> command refers to Environment Modules. We use [Lmod](https://lmod.readthedocs.io/en/latest/index.html), which is the [Lua](https://www.lua.org/) flavor of Environment Modules. The `$MODULEPATH` environment variable is a list of directories in which Lmod searches for modules. With a module hierarchy, not all directories are added to the modulepath by default.

This means **not all modules can be found with <red>`module avail`</red> by default.**

## What does this mean for my workflow? ##

Without extra steps you may encounter the following error:

<pre><code><strong><red>No module(s) or extension(s) found!</red></strong>
If the avail list is too long consider trying:

"module --default avail" or "ml -d av" to just list the default modules.
"module overview" or "ml ov" to display the number of modules for each name.

Use "module spider" to find all possible modules and extensions.
Use "module keyword key1 key2 ..." to search for all possible modules matching any of the "keys".
</code></pre>

In this case you can follow the documentation on [how to use the hierarchy](../software/module-hierarchy.md#how-to-use-a-non-default-module).

In short, you use the <red>`unity-module-find`</red> command, and from that output you should be able to tell which other modules need to be loaded first.

In many cases, it can be as simple as changing <red>`module load gromacs`</red> into <red>`module load openmpi gromacs`</red>.

## Does this affect me? ##
The following modules are no longer in the default modulepath:

* modules built with the **intel classic compilers**
    * zlib/1.2.12-intel@2021.4.0
    * pigz
* modules that use **mpi**
    * cgns
    * fftw/3.3.8+openmpi4.1.3
    * fftw/3.3.10+intel-oneapi-mpi2021.6.0
    * grace
    * gromacs
    * med
    * mmg
    * netcdf
    * openfoam
    * valgrind
* modules built for specific CPU **micro-architectures**
    * cascadelake
    * haswell
    * icelake
    * skylake_avx512
    * zen
    * zen2

## Why? ##

#### Module name length ####
Historically we have tried to make each module name unique. For example:
```
fftw/3.3.8+openmpi4.1.3
fftw/3.3.8+intel-oneapi-mpi2021.6.0
```
This has worked well enough, but long module names make it harder for Lmod to display many modules on one screen, because horizontal whitespace can be used for more columns.

Gromacs, for example: `gromacs/2021.3+openmpi4.1.3-intel@2021.4` would be shortened to `gromacs/2021.3`.

#### Module name conflicts ####
If module names are not unique, it can be difficult to choose which module to load. When two modules from different directories have the same name, Lmod will [decide](https://lmod.readthedocs.io/en/latest/060_locating.html#marking-a-version-as-default) which is default and mark it with a `(D)` flag. The only way to get around this is to manually manipulate `$MODULEPATH` to exclude certain directories until the desired module is marked as default. With the hierarchy, it's implicit that if you add special modules to your modulepath, you want those special modules to take priority.

#### Module Conflicts ####
Some software (particularly that which uses mpi) needs to be built in a similar manner to its dependencies. NetCDF, for example, will not work unless HDF5 and MPI are built with the same compiler and with certain parameters.

With modules specific to CPU micro-architectures, it's possible to compile software on one node that is unable to run on other nodes. For example, linking off of Skylake modules may lead to problems when running on older Haswell nodes.

If you try to compile using a set of incompatible modules, bad things can happen. At best, Cmake/Autotools will tell you to use something else; At worst, you can struggle with nebulous compiler errors for hours on end. At runtime the result is largely the same.

From the [Lmod documentation](https://lmod.readthedocs.io/en/latest/080_hierarchy.html):
> it is quite easy to load an incompatible set of modules. Now, it is possible that the system administrators at your site might have set up conflicts to avoid loading mismatched modules. However, using conflicts can be fragile. What happens if a site adds a new compiler such as clang or pgi or a new mpi stack? All those module file conflict statements will have to be updated.

A module hierarchy is a robust and elegant solution to avoid module conflicts.

## What is going on under the hood? ##
Our current module tree has two main directories with many modules inside.
```
/modules/modulefiles
/modules/spack_modulefiles
```
We are simply splitting it into multiple directories.
```
/modules/modulefiles
/modules/spack_modulefiles
├── linux-ubuntu20.04-x86_64
|   ├── Core
|   ├── intel/2021.4.0
|   ├── intel-oneapi-mpi/2021.6.0
|   │   └── openblas/0.3.18
|   ├── openblas/0.3.18
|   ├── openmpi/4.1.3
|   |   └── intel-mkl/2020.4.304
|   ├── openmpi/4.1.4
|   |   └── intel-mkl/2020.4.304
|   └── atlas/3.10.3
├── linux-ubuntu20.04-aarch64
|   └── ...
└── linux-ubuntu20.04-ppc64le
    └── ...

```

The Unity module set is split in two. `/modules/modulefiles` contains our homebrew modules, those compiled by hand by the admins. `/modules/spack_modulefiles` contains modules created by Spack. **`/modules/modulefiles` is not changing.**

At the start of each new login shell, `$MODULEPATH` contains only `/modules/modulefiles/` and `/modules/spack_modulefiles/linux-ubuntu20.04-<architecture>/Core`. The "Core" directory contains the modules compiled with Ubuntu's default GNU compiler suite, and without any special providers. Modules made with another compiler, or with special providers, are separated from Core and given their own directory. When you `module load` a compiler or special provider, its directory is added to `$MODULEPATH`, and any modules in that directory are now available to use.

#### Also included in this change ####

* Lmod will no longer allow you to load modules without a version name.
* Every new Slurm job will <red>`module purge`</red>. You will have to make sure that your jobs load modules all by themselves.
    * This is to ensure that incompatible modules are not used.
* New commands are available in your shell:
    * <red>`unity-module-find`</red>
    * <red>`unity-module-hierarchy`</red>
    * <red>`unity-module-hierarchy-help`</red>
    * <red>`unity-slurm-list-constraints`</red>
    * <red>`unity-slurm-find-nodes`</red>
* We are switching Spack TCL modules to Lua.
    * This shouldn't affect the user experience.

## Learn more ##

[Using the Module Hierarchy](../software/module-hierarchy.md)

[https://lmod.readthedocs.io/en/latest/010_user.html#module-hierarchy](https://lmod.readthedocs.io/en/latest/010_user.html#module-hierarchy)

[https://lmod.readthedocs.io/en/latest/080_hierarchy.html](https://lmod.readthedocs.io/en/latest/080_hierarchy.html)
