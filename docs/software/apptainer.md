# Containers #

Containers allow you to disregard all of the software installed on a given machine,
and instead run a completely different software stack off the same kernel.
This means you can run Debian, CentOS, Arch Linux, all on on Unity.
Containers run your software in an isolated environment, which avoids unwanted interference
and also makes your software very consistent and reproducible.

If you're familiar with containers, then you've probably heard of Docker.
The problem with Docker is that it requires root permissions, which makes it un-suitable for HPC.
Apptainer works similarly to Docker but it manages to build and run containers without root access.

To use Apptainer you will need to first load the Apptainer module:
```
module load apptainer/1.1.5
```

## Building container images ##
### Pull a container from Online ###
You can download and a recipe from online and build it into an image in one simple command:
```
apptainer pull <output-image-file> <container-location>
apptainer pull lolcow.sif docker://sylabsio/lolcow:latest
```

### Write your own Recipe ###

You might want to modify a container you found online.
Rather than making your image into a sandbox and editing the files by hand,
best practice would be to write your modifications into a recipe.
This makes your software environment reproducible.

Here's an example of a simple recipe `train.def`:
```
Bootstrap: docker
From: ubuntu:focal

%post
apt update && apt install -y sl

%runscript
/usr/games/sl
```

!!!note
    Apptainer requires a recipe in the form of a definition (.def) file.
    You can convert a dockerfile to a .def file using [Singularity Python](https://singularityhub.github.io/singularity-cli/recipes):

    `module load spython`

    `spython recipe ./my-dockerfile > my-def-file`

Once your recipe is complete, build it:
```
apptainer build <output-image-file> <recipe-path>
apptainer build train.sif train.def
```

!!!note
    Sometimes a build will fail with an error related to bind-mounting `/work`.
    If mounting `/work` at build-time is not required, then you can just edit `APPTAINER_BINDPATH`
    so that Apptainer will no longer try to mount it.

Useful arguments:

* **bind mount (`-B --bind`)**: make a directory on Unity's filesystem available inside the container.
This is a comma-delimited list of directory mappings of the form: `source:destination`.
Other options are also available, see the documentation.
    * This is also determined by environment variable `APPTAINER_BINDPATH`, which has a default value:
    `/work,/home,/nese,/project,/gypsum,/scratch,/modules,/nas,/datasets`
* **Docker login (`--docker-login`)**: login to a Docker repository.
* **sandbox (`-s --sandbox`)**: build the container in a writable directory, rather than a .sif image.

Learn More:

* [Apptainer docs: pull](https://apptainer.org/docs/user/main/cli/apptainer_pull.html)
* [Apptainer docs: definition file](https://apptainer.org/docs/user/1.0/definition_files.html)
* [Apptainer docs: build](https://apptainer.org/docs/user/main/cli/apptainer_build.html)


## Using container images ##
Given an Apptainer image (`.sif` or sandbox directory), you can:

* run the recipe's `runscript` with `apptainer run <image-file> <optional runscript arguments>`
* start a shell with `apptainer shell <image-file>`
* run a specific command with `apptainer exec <image-file> <command>`

Useful arguments:

* **nvidia (`--nv`)**: enable Nvidia GPU support
* **bind mount (`-B --bind`)**: see description above
* **clean environment (`-e --cleanenv`)**: don't export any environment variables into the container.
* **fake root access (`-f --fakeroot`)**: simulate root access inside the container.

Learn More:

* [Apptainer docs: run](https://apptainer.org/docs/user/main/cli/apptainer_run.html)
* [Apptainer docs: exec](https://apptainer.org/docs/user/main/cli/apptainer_exec.html)
* [Apptainer docs: shell](https://apptainer.org/docs/user/main/cli/apptainer_shell.html)
