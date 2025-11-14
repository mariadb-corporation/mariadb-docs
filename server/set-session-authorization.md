# SET SESSION AUTHORIZATION

{% hint style="info" %}
This statement is available from MariaDB 12.0.
{% endhint %}

Certain users can perform server actions as another user:

* This is implemented through the `SET SESSION AUTHORIZATION` statement.
* This permits everything that can be done in a [stored procedure](server-usage/stored-routines/stored-procedures/) with an arbitrary definer.
* In particular, this bypasses [account lock](security/user-account-management/account-locking.md), [expired password](security/user-account-management/user-password-expiry.md), authentication, `REQUIRE SSL` checks, and so on.
* Users are required to have the [SET USER](reference/sql-statements/account-management-sql-statements/grant.md#set-user) privilege.
* Does not work inside [transactions](reference/sql-statements/transactions/), prepared statements and [stored procedures](server-usage/stored-routines/stored-procedures/).

### Examples

```sql
SELECT USER(), CURRENT_USER(), DATABASE();
```

```
+--------------------+--------------------+------------+
| user()             | current_user()     | database() |
+--------------------+--------------------+------------+
| msandbox@localhost | msandbox@localhost | test       |
+--------------------+--------------------+------------+
1 row in set (0.000 sec)
```

```sql
SET SESSION AUTHORIZATION foo@localhost;
SELECT USER(), CURRENT_USER(), DATABASE();
```

```
+---------------+----------------+------------+
| user()        | current_user() | database() |
+---------------+----------------+------------+
| foo@localhost | foo@%          | NULL       |
+---------------+----------------+------------+
```
