!!! note
    The Unity docs are still a work-in-progress. Some docs may be missing, or incomplete. If you would like to contribute to these docs, please submit PRs to the upstream repository [here](https://github.com/UMass-RC/unity-docs).

# Introduction to Unity #
This introductory tutorial will help you build an understanding of what an HPC Cluster, or **High Performance Computing Cluster** is, and how to most effectively utilize it.


### Defining some Terms ###
<!--At its most basic level, you are learning how to use a **cluster**. A cluster is many servers (or computers) joined together in an effort to work together, where a single server is known as a **node**. Unity is an **HPC**, or High Performance Computing cluster. This means we focus most on computational power and efficiency, as the name entails. The primary use case of Unity is by researchers wanting more computational power than what is available on their own. -->

When working with HPCs, it can be helpful to understand what's happening behind the scenes. This tutorial will go over what an ***HPC*** is. A **H**igh **P**erformance **C**omputer--**HPC**-- is super computer that is made up of many powerful computers that are called **Clusters**. A **Cluster** is made up of powerful computer parts that are connected to each other over a local network--this is akin to the motherboard on your local desktop/laptop. But for the purposes of this tutorial, it suffices to think of a **Cluster** as powerful computer, structurally similar to your personal desktop/laptop at home, just a lot more powerful.

Think about your personal laptop/desktop. When you use your computer, the computer's Operating System (OS) decides what resources (cpu, ram, etc.) should be used, based on what you are doing at that time. For example, if you were to open the computer's calculator punch in some numbers and multiply them, the computer's OS would determine how much of the computer's CPU should be used to perform the calculation, and how much of the computer's graphics card to use in rendering the Graphical Interface of the calculator. In some cases, the rendering of the Graphical Interface and calculations could both be performed on the just the graphics card, or the CPU.

Keeping with this idea of your OS dictating the distribution of computer resources, let's examine how a Cluser distributes its resources for an uploaded **job**; a **job** is any operation or task you run on the cluster. When a job is loaded onto the Unity cluster, what is known as a **scheduler** determines what Cluster resources to give you, just like your personal computer's OS system would. You can picture the cluster as a scaled-up version of a single personal computer. Making up the cluster are **Nodes**. A **Node** is the part of the cluster that jobs get run on, like a GPU or CPU. When working with Clusters, it's easier to call these computer parts Nodes because sometimes just one of these computer parts is sufficient to run a job.

<h4>In summary:</h4>

* **High Performance Computers (HPC)**: Super Computers made up of many **Clusters** that are interconnected over a local (within the same building) network.

* **Cluster**: Clusters are the computers that make up **High Performace Computers (HPC)**. They themselves are computers, and can be thought of like your desktop/laptop at home.

* **Scheduler**: Linux based distributer of resources. If you request 2 CPUs, and 2 GPUs, the Scheduler is what will make those resources available for you. This is akin to your computer's OS in that it assigns parts (**Nodes**) of the computer to you in order for those Nodes to run your software. The Scheduler for the Unity Cluster is called <a href="https://support.ceci-hpc.be/doc/_contents/QuickStart/SubmittingJobs/SlurmTutorial.html" target="_blank" title = "Open new tab describing Slurm">**Slurm**</a>. **Slurm** sits on the Unity Cluster, and distributes the resources of the Unity Cluster accordingly.

* **Nodes**: Using the laptop/desktop comparison, a **Node** is akin to an individual part of the desktop/laptop, like the CPU or GPU where computations & programs are run.

* **A Job**: When something is uploaded onto the **Cluster** and used to run an operation, or when Cluster resources are utilized to run a program, this use of the **Cluster's** resources is called a **Job**.


### How Unity Works ###
<!-- While you may not need to master every bit of the operation here at the Unity Cluster, it is important that you generally know how the cluster operates, because it can help your troubleshooting in the future. Below is a simplified diagram of the structure of Unity.  -->

Here is a general step by step process that governs how the Unity Cluster works:

![Unity Diagram](res/unity.png)

1. The client connects to Unity using [SSH](connecting/ssh.md), or the [Jupyter Lab](connecting/jupyter.md). (Bottom right of image)
    * When you log into the Unity Cluster, you can interact with the Cluster either using Jupyter Lab, or Terminal. 
    * If you are not comfortable working with a Linux SSH terminal interface, it it recommended that you use Jupyter Lab.
2. Once connected, a job is requested through the scheduler, and the scheduler adds your requests to each *necessary que*.
    * '*Necessary*' because if the job requested requires 2 GPUs and 1 CPU then you need 2 positions in the GPU que and 1 position in the CPU que. This means that the wait time to get your required resources could be longer, but this doesn't mean the runtime of your job will also be longer.
3. Once resources are available (cores, gpu, memory, etc.), the scheduler starts your job.
4. Once your job completes, the result returns to the client.


#### 1. Connecting to the cluster ####
You can connect to Unity in two ways, an SSH connection (the standard linux console), or an instance of JupyterLab:

[JupyterLab](connecting/jupyter.md) is the easiest to get up and going. When connecting the portal, click on JupyterLab tab at the bottom of the options list on the left side of the window. This will take you to the JupyterHub for Unity, which looks like this: 

![JupyterHub](res/JupyterHub Image.png)

You will be asked to select what computer resources you want/need for the job you want to upload. Once you attempt to spawn your notebook and resources become available, you will be able to use JupyterLab as if it is running on your own computer.

[SSH](connecting/ssh.md) is the more traditional method of using an HPC cluster. You will connect to the login node of unity, and you will be responsible for starting your own jobs. This can be more useful than jupyter for jobs that last a long time that must be left unattended, or to have much more refined control over the resources allocated for your job.

#### 2. Requesting Resources ####
If you are on an SSH connection, you will have to manually request resources. Once you decide on what resources you want, you will submit that information to the scheduler, which will place you in a queue. If your resources are available immediately, your request will return right away, if not, you will be held in the queue until your requested resources become available.

Requesting resources in the cluster and all parameters allowed is discussed in more detail [here](slurm/index.md).

#### 3. Starting Job ####
Once the scheduler has started your job, it will run on some node in the cluster, using some resources that were defined by your parameters. It is not important what node the job runs on from the point of view of the client.

#### 4. Ending Job ####
Once the job has finished, the scheduler will return whatever info you requested in your parameters.