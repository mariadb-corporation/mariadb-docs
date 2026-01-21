# DBT3 Example Preparation Time

This page contains database preparation and creation times that were discovered\
while working on the [DBT3 Automation Scripts](dbt3-automation-scripts.md).

## Database creation times

| Setup                                                                                                                                                                                    | Time                                 | Size on Disk |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ------------ |
| Postgre s30 on pitbull                                                                                                                                                                   | 758 min = 12 h 38 min.               | 75 GB        |
| MariaDB + MyISAM s10 on 4CPU 4GB RAM developer machine                                                                                                                                   | 96 m 22s = 1h 36m 22s                | 17 GB        |
| MariaDB + MyISAM s100 on facebook-maria2:                                                                                                                                                | 424m 4s = 7h 4m 4s.                  | 162 GB       |
| MariaDB + InnoDB s100 on facebook-maria2:                                                                                                                                                | 577m 42s = 9h 37m 42s.               |              |
| [MariaDB 5.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-3-series/mariadb-532-release-notes) + InnoDB s30 on facebook-maria1 | 122m39.753s = 2h 2m 40s.             | 71 GB        |
| [MariaDB 5.5.18](https://github.com/mariadb-corporation/docs-server/blob/test/en/mariadb-5518-release-notes/README.md) + InnoDB s30 on facebook-maria1                                   | 150m46.218s = 2h 30m 46s.            | 71 GB        |
| MySQL 5.6.4 + InnoDB s30 on facebook-maria1:                                                                                                                                             | 140m18.272s = 2h 20m 18s.            | 71 GB        |
| MariaDB + MyISAM s30 on pitbull with pre\_create\_PK                                                                                                                                     | > 3h 30m (with limited RAM to 11 GB) |              |
| MariaDB + MyISAM s30 on facebook-maria1:                                                                                                                                                 | 99m 8s = 1h 39m 8s.                  | 49 GB        |
| MySQL 5.6.4 + MyISAM s30 on facebook-maria1                                                                                                                                              | 114m 17s.                            | 49 GB        |

## Dataload creation time

| Setup                                      | Time            | Size on Disk                      |
| ------------------------------------------ | --------------- | --------------------------------- |
| Scale 10 on 4CPU 4GB RAM developer machine | 8 min 44 sec.   | 10.4 GB                           |
| Scale 30 on pitbull.askmonty.org           | 20 min 28 sec.  | 32 GB (with limited RAM to 11 GB) |
| Scale 100 on facebook-maria2               | 78 min 27.601s. | 106 GB                            |
| Scale 30 on facebook-maria1                | 23 min 40 sec.  |                                   |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
