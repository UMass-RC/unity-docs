# Types of Priority

Nodes you purchase will be included in the Unity ecosystem - meaning you'll be able to use the web portal, access all the same storage, and access JupyterLab. When purchasing hardware for integration with Unity, there are three types of "priority" that you can request for your hardware.

!!! note
    The below only applies to compute hardware, storage hardware will almost always be owned by the purchasing PI only and not shared with users.

## Preemption (Strictest)
Priority nodes are added to: preempt partitions (cpu-preempt/gpu-preempt), and a newly created lab partition for use only by your lab

Preemption is enabled in this mode. This means that if a priority user (member of the lab) wants to start a job but the nodes are full, non-priority jobs will be requeued on the spot for priority jobs. The requeued job will start again once resources are available. Your nodes are added to cpu/gpu-preempt partition depending on the type, in addition to the priority partition. This results in immediate access to the full capabilities of your own hardware, but the strictest limitations for general users of the cluster.

## Queueing Priority
Priority nodes are added to: general partitions (cpu/gpu), and a newly created lab partition for use only by your lab

Preemption is disabled in this mode, but your lab still gets queueing priority, which means if jobs are waiting to start on your hardware, your lab's jobs will always start first and take precedent. However, if your nodes are already full of general jobs, you will not be able to access this space until those jobs are done. As a result, we generally restrict general jobs to short queue timing (24 hours) such that priority users will not need to wait over a week etc. for non-priority jobs.

## No Priority
In this mode no priority partition is created, and your nodes are contributed directly to the general partitions. It is not clear how this will affect billing for general hardware yet.
