# Spell Check: Technical Test

This file tests for false positives.
These words should be IGNORED:

* InnoDB
* Galera
* mariadbd
* mysqld
* k8s

We can also test code blocks:
```sql
SELECT * FROM my_table;
```

And inline code like `my_var` or `my_func_wrod()` should be fine.
