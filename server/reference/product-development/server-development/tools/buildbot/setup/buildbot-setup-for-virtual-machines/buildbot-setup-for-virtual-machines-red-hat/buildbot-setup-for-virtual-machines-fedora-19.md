---
description: >-
  Explains how to provision and configure virtual machine instances specifically
  for Buildbot testing.
---

# Buildbot Setup for Virtual Machines - Fedora 19

## Base Install

```
qemu-img create -f qcow2 /kvm/vms/vm-fedora19-i386-serial.qcow2 20G
qemu-img create -f qcow2 /kvm/vms/vm-fedora19-amd64-serial.qcow2 20G
```

Start each VM booting from the server install iso one at a time and perform\
the following install steps:

```
kvm -m 2048 -hda /kvm/vms/vm-fedora19-i386-serial.qcow2 -cdrom /ds413/iso/fedora/Fedora-19-i386-DVD.iso -redir tcp:2289::22 -boot d -smp 2 -cpu qemu64 -net nic,model=virtio -net user
kvm -m 2048 -hda /kvm/vms/vm-fedora19-amd64-serial.qcow2 -cdrom /ds413/iso/fedora/Fedora-19-x86_64-DVD.iso -redir tcp:2290::22 -boot d -smp 2 -cpu qemu64 -net nic,model=virtio -net user
```

Once running you can connect to the VNC server from your local host with:

```
vncviewer -via ${remote-host} localhost
```

Replace ${remote-host} with the host the vm is running on.

**Note:** When you activate the install, vncviewer may disconnect with a complaint about the rect being too large. This is fine. The Fedora installer has just resized the vnc screen. Simply reconnect.

Install, picking default options mostly, with the following notes:

* Under "Network Configuration" set the hostnames to fedora19-amd64 and fedora19-i386
* Change "Software Selection" to "Minimal Install" (default is "Gnome Desktop")
* For "Installation Destination" select the disk then click continue.
* do not check the encryption checkbox
* On "Installation Options" screen, expand the "Partition scheme configuration" box and select a "Partition type" of "Standard Partition"
* While installing, set the root password and an initial user

When the install is finished, you will be prompted to reboot. Go ahead and do so, but it will fail. Kill the VM (after the reboot fails) and start it up again:

```
kvm -m 2048 -hda /kvm/vms/vm-fedora19-i386-serial.qcow2 -redir tcp:2289::22 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user
kvm -m 2048 -hda /kvm/vms/vm-fedora19-amd64-serial.qcow2 -redir tcp:2290::22 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user
```

Log in using the initial user created during the install:

```
ssh -p 2289 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i ~/.ssh/buildbot.id_dsa localhost
ssh -p 2290 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i ~/.ssh/buildbot.id_dsa localhost
```

After logging in, add the initial user to the "wheel" group.

```
usermod -a -G wheel ${username}
```

Enable password-less sudo for the "wheel" group and serial console sudo:

```
visudo
# Uncomment the line "%wheel        ALL=(ALL)       NOPASSWD: ALL"
# Comment out this line:
# Defaults    requiretty
```

Edit /boot/grub/menu.lst:

```
sudo vi /etc/default/grub

# Add/edit these entries:
    GRUB_CMDLINE_LINUX_DEFAULT="console=tty0 console=ttyS0,115200n8"
    GRUB_TERMINAL="serial"
    GRUB_SERIAL_COMMAND="serial --unit=0 --speed=115200 --word=8 --parity=no --stop=1"

grub2-mkconfig -o /boot/grub2/grub.cfg
```

Logout as root, and then, from the VM host server:

Create a .ssh folder:

```
ssh -t -p 2289 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i ~/.ssh/buildbot.id_dsa localhost "mkdir -v .ssh"
ssh -t -p 2290 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i ~/.ssh/buildbot.id_dsa localhost "mkdir -v .ssh"
```

Copy over the authorized keys file:

```
scp -P 2289 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no /kvm/vms/authorized_keys localhost:.ssh/
scp -P 2290 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no /kvm/vms/authorized_keys localhost:.ssh/
```

Set permissions on the .ssh folder correctly:

```
ssh -t -p 2289 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i ~/.ssh/buildbot.id_dsa localhost "chmod -R go-rwx .ssh"
ssh -t -p 2290 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i ~/.ssh/buildbot.id_dsa localhost "chmod -R go-rwx .ssh"
```

Create the buildbot user:

```
ssh -p 2289 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no localhost 'chmod -R go-rwx .ssh; sudo adduser buildbot; sudo usermod -a -G wheel buildbot; sudo mkdir ~buildbot/.ssh; sudo cp -vi .ssh/authorized_keys ~buildbot/.ssh/; sudo chown -vR buildbot:buildbot ~buildbot/.ssh; sudo chmod -vR go-rwx ~buildbot/.ssh'
ssh -p 2290 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no localhost 'chmod -R go-rwx .ssh; sudo adduser buildbot; sudo usermod -a -G wheel buildbot; sudo mkdir ~buildbot/.ssh; sudo cp -vi .ssh/authorized_keys ~buildbot/.ssh/; sudo chown -vR buildbot:buildbot ~buildbot/.ssh; sudo chmod -vR go-rwx ~buildbot/.ssh'
```

su to the local buildbot user and ssh to the vm to put the key in known\_hosts:

For i386:

```
sudo su - buildbot
ssh -p 2289 buildbot@localhost
# exit, then exit again
```

For amd64:

```
sudo su - buildbot
ssh -p 2290 buildbot@localhost
# exit, then exit again
```

Upload the ttyS0 file and put it where it goes:

```
scp -P 2289 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no /kvm/vms/ttyS0 buildbot@localhost:
scp -P 2290 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no /kvm/vms/ttyS0 buildbot@localhost:

ssh -p 2289 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no buildbot@localhost 'sudo mkdir -v /etc/event.d;sudo mv -vi ttyS0 /etc/event.d/;'
ssh -p 2290 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no buildbot@localhost 'sudo mkdir -v /etc/event.d;sudo mv -vi ttyS0 /etc/event.d/;'
```

Update the VM:

```
ssh -p 2289 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no buildbot@localhost
ssh -p 2290 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no buildbot@localhost
```

Once logged in:

```
sudo yum update
```

Change selinux policy to `permissive`:

```
sudo vi /etc/selinux/config 
# change:
SELINUX=enforcing
# to:
SELINUX=permissive
```

After updating, shut down the VM:

```
sudo shutdown -h now
```

## VMs for building .rpms

```
for i in '/kvm/vms/vm-fedora19-i386-serial.qcow2 2289 qemu64' '/kvm/vms/vm-fedora19-amd64-serial.qcow2 2290 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/build/')" \
  "= scp -P $2 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no /kvm/thrift-0.9.0.tar.gz buildbot@localhost:/dev/shm/" \
  "sudo yum -y groupinstall 'Development Tools'" \
  "sudo yum -y install yum-utils" \
  "sudo yum-builddep -y mariadb" \
  "sudo yum -y install automake libtool flex pkgconfig gcc-c++ libevent-devel python-devel ruby-devel rpm-build" \
  "sudo yum -y install cmake tar wget tree gperf readline-devel ncurses-devel zlib-devel pam-devel libaio-devel openssl-devel" \
  "sudo yum -y install libxml2 libxml2-devel bison bison-devel boost-devel unixODBC-devel bzr perl perl\(DBI\)" \
  "sudo yum -y remove systemtap-sdt-dev" \
  "bzr co --lightweight lp:mariadb-native-client" \
  "sudo mkdir -vp /usr/src/redhat/SOURCES /usr/src/redhat/SPECS /usr/src/redhat/RPMS /usr/src/redhat/SRPMS" \
  "cd /usr/local/src;sudo tar zxf /dev/shm/thrift-0.9.0.tar.gz;pwd;ls" \
  "cd /usr/local/src/thrift-0.9.0;echo;pwd;sudo ./configure --prefix=/usr --enable-shared=no --enable-static=yes CXXFLAGS=-fPIC CFLAGS=-fPIC && echo && echo 'now making' && echo && sleep 3 && sudo make && echo && echo 'now installing' && echo && sleep 3 && sudo make install" ; \
done
```

## VMs for install testing.

```
for i in '/kvm/vms/vm-fedora19-i386-serial.qcow2 2289 qemu64' '/kvm/vms/vm-fedora19-amd64-serial.qcow2 2290 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/install/')" \
    "sudo yum -y update" \
    "sudo yum -y install patch tar libaio perl perl-Time-HiRes perl-DBI unixODBC" ; \
done
```

## VMs for MySQL upgrade testing

```
for i in '/kvm/vms/vm-fedora19-i386-serial.qcow2 2289 qemu64' '/kvm/vms/vm-fedora19-amd64-serial.qcow2 2290 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/upgrade/')" \
    "sudo yum -y update" \
    "sudo yum -y install patch tar mysql-server libtool-ltdl unixODBC" \
    "sudo systemctl enable mysqld.service" \
    "sudo systemctl start mysqld.service" \
    'mysql -uroot -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"' ; \
done
```

## VMs for MariaDB upgrade testing

```
for i in '/kvm/vms/vm-fedora19-amd64-serial.qcow2 2290 qemu64' '/kvm/vms/vm-fedora19-i386-serial.qcow2 2289 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/upgrade2/')" \
    'sudo yum -y update' \
    "= scp -P $2 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no /kvm/vms/MariaDB-${2}.repo buildbot@localhost:/tmp/MariaDB.repo" \
    'sudo rpm --verbose --import https://yum.mariadb.org/RPM-GPG-KEY-MariaDB' \
    'sudo mv -vi /tmp/MariaDB.repo /etc/yum.repos.d/' \
    'sudo yum -y remove mysql-libs' \
    'sudo yum -y install MariaDB-server MariaDB-client MariaDB-test libtool-ltdl unixODBC' \
    'sudo yum -y install cronie cronie-anacron crontabs.noarch patch tar' \
    'sudo /etc/init.d/mysql start' \
    'mysql -uroot -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"' \
    'sudo rm -v /etc/yum.repos.d/MariaDB.repo' \
    'sudo yum -y update' \
    "= scp -P $2 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no /kvm/vms/MariaDB.local.repo buildbot@localhost:/tmp/" \
    'sudo mv -vi /tmp/MariaDB.local.repo /etc/yum.repos.d/'; \
done
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
