---
description: >-
  Explains how to provision and configure virtual machine instances specifically
  for Buildbot testing.
---

# Buildbot Setup for Virtual Machines - Red Hat 6 x86

The following steps were used to create a Red Hat 6 x86 build slave.

## Initial Setup

```
cd vms
qemu-img create -f qcow2 vm-rhel6-x86-base.qcow2 8G
kvm -m 1024 -hda vm-rhel6-x86-base.qcow2 -cdrom ../iso/red-hat/rhel-server-6.0-i386-dvd.iso -redir 'tcp:22275::22' -boot d -smp 2 -cpu qemu32,-nx -net nic,model=virtio -net user
```

When the VM boots. Go through the prompts.

Re-initialize the drive, when prompted.

Set the Hostname to "rhel6-x86".

Configure Network, set eth0 to "Connect Automatically"

Set the root password.

Set partitioning type to: Use All Space

Don't encrypt the partitions (just adds overhead).

Select "Write Changes to Disk" on the popup that appears.

Set the software set to "Virtual Host".

After clicking next on the install-type page, the installation will finally start.

After installation completes, click reboot. Then shutdown the VM.

## Serial Console Setup

```
cd vms
qemu-img create -b vm-rhel6-x86-base.qcow2 -f qcow2 vm-rhel6-x86-serial.qcow2
kvm -m 1024 -hda vm-rhel6-x86-serial.qcow2 -redir 'tcp:22275::22' -boot c -smp 2 -cpu qemu32,-nx -net nic,model=virtio -net user
```

Login as root.

Add to /boot/grub/menu.lst:

```
serial --unit=0 --speed=115200 --word=8 --parity=no --stop=1
terminal --timeout=3 serial console
```

also add in menu.lst to kernel line (after removing 'quiet'):

```
console=tty0 console=ttyS0,115200n8
```

Add login prompt on serial console:

```
cat >>/etc/inittab <<END

# Serial console.
S0:2345:respawn:/sbin/agetty -h -L ttyS0 19200 vt100
END
```

## Create buildbot account

With the network up and running, it's time to add a user so that we don't have\
to login as root all the time.

```
useradd buildbot
# Password is disabled by default in Centos5.
usermod -a -G wheel buildbot
visudo
# Uncomment the line "%wheel        ALL=(ALL)       NOPASSWD: ALL"
# Comment out this line:
# Defaults    requiretty

# Put in public ssh key for own account and host buildbot account.
# Note that Centos5 seems to require .ssh/authorized_keys chmod go-rwx.
su - buildbot
mkdir .ssh
chmod go-rwx .ssh

# scp the key from the vm host over to .ssh/authorized_keys

chmod go-rwx .ssh/authorized_keys
```

Now logout and then ssh to the VM as the buildbot user. On my local box I added\
the following to my /.ssh/config file to make logging in easier:

```
Host rhel6-x86
HostName localhost
  User buildbot
  IdentityFile ~/.ssh/id_rsa
  Port 2225
```

With the above in place I can simply type:

```
ssh rhel6-x86
```

...to connect to the vm.

## RHN and Updates

Register the system with RHN:

```
sudo rhn_register
```

Choose defaults when registering. After the process is complete:

```
sudo yum update
```

The first time you update you'll be prompted to import some GPG keys from Red\
Hat. The updating process may take a while, depending on the number of updates\
and the speed of your Internet connection.

After updating shutdown so we can make more copies.

```
sudo shutdown -h now
```

## Image for RPM Build

```
qemu-img create -b vm-rhel6-x86-serial.qcow2 -f qcow2 vm-rhel6-x86-build.qcow2
kvm -m 1024 -hda vm-rhel6-x86-build.qcow2 -redir 'tcp:22275::22' -boot c -smp 2 -cpu qemu32,-nx -net nic,model=virtio -net user -nographic
```

Wait for the system to boot.

Install compilers etc:

```
sudo yum groupinstall "Development Tools"
sudo yum install libaio-devel openssl-devel
```

If the "Development Tools" group is not available, the following lines will install the packages from it:

```
# Mandatory Packages:
sudo yum install autoconf automake binutils bison flex gcc gcc-c++ gettext
sudo yum install libtool make patch pkgconfig redhat-rpm-config rpm-build

# Default Packages:
sudo yum install byacc cscope ctags cvs diffstat doxygen elfutils gcc-gfortran
sudo yum install git indent intltool patchutils rcs subversion swig systemtap

# Optional Packages:
sudo yum install ElectricFence ant babel bzr chrpath cmake compat-gcc-34
sudo yum install compat-gcc-34-c++ compat-gcc-34-g77 dejagnu expect gcc-gnat
sudo yum install gcc-java gcc-objc gcc-objc++ imake jpackage-utils libstdc++-docs
sudo yum install mercurial mod_dav_svn nasm perltidy python-docs rpmdevtools
sudo yum install rpmlint systemtap-sdt-devel systemtap-server
```

Other packages to install:

```
sudo yum install gperf readline-devel ncurses-devel zlib-devel perl perl\(DBI\)
```

Create rpm directories and download 5.0 rpm for shared-compat:

```
sudo mkdir -vp /usr/src/redhat/SOURCES /usr/src/redhat/SPECS /usr/src/redhat/RPMS /usr/src/redhat/SRPMS
sudo mkdir -vp /srv/shared/yum/CentOS/5/i386/RPMS/
cd /srv/shared/yum/CentOS/5/i386/RPMS/
sudo wget http://mirror.ourdelta.org/yum/CentOS/5/i386/RPMS/MySQL-OurDelta-shared-5.0.87.d10-65.el5.i386.rpm
```

## Image for install/test

```
qemu-img create -b vm-rhel6-x86-serial.qcow2 -f qcow2 vm-rhel6-x86-install.qcow2
kvm -m 1024 -hda vm-rhel6-x86-install.qcow2 -redir 'tcp:22275::22' -boot c -smp 2 -cpu qemu32,-nx -net nic,model=virtio -net user -nographic
```

Install extra dependencies:

```
sudo yum install perl perl\(DBI\)
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
