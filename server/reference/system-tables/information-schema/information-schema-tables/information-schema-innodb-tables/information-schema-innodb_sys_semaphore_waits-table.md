---
description: >-
  The INNODB_SYS_SEMAPHORE_WAITS table displays threads currently waiting for
  semaphores, which is useful for debugging high-concurrency contention.
---

# Information Schema INNODB\_SYS\_SEMAPHORE\_WAITS Table

The [Information Schema](../../) INNODB\_SYS\_SEMAPHORE\_WAITS table is meant to contain information about current semaphore waits. At present it is not correctly populated. See [MDEV-21330](https://jira.mariadb.org/browse/MDEV-21330).

The [PROCESS privilege](../../../../sql-statements/account-management-sql-statements/grant.md#process) is required to view the table.

It contains the following columns:

| Column             | Description                             |
| ------------------ | --------------------------------------- |
| THREAD\_ID         | Thread id waiting for semaphore         |
| OBJECT\_NAME       | Semaphore name                          |
| FILE               | File name where semaphore was requested |
| LINE               | Line number on above file               |
| WAIT\_TIME         | Wait time                               |
| WAIT\_OBJECT       |                                         |
| WAIT\_TYPE         | Object type (mutex, rw-lock)            |
| HOLDER\_THREAD\_ID | Holder thread id                        |
| HOLDER\_FILE       | File name where semaphore was acquired  |
| HOLDER\_LINE       | Line number for above                   |
| CREATED\_FILE      | Creation file name                      |
| CREATED\_LINE      | Line number for above                   |
| WRITER\_THREAD     | Last write request thread id            |
| RESERVATION\_MODE  | Reservation mode (shared, exclusive)    |
| READERS            | Number of readers if only shared mode   |
| WAITERS\_FLAG      | Flags                                   |
| LOCK\_WORD         | Lock word (for developers)              |
| LAST\_READER\_FILE | Removed                                 |
| LAST\_READER\_LINE | Removed                                 |
| LAST\_WRITER\_FILE | Last writer file name                   |
| LAST\_WRITER\_LINE | Above line number                       |
| OS\_WAIT\_COUNT    | Wait count                              |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
