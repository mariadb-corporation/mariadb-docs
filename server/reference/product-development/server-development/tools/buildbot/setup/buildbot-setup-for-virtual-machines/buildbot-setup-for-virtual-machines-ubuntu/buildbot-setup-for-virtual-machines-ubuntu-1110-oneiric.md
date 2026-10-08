---
description: >-
  Explains how to provision and configure virtual machine instances specifically
  for Buildbot testing.
---

# Buildbot Setup for Virtual Machines - Ubuntu 11.10 "oneiric"

## Base Install

```
qemu-img create -f qcow2 /kvm/vms/vm-oneiric-amd64-serial.qcow2 8G
qemu-img create -f qcow2 /kvm/vms/vm-oneiric-i386-serial.qcow2 8G

# Start each VM booting from the server install iso one at a time and perform
# the following install steps:
kvm -m 1024 -hda /kvm/vms/vm-oneiric-amd64-serial.qcow2 -cdrom /kvm/iso/ubuntu-11.10-server-amd64.iso -redir tcp:2255::22 -boot d -smp 2 -cpu qemu64 -net nic,model=virtio -net user
kvm -m 1024 -hda /kvm/vms/vm-oneiric-i386-serial.qcow2 -cdrom /kvm/iso/ubuntu-11.10-server-i386.iso -redir tcp:2256::22 -boot d -smp 2 -cpu qemu32,-nx -net nic,model=virtio -net user

# Once running you can connect to the VNC server from your local host with:
#
#    vncviewer -via ${remote-host} localhost
#
# (replace ${remote-host} with the host the vm is running on)

# Install, picking default options mostly, with the following notes:
# * Set the hostname to ubuntu-oneiric
# * When partitioning disks, choose "Guided - use entire disk" (we do not want LVM)
# * No automatic updates
# * Choose software to install: OpenSSH server


# Now that the VM is installed, it's time to configure it.
# If you have the memory you can do the following simultaneously:
kvm -m 1024 -hda /kvm/vms/vm-oneiric-amd64-serial.qcow2 -cdrom /kvm/iso/ubuntu-11.10-server-amd64.iso -redir tcp:2255::22 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user -nographic
kvm -m 1024 -hda /kvm/vms/vm-oneiric-i386-serial.qcow2 -cdrom /kvm/iso/ubuntu-11.10-server-i386.iso -redir tcp:2256::22 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user -nographic

ssh -p 2255 localhost
# edit /boot/grub/menu.lst and visudo, see below

ssh -p 2256 localhost
# edit /boot/grub/menu.lst and visudo, see below

ssh -t -p 2255 localhost "mkdir -v .ssh; sudo addgroup $USER sudo"
ssh -t -p 2256 localhost "mkdir -v .ssh; sudo addgroup $USER sudo"

scp -P 2255 /kvm/vms/authorized_keys localhost:.ssh/
scp -P 2256 /kvm/vms/authorized_keys localhost:.ssh/

echo $'Buildbot\n\n\n\n\ny' | ssh -p 2255 localhost 'chmod -R go-rwx .ssh; sudo adduser --disabled-password buildbot; sudo addgroup buildbot sudo; sudo mkdir ~buildbot/.ssh; sudo cp -vi .ssh/authorized_keys ~buildbot/.ssh/; sudo chown -vR buildbot:buildbot ~buildbot/.ssh; sudo chmod -vR go-rwx ~buildbot/.ssh'
echo $'Buildbot\n\n\n\n\ny' | ssh -p 2256 localhost 'chmod -R go-rwx .ssh; sudo adduser --disabled-password buildbot; sudo addgroup buildbot sudo; sudo mkdir ~buildbot/.ssh; sudo cp -vi .ssh/authorized_keys ~buildbot/.ssh/; sudo chown -vR buildbot:buildbot ~buildbot/.ssh; sudo chmod -vR go-rwx ~buildbot/.ssh'

scp -P 2255 /kvm/vms/ttyS0.conf buildbot@localhost:
scp -P 2256 /kvm/vms/ttyS0.conf buildbot@localhost:

ssh -p 2255 buildbot@localhost 'sudo cp -vi ttyS0.conf /etc/init/; rm -v ttyS0.conf; sudo shutdown -h now'
ssh -p 2256 buildbot@localhost 'sudo cp -vi ttyS0.conf /etc/init/; rm -v ttyS0.conf; sudo shutdown -h now'
```

Enabling passwordless sudo:

```
sudo VISUAL=vi visudo
# Add line at end: `%sudo ALL=NOPASSWD: ALL'
```

Editing /boot/grub/menu.lst:

```
sudo vi /etc/default/grub

# Add/edit these entries:
    GRUB_CMDLINE_LINUX_DEFAULT="console=tty0 console=ttyS0,115200n8"
    GRUB_TERMINAL="serial"
    GRUB_SERIAL_COMMAND="serial --unit=0 --speed=115200 --word=8 --parity=no --stop=1"

sudo update-grub
```

## VMs for building .debs

```
for i in '/kvm/vms/vm-oneiric-amd64-serial.qcow2 2255 qemu64' '/kvm/vms/vm-oneiric-i386-serial.qcow2 2256 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/build/')" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get update" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get -y build-dep mysql-server-5.1" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y devscripts hardening-wrapper fakeroot doxygen texlive-latex-base ghostscript libevent-dev libssl-dev zlib1g-dev libreadline6-dev" ; \
done
```

Install cmake (required for [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)) with:

```
kvm -m 1024 -hda ${vm} -redir tcp:22565::22 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user -nographic

ssh -o IdentityFile=.ssh/buildbot.id_dsa -p 22565 buildbot@localhost

wget http://www.cmake.org/files/v2.8/cmake-2.8.6.tar.gz
tar -zxvf cmake-2.8.6.tar.gz
cd cmake-2.8.6;./configure
make
sudo make install

sudo /sbin/shutdown -h now
```

Also:

* [Installing the Boost library needed for the OQGraph storage engine](../buildbot-setup-for-virtual-machines-additional-steps/installing-the-boost-library-needed-for-the-oqgraph-storage-engine.md)

## VMs for install testing.

See above for how to obtain my.seed and sources.append.

```
for i in '/kvm/vms/vm-oneiric-amd64-serial.qcow2 2255 qemu64' '/kvm/vms/vm-oneiric-i386-serial.qcow2 2256 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/install/')" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get update" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y debconf-utils" \
    "= scp -P $2 /kvm/vms/my.seed /kvm/vms/sources.append buildbot@localhost:/tmp/" \
    "sudo debconf-set-selections /tmp/my.seed" \
    "sudo sh -c 'cat /tmp/sources.append >> /etc/apt/sources.list'"; \
done
```

## VMs for MySQL upgrade testing

```
for i in '/kvm/vms/vm-oneiric-amd64-install.qcow2 2255 qemu64' '/kvm/vms/vm-oneiric-i386-install.qcow2 2256 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/install/upgrade/')" \
    'sudo DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server-5.1' \
    'mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"' ;\
done
```

## VMs for MariaDB upgrade testing

_The steps below are based on the Natty steps on_ [_Installing VM images for testing .deb upgrade between versions_](../buildbot-setup-for-virtual-machines-additional-steps/installing-vm-images-for-testing-deb-upgrade-between-versions.md)_._

64-bit Ubuntu oneiric:

```
qemu-img create -b vm-oneiric-amd64-install.qcow2 -f qcow2 vm-oneiric-amd64-upgrade2.qcow2
kvm -m 512 -hda vm-oneiric-amd64-upgrade2.qcow2 -redir 'tcp:2200::22' -boot c -smp 1 -cpu qemu64 -net nic,model=virtio -net user -nographic
ssh -p 2200 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no buildbot@localhost

sudo sh -c 'cat > /etc/apt/sources.list.d/tmp.list'
deb http://ftp.osuosl.org/pub/mariadb/repo/5.2/ubuntu natty main
deb-src http://ftp.osuosl.org/pub/mariadb/repo/5.2/ubuntu natty main

sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 1BB943DB
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-unauthenticated mariadb-server mariadb-test libmariadbclient-dev
sudo rm /etc/apparmor.d/usr.sbin.mysqld
sudo /etc/init.d/apparmor restart
sudo apt-get -f install
mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"
sudo rm /etc/apt/sources.list.d/tmp.list
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y
sudo shutdown -h now
```

32-bit Ubuntu oneiric:

```
qemu-img create -b vm-oneiric-i386-install.qcow2 -f qcow2 vm-oneiric-i386-upgrade2.qcow2
kvm -m 512 -hda vm-oneiric-i386-upgrade2.qcow2 -redir 'tcp:2200::22' -boot c -smp 1 -cpu qemu64 -net nic,model=virtio -net user -nographic
ssh -p 2200 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no buildbot@localhost

sudo sh -c 'cat > /etc/apt/sources.list.d/tmp.list'
deb http://ftp.osuosl.org/pub/mariadb/repo/5.2/ubuntu natty main
deb-src http://ftp.osuosl.org/pub/mariadb/repo/5.2/ubuntu natty main

sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 1BB943DB
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-unauthenticated mariadb-server mariadb-test libmariadbclient-dev
sudo rm /etc/apparmor.d/usr.sbin.mysqld
sudo /etc/init.d/apparmor restart
sudo apt-get -f install
mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"
sudo rm /etc/apt/sources.list.d/tmp.list
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y
sudo shutdown -h now
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
