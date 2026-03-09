---
description: >-
  Documentation for the runvm script, which manages virtual machine lifecycles
  during the Buildbot testing process.
---

# Buildbot runvm

One type of build we do in BuildBot is to build and test [MariaDB](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/mariadb/README.md) binary\
packages for the platforms we release on. We build and test packages for Debian\
(4 and 5), Ubuntu (8.04 to 10.04), Centos 5, and generic Linux; amd64 and i386\
architectures. This testing is done with virtual machines run in [KVM](https://www.linux-kvm.org/page/Main_Page).

To better control the startup and shutdown of the virtual machines we use a\
small wrapper around KVM we developed called **runvm**. The purpose of this\
tool is to make it easy to boot up a virtual machine, run some build commands\
inside it, and shut it down cleanly.

This wrapper encapsulates the steps needed to boot up a virtual machine, run a\
series of commands inside it, and shut it down gracefully afterwards. Some\
special care is taken in the script to ensure that the virtual machine is\
always shut down after use (gracefully if possible), even in case of various\
failures or the loss of the parent process or controlling TTY. And if a\
conflicting virtual machine somehow manages to escape shutdown, runvm\
automatically attempts to terminate it before starting a new one. This extra\
robustness is important for fully automated testing as in our [Buildbot](./)\
setup, to ensure that the system can run unattended for longer periods of time.

Essentially, instead of a normal Buildbot session which would do something like\
this on the slave:

```make
./configure && make
```

We instead use _runvm_ to do the same inside a virtual machine running as a\
KVM guest with the build slave as host:

```
runvm image.qcow2 "./configure" "make"
```

See the **runvm Usage Examples** or **runvm --help** sections below for more detailed examples, but this is the basic idea.

## runvm Usage Examples

### Usage Example One

Here is an example command you could use to run a build inside a virtual machine using runvm:

```bash
runvm --port=2222 ubuntu-hardy-i386.qcow2 \
  "= scp -P 2222 mariadb-5.1.41-rc.tar.gz localhost:" \
  "tar zxf mariadb-5.1.41-rc.tar.gz" \
  "cd mariadb-5.1.41-rc && ./configure" \
  "cd mariadb-5.1.41-rc && make"
```

In this example, `ubuntu-hardy-amd64.qcow2` is a KVM image already\
installed with compilers and set up for password-less ssh access (using public\
key authentication). Port 2222 on the host side is forwarded to the ssh service\
(port 22) on the guest side (so by specifying different `--port`\
options it is easy to run multiple `runvm` invocations in parallel;\
in our Buildbot setup we run 3 builds in parallel this way).

Note the use of the `scp` command, prefixed with an equals sign\
"`=`" Commands prefixed in this way are run on the host side rather\
than the guest side; this is a convenient way to copy data in or results out of\
the virtual machine while the `runvm` session is running.

Using `runvm` in this way we are able to easily and flexibly manage\
a large number of virtual machines for automated builds with very little\
overhead and complexity. In fact we have around 70 distinct virtual machines!\
The only resource they take is a little disk space (around 37 GByte). And the\
virtual machines images are also simple to set up, requiring only a minimal\
install; no need to set up networking bridges or IP addresses, or to install a\
Buildbot client. All the complex logic runs on the host system, which only\
needs to be installed once.

By keeping the virtual images simple, builds and tests run in a minimal\
environment, which is useful to detect any missing dependencies or other\
problems that do not show themselves on normal developer machines with a full\
desktop install (we even do install testing on a separate virtual machine from\
the one used to build, with compilers etc. not installed on the one used to\
test installation).

### Usage Example Two

A further refinement of **example one** (above) is to create a new\
temporary virtual machine image before each step as a copy of a reference\
image, run the build, and throw away the temporary image after the build. This\
avoids any possibility of a previous build influencing a following build in any\
way (and thus also simplifies the build setup, as we can install stuff freely\
without any need to do cleanup). It also avoids having to fix a broken image,\
like needing to manually run `fsck` after a crash or similar issue. We use this technique for most of our binary package builds in Buildbot.

To use this copy-and-discard technique with runvm, the --base-image option is useful:

```bash
runvm --port=2222 --base-image=ubuntu-hardy-i386.qcow2 tmp.qcow2 \
  "= scp -P 2222 mariadb-5.1.41-rc.tar.gz localhost:" \
  "tar zxf mariadb-5.1.41-rc.tar.gz" \
  "cd mariadb-5.1.41-rc && ./configure" \
  "cd mariadb-5.1.41-rc && make"
```

This will run the build in a temporary copy `tmp.qcow2` of the\
reference image `ubuntu-hardy-i386.qcow2`, without modifying the\
reference image in any way. This uses the copy-on-write feature of the qcow2\
image format (see `qemu-img(1)`), so it even takes only very little\
time (fraction of a second) and minimal space (only changed blocks are written\
to the new image).

### Additional Usage Examples

The above two examples show basically how the package testing in our Buildbot\
setup is done. There are some further details of course, like more options for\
the build commmands and extra care to get logfiles out to debug problems; the\
full details are available in our [Buildbot configuration file](https://bazaar.launchpad.net/~maria-captains/mariadb-tools/trunk/annotate/head%3A/buildbot/maria-master.cfg).\
But the basic principle is just a number of `runvm` commands like the examples above.

## Getting runvm

The `runvm` tool is available under GPL on Lauchpad in the project [Tools for MariaDB](https://launchpad.net/mariadb-tools). In the bzr repository it is found as [buildbot/runvm](https://bazaar.launchpad.net/~maria-captains/mariadb-tools/trunk/annotate/head%3A/buildbot/runvm). 0If someone finds it useful or has suggestions for improvements, please drop us a line on the [maria-developers](https://launchpad.net/~maria-developers)\
mailing list.

## runvm --help

Since it might be useful, here is the output from **runvm --help** (check the\
latest version of the tool for up-to-date output):

```
Usage: ./runvm <options> image.qcow2 [command ...]

Boot the given KVM virtual machine image and wait for it to come up.
Run the list of commands one at a time, aborting on receiving an error.
When all commands are run (or one of them failed), shutdown the virtual
machine and exit.

Commands are by default run inside the virtual machine using ssh(1). By
prefixing a command with an equals sign '=', it will instead be run on the
host system (for example to copy files into or out of the virtual machine
using scp(1)).

Some care is taken to ensure that the virtual machine is shutdown
gracefully and not left running even in case the controlling tty is
closed or the parent process killed. If a previous virtual machine is
already running on a conflicting port, an attempt is made to shut it
down first. For this purpose, a PID file is created in $HOME/.runvm/

Available options:

  -p, --port=N        Forward this port on the host side to the ssh port (port
                      22) on the guest side. Must be different for each runvm
                      instance running in parallel to avoid conflicts. The
                      default is 2222.
                      To copy files in/out of the guest use a command prefixed
                      with '=' calling scp(1) with the -P option using the port
                      specified here, like this:
                          runvm img.qcow2 "=scp -P 2222 file.txt localhost:"
  -u, --user=USER     Name of the account to ssh into in the guest. Defaults to
                      the name of the user invoking runvm on the host.
  -m, --memory=N      Amount of memory (in megabytes) to allocate to the guest.
                      Defaults to 2047.
  --smp=N             Number of CPU cores to allocate to the guest.
                      Defaults to 2.
  -c, --cpu=NAME      Type of CPU to emulate for KVM, see qemu(1) for details.
                      For example:
                          --cpu=qemu64      For 64-bit amd64 emulation
                          --cpu=qemu32      For 32-bit x86 emulation
                          --cpu=qemu32,-nx  32-bit and disable "no-execute"
                      The default is qemu32,-nx
  --netdev=NAME       Network device to emulate. The 'virtio' device has good
                      performance but may not have driver support in all
                      operating systems, if so another can be specified.
                      The default is virtio.
  --kvm=OPT           Pass additional option OPT to kvm. Specify multiple times
                      to pass more than one option. For example
                          runvm --kvm=-cdrom --kvm=mycd.iso img.qcow2 ...
  --initial-sleep=SECS
                      Wait this many seconds before starting to poll the guest
                      ssh port for it to be up. Default 15.
  --startup-timeout=SECS
                      Wait at most this many seconds for the guest OS to respond
                      to ssh. If this time is exceeded assume it has failed to
                      boot correctly. Default 300.
  --shutdown-timeout=SECS
                      Wait at most this many seconds for the guest OS to
                      shutdown gracefully after sending a shutdown command. If
                      this time is exceeded, assume the guest has failed to
                      shutdown gracefully and kill it forcibly. Default 120.
  --kvm-retries=N     If the guest fails to come up, retry the boot this many
                      times before giving up. This helps if the virtual machine
                      sometimes crashes during boot. Default 3.
  -l, --logfile=FILE  File to redirect the output from kvm into. This includes
                      any (error) messages from kvm, and also includes anything
                      the guest writes to the kvm emulated serial port (it can
                      be useful to set the guest to send boot loader and kernel
                      messages to the serial console and log them with this
                      option). Default is to not log this output anywhere.
  -b, --base-image=IMG
                      Instead of booting an existing image, create a new
                      copy-on-write image based on IMG. This uses the -b option
                      of qemu-img(1). IMG is not modified in any way. This way,
                      the booted image can be discarded after use, so that each
                      use of IMG is using the same reference image with no risk
                      of "polution" between different invocations.
                      Note that this DELETES any existing image of the same
                      name as the one specified on the command line to boot! It
                      will be replaced with the image created as a copy of IMG,
                      with any modifications done during the runvm session.
```

_This page is based on a_ [_blog post_](https://kristiannielsen.livejournal.com/11007.html) _by Kristian Nielsen, the primary developer of_ `runvm`.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
