---
description: >-
  MariaDB Enterprise Manager 25.10.1 is a Stable (GA) release of MariaDB
  Enterprise Manager 25.10, released on 2026-03-23
---

# MariaDB Enterprise Manager 25.10.1 Release Notes

**Release Date:** 23 Mar 2026

Release 25.10.1 is a GA release.

This document describes the changes in release 25.10.1, when compared to the previous release in the same series.

### New Features <a href="#new-features" id="new-features"></a>

* MEMA-197 Ability to change the agent listening port for MaxScale
* MEMA-200 Added Podman deployment option

### Bug fixes <a href="#bug-fixes" id="bug-fixes"></a>

* MEMA-198 Database servers with topology name or server name containing dots are shown as "Not registered"
* MEMA-199 Display servers with broken replication in an error state for MaxScale database topologies

### Packaging <a href="#packaging" id="packaging"></a>

* Enterprise Manager is delivered as a suite of container images (via MariaDB Enterprise Docker Registry).
* Agent is delivered via the `mema-agent` OS package via RPM/DEB packages (via MariaDB Enterprise Tools repository).
* Air-gapped installation is supported by exporting and transferring the images and configuration archive to the target environment.

