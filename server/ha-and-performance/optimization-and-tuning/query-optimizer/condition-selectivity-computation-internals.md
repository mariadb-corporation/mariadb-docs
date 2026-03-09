# Condition Selectivity Computation Internals

This page describes how the MariaDB optimizer computes condition selectivities.

## calculate\_cond\_selectivity\_for\_table(T)

This function computes selectivity of the restrictions on a certain table T.\
(TODO: name in the optimizer trace)

Selectivity is computed from

* selectivities of restrictions on different columns ( [histogram data](../query-optimizations/statistics-for-optimizing-queries/histogram-based-statistics.md))
* selectivities of potential range accesses.

Restrictions on different columns, as well as disjoint sets of columns, are considered independent, so their selectivities are multiplied.

### Data From Potential Range Accesses

First, we take into account the selectivities of potential range accesses.

If range accesses on indexes IDX1 and IDX2 do not use the same table column (either the indexes do not have common columns, or they do but range accesses do not use them), then they are considered independent, and their selectivities can be multiplied.

However, in general, range accesses on different indexes may use restrictions on the same column and so cannot be considered independent.

In this case, the following approach is used:

We start with selectivity=1, an empty set of range accesses, and an empty set of columns for which we have taken the selectivity into account.

Then, we add range accesses one by one, updating the selectivity value and noting which columns we have taken into account.

Range accesses that use more key parts are added first.

If we are adding a range access $R whose columns do not overlap with the ones already added, we can just multiply the total selectivity by $R's selectivity.

If $R's columns overlap with columns we've got selectivity data for, the process is as follows:

Find the prefix of columns whose selectivity hasn't been taken into account yet.\
Then, take the selectivity of the whole range access and multiply it by

```
rec_per_key[i-1]/rec_per_key[i]
```

(TODO: and this logic is not clear. More, one can produce table->cond\_selectivity>1 this way. See [MDEV-20740](https://jira.mariadb.org/browse/MDEV-20740))

### Data From Histograms

Then, we want to take into account selectivity data from [histograms](../query-optimizations/statistics-for-optimizing-queries/histogram-based-statistics.md). Each histogram covers one single column.

If the selectivity of a column hasn't been taken into account on the previous step, we take it into account now by multiplying the selectivity by it. Otherwise, we assume that range access has fully taken the column selectivity into account and do nothing.

The third step is sampling-based selectivity data which is out of the scope of this document.

## table\_cond\_selectivity()

This function computes selectivity of restrictions that can be applied after table T has been joined with the join prefix `{T1, ..., Tk}`.

There are two cases:

* Table T uses ref access. In this case, the returned rows match the equalities ref\_access is constructed from. Restrictions on just table T are not checked, yet.
* Table T uses ALL/index/quick select. In this case, restrictions on table T have been applied but cross-table restrictions were not.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
