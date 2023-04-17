# Module Hierarchy #

Environment Modules is a tool to change dynamically what software is available for use by a given user at a given time. Before you read this, it's recommended that you first read the  [introduction](index.md) and the [module usage guide](module-usage.md).

As a Unity user, you have access to many modules built with various software stacks. As Unity grows and more modules are installed with more stacks, it can become difficult to effectively manage them all. Our strategy is to create a **module hierarchy** to divide modules according to their stacks. This makes it much more difficult to accidentally load modules which are incompatible with each other.

The `$MODULEPATH` environment variable is a list of directories in which Lmod searches for modules. With a module hierarchy, not all directories are added to the modulepath by default.

This means **not all modules can be found with <red>`module avail`</red> by default.**

### Here is the full Unity module hierarchy as of 2023/4/15: ###

<red>Compilers</red> are red, and <blue>providers</blue> are blue.

<pre><code>/modules/modulefiles/

/modules/spack_modulefiles/
├── linux-ubuntu20.04-x86_64
|   ├── <red>Core</red>
|   ├── <red>intel</red>
|   │   └── 2021.4.0
|   ├── <blue>atlas</blue>
|   │   └── 3.10.3-sfhhdph
|   │       └── <red>Core</red>
|   ├── <blue>intel-oneapi-mpi</blue>
|   │   └── 2021.6.0-h3cppyo
|   │       ├── <red>Core</red>
|   │       └── <blue>openblas</blue>
|   │           └── 0.3.18-6pbqv7b
|   │               └── <red>Core</red>
|   ├── <blue>openblas</blue>
|   │   └── 0.3.18-6pbqv7b
|   │       └── <red>Core</red>
|   └── <blue>openmpi</blue>
|       ├── 4.1.3-3rgk3nu
|       │   ├── <red>Core</red>
|       │   └── <blue>intel-mkl</blue>
|       │       └── 2020.4.304-gmusbfh
|       │           └── <red>Core</red>
|       └── 4.1.4-tauaqk4
|           ├── <red>Core</red>
|           └── <blue>intel-mkl</blue>
|               └── 2020.4.304-gmusbfh
|                   └── <red>Core</red>
├── linux-ubuntu20.04-aarch64
│   └── <red>Core</red>
└── linux-ubuntu20.04-ppc64le
    ├── <red>Core</red>
    ├── <blue>openblas</blue>
    │   └── 0.3.21-coxg6gz
    │       └── <red>Core</red>
    └── <blue>openmpi</blue>
        ├── 4.1.3-edoxxdf
        │   ├── <red>Core</red>
        │   └── xl
        │       └── 16.1
        └── 4.1.4-476r55m
            └── <red>Core</red>

</code></pre>
!!!note
    Random characters at the end of compiler/provider version numbers can usually be ignored.

    `Core` refers to modules compiled with Ubuntu's default GNU compiler suite, and without any special providers. The majority of Unity's modules are found here.

    `intel` refers to the classic intel compilers (`icc`, `ifort`, `icpc`, ...).

    The `intel-oneapi-compilers-classic` module adds `intel` to modulepath.

## Hierarchy naming scheme ##
<pre><code>linux-ubuntu20.04-[architecture]/<red>[compiler]</red>/<strong>[name]/[version]</strong>
linux-ubuntu20.04-[architecture]/<blue>[provider]</blue>/<red>[compiler]</red>/<strong>[name]/[version]</strong>
linux-ubuntu20.04-[architecture]/<blue>[provider]</blue>/<blue>[another-provider]</blue>/<red>[compiler]</red>/<strong>[name]/[version]</strong>
</code></pre>

* In this naming scheme, `Core` counts as a compiler.

## How to use the hierarchy ##
You can find modules anywhere in the hierarchy with the <red>`unity-module-find`</red> command.

From the full path of your desired module you should be able to tell which other modules need to be loaded first.

!!!note
    `Core` is always automatically added to `$MODULEPATH`!

#### Example: ####
<pre><code>user@login1:~$ module load gromacs/2021.3
<strong><red>No module(s) or extension(s) found!</red></strong>
If the avail list is too long consider trying:

"module --default avail" or "ml -d av" to just list the default modules.
"module overview" or "ml ov" to display the number of modules for each name.

Use "module spider" to find all possible modules and extensions.
Use "module keyword key1 key2 ..." to search for all possible modules matching any of the "keys".
</code></pre>

<pre><code>user@login1:~$ unity-module-find gromacs
Modules found:
linux-ubuntu20.04-x86_64/intel-oneapi-mpi/2021.6.0-h3cppyo/Core/<red>gromacs/2021.3</red>
<strong>linux-ubuntu20.04-x86_64/openmpi/4.1.3-3rgk3nu/intel-mkl/2020.4.304-gmusbfh/Core/<red>gromacs/2021.3</red></strong>
</code></pre>

This is the module that I want:
<pre><code>linux-ubuntu20.04-x86_64/<strong><blue>openmpi</blue></strong>/4.1.3-3rgk3nu/<strong><blue>intel-mkl</blue></strong>/2020.4.304-gmusbfh/<strong><red>Core</red></strong>/gromacs/2021.3
</code></pre>

In that path I can see which modules must loaded first. The new command becomes:
```
$ module load openmpi/4.1.3 intel-mkl/2020.4.304 gromacs/2021.3
```

### Learn more ###
[About the Hierarchy Change](../updates/index.md#the-module-hierarchy-change-coming-soon)

[https://lmod.readthedocs.io/en/latest/010_user.html#module-hierarchy](https://lmod.readthedocs.io/en/latest/010_user.html#module-hierarchy)

[https://lmod.readthedocs.io/en/latest/080_hierarchy.html](https://lmod.readthedocs.io/en/latest/080_hierarchy.html)
