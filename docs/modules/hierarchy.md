# Module Hierarchy #

The <red>`module`</red> command refers to Environment Modules. We use [Lmod](https://lmod.readthedocs.io/en/latest/index.html), which is Environment Modules implemented in Lua. The **modulepath** environment variable `$MODULEPATH` is a list of directories in which Lmod searches for modules. With a module hierarchy, not all directories are added to the modulepath by default.

This means **not all modules can be found with <red>`module avail`</red> by default.**

Here is the full Unity module hierarchy as of 2022/10/26:
<pre><code><strong>/modules/modulefiles/</strong>

x86_64
|── <strong><red>gcc</red>/9.4.0/</strong>
|── <red>intel</red>/2021.4/
|── <blue>intel-oneapi-mpi</blue>/2021.6.0-h3cppyo/
|   \─ <red>gcc</red>/9.4.0/
|── <blue>openblas</blue>/0.3.18-6pbqv7b/
|   \─ <red>gcc</red>/9.4.0/
|── <blue>openmpi</blue>/4.1.3-3rgk3nu/
|   |── <red>gcc</red>/9.4.0/
|   |── <blue>intel-mkl</blue>/2020.4.304-gmusbfh/
|   |   \─ <red>gcc</red>/9.4.0/

cascadelake
|── <red>gcc</red>/9.4.0/
|── <red>intel</red>/2021.4/
|── <blue>intel-oneapi-mpi</blue>/2021.6.0-ad5zrqt/
|   \─ <red>gcc</red>/9.4.0/
|── <blue>openblas</blue>/0.3.18-cuu4pwk/
|   \─ <red>gcc</red>/9.4.0/
|── <blue>openmpi</blue>/4.1.3-lih7mwq/
|   |── <red>gcc</red>/9.4.0/
|   |── <blue>intel-mkl</blue>/2020.4.304-w2r5zyv/
|   |   \─ <red>gcc</red>/9.4.0/

haswell
|── <red>gcc</red>/9.4.0/
|── <red>intel</red>/2021.4/
|── <blue>intel-oneapi-mpi</blue>/2021.6.0-dxpge2x/
|   \─ <red>gcc</red>/9.4.0/
|── <blue>openblas</blue>/0.3.18-zoqwa7c/
|   \─ <red>gcc</red>/9.4.0/
|── <blue>openmpi</blue>/4.1.3-habm2fz/
|   |── <red>gcc</red>/9.4.0/
|   |── <blue>intel-mkl</blue>/2020.4.304-drachcs/
|   |   \─ <red>gcc</red>/9.4.0/

icelake
|── <red>gcc</red>/9.4.0/
|── <blue>openmpi</blue>/4.1.3-lih7mwq/
|   \─ <red>gcc</red>/9.4.0/

skylake_avx512
|── <red>gcc</red>/9.4.0/
|── <red>intel</red>/2021.4/
|── <blue>intel-oneapi-mpi</blue>/2021.6.0-ad5zrqt/
|   \─ <red>gcc</red>/9.4.0/
|── <blue>openblas</blue>/0.3.18-cuu4pwk/
|   \─ <red>gcc</red>/9.4.0/
|── <blue>openmpi</blue>/4.1.3-lih7mwq/
|   |── <red>gcc</red>/9.4.0/
|   |── <blue>intel-mkl</blue>/2020.4.304-usztzez/
|   |   \─ <red>gcc</red>/9.4.0/

zen
|── <red>gcc</red>/9.4.0/
|── <red>intel</red>/2021.4/
|── <blue>intel-oneapi-mpi</blue>/2021.6.0-364ncu6/
|   \─ <red>gcc</red>/9.4.0/
|── <blue>openblas</blue>/0.3.18-wr2rrpa/
|   \─ <red>gcc</red>/9.4.0/
|── <blue>openmpi</blue>/4.1.3-bonsmsu/
|   |── <red>gcc</red>/9.4.0/
|   |── <blue>intel-mkl</blue>/2020.4.304-7t7xybh/
|   |   \─ <red>gcc</red>/9.4.0/

zen2
|── <red>gcc</red>/9.4.0/
|── <red>intel</red>/2021.4/
|── <blue>intel-oneapi-mpi</blue>/2021.6.0-vwuo3ee/
|   \─ <red>gcc</red>/9.4.0/
|── <blue>openblas</blue>/0.3.18-mf2vweb/
|   \─ <red>gcc</red>/9.4.0/
|── <blue>openmpi</blue>/4.1.3-velsqdk/
|   |── <red>gcc</red>/9.4.0/
|   |── <blue>intel-mkl</blue>/2020.4.304-iycblyc/
|   |   \─ <red>gcc</red>/9.4.0/
</code></pre>
where <red>compilers are red</red>, <blue>providers are blue</blue>, and **limited view default directories are bold**.
!!!note
    `intel` refers to the classic intel compilers (`icc`, `ifort`, `icpc`, ...).

    The `intel-oneapi-compilers-classic` module adds `intel` to modulepath.

## Hierarchy naming scheme ##
<pre><code>linux-ubuntu20.04-[architecture]/[compiler]/[compiler-version]/<red>[module-name]/[version]</red>
linux-ubuntu20.04-[architecture]/[provider]/[provider-version]/[compiler]/[compiler-version]/<red>[module-name]/[version]</red>
</code></pre>

* Nested providers are possible.
* Each of these paths have a prefix of `/modules/spack/share/spack/lmod/`.

## How to use the hierarchy ##
You can find modules anywhere in the hierarchy with the <red>`unity-module-find`</red> command.

From the full path of your desired module you should be able to tell which other modules need to be loaded first.

#### Example: ####
<pre><code>simonleary_umass_edu@login1:~$ module load gromacs
<strong><red>No module(s) or extension(s) found!</red></strong>
If the avail list is too long consider trying:

"module --default avail" or "ml -d av" to just list the default modules.
"module overview" or "ml ov" to display the number of modules for each name.

Use "module spider" to find all possible modules and extensions.
Use "module keyword key1 key2 ..." to search for all possible modules matching any of the "keys".
</code></pre>

<pre><code>simonleary_umass_edu@login1:~$ unity-module-find gromacs
Modules found:
linux-ubuntu20.04-cascadelake/openmpi/4.1.3-lih7mwq/intel-mkl/2020.4.304-w2r5zyv/gcc/9.4.0/<red>gromacs/2021.3</red>
linux-ubuntu20.04-haswell/openmpi/4.1.3-habm2fz/intel-mkl/2020.4.304-drachcs/gcc/9.4.0/<red>gromacs/2021.3</red>
linux-ubuntu20.04-skylake_avx512/openmpi/4.1.3-lsrnpnm/intel-mkl/2020.4.304-usztzez/gcc/9.4.0/<red>gromacs/2021.3</red>
linux-ubuntu20.04-x86_64/intel-oneapi-mpi/2021.6.0-h3cppyo/gcc/9.4.0/<red>gromacs/2021.3</red>
<strong>linux-ubuntu20.04-x86_64/openmpi/4.1.3-3rgk3nu/intel-mkl/2020.4.304-gmusbfh/gcc/9.4.0/<red>gromacs/2021.3</red></strong>
linux-ubuntu20.04-zen/openmpi/4.1.3-bonsmsu/intel-mkl/2020.4.304-7t7xybh/gcc/9.4.0/<red>gromacs/2021.3</red>
linux-ubuntu20.04-zen2/openmpi/4.1.3-velsqdk/intel-mkl/2020.4.304-iycblyc/gcc/9.4.0/<red>gromacs/2021.3</red>
</code></pre>

This is the module that I want:
<pre><code>linux-ubuntu20.04-x86_64/<strong>openmpi</strong>/4.1.3-3rgk3nu/<strong>intel-mkl</strong>/2020.4.304-gmusbfh/<strong>gcc</strong>/9.4.0/<strong>gromacs</strong>/2021.3
</code></pre>
In its path I can see `openmpi`, `intel-mkl`, `gcc`, and `gromacs`. Each of these are modules.

gcc is loaded by default, so I can ignore it. I can load the other modules in series in one line:
```
$ module load openmpi intel-mkl gromacs
```

!!!note
    `intel` as part of the path to a module refers to the classic intel compilers (`icc`, `ifort`, `icpc`, ...).

    The `intel-oneapi-compilers-classic` module adds `intel` to modulepath.


## Micro-architecture ##

Micro-architecture specific modules are optimized for particular CPU's, but can cause problems if used on other CPU's. If you want better performance for your job you can use these modules, but you should also use slurm constraints so that you always get a node with the correct type of CPU.

#### Slurm constraints ####
You can see possible constraints for each node on our [node list](../technical/nodelist.md).

**`sbatch` script:**
```
#SBATCH -C linux-ubuntu20.04-skylake_avx512
module load microarch/skylake_avx512
...
```

**`srun` interactive session:**
```
srun --pty -C linux-ubuntu20.04-skylake_avx512 bash
module load microarch/skylake_avx512
...
```

## Opt Out ##
While you can't put the directories back together, you can use the 'flat' module view rather than the limited view. This will add every directory of the hierarchy to your modulepath in an arbitrary order. There are problems with the flat view, like [module name conflicts](../hierarchy-change.md#module-name-conflicts). **This is not recommended**, and support will not be given for issues with the flat view.

To enable the flat view:
```
export LMOD_ENABLE_LIMITED_VIEW=false
```
And to make the change persist:
```
echo "export LMOD_ENABLE_LIMITED_VIEW=false" >> ~/.bashrc
```
The change will be applied on your next login shell. You can also reload the modulepath in your current shell:
```
source /etc/profile
```


### Learn more ###
[About the Hierarchy Change](../hierarchy-change.md)

[https://lmod.readthedocs.io/en/latest/010_user.html#module-hierarchy](https://lmod.readthedocs.io/en/latest/010_user.html#module-hierarchy)

[https://lmod.readthedocs.io/en/latest/080_hierarchy.html](https://lmod.readthedocs.io/en/latest/080_hierarchy.html)
