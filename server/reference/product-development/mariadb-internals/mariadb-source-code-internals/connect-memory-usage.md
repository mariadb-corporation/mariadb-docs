---
description: >-
  Provides a technical breakdown of how the server allocates and manages memory
  for each client connection and thread.
---

# Connection Memory Usage

{% include "../../../../.gitbook/includes/this-page-contains-backgrou....md" %}

When creating a connection, a THD object is created for that connection. This contains\
all connection information and also caches to speed up queries and avoid frequent malloc() calls.

When creating a new connection, the following malloc() calls are done for the THD:

The following information is the state in [MariaDB 10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1061-release-notes) when compiled without debugging.

## Local Thread Memory

This is part of `select memory_used from information_schema.processlist`.

| Amount allocated | Where allocated                                                                                    | Description                                      |
| ---------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| 26646            | THD::THD                                                                                           | Allocation of THD object                         |
| 256              | Statement\_map::Statement\_map(), my\_hash\_init(key\_memory\_prepared\_statement\_map, \&st\_hash | Prepared statements                              |
| 256              | my\_hash\_init(key\_memory\_prepared\_statement\_map, \&names\_hash                                | Names of used prepared statements                |
| 128              | wsrep\_wfc(), Opt\_trace\_context(), dynamic\_array()                                              |                                                  |
| 1024             | Diagnostics\_area::init(),init\_sql\_alloc(PSI\_INSTRUMENT\_ME, \&m\_warn\_root                    |                                                  |
| 120              | Session\_sysvars\_tracker, global\_system\_variables.session\_track\_system\_variables             | Tracking of changed session variables            |
| 280              | THD::THD,my\_hash\_init(key\_memory\_user\_var\_entry,\&user\_vars                                 |                                                  |
| 280              | THD::THD,my\_hash\_init(PSI\_INSTRUMENT\_ME, \&sequences                                           | Cache of used sequences                          |
| 1048             | THD::THD, m\_token\_array= my\_malloc(PSI\_INSTRUMENT\_ME, max\_digest\_length                     |                                                  |
| 16416            | CONNECT::create\_thd(), my\_net\_init(), net\_allocate\_new\_packet()                              | This is for reading data from the connected user |
| 16416            | check\_connection(), thd->packet.alloc()                                                           | This is for sending data to connected user       |

## Objects Stored in THD->memroot During Connect

| Amount allocated | Where allocated                                                         | Description                            |
| ---------------- | ----------------------------------------------------------------------- | -------------------------------------- |
| 72               | send\_server\_handshake\_packet, mpvio->cached\_server\_packet.pkt=     |                                        |
| 64               | parse\_client\_handshake\_packet, thd->copy\_with\_error(...db,db\_len) |                                        |
| 32               | parse\_client\_handshake\_packet, sctx->user=                           |                                        |
| 368              | ACL\_USER::copy(), root=                                                | Allocation of ACL\_USER object         |
| 56               | ACL\_USER::copy(), dst->user= safe\_lexcstrdup\_root(root, user)        |                                        |
| 56               | ACL\_USER::copy()                                                       | Allocation of other connect attributes |
| 56               | ACL\_USER::copy()                                                       |                                        |
| 64               | ACL\_USER::copy()                                                       |                                        |
| 64               | ACL\_USER::copy()                                                       |                                        |
| 32               | mysql\_change\_db()                                                     | Store current db in THD                |
| 48               | dbname\_cache->insert(db\_name)                                         | Store db name in db name cache         |
| 40               | mysql\_change\_db(), my\_register\_filename(db.opt)                     | Store filename db.opt                  |
| 8216             | load\_db\_opt(), init\_io\_cache()                                      | Disk cache for reading db.opt          |
| 1112             | load\_db\_opts(), put\_dbopts()                                         | Cache default database parameters      |

## State at First Call to mysql\_execute\_command

```
(gdb) p thd->status_var.local_memory_used
$24 = 75496
(gdb) p thd->status_var.global_memory_used
$25 = 17544
(gdb) p thd->variables.query_prealloc_size
$30 = 24576
(gdb) p thd->variables.trans_prealloc_size
$37 = 4096
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
