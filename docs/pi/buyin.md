# Buy-In Model

The Unity cluster offers a buy-in model where the PI will purchase hardware which will be integrated into the Unity cluster ecosystem, with priority given to the purchaser of the new hardware.

!!! note
    The information below is intended to be a reference for PIs who are thinking about the buy-in model for the Unity cluster. All quotes should be approved and modified as needed by the Unity cluster team prior to the PI purchasing anything. This is particularily important for specific types of cables.

## Why buy-in? ##

The Unity cluster ecosystem offers and easy to use environment for data scientists with multiple front-ends, including traditional console access, as well as the JupyterLab interface. Since buy-in nodes are integrated into the cluster the PI does not have to worry about deployment or administration of the systems. In addition, since the Unity cluster has centralized service nodes, setting up a head node is generally not required.

Even though your buy-in nodes will be able to used by users outside of your group, the PI will be able to select exactly how much priority is given to the lab. See [priority queues]() for more details.

## What to buy? ##

### Compute Nodes

**Minimum requirements for compute node**  

* IPMI controller with discrete managment port and remote KVM
* At least 10 GiB/s NIC
* amd64/x86_64 architecture CPU
* Redundant PSU

### Storage Nodes

In some cases the PI may want their own storage node. It is important to note that while the Unity cluster admins will maintain the storage node and address incidents, the PI is responsible for providing "cold spare" storage drives in the event of drive failure, or risk data loss. The storage will be mounted on every node of the cluster.

**Minimum requirements for storage node**  

* IPMI controller with discrete management port and remote KVM
* HBA card(s) (or a RAID controller that can properly operate in HBA mode) - this is because we use ZFS software RAID as a more reliable data storage solution.
* Redundant PSU

### Persistent Service Nodes

Some labs may require a persistent service running on the cluster, for example, a SQL database. For this, the PI and their group will have access to this node to setup as they please, and that node will stay persistent in the Unity ecosystem. Depending on availability, a private container on an existing Unity service node can be setup.

**Minimum requirements for service node**  

* IPMI controller with discrete management port and remote KVM
* Redundant PSU

### Network Equipment

For any node that is ordered, the appropriate cables must also be ordered. For a standard node that would include:

* 3 meter / 10 ft copper CAT6 ethernet cable (for IPMI port) ([example](https://www.fs.com/products/57408.html?attribute=2202&id=168537))
* 3 meter / 10 ft fiber LC Duplex Multimode (850nm) cable ([example](https://www.fs.com/products/40233.html)), with associated tranceivers on both ends **OR** 3 meter / 10 ft copper DAC cable ([example](https://www.fs.com/products/40141.html?attribute=1322&id=222612))

If the buy-in is large enough to fill at least most of a 44U server cabinet, the PI may be asked to purchase a TORS (top-of-rack switch) for the data plane, and a 1G TORS for the management network. It may also be necessary to buy certain equipment if there are specific operational requirements, to be discussed with the Unity cluster team.

**Minimum requirements for data switch**  

* Ethernet switch (ie. not InfiniBand)
* Redundant PSU
* At least 4 100 GiB/s QSFP28 or higher ports for uplink
* Sufficiently large amount of end-device ports to support all the hardware in the rack (48 port is standard)
* Dell or Mellanox branded switches are preferred
* Example: Dell s5048-ON, Dell s4048-ON, Mellanox SN2410

**Minimum requirements for IPMI switch**  

* Sufficiently large amount of 1G RJ45 ports to support all the hardware in the rack (48 port is standard)
* Dell or Mellanox branded switches are preferred
* Example: Dell s3048-ON

## How to get started?

Send an email to [hpc@umass.edu](mailto:hpc@umass.edu) with your requirements.