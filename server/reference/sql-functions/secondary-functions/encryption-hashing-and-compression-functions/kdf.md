---
description: >-
  Derive a key. This function derives a key from a password using a Key
  Derivation Function (KDF), enhancing security for password storage.
---

# KDF

{% hint style="info" %}
`KDF()` is a key derivation function available from [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.3/11.3.0).
{% endhint %}

## Syntax

```sql
KDF(key_str, salt [, {info | iterations} [, kdf_name [, width ]]])
```

## Description

`KDF` is a key derivation function, similar to OpenSSL's EVP\_KDF\_derive(). The purpose of a KDF is to be slow, so if the calculated value is lost/stolen, the original `key_str` is not achievable easily with modern GPU. KDFs are therefore an ideal replacement for password hashes. KDFs can also pad out a password secret to the number of bits used in encryption algorithms.

For generating good encryption keys for [AES\_ENCRYPT](aes_encrypt.md) a less expensive but cryptographically secure function like [RANDOM\_BYTES](random_bytes.md) is recommended.

* <kbd>kdf\_name</kbd> is "hkdf" or "pbkdf2\_hmac" (default).
* Width (in bits) can be any number divisible by 8, by default it's taken from @@block\_encryption\_mode.
* Iterations must be positive, and is 1000 by default.

Note that OpenSSL 1.0 doesn't support HKDF, so in this case `NULL` is returned. This OpenSSL version is still used in SLES 12 and CentOS 7.

## Examples

```sql
select hex(kdf('foo', 'bar', 'infa', 'hkdf')); 
+----------------------------------------+
| hex(kdf('foo', 'bar', 'infa', 'hkdf')) |
+----------------------------------------+
| 612875F859CFB4EE0DFEFF9F2A18E836       |
+----------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
