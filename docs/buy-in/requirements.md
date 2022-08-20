# Hardware Requirements

!!! note
    This page is here for reference. Please do not purchase hardware intended for the Unity cluster until checking with the Unity team.

## General Node Requirements

Each server purchased is required to have the following hard requirements:

* IPMI 2.0 supported BMC with remote KVM built-in with discrete RJ45 management port
* Physical Ports
    * VGA Port
    * USB Port
        * 10G SFP+ Port or 25G SFP28 port
            * *Note: If you require higher bandwidth for your nodes, that can be discussed, but will most likely require purchasing an addition switch (see below)*
        * At least 250GB boot SSD (Solid-state drive)
        * 2x redundant PSU (Power supply unit)

Each server purchased is recommended to have the following soft requirements:

* 2x boot drive for redundancy

## Storage Node Requirements

* The storage controller should be an HBA card or a RAID card that can operate in HBA mode, since we will be using ZFS software raid.
* At least 2 data plane (10/25G) ports for redundant connection.
* 2x boot drives for redundancy

## Network Equipment

On a case-by-case basis, it may be necessary to purchase network switches if enough hardware was purchased to span a rack.

If that is the case, each rack requires the following for the top-of-rack data switch:

* For 10/25G Nodes Mellanox SN2410
* For 100G Nodes Mellanox SN2700

In addition, a 1G switch is required for IPMI connection.

* For IPMI Any 1G switch that has L2 capability (Mellanox preferred)

