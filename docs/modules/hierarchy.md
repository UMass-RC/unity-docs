# Module Hierarchy #

The modulepath (`$MODULEPATH`) is a list of directories in which Lmod (<red>`module`</red>) searches for modules.

In the limited view, not all directories are added to the modulepath by default.

This means not all modules can be found in <red>`module avail`</red> by default.

### The hierarchy (as of 2022/10/24) ###
<pre><code><strong>/modules/modulefiles/ (D)</strong>

/modules/spack/.../linux-ubuntu20.04-x86_64/
├── <strong><red>gcc</red>/9.4.0/ (C)(D)</strong>
├── <red>intel</red>/2021.4/ (C)
├── <blue>intel-oneapi-mpi</blue>/2021.6.0-ad5zrqt/ (P)
    ├── <red>gcc</red>/9.4.0/ (C)
├── <blue>openblas</blue>/0.3.18-cuu4pwk/ (P)
    ├── <red>gcc</red>/9.4.0/ (C)
├── <blue>openmpi</blue>/4.1.3-lih7mwq/ (P)
    ├── <red>gcc</red>/9.4.0/ (C)
    ├── <blue>intel-mkl</blue>/2020.4.304-w2r5zyv/ (P)
        ├── <red>gcc</red>/9.4.0/ (C)
</code></pre>
where `(C)` is a <red>compiler</red>, `(P)` is a <blue>provider</blue>, and `(D)` is included by <strong>default</strong>.

!!!note
    `intel` refers to the classic intel compilers, the module for which is named `intel-oneapi-compilers-classic`

### Hierarchy naming scheme ###

<pre><code>linux-ubuntu20.04-[architecture]/[compiler]/[compiler-version]/<red>[module-name]/[version]</red>
linux-ubuntu20.04-[architecture]/[provider]/[provider-version]/[compiler]/[compiler-version]/<red>[module-name]/[version]</red>
</code></pre>

* Nested providers are possible.

### How to use a non-default module ###
You can find modules anywhere in the hierarchy with the <red>`unity-module-find`</red> command.

The module you find will be under a non-default provider, compiler, or architecture.

* If under an architecture, get a slurm job on a node with that architecture.
    * To switch your session to a node with arch 'x86_64_v4', use <red>`srun --pty -C x86_64_v4 /bin/bash`</red>.
* If under a provider/compiler, <red>`module load`</red> that provider/compiler.
    * You can load multiple modules in one line. For example:
```
$ module find gromacs

linux-ubuntu20.04-x86_64/openmpi/4.1.3-3rgk3nu/intel-mkl/2020.4.304-gmusbfh/gcc/9.4.0/gromacs/2021.3

$ module load openmpi intel-mkl gromacs
```


### Learn more ###
[https://lmod.readthedocs.io/en/latest/010_user.html#module-hierarchy](https://lmod.readthedocs.io/en/latest/010_user.html#module-hierarchy)

[https://lmod.readthedocs.io/en/latest/080_hierarchy.html](https://lmod.readthedocs.io/en/latest/080_hierarchy.html)
