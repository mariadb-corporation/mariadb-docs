---
description: >-
  Encrypt a string. This function encrypts a string using a password, returning
  a binary string. It is the reverse of the DECODE function.
---

# ENCODE

## Syntax

```sql
ENCODE(str,pass_str)
```

## Description

{% hint style="warning" %}
`ENCODE` is not considered cryptographically secure, and should not be used for password encryption.
{% endhint %}

Encrypt `str` using `pass_str` as the password. To decrypt the result, use [DECODE()](decode.md).

The result is a binary string of the same length as `str`.

The strength of the encryption is based on how good the random generator is.

It is not recommended to rely on the encryption performed by the ENCODE function. Using a salt value (changed when a password is updated) will improve matters somewhat, but for storing passwords, consider a more cryptographically secure function, such as [SHA2()](sha2.md).

## Examples

```sql
ENCODE('not so secret text', CONCAT('random_salt','password'))
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
