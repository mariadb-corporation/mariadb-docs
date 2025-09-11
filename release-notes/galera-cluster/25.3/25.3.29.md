# Galera 25.3.29 Release Notes

Codership is pleased to announce the release of Galera Replication library 3.29, implementing wsrep API version 25.

The library is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, CentOS, RHEL, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of Galera for FreeBSD is available in the FreeBSD Ports Collection.

Notable fixes in Galera replication since last binary release by Codership (3.28):

* A bug in GCS where JOIN message was delivered even if the node was in DONOR state was fixed.
* An issue where GCache could contain mixed histories from different clusters was fixed.
*   Setting `socket.recv_buf_size` was not effective because it was done after the socket was connected or accepted. Also the default value caused TCP receive buffer autotuning to be disabled. This lead to suboptimal performance in high bandwidth WAN clusters.

    The default value for `socket.recv_buf_size` was changed to 'auto' which lets the kernel to tune TCP receive buffer. A new variable `socket.send_buf_size` with default value 'auto' was added to allow also send buffer tuning. (codership/galera#552)
* GComm socket timestamping/liveness checking caused false positives during replication of large transactions, which caused excessive amounts of broken connections. (codership/galera#553)
* Large transactions were able to monopolize bandwidth when segmentation was configured. This caused messages which were relayed by segment representative to be delayed. As a fix implemented fair queuing of messages. (codership/galera#553)
* GComm EVS layer did excessive broadcasting to retransmit missing messages when packets were lost or delayed. The communication protocol was optimized to use point-to-point messaging to deliver missing messages and to rate limit retransmission requests. (codership/galera#554)
* Because of a bug in quorum computation, two primary conflicting primary components were formed when the group merged and partitioned again while the new primary view was forming. (codership/galera#563)

## Reminder: Changes to Repositories Structure

With the new release the repository structure is changed to allow for existence of all of the wsrep-patched mysql versions currently supported: 5.5 through 5.7. Thus the repository layout requires from the user to adjust his or her repository configuration to accomodate those changes. In order to have the WSREP and Galera library installed, one would need to add the following repositories: 1. Galera-3 repository for galera library: e.g. https://releases.galeracluster.com/galera-3// 2. Corresponding mysql-wsrep repository: e.g. https://releases.galeracluster.com/mysql-wsrep-/ here: _ldist_ is Linux distribution (Ubuntu, Centos, ...) and _mversion_ is MySQL version, i.e. 5.5, 5.6, 5.7

### How To Install

Repositories contain dummy or meta packages, called mysql-wsrep- which are convenience packages for installation of the corresponding version of WSREP. One can install the whole suite by running, for example: `apt-get install mysql-wsrep-5.6 galera-3`

**Quirks for Ubuntu Xenial and 5.6**

Due to the peculiarities of how apt resolves packages and presence of 5.7 libraries in Xenial repositories the command above might require additional steps/changes in order to succeed.

One would need to either configure apt pinning for codership repositories for them to have priority over upstream packages or to specify mysql-common package version explicitly as the one located in the WSREP repositories in order to get things installed.
