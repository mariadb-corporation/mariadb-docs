---
title: backports-11.4.8-5
---

* Segmented key cache for Aria ([MENT-2361](https://jira.mariadb.org/browse/MENT-2361))
  * A new variable [aria-pagecache-segments](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria/aria-system-variables#aria_pagecache_segments) (default 1) to define the number of segments has been added. The default disables the new feature.
