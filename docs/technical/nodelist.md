# Node List

The Unity cluster is a heterogeneous cluster. We plan to keep it a heterogeneous cluster. To clear confusion, a node list is below, with slurm constraints to refine your node selection.

!!! note
You can use the `-C` flag in your slurm jobs to batch your jobs to a specific set of nodes. If you don't include a constraint, your job may land in any number of nodes in the partition.

### CPU Nodes
{% include-markdown "../../sheets-to-md/output/cpu-nodes.md" %}

### GPU Nodes
{% include-markdown "../../sheets-to-md/output/gpu-nodes.md" %}
