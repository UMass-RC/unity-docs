
# Common Terms
Here are some definitions for common terms used in this documentation:

## HPC Jargon ##

**High Performance Computer Cluster (HPC Cluster)**: A system made up of many smaller computers that behaves like one large computer. HPC allows a user to utilize the power of many computers simultaneously.

**Scheduler**: Distributer of resources. If you request 2 CPU cores for your **job**, the **scheduler** will reserve those cores and connect you to them. In a multi-threaded computer, the operating system also distributes resources and manages tasks like a job scheduler. The Scheduler for the Unity cluster is called [Slurm](https://support.ceci-hpc.be/doc/_contents/QuickStart/SubmittingJobs/SlurmTutorial.html).

**Node**: One of the computers that serves as part of an **HPC cluster**. See [node list](technical/nodelist.md).

* **Login Node**: This is what you are running on when you first [log in to Unity via ssh](connecting/ssh.md). Only small tasks should be run here. The login nodes have strict CPU and memory limits to disincentivize running big tasks.
    * Also known as a **Head Node** in other clusters.
* **Compute Node**: These are nodes intended for your big tasks. These are accessed by [scheduling jobs in Slurm](slurm/index.md).

**Job**: The task that you provide for the cluster to execute, and what resources should be allocated to do so.

**Partition**: A grouping of nodes. See [partition list](technical/partitionlist.md).

**Queue**: Often used interchangably with **partition**.

![Unity Diagram](res/unity.png)

**Principal Investigator (PI)**: The individual responsible for a research grant. All users on Unity must be tied to a PI. [Learn more about PI's](https://www.umass.edu/research/what-principal-investigator-pi-and-who-eligible)

## Software Jargon ##

**Package**: Installed software. Includes binaries, libraries, and other files. Typically cannot be moved about the filesystem once installed.

**Binary**: An executable file.

**Library**: Allows distribution of C code about the filesystem. [Learn more about libraries](https://2066.medium.com/what-is-a-c-library-d5501c4a56fc)

**Module**: Script that modifies your environment to include a package. See [environment modules](module-intro).

**Environment**: Set of environment variables. Defines the state of your current login **shell**. See [environment modules](module-intro).

**Conda environment**: Set of installed packages. Activating a conda environment modifies your **shell** environment to include these packages. See [conda](software/conda.md).

**Compile**: A compiler takes source code and turns it into binaries and libraries. Source code alone cannot be run by an operating system, it must be compiled into machine code or interpreted by an interpreter. C is compiled, Python is interpreted (sort of).

* [Learn more about compilers](https://www.freecodecamp.org/news/what-is-a-compiler-in-c/)
* [Compiled vs Interpreted Languages](https://www.freecodecamp.org/news/compiled-versus-interpreted-languages/3)

## Linux Jargon ##

**Interface**: The connection between you and your program.

* **Graphical User Interface (GUI)**: The general term for graphical applications, where you click buttons, type in text boxes, and see visuals. Anything that uses the mouse.
* **Command Line Interface (CLI)**: The general term for text-based applications, where you enter commands and then read whatever comes out. Uses only the keyboard.

**Console**: Often used interchangably with **terminal**.

**Terminal**: The terminal is the graphical application that you type your commands in. In windows, this can be the the Command Prompt (`cmd`) or the [Windows Terminal App](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701) (recommended). In Mac, it's just called Terminal. The terminal runs the shell.

* You can think of the terminal as just the borders of the window where you type commands. You can think of the shell as what's inside those borders.

**Shell**: The shell interprets your commands and starts processes on the operating system. It depends on the terminal to take input from the user and to display output to the user. The shell stores your environment and allows you to write shell scripts. [Learn more about shells](https://www.educba.com/what-is-shell-in-linux/)

## Linux Filesystem Jargon ##

**Symlink**: Shortcut.

**Directory**: Folder.

* **Current Working Directory (CWD)**: The directory that is currently open in your program (often the shell). In a **path**, the CWD can be referenced with the `.` symbol.

* **Parent Directory**: The parent is the directory that is one above *this* directory. Every directory has a parent, except the **root**. In a **path**, the parent directory can be referenced with the `..` symbol.

**Path**: A path is a list of directories delimited by `/` slashes, followed by the name of a file. If the filesystem were a city, a path would be the directions to your apartment. Each directory in the path would be which road to take at the next crossroads.

* **Relative Path**: A path that does not start from a known landmark but from your current location `CWD`.
    * `./.conda/envs/testName/bin/activate` is a relative path.
* **Absolute Path**: A path that starts from a known landmark **root** `/`.
    * `/home/$USER/.conda/envs/testName/bin/activate` is an absolute path.

**Root**: The filesystem can be visualized like a tree (not the plant, the [data structure](https://www.google.com/search?q=tree+data+structure&hl=en&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiQ3Kae1pL7AhXREFkFHRt-AE0Q_AUoAXoECAEQAw&cshid=1667501261642934&biw=1238&bih=1299)). The root of the tree is the directory from which all others descend from.