---
description: >-
  Row-level security (RLS) restricts access to individual rows of a GridGain 9
  table based on user roles, enforced by the database through security policies.
---

# Row-Level Security

Row-level security (RLS) is a security feature that restricts access to **rows** of a table based on user roles.
While [Role-Based Authorization](role-based-access.md) controls **whether** a user can access a table at all, row-level security controls **which rows within that table** are visible to and changeable by a user.

Access is decided per row by evaluating **security policies** attached to the table against the current user.
This is commonly used to meet compliance requirements and to isolate sensitive data when multiple users
or tenants share the same table.

Since the row-level security rules are enforced by the database, an application cannot accidentally
or deliberately bypass them.

## Limitations

- [**Secondary distribution zones**](../storage/distribution-zones.md#using-secondary-zones). Tables that use a secondary distribution zone are not supported
with row-level security.

- [**Near caches**](../../developers-guide/near-cache.md). The near cache does not track row-level security policy changes.
An entry that was cached while visible and later becomes hidden by a policy change is refreshed
(removed from the cache) only after it expires (based on `expireAfterAccess` and `expireAfterUpdate`) or
on the next access that re-validates it. Until then, the stale row may still be served from the near cache.

## Performance Considerations

Policy expressions are evaluated for every row that a query touches, so complex predicates can affect query performance.
Keep `USING` expressions as simple as possible in your queries.

## What is Row-Level Security

Row-level security has two independent parts:

1. A per-table **switch** that turns row-level security on or off.
2. One or more **policies** that grant visibility to specific roles.

### Security Policies

A **policy** consists of:

- **name** - unique name of the policy within the schema of the target table.
- **table** - name of the table it protects.
- **roles** - set of roles it applies to (or `EVERYONE`).
- **expression** - boolean `USING` predicate that is evaluated for each row.

A user is subject to a policy if any of the user's roles is listed in the policy
(or if the policy targets `EVERYONE`). For each row, the policy's predicate is
evaluated using that row's column values and the current user. If the predicate returns `TRUE`,
the row is visible to the user.

When row-level security is enabled on a table, but **no applicable policy** exists for the current user,
the user sees **no rows** and cannot insert any rows. You must explicitly create policies to grant visibility.
Enabling row-level security without defining any policy effectively hides the entire table from regular users.

{% hint style="info" %}
Row-level security applies to users authenticated through the regular client connection.
Internal system operations run in a privileged context that bypasses row-level security.
{% endhint %}

#### How Policies Are Evaluated

The following rules are applied when evaluating policies:

- A policy is **applicable** to a user if it is defined on the table being accessed and either:
  - the policy targets `EVERYONE`, or
  - the policy's role set includes at least one of the roles assigned to the user.
- Policies that target only roles the user does not have are ignored for that user.
- Policies are **restrictive**, which means that all policies applicable to the user
combine using a logical `AND` to narrow down access:

  - A row is **visible** only if there is at least one applicable policy and the `USING`
predicate of **every** applicable policy evaluates to `TRUE` for that row.
  - If even one applicable policy's predicate evaluates to `FALSE`, the row is hidden.
  - If the user has no applicable policy at all, no rows are visible (see [Security Policies](#security-policies)).

  For example, you can grant managers full access with one policy and limit developers to their own rows
with another. A user that holds both roles is allowed to see a row only if both policies permit it.
- When a row-level security enabled table is replicated with [**Data Center Replication (DCR)**](../data-center-replication/README.md), filtering occurs according to the
configured policies, so the replication user on source cluster must have a role (and the corresponding policy)
that allows reading all rows in the table. As a best practice, grant the replication user a role with
a `USING (TRUE)` policy on each replicated table that has row-level security enabled.

### Policy Expressions

The following restrictions apply to policy expressions:

- The expression must evaluate to `BOOLEAN`.
- Only columns that exist in the target table may be referenced.
- Certain context-dependent temporal functions cannot be used in a policy expression.
See [CREATE POLICY](../../sql-reference/access-control.md#create_policy) for the complete list.

### Read Operation Handling

For read operations (`SELECT`, scans, index lookups, key-value `get`), rows that are not visible
to the user are silently filtered out of the result. The user does not see them.

### Write Operation Handling

Write operations cannot create or expose rows the user is not allowed to see:

- **INSERT** — every inserted row (including values supplied by column `DEFAULT` expressions)
must be visible to the user under the applicable policies. Otherwise, the statement fails
with a row-level security violation. Batch inserts are atomic with respect to row-level security:
if a single row in the batch violates a policy, the whole batch is rejected.
- **UPDATE** and **DELETE** — only rows visible to the user are affected. A user cannot modify a row in a way
that would move it out of their own visibility (for example, reassigning a row to another owner).
Such an update is rejected.

When a write operation violates a policy, the operation fails with a
[`GG-SECURITY-4`](../handling-exceptions.md#security-exceptions) error (`Row-level security constraint violation`).

## Setting Up Row-Level Security

{% hint style="info" %}
Row-level security requires [authentication to be enabled](authentication.md#basic-authentication) on the cluster.
{% endhint %}

Setting up and managing row-level security requires the `MANAGE_RLS` privilege on the target table
(see [User Permissions and Roles](permissions.md)).

At a high level, the steps for setting up row-level security are as follows:

1. Choose which tables require row-level security.
2. Create roles and grant access to tables by those roles. ([CREATE ROLE](../../sql-reference/access-control.md#create-role), [GRANT](../../sql-reference/access-control.md#grant))
3. Define row-level security policies that control which rows each role can access. ([CREATE POLICY](../../sql-reference/access-control.md#create_policy))
4. Enable row-level security on the table. ([ALTER TABLE ... SET ROW LEVEL SECURITY ON](../../sql-reference/ddl.md#set_rls))

### Defining Policies

Create a policy with [CREATE POLICY](../../sql-reference/access-control.md#create_policy) statement. The policy grants the listed
roles visibility of the rows for which the `USING` expression evaluates to `TRUE`. Omit the `TO` clause (or specify
`EVERYONE`) to apply the policy to all roles.

```sql
-- Managers can see all rows.
CREATE POLICY managers_all ON employees TO MANAGER USING (TRUE);

-- Developers can see only the rows they own.
CREATE POLICY developers_own ON employees TO DEVELOPER USING (CURRENT_USER = username);
```

### Enabling Row-Level Security

When creating a table, you can enable row-level security for it by using the `ROW LEVEL SECURITY` table property:

```sql
CREATE TABLE employees (id INT PRIMARY KEY, username VARCHAR, salary INT)
    WITH (ROW LEVEL SECURITY ON);
```

To enable row-level security on a table that already exists, use `ALTER TABLE`:

```sql
ALTER TABLE employees SET ROW LEVEL SECURITY ON;
```

{% hint style="warning" %}
When row-level security is enabled but no policy exists yet, regular users see no rows at all.
{% endhint %}

### Example

Suppose an `employees` table stores the owning user name in the `username` column.
We want users with role `MANAGER` to see all rows of the table, and the users with role `DEVELOPER` to see only their own rows.

Run the following script as an administrator.

```sql
CREATE SCHEMA TEST;
CREATE TABLE test.employees (id INT PRIMARY KEY, username VARCHAR, salary INT);

-- Create users and roles
CREATE USER Jack IDENTIFIED WITH plain_password BY 'password';
CREATE USER Sarah IDENTIFIED WITH plain_password BY 'password';
CREATE ROLE MANAGER;
CREATE ROLE DEVELOPER;
GRANT MANAGER to Jack;
GRANT DEVELOPER to Sarah;
GRANT PRIVILEGES SELECT_FROM_TABLE ON TEST TO DEVELOPER, MANAGER;

-- Turn on row-level security. At this point no policy exists,
-- so regular users see no rows at all.
ALTER TABLE test.employees SET ROW LEVEL SECURITY ON;

-- Create policy for managers (can see all rows).
CREATE POLICY managers_all ON test.employees
        TO MANAGER
        USING (TRUE);

-- Create policy for developers (can see only the rows they own).
CREATE POLICY developers_own ON test.employees
        TO DEVELOPER
        USING (CURRENT_USER = username);

-- Add some data to the table
INSERT INTO test.employees (id, username, salary) VALUES
        (1, 'jack', 100),
        (2, 'sarah', 200),
        (3, 'bob', 150);
```

With these policies in place:

- If user connects to the cluster using `Jack` credentials, the query `SELECT * FROM employees` returns all three rows.
- If user connects to the cluster using `Sarah` credentials, the query returns only the row where `username = 'sarah'`.
- The same rules apply to `UPDATE`, `DELETE`, and `INSERT`; for example, `Sarah` cannot insert or update a row whose `username` is not `sarah`.

## Managing Row-Level Security

Managing the row-level security setting and policies requires the `MANAGE_RLS` privilege on the target table
(see [User Permissions and Roles](permissions.md)). The full command syntax is
described in [ALTER TABLE ... SET ROW LEVEL SECURITY](../../sql-reference/ddl.md#set_rls) (the per-table switch)
and in the [policy commands](../../sql-reference/access-control.md#create_policy) (CREATE, ALTER, and DROP POLICY).

### Disabling Row-Level Security

To turn row-level security off for a table:

```sql
ALTER TABLE employees SET ROW LEVEL SECURITY OFF;
```

While row-level security is disabled, all rows are visible according to the regular
[role-based](role-based-access.md) privileges; the policies are retained
and take effect again when row-level security is re-enabled.

### Inspecting Policies

All configured policies are listed in the [`SYSTEM.POLICIES` system view](../metrics/system-views.md#policies).

### Modifying Policies

Use the [ALTER POLICY](../../sql-reference/access-control.md#alter_policy) statement to change the roles and/or the predicate of
an existing policy. At least one of the `TO` and `USING` clauses must be specified; only the clauses you provide
are changed.

```sql
-- Change only the roles.
ALTER POLICY developers_own TO DEV_ROLE, QA_ROLE;

-- Change only the predicate.
ALTER POLICY developers_own USING (LOWER(CURRENT_USER) = LOWER(username));
```

### Removing Policies

Use [DROP POLICY](../../sql-reference/access-control.md#create_policy) to remove a policy. If the dropped policy was
the only one granting a user access, that user no longer sees any rows while row-level security remains enabled
on the table.

```sql
DROP POLICY developers_own;
```

## See Also

- [ALTER TABLE ... SET ROW LEVEL SECURITY](../../sql-reference/ddl.md#set_rls) — the per-table switch.
- [CREATE / ALTER / DROP POLICY](../../sql-reference/access-control.md#create_policy) — the policy command syntax reference.
- [Role-Based Authorization](role-based-access.md) — how roles and privileges work.
- [User Permissions and Roles](permissions.md#table) — the `MANAGE_RLS` privilege.
