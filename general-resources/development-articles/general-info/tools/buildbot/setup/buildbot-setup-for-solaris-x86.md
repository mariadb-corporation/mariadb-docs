
# Buildbot Setup for Solaris x86

The following steps were used to create a Solaris 10 x86 BuildSlave.


I started with a default install of Solaris 10.


First I added a new user with:


```
groupadd sudo
useradd -d /export/home/${username} -m -s /bin/bash -g staff -G sudo ${username}
passwd ${username}
```

I then logged in as the new user and setup an ssh key.


Now to install software


Prior to actually installing the software, I adjusted the global profile so that the /usr/local/ dirs were included in the various PATHs:


```
vi /etc/profile

# Add the following lines:

LD_LIBRARY_PATH=/opt/csw/lib:/usr/local/lib:/usr/sfw/lib:$LD_LIBRARY_PATH # Add required libraries
PYTHONPATH=/usr/local/lib/python2.5/site-packages:$PYTHONPATH
PATH=/usr/local/bin:/usr/bin:/usr/sbin:/etc:/usr/sfw/bin:$PATH # Puts "local" packages in your path
export LOGNAME PATH PYTHONPATH LD_LIBRARY_PATH
```

The extra software, I downloaded from sunfreeware:


```
cd /tmp
ftp ftp.sunfreeware.com
anonymous
none

bin
cd pub/freeware/intel/10/
mget python-2.5.1-sol10-x86-local.gz sudo-1.7.4p4-sol10-x86-local.gz libintl-3.4.0-sol10-x86-local.gz libgcc-3.4.6-sol10-x86-local.gz libiconv-1.13.1-sol10-x86-local.gz

mget automake-1.9-sol10-intel-local.gz autogen-5.9.8-sol10-x86-local.gz autoconf-2.68-sol10-x86-local.gz gcc-4.5.1-sol10-x86-local.gz

mget m4-1.4.15-sol10-x86-local.gz libtool-2.4-sol10-x86-local.gz gmp-4.2.1-sol10-x86-local.gz

mget md5-6142000-sol10-intel-local.gz openssl-1.0.0c-sol10-x86-local.gz libsigsegv-2.9-sol10-x86-local.gz tcl-8.5.9-sol10-x86-local.gz tk-8.5.9-sol10-x86-local.gz perl-5.12.2-sol10-x86-local.gz

mget libtool-2.4-sol10-x86-local.gz sed-4.2.1-sol10-x86-local.gz zlib-1.2.5-sol10-x86-local.gz binutils-2.21-sol10-x86-local.gz groff-1.21-sol10-x86-local.gz bzip2-1.0.6-sol10-x86-local.gz

mget make-3.82-sol10-x86-local.gz sed-4.2.1-sol10-x86-local.gz gdb-6.8-sol10-x86-local.gz coreutils-8.9-sol10-x86-local.gz cmake-2.6.0-sol10-x86-local.gz

quit
```

With all of the software downloaded, I next setup and configured sudo and python:


```
su
gunzip -v python-2.5.1-sol10-x86-local.gz 
pkgadd -d python-2.5.1-sol10-x86-local

gunzip -v libintl-3.4.0-sol10-x86-local.gz libgcc-3.4.6-sol10-x86-local.gz libiconv-1.13.1-sol10-x86-local.gz sudo-1.7.4p4-sol10-x86-local.gz

pkgadd -d libintl-3.4.0-sol10-x86-local
pkgadd -d libgcc-3.4.6-sol10-x86-local
pkgadd -d libiconv-1.13.1-sol10-x86-local
pkgadd -d sudo-1.7.4p4-sol10-x86-local

mkdir -p /usr/local/var/lib/
/usr/local/sbin/visudo
```

With sudo now working, I logged out and then back in. I then installed the other packages:


```
cd /tmp

gunzip -v *.gz

sudo pkgadd -d autoconf-2.68-sol10-x86-local
sudo pkgadd -d autogen-5.9.8-sol10-x86-local
sudo pkgadd -d automake-1.9-sol10-intel-local
sudo pkgadd -d binutils-2.21-sol10-x86-local
sudo pkgadd -d gcc-4.5.1-sol10-x86-local
sudo pkgadd -d groff-1.21-sol10-x86-local
sudo pkgadd -d libsigsegv-2.9-sol10-x86-local
sudo pkgadd -d make-3.82-sol10-x86-local
sudo pkgadd -d m4-1.4.15-sol10-x86-local
sudo pkgadd -d md5-6142000-sol10-intel-local
sudo pkgadd -d openssl-1.0.0c-sol10-x86-local
sudo pkgadd -d perl-5.12.2-sol10-x86-local
sudo pkgadd -d tcl-8.5.9-sol10-x86-local
sudo pkgadd -d tk-8.5.9-sol10-x86-local
sudo pkgadd -d zlib-1.2.5-sol10-x86-local
sudo pkgadd -d bzip2-1.0.6-sol10-x86-local
sudo pkgadd -d libtool-2.4-sol10-x86-local
sudo pkgadd -d sed-4.2.1-sol10-x86-local
sudo pkgadd -d gdb-6.8-sol10-x86-local
sudo pkgadd -d coreutils-8.9-sol10-x86-local
sudo pkgadd -d gmp-4.2.1-sol10-x86-local
sudo pkgadd -d cmake-2.6.0-sol10-x86-local
```

With those packages installed it was time to install the pieces of software which don't have pre-built packages:


Install Zope Interface:


```
cd /tmp
wget http://www.zope.org/Products/ZopeInterface/3.3.0/zope.interface-3.3.0.tar.gz
gunzip -v zope.interface-3.3.0.tar.gz
gtar -xf zope.interface-3.3.0.tar
cd zope.interface-3.3.0/
python setup.py build
sudo python setup.py install
```

Install the latest Twisted framework:


```
cd /tmp
wget http://tmrc.mit.edu/mirror/twisted/Twisted/10.2/Twisted-10.2.0.tar.bz2
bunzip2 Twisted-10.2.0.tar.bz2 
gtar -xf Twisted-10.2.0.tar 
cd Twisted-10.2.0
sudo python setup.py install
```

Install Bazaar:


```
cd /tmp
wget http://launchpad.net/bzr/2.2/2.2.2/+download/bzr-2.2.2.tar.gz
gunzip -v bzr-2.2.2.tar.gz
gtar -xf bzr-2.2.2.tar
cd bzr-2.2.2
sudo python setup.py install
```

Install ccache:


```
cd /tmp
wget http://samba.org/ftp/ccache/ccache-3.1.4.tar.gz
gunzip ccache-3.1.4.tar.gz
gtar xvf ccache-3.1.4.tar
cd ccache-3.1.4
./configure --prefix /usr
make
sudo make install
```

Configure and start NTP:


```
sudo cp /etc/inet/ntp.server /etc/inet/ntp.conf
sudo vi /etc/inet/ntp.conf

#
# Comment out the following lines:
#server 127.127.XType.0
#fudge 127.127.XType.0 stratum 0
#broadcast 224.0.1.1 ttl 4
#
# Add in the following lines:

server 0.us.pool.ntp.org
server 1.us.pool.ntp.org
server 2.us.pool.ntp.org
server 3.us.pool.ntp.org

# save the file and quit back the command prompt

sudo touch /var/ntp/ntp.drift
sudo ntpdate 0.us.pool.ntp.org
sudo svcadm enable svc:/network/ntp
```

Check out and make a test build of MariaDB:


```
cd
mkdir src
cd src/
bzr branch lp:maria trunk
cd trunk/
BUILD/compile-solaris-amd64
```

Add a user for buildbot:


```
sudo useradd -d /export/home/buildbot -m buildbot
```

Install Buildbot:


```
cd /tmp
wget http://buildbot.googlecode.com/files/buildbot-slave-0.8.3.tar.gz
gunzip -v buildbot-slave-0.8.3.tar.gz
gtar -xf buildbot-slave-0.8.3.tar
cd buildbot-slave-0.8.3/
sudo python setup.py install
```

Create the buildbot as the buildbot user:


On the build master, add new entry to /etc/buildbot/maria-master-private.cfg


Remember the ${slave-name} and ${password} configured above, they're used in
the next step.


Back on the solaris machine:


```
sudo su - buildbot
buildslave create-slave --usepty=0 /export/home/buildbot/maria-slave \
hasky.askmonty.org:9989 ${slavename} ${password}

echo '${contact-email-address}' > /export/home/buildbot/maria-slave/info/admin
echo 'A host running Solaris 10 x86.' > /export/home/buildbot/maria-slave/info/host

exit
```

Now start the slave:


```
sudo su - buildbot
buildslave start maria-slave
```

That's the basic process.


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
