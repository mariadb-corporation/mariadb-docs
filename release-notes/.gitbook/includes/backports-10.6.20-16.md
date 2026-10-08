---
title: backports-10.6.20-16
---

* New, Detailed Replication Lag Representation (MENT-2095)
  * The Seconds\_Behind\_Master field of SHOW REPLICA STATUS can be complex and confusing, especially when parallel replication, delayed replication, or the option sql\_slave\_skip\_counter is used. To help provide a consistent view of replication lag, three new fields have been added to the statement's output to provide specific timing information about the state of the IO and SQL threads.
  * Three new values have been added to the replica status:
    * `Master_last_event_time`
      * Timestamp of the last event read from the primary by the IO thread
    * `Slave_last_event_time`
      * Timestamp from the primary of the last event committed on the replica
    * `Master_Slave_time_diff`
      * The difference of the above two timestamps
* New Information Schema Table For Password Related Data (MENT-2145)\
  A new information Schema view, USERS, has been added, which DBAs can use to get insights about password related information for a user. This information can be used:
  * by an application to inform a user about a password about to expire or an account which is at risk of being blocked due to the number of wrong passwords entered
  * by DBAs to query users which have been blocked because of too many invalid passwords entered
  * The new view includes the fields:
    * `USER` – A string including user name and host
    * `PASSWORD_ERRORS` – A counter with the current number of wrong passwords entered
      * Reset to 0 when a correct password has been entered
      * An account is blocked, if `max_password_errors` is reached
      * `NULL` for accounts with privilege `CONNECTION ADMIN`
    * `PASSWORD_EXPIRATION_TIME` – The date and time when the password expires or NULL, if the password never expires
* GTID binlog events now include the thread ID (MENT-2180)
  * The thread ID and the corresponding statement can now be retrieved from binary logs
  * The output of mariadb-binlog also includes the thread ID
