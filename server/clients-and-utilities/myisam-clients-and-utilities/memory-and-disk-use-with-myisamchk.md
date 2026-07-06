---
description: >-
  Tune myisamchk memory and disk usage to speed up checking and repairing
  large MyISAM tables.
---

# Memory and Disk Use With myisamchk

myisamchk's performance can be dramatically enhanced for larger tables by making sure that its memory-related variables are set to an optimum level.

By default, myisamchk will use very little memory (about 3MB is allocated), but can temporarily use a lot of disk space. If disk space is a limitation when repairing, the _--safe-recover_ option should be used instead of _--recover_. However, if TMPDIR points to a memory file system, an out of memory error can easily be caused, as myisamchk places temporary files in TMPDIR. The _--tmpdir=path_ option should be used in this case to specify a directory on disk.

myisamchk has the following requirements for disk space:

* When repairing, space for twice the size of the data file, available in the same directory as the original file. This is for the original file as well as a copy. This space is not required if the --quick option is used, in which case only the index file is re-created.
* Disk space in the temporary directory (TMPDIR or the tmpdir=path option) is needed for sorting if the --recover or --sort-recover options are used when not using --safe-recover). The space required is approximately (largest\_key + row\_pointer\_length) \* number\_of\_rows \* 2. To get information about the length of the keys as well as the row pointer length, use myisamchk -dv table\_name.
* Space for a new index file to replace the existing one. The old index is first truncated, so unless the old index file is not present or is smaller for some reason, no significant extra space is needed.

There are a number of [system variables](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) that are useful to adjust when running myisamchk. They will increase memory usage, and since some are per-session variables, you don't want to increase the general value, but you can either pass an increased value to myisamchk as a command line option, or with a \[myisamchk] section in your [my.cnf](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) file.

* [sort\_buffer\_size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sort_buffer_size). By default this is 4M, but it's very useful to increase to make myisamchk sorting much faster. Since the server won't be running when you run myisamchk, you can increase substantially. 16M is usually a minimum, but values such as 256M are not uncommon if memory is available.
* [key\_buffer\_size](../../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size) (which particularly helps with the --extend-check and --safe-recover options.
* [read\_buffer\_size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#read_buffer_size)
* [write\_buffer\_size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#write_buffer_size)

For example, if you have more than 512MB available to allocate to the process, the following settings could be used:

```
myisamchk 
  --myisam_sort_buffer_size=256M
  --key_buffer_size=512M
  --read_buffer_size=64M
  --write_buffer_size=64M
...
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
