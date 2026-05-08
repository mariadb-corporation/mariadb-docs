---
description: >-
  Install the MariaDB Jupyter Kernel via pip using either a quick setup for
  existing environments or a complete Miniconda-based setup, with platform
  support notes for Linux and macOS.
---

# MariaDB Jupyter Kernel Installation

The [mariadb\_kernel](https://github.com/MariaDB/mariadb_kernel) project uses the [MariaDB command-line client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/mysql-command-line-client) under the hood as a child process, thus having MariaDB installed on your system is a hard requirement in order to be able to use the kernel.

If you don’t have it already installed, you can download the binaries from [here](https://mariadb.org/download/).\
You also need [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) or [Notebook](https://jupyter.org/)

If your MariaDB binaries are not in `PATH`, see the [Configuring](configuring-the-mariadb-jupyter-kernel.md) section to see how you can point the kernel to the right binaries path.

## Quick Installation Steps

Follow these steps if you already have a clean [Python](https://www.python.org/download/releases/3.0/) environment and [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) installed on your computer.

1. Install the kernel

```bash
python3 -m pip install mariadb_kernel
```

2. Install the kernelspec so that the kernel becomes visible to [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/)

```bash
python3 -m mariadb_kernel.install
```

## Complete Installation Steps

This guide helps you set up a fresh [Miniconda](https://docs.conda.io/en/latest/miniconda.html) environment where you can install the kernel and the Jupyter applications without interfering with your normal environment.

1. Download and install [miniconda](https://docs.conda.io/en/latest/miniconda.html)

```bash
# After you downloaded the script run:
sh ./Miniconda3-latest-Linux-x86_64.sh
```

2. Create a new environment

```bash
conda create -n maria_env python=3.7
```

3. Activate the new env

```bash
# You should see the terminal prompt prefixed with (maria_env)
conda activate maria_env
```

4. Install [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/)

```bash
conda install -c conda-forge jupyterlab
```

5. Install the kernel

```bash
python3 -m pip install mariadb_kernel
```

6. Install the kernelspec so that the kernel becomes visible to [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/)

```bash
python3 -m mariadb_kernel.install
```

## Platform Coverage

Our plan is to make [mariadb\_kernel](https://github.com/MariaDB/mariadb_kernel) as platform independent as [Jupyter](https://jupyter.org) is. That means, fully functional on at least Linux, macOS and Windows.

Unfortunately at the moment, we can only guarantee it should work fine on POSIX-compliant systems, i.e. most Linux distributions and macOS as long as the prerequisites of the project are present on your system.\
This limitation is inherited from particular Python APIs that use POSIX-specific system calls and also from our dependency package [Pexpect](https://pexpect.readthedocs.io/en/stable/) which has certain limitations on Windows systems.

Please create an issue [here](https://github.com/MariaDB/mariadb_kernel/issues) or vote (just write a quick comment saying that issue affects you as well) for an existing one if you’re on a particular platform that [mariadb\_kernel](https://github.com/MariaDB/mariadb_kernel) doesn’t currently work on. This will help us understand how we should focus our development efforts.


{% @marketo/form formId="4316" %}
