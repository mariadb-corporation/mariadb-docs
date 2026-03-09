# optimizer\_adjust\_secondary\_key\_costs

#### `optimizer_adjust_secondary_key_costs`

* Description: Gives the user the ability to affect how the costs for secondary keys using `ref` are calculated in the few cases when [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106) up to [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/what-is-mariadb-1011) makes a sub-optimal choice when optimizing `ref` access, either for key lookups or `GROUP BY`. `ref`, as used by [EXPLAIN](../../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain.md), means that the optimizer is using key-lookup on one value to find the matching rows from a table. Unused from [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/what-is-mariadb-110). In [MariaDB 10.6.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-18-release-notes) the variable was changed from a number to a set of strings and `disable_forced_index_in_group_by` (value 4) was added.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `set`
* Default Value: `fix_reuse_range_for_ref`, `fix_card_multiplier`
* Range: `0` to `63` or any combination of `adjust_secondary_key_cost`, `disable_max_seek` or `disable_forced_index_in_group_by`, `fix_innodb_cardinality`,`fix_reuse_range_for_ref`, `fix_card_multiplier`
* Introduced: [MariaDB 10.6.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-17-release-notes), [MariaDB 10.11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-7-release-notes)

```sql
MariaDB [securedb]> select @@version;
+-----------------------------------+
| @@version             |
+-----------------------------------+
| 10.6.20-16-MariaDB-enterprise-log |
+-----------------------------------+
1 row in set (0.001 sec)

MariaDB [securedb]> select @@optimizer_adjust_secondary_key_costs;
+---------------------------------------------+
| @@optimizer_adjust_secondary_key_costs   |
+---------------------------------------------+
| fix_reuse_range_for_ref,fix_card_multiplier |
+---------------------------------------------+
```

**MariaDB starting with** [**11.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/what-is-mariadb-110)

`optimizer_adjust_secondary_key_costs` will be obsolete starting from [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/what-is-mariadb-110) as the new optimizer in 11.0 does not have max\_seek optimization and is already using cost based choices for index usage with GROUP BY.

The value for `optimizer_adjust_secondary_key_costs` is one of more of the following:

| Value                                 | Version added                                                                                                                | Old behavior                                                                                                                                                                                                                       | Change when variable is used                                                                                                                                                                                                                                                |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| adjust\_secondary\_key\_cost          | [10.6.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-17-release-notes) | Limit ref costs by max\_seeks                                                                                                                                                                                                      | The secondary key costs for ref are updated to be at least five times the clustered primary key costs if a clustered primary key exists                                                                                                                                     |
| disable\_max\_seek                    | [10.6.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-17-release-notes) | ref cost on secondary keys is limited to max\_seek = min('number of expected rows'/ 10, scan\_time\*3)                                                                                                                             | Disable 'max\_seek' optimization and do a slight adjustment of filter cost                                                                                                                                                                                                  |
| disable\_forced\_index\_in\_group\_by | [10.6.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-18-release-notes) | Use a rule-based choice when deciding to use an index to resolve GROUP BY                                                                                                                                                          | The choice is now cost based                                                                                                                                                                                                                                                |
| fix\_innodb\_cardinality              | [10.6.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-19-release-notes) | By default InnoDB doubles the cardinality for indexes in an effort to force index usage over table scans. This can cause the optimizer to create sub-optimal plans for ranges or index entries that cover a big part of the table. | Using this option removes the doubling of cardinality in InnoDB. fix\_innodb\_cardinality is recommended to be used only as a server startup option, as it is enabled for a table at first usage. See [MDEV-34664](https://jira.mariadb.org/browse/MDEV-34664) for details. |
| fix\_reuse\_range\_for\_ref           | [10.6.20](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-20-release-notes) | Number of estimated rows for 'ref' did not always match costs from range optimizer                                                                                                                                                 | Use cost from range optimizer for 'ref' if all used key parts are constants. The old code did not always do this                                                                                                                                                            |
| fix\_card\_multiplier                 | [10.6.20](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-20-release-notes) | Index selectivity can be bigger than 1.0 if index statistics is not up to date. Not on by default.                                                                                                                                 | Ensure that the calculated index selectivity is never bigger than 1.0. Having index selectivity bigger than 1.0 causes MariaDB to believe that there is more rows in the table than in reality, which can cause wrong plans. This option is on by default.                  |

One can set all options with:

```sql
SET @@optimizer_adjust_secondary_key_costs='all';
```

## Explanations of the old behavior in MariaDB 10.x

The reason for the max\_seek optimization was originally to ensure that MariaDB would use a key instead of a table scan. This works well for a lot of queries, but can cause problems when a table scan is a better choice, such as when one would have to scan more than 1/4 of the rows in the table (in which case a table scan is better).

## See Also

* The [optimizer\_switch](optimizer-switch.md) system variable.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
