# Node List #
!!! note
    The Unity cluster is a heterogeneous cluster. We plan to support a number of varying system hardware.

## Info ##
This page will be updated when cluster hardware changes. It will reflect the nodes available in each slurm partition.  

**Note** Nodes labeled with *Priority Hardware* are generally buy-in nodes which are available for general use, but your job may be temporarily suspended in favor of priority users, if running on those nodes. Nodes labeled with *Not Available* are not available for general use, but are still listed for reference.

## CPU Partition ##
#### Nodes 1-8 ####
**Type** Lenovo ThinkSystem SD530  
**CPU** 2x Intel Xeon Gold 6126 (12 Cores, 24 Threads)  
**RAM** 192 GiB (Node(s) 1,5-8), 384 GiB (Nodes 2-4)  

#### Nodes 13-25 ####
**Type** Dell Poweredge R640  
**CPU** 2x Intel Xeon Gold 6148 (20 Cores, 40 Threads)  
**RAM** 192 GiB  

#### Nodes 26-32 *Priority Hardware* ####
**Type** Lenovo ThinkSystem SR635  
**CPU** 1x AMD EPYC-Rome 7402 (24 Cores, 48 Threads)  
**RAM** 128 GiB  

## GPU Partition ##
#### Nodes 9-10 ####
**Type** Lenovo ThinkSystem SR650  
**CPU** 2x Intel Xeon Silver 4110 (8 Cores, 16 Threads)  
**GPU** 2x nVidia Tesla V100 - Driver 440.1  
**RAM** 192 GiB  

#### Nodes 11-12 ####
**Type** Dell Poweredge R740  
**CPU** 2x Intel Xeon Gold 6140 (18 Cores, 36 Threads)  
**GPU** 2x nVidia Tesla V100 - Driver 440.1  
**RAM** 192 GiB