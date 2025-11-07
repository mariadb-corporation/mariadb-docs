# SHOW CREATE SERVER

{% tabs %}
{% tab title="Current" %}
#### Syntax

```sql
SHOW CREATE SERVER server_name
```

#### Description

Shows the [CREATE SERVER](../../data-definition/create/create-server.md) statement that created the given server definition.

#### Example

```sql
SHOW CREATE SERVER srv1\G
*************************** 1. row ***************************
       Server: srv1
Create Server: CREATE SERVER `srv1` FOREIGN DATA WRAPPER mysql 
  OPTIONS (HOST '172.30.0.58', DATABASE 'db1', USER 'maxscale', PASSWORD 'password');
```
{% endtab %}

{% tab title="< 11.7" %}
The `SHOW CREATE SERVER` statement is not available.
{% endtab %}
{% endtabs %}

## See Also

* [CREATE SERVER](../../data-definition/create/create-server.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
