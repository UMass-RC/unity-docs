# Unity Software Overview

## Means of installing packages ##

### `apt` package manager ###
The Ubuntu system package manager `apt` downloads its packages pre-compiled from the [Ubuntu repository](https://packages.ubuntu.com/). These are placed in standard locations like `/usr/bin` so that they are always found in your `$PATH`. This can only be done by administrators. To avoid conflicts, most software is only available in one version. These packages will change with an (inevitable) [operating system update](http://www.releases.ubuntu.com/jammy/). The admin team is trying to avoid `apt` installs for research computing software.

Relevant Documentation:

* None

### Environment Modules ###
There are a wide variety of modules available with the <red>`module`</red> command. Most software requests are fulfilled here. These are compiled by the admins and are stored in `/modules/apps/` or in `/modules/spack/opt/spack/`.

Relevant Documentation:

* [intro to environment modules](module-intro.md)
* [using environment modules](module-usage.md)
* [module hierarchy](module-hierarchy.md)

### Conda ###
The conda package manager allows users to compile software easily and without admin privileges. Conda environments can be created for any software set, and can be enabled/disabled dynamically not unlike modules.

Relevant Documentation:

* [conda](conda.md)

### R package manager ###
Coming soon!

<!--
The R package manager allows users to compile software easily and without admin privileges.

Relevant Documentation:

* [R](R.md)
-->

### Docker (Singularity) ###
Coming soon!
