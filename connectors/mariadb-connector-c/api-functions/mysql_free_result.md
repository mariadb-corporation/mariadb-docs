---
description: >-
  mysql_free_result releases the memory allocated for a MariaDB result set; row
  values obtained from prior mysql_fetch_row calls become invalid after this
  call.
---

# mysql\_free\_result

## Syntax

```c
void mysql_free_result(MYSQL_RES * result);
```

## Parameter

* `result` - a result set identifier returned by [mysql\_store\_result()](mysql_store_result.md) or [mysql\_use\_result()](mysql_use_result.md).

## Description

Frees the memory associated with a result set.&#x20;

## Return Value

Returns void.

{% hint style="info" %}
* You should always free your result set with mysql\_free\_result() as soon it's not needed anymore
* Row values obtained by a prior [mysql\_fetch\_row()](mysql_fetch_row.md) call will become invalid after calling mysql\_free\_result().
{% endhint %}

## See Also

* [mysql\_store\_result()](mysql_store_result.md)
* [mysql\_use\_result()](mysql_use_result.md)

{% @marketo/form formId="4316" %}
