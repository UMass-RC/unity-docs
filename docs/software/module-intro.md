# Intro. to Environment Modules #

As a Unity user, you have access to a wide variety of software. Making all of this software available simultaneously and without conflicts is a complex problem, and the solution is Environment modules.

An **environment** is a set of shell variables of the form `KEY="VALUE"`.

!!! note
    You can see your current environment using the <red>`env`</red> command.

### The `PATH` environment variable ###
`$PATH` is a list of directories (folders) delimited by colons.
```
$ echo $PATH
/usr/local/bin:/usr/bin:/bin
```
Most of the commands you use in the shell are actually executable files somewhere on the filesystem. When you enter a command, the shell searches the directories in `$PATH` (from left to right) for an executable by that name. If there are multiple executables of the same name, whichever is found earlier in the `$PATH` (further to the left) is used.

**This means that the commands available in your shell can be changed by changing your environment variables.**

### Modules ###
Environment modules are scripts that modify your environment. We use modules to add new directories to your `$PATH`, making the executables within available for use. We 'prepend' the `$PATH`, making this new directory furthest to the left. This makes sure that the executables within are chosen first by the shell when you call their name.

```
$ which python3
/usr/bin/python3
$ module load python/3.9.1
$ which python3
/modules/apps/python/3.9.1/bin/python3
```
```
$ echo $PATH
/usr/local/bin:/usr/bin:/bin
$ module load python/3.9.1
$ echo $PATH
/modules/apps/python/3.9.1/bin:/usr/local/bin:/usr/bin:/bin
```

!!!note
    The scripts that modify your environment are called "modules", "modulefiles", or "environment modules".
    Our module system as a whole is called "Lmod".
    There is another module system out there called "Tmod" or "Environment Modules", which Lmod is based off of.
    These names can be confusing.

### Learn More
[the `PATH` Environment Variable](https://superuser.com/questions/284342/what-are-path-and-other-environment-variables-and-how-can-i-set-or-use-them)

[Lmod documentation](https://lmod.readthedocs.io/en/latest/010_user.html)
