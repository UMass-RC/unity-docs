# Node List #
!!! note
    The Unity cluster is a heterogeneous cluster. We plan to keep it a heterogeneous cluster. To clear confusion, a node list is below, with slurm constraints to refine your node selection.

## Info ##
This page will be updated with new additions to the cluster.

!!! note
    Nodes labeled with *Priority Hardware* are generally buy-in nodes which are available for general use using a partition flagged with `-preempt`, such as `cpu-preempt`, but your job may be temporarily suspended in favor of priority users. Your job's state will be saved in memory and will be automatically resumed when there is room on the allocated nodes once again.

!!! note
    You can use the `-C` flag in your slurm jobs to batch your jobs to a specific set of nodes. If you don't include a constraint, your job may land in any number of nodes in the partition.

## Compute Nodes ##
#### Nodes 1-8 ####
**Type** Lenovo ThinkSystem SD530  
**CPU** 2x Intel Xeon Gold 6126 (12 Cores, 24 Threads)  
**RAM** 192 GiB (Node(s) 1,5-8), 384 GiB (Nodes 2-4)  
**Contraints** len_sd530_2018,intel

#### Nodes 13-25 ####
**Type** Dell Poweredge R640  
**CPU** 2x Intel Xeon Gold 6148 (20 Cores, 40 Threads)  
**RAM** 192 GiB  
**Contraints** dell_r640_2020,intel

#### Nodes 26-32 *Priority Hardware* ####
**Type** Lenovo ThinkSystem SR635  
**CPU** 1x AMD EPYC-Rome 7402 (24 Cores, 48 Threads)  
**RAM** 128 GiB  
**Contraints** cee_len_sr635_2020,amd

#### Nodes 68-75 *Priority Hardware* ####
**Type** SuperMicro SBI-4429P  
**CPU** 2x Xeon Silver 4215R (8 Cores, 16 Threads)  
**RAM** 192 GiB  
**Contraints** astro_smicro_sbi4429pt2n_2021,intel

## GPU Nodes ##
#### Nodes 9-10 ####
**Type** Lenovo ThinkSystem SR650  
**CPU** 2x Intel Xeon Silver 4110 (8 Cores, 16 Threads)  
**GPU** 2x nVidia Tesla V100 - Driver 440.1  
**RAM** 192 GiB  
**Contraints** len_sr650_2018,intel

#### Nodes 11-12 ####
**Type** Dell Poweredge R740  
**CPU** 2x Intel Xeon Gold 6140 (18 Cores, 36 Threads)  
**GPU** 2x nVidia Tesla V100 - Driver 440.1  
**RAM** 192 GiB  
**Contraints** len_sr650_2018,intel

#### Nodes 35-67 *Priority Hardware* ####
**Type** ASRock  
**CPU** AMD Ryzen Threadripper 1900X (8 Cores, 12 Threads)  
**GPU** 2x Nvidia GeForce RTX 2080  
**RAM** 32 GiB  
**Constraints** astro_asrock_x399_2020,amd  

#### Nodes 35-67 ####
**Type** Gigabyte  
**CPU** 2x Intel Xeon Silver 4214R (12 Cores, 12 Threads)  
**GPU** 8x Nvidia GeForce RTX 2080ti  
**RAM** 192 GiB  
**Constraints** ials_gbyte_g291280_2021,intel  