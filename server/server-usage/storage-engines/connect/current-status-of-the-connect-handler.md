---
description: The CONNECT storage engine has been deprecated.
---

# Current Status of the CONNECT Handler

{% hint style="warning" %}
This storage engine has been deprecated.
{% endhint %}

The CONNECT handler is a GA (stable) release. It was written starting both from an aborted project written for MySQL in 2004 and from the “DBCONNECT” program. It was tested on all the examples described in this document, and is distributed with a set of 53 test cases. Here is a not limited list of future developments:

1. Adding more table types.
2. Make more tests files (53 are already made)
3. Adding more data types, in particular unsigned ones (done for unsigned).
4. Supporting indexing on nullable and decimal columns.
5. Adding more optimize tools (block indexing, dynamic indexing, etc.) (done)
6. Supporting MRR (done)
7. Supporting partitioning (done)
8. Getting NOSQL data from the Net as answers from REST queries (done)

No programs are bug free, especially new ones. Please [report all bugs](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/community/bug-tracking/reporting-bugs) or documentation errors using the means provided by MariaDB.

<sub>_This page is licensed: GPLv2_</sub>

{% @marketo/form formId="4316" %}
