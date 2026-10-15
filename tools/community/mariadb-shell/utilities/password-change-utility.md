---
description: >-
  Change the password of your own MariaDB account or of another account with
  util.change_password(), interactively or from a script.
---

# Password Change Utility

`util.change_password()` changes the password of a MariaDB account over the global session. Without options, it changes the password of the account you are connected as and prompts for the new password twice, so the password never appears in your command history or on the screen.

## Syntax

```python
util.change_password([options])
```

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `account` | string | The current account | The account to change, in the form `user@host`, for example `"app@%"` or `"report@localhost"`. |
| `newPassword` | string | Not set | The new password. If you don't give it, the shell prompts for it twice. |

The utility accepts no other options. MariaDB Server has no random passwords and no dual (retained) passwords, so options for those features are rejected:

```text
ValueError: Invalid options at Argument #1: random
```

The utility needs an open global session. It isn't available through command line integration; run it in Python mode or in a script passed with `-f` or `--pyc`.

## Changing Your Own Password

Connect as the account and call the utility without options:

```text
MariaDB 127.0.0.1:3306 ssl  Py > util.change_password()
Changing password for app@%.
Enter new password: ********
Confirm new password: ********
NOTE: Password has been successfully updated.
```

If the two entries don't match, the shell asks again. After three mismatches, the utility stops with `Failed to enter matching passwords.`

For your own account, the utility runs `SET PASSWORD = PASSWORD(...)`. That statement needs no privilege beyond being connected, and it keeps the authentication plugin of the account. For example, an account that authenticates with `ed25519` still does so after the change.

{% hint style="info" %}
The utility treats the account as your own only when `account` is omitted or matches the value of `CURRENT_USER()` exactly, such as `app@%`. If you write your own account in a different form, such as `'app'@'%'`, the utility handles it like another account and needs the privileges described below.
{% endhint %}

## Changing the Password of Another Account

Pass the account in the `account` option:

```text
MariaDB localhost:3306 ssl  Py > util.change_password({"account": "report@localhost"})
Changing password for report@localhost.
Enter new password: ********
Confirm new password: ********
NOTE: Password has been successfully updated.
```

For another account, the utility runs `SET PASSWORD FOR ... = PASSWORD(...)`, which also keeps the authentication plugin of the account. You need the `CREATE USER` privilege or the `UPDATE` privilege on the `mysql` schema. Before it prompts, the utility reads the account definition with `SHOW CREATE USER`, so you also need to be allowed to read account definitions. Without these privileges, or if the account doesn't exist, the utility stops before it prompts:

```text
mysqlsh.DBError: MySQL Error (1044): Access denied for user 'app'@'%' to database 'mysql'
mysqlsh.DBError: MySQL Error (1133): Can't find any matching row in the user table
```

## Password Validation

If the server has a password validation plugin, such as `simple_password_check` or `cracklib_password_check`, and rejects the new password, the utility shows the reason and prompts for another password:

```text
Changing password for app@%.
Your password does not satisfy the current policy requirements (simple_password_check)
Enter new password:
```

This also happens when you passed the rejected password in `newPassword`. After three rejected passwords, the utility stops with `Failed to change password:` and the last error from the server. Other errors stop the utility at once.

## Using the Utility in Scripts

In a script, pass the new password in `newPassword` so that the utility doesn't prompt. Read the password from a secure source rather than writing it into the script:

{% code title="rotate_report_password.py" %}
```python
import os

util.change_password({
    "account": "report@localhost",
    "newPassword": os.environ["REPORT_NEW_PASSWORD"],
})
```
{% endcode %}

```sh
REPORT_NEW_PASSWORD='...' mariadb-shell admin@db1.example.com --py -f rotate_report_password.py
```

If you store passwords in the [credential store](../connecting/credential-store.md), update the stored password after the change, because the shell doesn't do it automatically.
