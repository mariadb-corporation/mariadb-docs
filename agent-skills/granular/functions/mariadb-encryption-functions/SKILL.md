---
name: mariadb-encryption-functions
description: "MariaDB encryption, hashing, and compression functions — AES_ENCRYPT/AES_DECRYPT keyed off block_encryption_mode (default aes-128-ecb) with optional IV/mode since 11.2; SHA2/SHA1/MD5 checksums; KDF and RANDOM_BYTES for key derivation; COMPRESS/UNCOMPRESS/UNCOMPRESSED_LENGTH; PASSWORD/OLD_PASSWORD/ENCRYPT for auth hashing; ENCODE/DECODE (weak, not removed) vs DES_ENCRYPT/DES_DECRYPT (removed in 13.0). Use when writing SQL that encrypts, hashes, derives keys from, or compresses data in MariaDB."
---

# MariaDB Encryption, Hashing, and Compression Functions

*Last updated: 2026-07-20*

Catalog of every built-in encryption, hashing, and compression function in MariaDB, with signature and a one-line semantic summary per entry. For a function not listed here, fall
back to the canonical reference at
<https://mariadb.com/docs/server/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions>.

> **Default context:** Assume MariaDB **11.8 LTS** unless the user specifies another version. Functions with a `*(since X.Y)*` annotation are only available from that version onward; everything else is in every current LTS branch (10.6, 10.11, 11.4, 11.8).

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
| --- | --- |
| `AES_ENCRYPT(str, key)` with just two arguments, expecting a randomized/IV-based cipher | With no `mode`/`iv` it uses the session's `block_encryption_mode` system variable, which **defaults to `aes-128-ecb`** — ECB has no IV and is deterministic (identical plaintext + key → identical ciphertext), which leaks equality patterns. *(Since 11.2)* pass an explicit IV and mode: `AES_ENCRYPT(str, key, iv, 'aes-256-cbc')`; generate the IV with `RANDOM_BYTES(16)` |
| Treating `AES_DECRYPT()` returning non-`NULL` as proof the key/mode was correct | It returns `NULL` only when it detects invalid data or incorrect padding — with a wrong key or wrong mode it can still return a non-`NULL` **garbage** string. A cipher/mode mismatch (e.g. encrypting with CBC, decrypting with ECB) is a common source of silent garbage, not an error |
| Storing `AES_ENCRYPT()`/`COMPRESS()`/`RANDOM_BYTES()`/`KDF()` output in `CHAR`/`VARCHAR`/`TEXT` | All four return a **binary string** — store it in `VARBINARY`/`BLOB`, or it gets mangled by charset conversion/trailing-space trimming. `AES_ENCRYPT()`'s result length follows `16 * (TRUNC(string_length/16) + 1)` because AES is block-padded |
| Reaching for `DES_ENCRYPT()`/`DES_DECRYPT()` for new code, or assuming they still work on a current server | **Removed in MariaDB 13.0**, along with the `--des-key-file` option and `FLUSH DES_KEY_FILE` statement (deprecated in earlier releases first). They still work at the 11.8 baseline, but code intended to run on 13.0+ must migrate to `AES_ENCRYPT()`/`AES_DECRYPT()` |
| Assuming `ENCODE()`/`DECODE()` were removed alongside `DES_ENCRYPT()`/`DES_DECRYPT()` in 13.0 | They were **not** removed — both remain registered functions. They are, however, explicitly documented as not cryptographically secure and unsuitable for password storage; prefer `AES_ENCRYPT()` (confidentiality) or `SHA2()` (one-way hashing) for anything security-sensitive |
| `SHA2(str, hash_len)` unexpectedly returning `NULL` on a server that otherwise works fine | Besides an invalid `hash_len` (must be 224, 256, 384, 512, or 0=256) or a `NULL` input, `SHA2()` also returns `NULL` (or is unusable) if the server was **not built with TLS/SSL support** — it depends on the SSL library's SHA implementation, unlike `MD5()`/`SHA1()` which are always available |
| Treating `PASSWORD(NULL)` as `NULL`-propagating like most functions | It returns an **empty string `''`**, not `NULL`, when the argument is `NULL` — check for `''` if you need to detect a missing input. `PASSWORD()` is also not a general-purpose hash: it produces the server's authentication string (format depends on the account's auth plugin) and is meant only for `SET PASSWORD`/`CREATE USER`, not application-level hashing |
| Using `MD5()` or `SHA1()` for password storage or as a general security hash | Both are checksums, not secure password hashes — `MD5()`'s page explicitly warns against using it as an encryption function due to known vulnerabilities; use `SHA2()` (or `KDF()` for a slow, brute-force-resistant derivation) instead |
| Assuming `KDF()` and `RANDOM_BYTES()` are available on any current MariaDB version | `RANDOM_BYTES()` is available *(since 10.10)* and `KDF()` *(since 11.3)* — both post-date the 10.6 LTS baseline this skill otherwise treats as universal, so gate their use if targeting an older still-maintained branch |

## Functions

<!-- BEGIN GENERATED -->
<!-- Extracted from server/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions -->
<!-- 17 functions, 0 pages skipped on extraction failure -->

### AES_DECRYPT
`AES_ENCRYPT(crypt_str, key_str, [, iv [, mode]])`  
This function allows decryption of data using the official AES (Advanced Encryption Standard) algorithm.

### AES_ENCRYPT
`AES_ENCRYPT(str, key, [, iv [, mode]])`  
`AES_ENCRYPT()` and AES_DECRYPT() allow encryption and decryption of data using the official AES (Advanced Encryption Standard) algorithm, previously known as "Rijndael." Encoding with a 128-bit key length is used (from MariaDB 11.2.0, this is the default, and can be changed).

### COMPRESS
`COMPRESS(string_to_compress)`  
Compresses a string and returns the result as a binary string.

### DECODE
`DECODE(crypt_str,pass_str)`  
In the default mode, `DECODE` decrypts the encrypted string <kbd>_crypt_str_</kbd> using <kbd>_pass_str_</kbd> as the password.

### DES_DECRYPT
`DES_DECRYPT(crypt_str[,key_str])`  
Decrypts a string encrypted with DES_ENCRYPT().

### DES_ENCRYPT
`DES_ENCRYPT(str[,{key_num|key_str}])`  
Encrypts the string with the given key using the Triple-DES algorithm.

### ENCODE
`ENCODE(str,pass_str)`  
Encrypt `str` using `pass_str` as the password.

### ENCRYPT
`ENCRYPT(str[,salt])`  
Encrypts a string using the Unix crypt() system call, returning an encrypted binary string.

### KDF
`KDF(key_str, salt [, {info | iterations} [, kdf_name [, width ]]])`  
`KDF` is a key derivation function, similar to OpenSSL's EVP_KDF_derive().

### MD5
`MD5(str)`  
Calculates an MD5 128-bit checksum for the string.

### OLD_PASSWORD
`OLD_PASSWORD(str)`  
`OLD_PASSWORD()` was added to MySQL when the implementation of PASSWORD() was changed to improve security.

### PASSWORD
`PASSWORD(str)`  
The `PASSWORD()` function is used for hashing passwords for use in authentication by the MariaDB server.

### RANDOM_BYTES
`RANDOM_BYTES(length)`  
Given a _length_ from 1 to 1024, generates a binary string of _length_ consisting of random bytes generated by the SSL library's random number generator.

### SHA1
`SHA1(str), SHA(str)`  
Calculates an SHA-1 160-bit checksum for the string _`str`_, as described in RFC 3174 (Secure Hash Algorithm).

### SHA2
`SHA2(str,hash_len)`  
Given a string _`str`_, calculates an SHA-2 checksum, which is considered more cryptographically secure than its SHA-1 equivalent.

### UNCOMPRESS
`UNCOMPRESS(string_to_uncompress)`  
Uncompresses a string compressed by the COMPRESS() function.

### UNCOMPRESSED_LENGTH
`UNCOMPRESSED_LENGTH(compressed_string)`  
Returns the length that the compressed string had before being compressed with COMPRESS().
<!-- END GENERATED -->

## See Also

- **`mariadb-string-functions`** — `HEX()`/`UNHEX()`, `TO_BASE64()`/`FROM_BASE64()` for rendering binary encryption/hash output as text
- **`mariadb-create-table`** — `VARBINARY`/`BLOB` column types for storing the binary results of `AES_ENCRYPT()`, `COMPRESS()`, `RANDOM_BYTES()`, and `KDF()`
- Canonical reference on `mariadb.com/docs`: <https://mariadb.com/docs/server/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions>
