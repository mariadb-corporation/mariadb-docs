# Extracting Entries from the Binary Log

Instructions to narrow down problems on a replication replica.

Sometimes a [binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log) event causes an error of some sort. A whole binary log file is sometimes impractical due to size or sensitivity reasons.

**Step 1: Copy the binary log locally**

This is just in case you don't quite extract the right information first. If the binlog expired off and you haven't got the right information, your bug report may not easily be reproducible.

```bash
sudo cp /var/lib/mysql/mysql-bin.000687 ~/
sudo chown $USER: ~/mysql-bin.000687
```

**Step 2: Create an extract header**

Binary logs have a header portion. Without the header [mariadb-binlog](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog) won't be able to read it. The header also contains valuable session information

We look at the binary log to see how big the header and session information is:

```sql
mariadb-binlog --base64-output=decode-rows --verbose mysql-bin.000687 | more
/*!50530 SET @@SESSION.PSEUDO_SLAVE_MODE=1*/;
/*!40019 SET @@session.max_insert_delayed_threads=0*/;
/*!50003 SET @OLD_COMPLETION_TYPE=@@COMPLETION_TYPE,COMPLETION_TYPE=0*/;
DELIMITER /*!*/;
# at 4
#150323 22:45:58 server id 76  end_log_pos 245  Start: binlog v 4, server v 5.5.39-MariaDB-log created 150323 22:45:58
# at 245
#150323 22:45:58 server id 76  end_log_pos 328  Query   thread_id=9709067       exec_time=0     error_code=0
SET TIMESTAMP=1427116558.923924/*!*/;
SET @@session.pseudo_thread_id=9709067/*!*/;
SET @@session.foreign_key_checks=1, @@session.sql_auto_is_null=0, @@session.unique_checks=1, @@session.autocommit=1/*!*/;
SET @@session.sql_mode=0/*!*/;
SET @@session.auto_increment_increment=1, @@session.auto_increment_offset=1/*!*/;
/*!\C utf8 *//*!*/;
SET @@session.character_set_client=33,@@session.collation_connection=33,@@session.collation_server=8/*!*/;
SET @@session.time_zone='SYSTEM'/*!*/;
SET @@session.lc_time_names=0/*!*/;
SET @@session.collation_database=DEFAULT/*!*/;
BEGIN
/*!*/;
# at 328
```

We see that the session information ends at 328 because of the last line, so we extract to that point.

```
dd if=mysql-bin.000687 of=mysql-bin.000687-extract-offset-129619 bs=1 count=328
```

We need to find out at what offset the entry at 129619 ends and it might be useful to extract some previous entries as well.

```bash
mariadb-binlog --base64-output=decode-rows --verbose mysql-bin.000687 | grep  '^# at ' |  grep -C 10 '^# at 129619$'
# at 127602
# at 127690
# at 128201
# at 128290
# at 128378
# at 128829
# at 128918
# at 129006
# at 129459
# at 129548
# at 129619
# at 129647
# at 130070
# at 130097
# at 130168
# at 130196
# at 130738
# at 130942
# at 130969
# at 131040
# at 131244
```

Take a look at those entries with:

```bash
mariadb-binlog --base64-output=decode-rows --verbose --start-position 129006  --stop-position 130168  mysql-bin.000687 | more
```

Now let's assume we want to start at our original 129619 and finish before 130168

```bash
dd if=mysql-bin.000687 bs=1 skip=129619 count=$(( 130168 - 129619 ))  >> mysql-bin.000687-extract-offset-129619
```

Check the extract:

```bash
mariadb-binlog mysql-bin.000687-extract-offset-129619
```

Upload this to the [private uploads](../../contributing-participating/mariadb-public-ftp-server.md) or attach to the public bug report if nothing sensitive there.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
