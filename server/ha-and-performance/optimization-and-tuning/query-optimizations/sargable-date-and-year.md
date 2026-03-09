# Sargable DATE and YEAR

Starting from [MariaDB 11.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/what-is-mariadb-111), conditions in the form

```sql
YEAR(indexed_date_col) CMP const_value
DATE(indexed_date_col) CMP const_value
```

are sargable, provided that

* CMP is any of `=`, `<=>`, `<`, `<=`, `>`, `>=` .
* `indexed_date_col` has a type of `DATE`, `DATETIME` or `TIMESTAMP` and is a part of some index.

One can swap the left and right hand sides of the equality: `const_value CMP {DATE|YEAR}(indexed_date_col)` is also handled.

Sargable here means that the optimizer is able to use such conditions to construct access methods, estimate their selectivity, or use them to perform partition pruning.

## Implementation

Internally, the optimizer rewrites the condition to an equivalent condition which doesn't use `YEAR` or `DATE` functions.

For example, `YEAR(date_col)=2023` is rewritten into`date_col between '2023-01-01' and '2023-12-31'`.

Similarly, `DATE(datetime_col) <= '2023-06-01'` is rewritten into`datetime_col <= '2023-06-01 23:59:59'`.

## Controlling the Optimization

The optimization is always ON, there is no Optimizer Switch flag to control it.

## Optimizer Trace

The rewrite is logged as `date_conds_into_sargable` transformation. Example:

```json
{
            "transformation": "date_conds_into_sargable",
            "before": "cast(t1.datetime_col as date) <= '2023-06-01'",
            "after": "t1.datetime_col <= '2023-06-01 23:59:59'"
          },
```

## References

* [MDEV-8320](https://jira.mariadb.org/browse/MDEV-8320): Allow index usage for DATE(datetime\_column) = const

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
