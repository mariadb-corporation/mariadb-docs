---
description: >-
  Technical requirements and installation procedures for running Buildbot on
  Solaris Sparc architecture.
---

# Buildbot Setup for Solaris Sparc

## Setting up a BuildBot slave on Solaris

**NOTE #1:**_It would probably make sense to create a seperate zone for the buildbot on your Solaris 10 system. That is left up to you!_

**NOTE #2:**_You might need to install the Zope Interface package for some of the Python pieces to work properly. Do this after installing Python 2.5. You can find information on the Zope Interface on their_ [_site_](https://pypi.python.org/pypi/zope.interface)_._

### Solaris 10 (SPARC)

Unless you want to spend time optimizing the underlying Solaris 10 (SPARC)\
installation, it is strongly suggested that you choose the "Entire" Software\
Group during the installation process. Once you have your Solaris 10 (SPARC)\
system on the network and able to access the Internet you can use the\
following suggestions to setup your buildbot:

1. By default Solaris 10 comes packages with Python 2.6.x. For compatibility reasons, you need to install Python 2.5.x. The author found it easiest to use Sunfreeware (ftp://ftp.sunfreeware.com/pub/freeware/sparc/5.10/):

```
$ cd /tmp
$ ftp ftp.sunfreeware.com
Name: anonymous
Password: (your email address)
ftp> bin
ftp> cd pub/freeware/sparc/5.10/
ftp> get python-2.5.4-sol10-sparc-local.gz
ftp> quit 
$ gunzip python-2.5.4-sol10-sparc-local.gz
$ pkgadd -d python-2.5.4-sol10-sparc-local
```

If you are unfamiliar with howto install packages from Sunfreeware please\
read their [howto](https://www.sunfreeware.com/indexsparc10.html).

1. Setup your environment:

* Create a user:

```
$ useradd -d /export/home/buildbot -m buildbot
```

It is imperative that you not use Bash as the buildbot user's shell.\
It could have been a dependency issue but I literally spent several days\
trying to solve why the buildbot wasn't checking out code with bzr only to\
discover that using the default Solaris shell fixed the problem. If someone\
comes up with a solution please let us know on the mailing list.

* Adjust the global profile (you could be more granular here but since I'm\
  setting up a dedicated system I wasn't):

```
$ vi /etc/profile
LD_LIBRARY_PATH=/opt/csw/lib:/usr/local/lib:/usr/sfw/lib:$LD_LIBRARY_PATH 

# Add required libraries

PYTHONPATH=/usr/local/lib/python2.5/site-packages:$PYTHONPATH 

# Makes Python 2.5 the default

PATH=/usr/local/bin:/usr/bin:/usr/sbin:/etc:/usr/sfw/bin:$PATH 

# Puts "local" packages in your path

export LOGNAME PATH PYTHONPATH LD_LIBRARY_PATH
```

1. Install the latest Twisted:

```
$ wget tmrc.mit.edu/mirror/twisted/Twisted/9.0/Twisted-9.0.0.tar.bz2
$ bunzip2 Twisted-9.0.0.tar.bz2
$ tar -xf Twisted-9.0.0.tar
$ cd Twisted-9.0.0
$ python setup.py build install
```

1. Install required packages from Sunfreeware:

```
automake, autoconf, gcc, m4, md5, openssl, libsigsegv, Tcl, Tk, perl,
libtool, sed, libgcc, gcc, libintl, libiconv, zlib, binutils, groff, cmake
```

1. Install the Bazaar DVCS:

* You can find a package on [Google Code](https://code.google.com/p/bzrunix/downloads/list).
* Install the latest Bazaar for Solaris 10. At the time of this writing it was\
  1.14.1: [bzr-1.14.1-sol10-sparc-local.gz](https://bzrunix.googlecode.com/files/bzr-1.14.1-sol10-sparc-local.gz) .

1. Volunteer your buildbot to the Maria team. Follow the directions listed in the Volunteering to run a build slave section of the [About Buildbot](../about-buildbot.md) page.
2. Create the buildbot as the buildbot user:

```
buildbot create-slave --usepty=0 /export/home/buildbot/maria-slave
hasky.askmonty.org:9989 ${buildbotname} <passwd>
```

Replace ${buildbotname} with the buildbot name you received from the\
MariaDB developers. Replace with the password they gave you.\
You can adjust these and other parameters anytime within the\
maria-slave/buildbot.tac file at anytime in the future.

1. Create a shared Bazaar repository in the buildbot build directory:

```
HOME=/export/home/buildbot; bzr init-repo maria-slave/${buildbotname}
```

Replace ${buildbotname} like you did in Step #7.

1. Attach the buildbot to the master (this assumes you are not logged in as buildbot):

```
sudo su - buildbot -c "/usr/bin/buildbot start /export/home/buildbot/maria-slave"
```

OPTIONAL: You can create a proper service by following (and modifying as necessary) these [directions](https://wadofstuff.blogspot.com/2007/01/smf-manifest-for-buildbot.html)

1. Please ask on the #maria [IRC](https://github.com/mariadb-corporation/docs-server/blob/test/en/irc/README.md) channel on irc.freenode.net if you have\
   problems or questions setting up your buildbot. Or ask on the on the [maria-developers](https://launchpad.net/~maria-developers) mailing list.
2. Check the status of your buildbot through the [BuildBot buildslaves](https://buildbot.askmonty.org/buildbot/buildslaves) page.

This howto was contributed by Adam Dutko. The original version is [here](https://littlehat.homelinux.org/tuts/MariaDB/buildbot/README-SOL10-SPARC).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
