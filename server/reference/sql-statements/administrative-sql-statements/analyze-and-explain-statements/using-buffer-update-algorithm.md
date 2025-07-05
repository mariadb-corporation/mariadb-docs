
# Using Buffer UPDATE Algorithm

This article explains the [UPDATE](../../data-manipulation/changing-deleting-data/update.md) statement's *Using Buffer* algorithm.


Consider the following table and query:



| Name | Salary |
| --- | --- |
| Name | Salary |
| Babatunde | 1000 |
| Jolana | 1050 |
| Pankaja | 1300 |



```sql
UPDATE employees SET salary = salary+100 WHERE salary < 2000;
```

Suppose the *employees* table has an index on the *salary* column, and the optimizer decides to use a range scan on that index.


The optimizer starts a range scan on the *salary* index. We find the first record *Babatunde, 1000*. If we do an on-the-fly update, we immediately instruct the storage engine to change this record to be *Babatunde, 1000+100=1100*.


Then we proceed to search for the next record, and find *Jolana, 1050*. We instruct the storage engine to update it to be *Jolana, 1050+100=1150*.


Then we proceed to search for the next record ... and what happens next depends on the storage engine. In some storage engines, data changes are visible immediately, so we will find the *Babatunde, 1100* record that we wrote at the first step, modifying it again, giving Babatunde an undeserved raise. Then we will see Babatunde again and again, looping continually.


In order to prevent such situations, the optimizer checks whether the UPDATE statement is going to change key values for the keys it is using. In that case, it will use a different algorithm:


1. Scan everyone with "salary<2000", remembering the rowids of the rows in a buffer.
1. Read the buffer and apply the updates.


This way, each row will be updated only once.


The `Using buffer` [EXPLAIN](explain.md) output indicates that the buffer as described above will be used.


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
