---
title: backports-10.6.19-15
---

* Starting with MariaDB Enterprise Server 10.6.19-15, the space occupied by freed pages within the InnoDB system tablespace can be reclaimed by adding an :autoshrink attribute to innodb\_data\_file\_path, like: (MENT-1304)

```
[mariadb]
...
innodb_data_file_path=ibdata1:12M;ibdata2:50M:autoextend:autoshrink
```

This allows the system tablespace to be truncated after the last allocated page within it, all the way to the specified minimum size (here: 12MiB).

In older release series InnoDB data files never shrink in size during normal operation. One could shrink .ibd files by rebuilding tables with OPTIMIZE TABLE, or the undo tablespace files by `SET GLOBAL innodb_undo_log_truncate=ON`

* The function CONV() , which converts a number between numeric base systems, now supports conversions up to base 62. This allows conversions to encodings to capital letters A-Z, lower case letters a-z, and numbers 0-9. The old limit was 36, not including lower case letters. (MENT-2031)

Example:

```sql
SELECT CONV(61,10,36);
```

```
+----------------+
| CONV(61,10,36) |
+----------------+
| 1P             |
+----------------+
SELECT CONV(61,10,62);
+----------------+
| CONV(61,10,62) |
+----------------+
| z              |
+----------------+
```
