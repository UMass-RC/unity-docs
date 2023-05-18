# Unity GPU Documentation

Graphics Processing Units (GPUs) provide a powerful tool to run code in
parallel at a larger scale than traditional CPU parallel workload. This comes
at the tradeoff with slower communication times. It is important to note that
using one or more GPUs does not guarantee that code will run faster, however
many popular software packages have been modified to incorporate GPUs for
better performance.

## Requesting GPU Resources

Requesting GPU access on Unity can be done via Slurm either for an interactive session or using a batch script.
Below are a minimal example of both interactive and batch jobs.

!!! Note: Not all software is able to use GPUs, and some software will require
special options, dependencies, or alternate versions to be able to run with
GPUs. Please ensure your software supports GPU use before requesting these
resources.

---

**Interactive**
```bash
srun -p GPU-preempt -t 02:00:00 --gpus=1 --pty /bin/bash
```


 **Batch Script**
```bash
#!/bin/bash

#SBATCH -p GPU-preempt # Submit job to to GPU-preempt partition
#SBATCH -t 02:00:00    # Set max job time for 2 hours
#SBATCH --gpus=1       # Request access to 1 GPU

./myscript.sh
```
---


## GPU-Enabled Software

**CUDA**: NVIDIA's parallel computing platform. A version of this will typically be required to be loaded for most GPU jobs, as this allows access to this NVIDIA compiler suite (nvcc, nvfortran) as well as the NVIDIA GPU profiling tool (nsys). 

**Note: be sure to check which version(s) of cuda are compatible with the software that is being used.**

- cuda/6.0
- cuda/6.5.14
- cuda/7.0
- cuda/7.5.18
- cuda/8.0
- cuda/8.0.61
- cuda/9.0
- cuda/9.2
- cuda/9.2.88
- cuda/10.0.130
- cuda/10.1.243
- cuda/10.2.89
- cuda/11.0.1
- cuda/11.0.3
- cuda/11.3.1
- cuda/11.4.0
- cuda/11.5.0
- cuda/11.8.0

**cuDNN**: Cuda Deep Neural Network library, often used to accelerate deep learning frameworks in Keras, PyTorch, TensorFlow, and others.

- cudnn/cuda10-7.5.0.56
- cudnn/cuda11-8.4.1.50
- cudnn/8.2.4.15-11.4

**OpenMPI**: The OpenMPI compilers for MPI compiled against the cuda compilers. This is necessary to use if software that uses both MPI and GPU acceleration.

- openmpi/4.1.3+cuda11.6.2-mpirun
- openmpi/4.1.3+cuda11.6.2

In addition to these, many programming languages are able to use one or more GPUs.

- Python
- Matlab
- Julia
- C++ (using Cuda or OpenACC)
- Fortran (using Cuda or OpenACC)
- C (using Cuda or OpenACC)



### Setting up a TensorFlow GPU Environment

Some software, especially with python, requires setting up the environment in a specific way.

For python programs that can use GPU, such as TensorFlow, this is best done using a conda environment.

The steps to set up a conda environment for TensorFlow is shown below:

---

1. request an interactive session with a GPU node

```bash
srun -t 01:00:00 -p GPU-preempt --gpus=1 --mem=16G --pty /bin/bash
```

2. load modules

```bash
module load miniconda/22.11.1-1
module load cuda/11.4.0
module load cudnn/cuda11-8.4.1.50
```

3. create the environment

```bash
conda create --name TensorFlow-env python=3.9 
```

Note: TensorFlow 2 requires a python version of at least 3.9

```bash
conda activate TensorFlow-env
pip install TensorFlow
pip install tensorrt
conda install ipykernel
```

Note: if you do not request enough memory, TensorRT will fail to install

4. Add environment to Jupyter 
```bash
python -m ipykernel install --user --name TensorFlow-env --display-name="TensorFlow-Env"

---

After completing these steps, a new kernel with the name "TensorFlow-Env" will be shown with new Open OnDemand sessions

