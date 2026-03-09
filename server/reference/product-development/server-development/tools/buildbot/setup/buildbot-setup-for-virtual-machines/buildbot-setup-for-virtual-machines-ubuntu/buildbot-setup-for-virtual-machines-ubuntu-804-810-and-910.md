---
description: >-
  Explains how to provision and configure virtual machine instances specifically
  for Buildbot testing.
---

# Buildbot Setup for Virtual Machines - Ubuntu 8.04, 8.10, and 9.10

These 6 platforms were installed together (i386 and amd64).

## Base Installations

Ubuntu 8.04 "Hardy" amd64:

```
qemu-img create -f qcow2 vm-hardy-amd64-serial.qcow2 8G
kvm -m 1024 -hda vm-hardy-amd64-serial.qcow2 -cdrom /kvm/ubuntu-8.04.3-server-amd64.iso -redir tcp:2228::22 -boot d -smp 2 -cpu qemu64 -net nic,model=virtio -net user
# Install, picking default options mostly, only adding openssh server.
kvm -m 1024 -hda vm-hardy-amd64-serial.qcow2 -cdrom /kvm/ubuntu-8.04.3-server-amd64.iso -redir tcp:2228::22 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user -nographic
ssh -p 2228 localhost
# edit /boot/grub/menu.lst and visudo, see below
sudo /sbin/shutdown -h now
kvm -m 1024 -hda vm-hardy-amd64-serial.qcow2 -cdrom /kvm/ubuntu-8.04.3-server-amd64.iso -redir tcp:2228::22 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user -nographic
ssh -t -p 2228 localhost "mkdir .ssh; sudo addgroup $USER sudo"
scp -P 2228 authorized_keys localhost:.ssh/
echo $'Buildbot\n\n\n\n\ny' | ssh -p 2228 localhost 'chmod -R go-rwx .ssh; sudo adduser --disabled-password buildbot; sudo addgroup buildbot sudo; sudo mkdir ~buildbot/.ssh; sudo cp .ssh/authorized_keys ~buildbot/.ssh/; sudo chown -R buildbot:buildbot ~buildbot/.ssh; sudo chmod -R go-rwx ~buildbot/.ssh'
scp -P 2228 ttyS0 buildbot@localhost:
ssh -p 2228 buildbot@localhost 'sudo cp ttyS0 /etc/event.d; rm ttyS0; sudo shutdown -h now'
```

Ubuntu 8.04 "Hardy" i386:

```
qemu-img create -f qcow2 vm-hardy-i386-serial.qcow2 8G
kvm -m 1024 -hda vm-hardy-i386-serial.qcow2 -cdrom /kvm/ubuntu-8.04.3-server-i386.iso -redir tcp:2229::22 -boot d -smp 2 -cpu qemu32,-nx -net nic,model=virtio -net user
# Install, picking default options mostly, only adding openssh server.
kvm -m 1024 -hda vm-hardy-i386-serial.qcow2 -cdrom /kvm/ubuntu-8.04.3-server-i386.iso -redir tcp:2229::22 -boot c -smp 2 -cpu qemu32,-nx -net nic,model=virtio -net user -nographic
ssh -p 2229 localhost
# edit /boot/grub/menu.lst and visudo, see below
ssh -t -p 2229 localhost "mkdir .ssh; sudo addgroup $USER sudo"
scp -P 2229 authorized_keys localhost:.ssh/
echo $'Buildbot\n\n\n\n\ny' | ssh -p 2229 localhost 'chmod -R go-rwx .ssh; sudo adduser --disabled-password buildbot; sudo addgroup buildbot sudo; sudo mkdir ~buildbot/.ssh; sudo cp .ssh/authorized_keys ~buildbot/.ssh/; sudo chown -R buildbot:buildbot ~buildbot/.ssh; sudo chmod -R go-rwx ~buildbot/.ssh'
scp -P 2229 ttyS0 buildbot@localhost:
ssh -p 2229 buildbot@localhost 'sudo cp ttyS0 /etc/event.d; rm ttyS0; sudo shutdown -h now'
```

Ubuntu 8.10 "Intrepid" amd64:

```
qemu-img create -f qcow2 vm-intrepid-amd64-serial.qcow2 8G
kvm -m 1024 -hda vm-intrepid-amd64-serial.qcow2 -cdrom /kvm/ubuntu-8.10-server-amd64.iso -redir tcp:2230::22 -boot d -smp 2 -cpu qemu64 -net nic,model=virtio -net user
# Install, picking default options mostly, only adding openssh server.
kvm -m 1024 -hda vm-intrepid-amd64-serial.qcow2 -cdrom /kvm/ubuntu-8.10-server-amd64.iso -redir tcp:2230::22 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user -nographic
ssh -p 2230 localhost
# edit /boot/grub/menu.lst and visudo, see below
ssh -t -p 2230 localhost "mkdir .ssh; sudo addgroup $USER sudo"
scp -P 2230 authorized_keys localhost:.ssh/
echo $'Buildbot\n\n\n\n\ny' | ssh -p 2230 localhost 'chmod -R go-rwx .ssh; sudo adduser --disabled-password buildbot; sudo addgroup buildbot sudo; sudo mkdir ~buildbot/.ssh; sudo cp .ssh/authorized_keys ~buildbot/.ssh/; sudo chown -R buildbot:buildbot ~buildbot/.ssh; sudo chmod -R go-rwx ~buildbot/.ssh'
scp -P 2230 ttyS0 buildbot@localhost:
ssh -p 2230 buildbot@localhost 'sudo cp ttyS0 /etc/event.d; rm ttyS0; sudo shutdown -h now'
```

Ubuntu 8.10 "Intrepid" i386:

```
qemu-img create -f qcow2 vm-intrepid-i386-serial.qcow2 8G
kvm -m 1024 -hda vm-intrepid-i386-serial.qcow2 -cdrom /kvm/ubuntu-8.10-server-i386.iso -redir tcp:2231::22 -boot d -smp 2 -cpu qemu32,-nx -net nic,model=virtio -net user
# Install, picking default options mostly, only adding openssh server.
kvm -m 1024 -hda vm-intrepid-i386-serial.qcow2 -cdrom /kvm/ubuntu-8.10-server-i386.iso -redir tcp:2231::22 -boot c -smp 2 -cpu qemu32,-nx -net nic,model=virtio -net user -nographic
ssh -p 2231 localhost
# edit /boot/grub/menu.lst and visudo, see below
ssh -t -p 2231 localhost "mkdir .ssh; sudo addgroup $USER sudo"
scp -P 2231 authorized_keys localhost:.ssh/
echo $'Buildbot\n\n\n\n\ny' | ssh -p 2231 localhost 'chmod -R go-rwx .ssh; sudo adduser --disabled-password buildbot; sudo addgroup buildbot sudo; sudo mkdir ~buildbot/.ssh; sudo cp .ssh/authorized_keys ~buildbot/.ssh/; sudo chown -R buildbot:buildbot ~buildbot/.ssh; sudo chmod -R go-rwx ~buildbot/.ssh'
scp -P 2231 ttyS0 buildbot@localhost:
ssh -p 2231 buildbot@localhost 'sudo cp ttyS0 /etc/event.d; rm ttyS0; sudo shutdown -h now'
```

Ubuntu 9.10 "Karmic" amd64:

```
qemu-img create -f qcow2 vm-karmic-amd64-serial.qcow2 8G
kvm -m 1024 -hda vm-karmic-amd64-serial.qcow2 -cdrom /kvm/ubuntu-9.10-server-amd64.iso -redir tcp:2232::22 -boot d -smp 2 -cpu qemu64 -net nic,model=virtio -net user
# Install, picking default options mostly, only adding openssh server.
kvm -m 1024 -hda vm-karmic-amd64-serial.qcow2 -cdrom /kvm/ubuntu-9.10-server-amd64.iso -redir tcp:2232::22 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user -nographic
ssh -p 2232 localhost
# edit /boot/grub/menu.lst and visudo, see below
ssh -t -p 2232 localhost "mkdir .ssh; sudo addgroup $USER sudo"
scp -P 2232 authorized_keys localhost:.ssh/
echo $'Buildbot\n\n\n\n\ny' | ssh -p 2232 localhost 'chmod -R go-rwx .ssh; sudo adduser --disabled-password buildbot; sudo addgroup buildbot sudo; sudo mkdir ~buildbot/.ssh; sudo cp .ssh/authorized_keys ~buildbot/.ssh/; sudo chown -R buildbot:buildbot ~buildbot/.ssh; sudo chmod -R go-rwx ~buildbot/.ssh'
scp -P 2232 ttyS0.conf buildbot@localhost:
ssh -p 2232 buildbot@localhost 'sudo cp ttyS0.conf /etc/init/; rm ttyS0.conf; sudo shutdown -h now'
```

Ubuntu 9.10 "Karmic" i386:

```
qemu-img create -f qcow2 vm-karmic-i386-serial.qcow2 8G
kvm -m 1024 -hda vm-karmic-i386-serial.qcow2 -cdrom /kvm/ubuntu-9.10-server-i386.iso -redir tcp:2233::22 -boot d -smp 2 -cpu qemu32,-nx -net nic,model=virtio -net user
# Install, picking default options mostly, only adding openssh server.
kvm -m 1024 -hda vm-karmic-i386-serial.qcow2 -cdrom /kvm/ubuntu-9.10-server-i386.iso -redir tcp:2233::22 -boot c -smp 2 -cpu qemu32,-nx -net nic,model=virtio -net user -nographic
ssh -p 2233 localhost
# edit /boot/grub/menu.lst and visudo, see below
ssh -t -p 2233 localhost "mkdir .ssh; sudo addgroup $USER sudo"
scp -P 2233 authorized_keys localhost:.ssh/
echo $'Buildbot\n\n\n\n\ny' | ssh -p 2233 localhost 'chmod -R go-rwx .ssh; sudo adduser --disabled-password buildbot; sudo addgroup buildbot sudo; sudo mkdir ~buildbot/.ssh; sudo cp .ssh/authorized_keys ~buildbot/.ssh/; sudo chown -R buildbot:buildbot ~buildbot/.ssh; sudo chmod -R go-rwx ~buildbot/.ssh'
scp -P 2233 ttyS0.conf buildbot@localhost:
ssh -p 2233 buildbot@localhost 'sudo cp ttyS0.conf /etc/init/; rm ttyS0.conf; sudo shutdown -h now'
```

For visudo to enable passwordless sudo:

```
sudo VISUAL=vi visudo

# uncomment `%sudo ALL=NOPASSWD: ALL' line in `visudo`, and move to end.
```

For 8.04/8.10/9.04, /boot/grub/menu.lst is edited as follows:

```
sudo vi /boot/grub/menu.lst

# Add this:
  serial --unit=0 --speed=115200 --word=8 --parity=no --stop=1
  terminal --timeout=3 serial console

# Also add in menu.lst to kernel line (after removing `quiet splash'):
  console=tty0 console=ttyS0,115200n8
```

For 9.10, /boot/grub/menu.lst is edited as follows:

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
for i in 'vm-hardy-amd64-serial.qcow2 2228 qemu64' 'vm-hardy-i386-serial.qcow2 2229 qemu32,-nx' 'vm-intrepid-amd64-serial.qcow2 2230 qemu64' 'vm-intrepid-i386-serial.qcow2 2231 qemu32,-nx' ; do \
  set $i; \
  runvm --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/build/')" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get build-dep -y mysql-server-5.0" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y devscripts hardening-wrapper fakeroot doxygen texlive-latex-base ghostscript libevent-dev libssl-dev zlib1g-dev libreadline5-dev" ; \
done

for i in 'vm-karmic-amd64-serial.qcow2 2232 qemu64' 'vm-karmic-i386-serial.qcow2 2233 qemu32,-nx' ; do \
  set $i; \
  runvm --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/build/')" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get update" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get -y build-dep mysql-server-5.1" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y devscripts hardening-wrapper fakeroot doxygen texlive-latex-base ghostscript libevent-dev libssl-dev zlib1g-dev libreadline5-dev" ; \
done
```

## VMs for install testing

See the [General Principles](../buildbot-setup-for-virtual-machines-general-principles.md)\
article for how to make the '`my.seed`' and '`sources.append`' files.

```
for i in 'vm-hardy-amd64-serial.qcow2 2228 qemu64' 'vm-hardy-i386-serial.qcow2 2229 qemu32,-nx' 'vm-intrepid-amd64-serial.qcow2 2230 qemu64' 'vm-intrepid-i386-serial.qcow2 2231 qemu32,-nx' 'vm-karmic-amd64-serial.qcow2 2232 qemu64' 'vm-karmic-i386-serial.qcow2 2233 qemu32,-nx' ; do \
  set $i; \
  runvm --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/install/')" \
	  "sudo DEBIAN_FRONTEND=noninteractive apt-get update" \
	  "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y debconf-utils" \
	  "= scp -P $2 my.seed sources.append buildbot@localhost:/tmp/" \
	  "sudo debconf-set-selections /tmp/my.seed" \
	  "sudo sh -c 'cat /tmp/sources.append >> /etc/apt/sources.list'"; \
done
```

## VMs for upgrade testing

```
for i in 'vm-hardy-amd64-install.qcow2 2228 qemu64' 'vm-hardy-i386-install.qcow2 2229 qemu32,-nx' 'vm-intrepid-amd64-install.qcow2 2230 qemu64' 'vm-intrepid-i386-install.qcow2 2231 qemu32,-nx' ; do \
  set $i; \
  runvm --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/install/upgrade/')" \
  'sudo DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server-5.0'
  'mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"' ; \
done

for i in 'vm-karmic-amd64-install.qcow2 2232 qemu64' 'vm-karmic-i386-install.qcow2 2233 qemu32,-nx' ; do \
  set $i; \
  runvm --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/install/upgrade/')" \
    'sudo DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server-5.1' \
    'mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"' ; \
done
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
