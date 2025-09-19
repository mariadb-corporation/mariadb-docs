# MariaDB ColumnStore 23.10.6 Release Notes

## Overview

MariaDB Enterprise ColumnStore 23.10.6 is a maintenance release of MariaDB Enterprise ColumnStore. MariaDB Enterprise ColumnStore is a columnar storage engine included with MariaDB Enterprise Server.

MariaDB Enterprise ColumnStore 23.10.6 was released on 8 September 2025. This release is of General Availability (GA) maturity. MariaDB Enterprise ColumnStore 23.10.6 is a GA release in the 23.10 series.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.6.23-19 and MariaDB Enterprise Server 11.4.8-5.

## Notable Changes

* cpimport: Add a `-header` option to skip a specified number of rows. (MCOL-4882)
* cpimport: Enhance error handling to log all failed records to a specified file. (MCOL-5164)
* S3: Add a verbose option to `testS3Connection` for more detailed output. (MCOL-4833)
* CMAPI: Clarify `cluster_mode` status when ColumnStore is offline to reduce confusion. (MCOL-5988)
* Error Messaging: Add a more verbose error message for "unable to open Buffered file". (MCOL-4869)
* Logging: Enhance logging to improve the new user experience. (MCOL-5877)
* Error Messaging: Log the table name when a table does not exist in ColumnStore for a more verbose error message. (MCOL-5915)
* CMAPI: Include log collection tools with CMAPI. (MCOL-5300)
* Platforms: Add build support for Red Hat Enterprise Linux 10 and packaging for SELinux policies. (MCOL-6155)

## Issues Fixed

**Can result in hang or crash**

* Timeout issue when `BRM_savesB_journal` is not found. (MCOL-5338)
* `cmapi` writes the local loopback address (`127.0.1.1`) instead of the real IP address. (MCOL-5913)
* CMAPI fails to remove a node from the cluster. (MCOL-6147)

## **Related to performance**

* Increase the default `cpimport` batch size to 8,000,000 to match the maximum extent size. (MCOL-6033)

## Platforms

In alignment with the enterprise lifecycle, MariaDB Enterprise ColumnStore 23.10.6 is provided for:

* Debian 11 (x86\_64, ARM64)
* Debian 12 (x86\_64, ARM64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Red Hat Enterprise Linux 9 (x86\_64, ARM64)
* Red Hat Enterprise Linux 10 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* Rocky Linux 9 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)
* Ubuntu 22.04 (x86\_64, ARM64)
* Ubuntu 24.04 (x86\_64, ARM64)
