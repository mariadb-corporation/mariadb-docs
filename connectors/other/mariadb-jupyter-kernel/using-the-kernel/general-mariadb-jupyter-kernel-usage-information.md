---
description: >-
  General usage guide for the MariaDB Jupyter Kernel, explaining how to open
  a notebook, select the kernel, try it via MyBinder, and work with sample
  notebooks on GitHub.
---

# General MariaDB Jupyter Kernel Usage Information

If you installed the kernel, installed its kernelspec and you have MariaDB installed on your system, you just need to open [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/), and when you create a new notebook, pick MariaDB as your kernel.

![](../../../.gitbook/assets/lab_open.png)

For some sample notebooks, check out the [notebooks](https://github.com/MariaDB/mariadb_kernel/tree/master/notebooks) directory in our GitHub repository page. Those should guide through what you can do with [mariadb\_kernel](https://github.com/MariaDB/mariadb_kernel).

You can also try [mariadb\_kernel](https://github.com/MariaDB/mariadb_kernel) using the amazing [MyBinder](https://mybinder.org) platform by clicking this badge

or you can click on the `Try MariaDB @ binder` badge from the [mariadb\_kernel GitHub repo](https://github.com/MariaDB/mariadb_kernel).

This takes absolutely no effort except one click; [Binder](https://mybinder.org) does everything for you!\
It sets up a MariaDB server and all the installation of the kernel and its requirements. Once this process is done, you will be redirected to a live notebook where you can type your commands.

Be aware that MyBinder does not save any state, whatever you change in a notebook in a session (unless you save the notebook locally yourself) will be lost once you close the page.\
We recommend using the MyBinder platform to try the MariaDB kernel when you quickly want to try a statement, if you'd like to see the latest features of the kernel in action or if you want to reproduce some results that a colleague has sent you. For all other use-cases we recommend you install the kernel and edit your notebooks locally.

Please be a bit patient when you launch MyBinder, the more people are clicking the MyBinder link, the higher the chances are that when you launch it, the Docker image of the kernel is already cached.\
If by any chance you see a Docker image building in the MyBinder logs, it shouldn't take more than a minute. Please be patient, if you wait one minute, it means you're helping all the other people launching the kernel after you to wait less! :-)


{% @marketo/form formId="4316" %}
