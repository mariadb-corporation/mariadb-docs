---
description: >-
  Plugin API reference: my_snprintf Service. Generated from the MariaDB server headers by doxygen and moxygen.
---



# my_snprintf Service

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Plugin Services`](plugin_api_services.md)

Portable and limited vsnprintf() implementation.

This is a portable, limited vsnprintf() implementation, with some extra features. "Portable" means that it'll produce identical result on all platforms (for example, on Windows and Linux system printf e formats the exponent differently, on different systems p either prints leading 0x or not, s may accept null pointer or crash on it). "Limited" means that it does not support all the C89 features. But it supports few extensions, not in any standard.

## Classes

| Name | Description |
|------|-------------|
| [`my_snprintf_service_st`](#my_snprintf_service_st) |  |

## Macros

| Name | Description |
|------|-------------|
| [`my_snprintf`](#my_snprintf)  | A portable, limited vsnprintf() implementation, with some extra features. |
| [`my_vsnprintf`](#my_vsnprintf)  |  |

---

### my_snprintf

```cpp
#define my_snprintf(to, n, fmt, to, n, fmt) my_snprintf_service->my_snprintf_type
```

Defined in service_my_snprintf.h:120

A portable, limited vsnprintf() implementation, with some extra features.

#### Returns
a number of bytes written to a buffer *excluding* terminating '\0'

> [!NOTE]
> The syntax of a format string is generally the same: 
> ```
> %[<flag>][<length>][.<precision>][<size modifier>]<format>[<format extension>]
> ```
>  where everything but the `format` is optional.

Two one-character `flags` are recognized:

* '0' has the standard zero-padding semantics;
* '-' is parsed, but silently ignored;

Both `length` and `precision` are the same as in the standard. They can be specified as integers, or as '*' to consume an int argument.

`size modifier` can be 'l', 'll', or 'z'.

Supported `format`s are `s` (null pointer is accepted, printed as "(null)"), `c`, `d`, `i`, `u`, `x`, `X`, `o`, `p` (works as "0x%x"), `f`, and `g`.

The `$n` syntax for positional arguments is supported.

Format extensions:

* Format 'sQ' quotes the string with "\`" (backtick)s similar to "%s", but also "escapes" existing backticks in the string to '\`\`' as in SQL ''''.
* Format 'sB' treats the argument as a byte sequence. It reads and prints exactly `precision` bytes without terminating on any `\0`s in the sequence. The default `precision` when it's unspecified is not defined.
* Format 'sT' replaces the end of the printed string with "..." if it was truncated.
* Format 'sS' is a synonym for 's'. It's an escape that avoid consuming the following plain char as one of the above extension suffixes. Example: "Data Class: %sSType"
* Format 'iE' treats the argument as an errno number. It prints this number, a space, then its corresponding error message in double quotes. In other words: 
```cpp
printf("%iE", n) === printf("%i \"%sT\"", n, strerror(n))
```
* Format 'dE' has no effect. Therefore, to escape 'iE', use 'dE' instead.

Unrecognized and multiple suffixes are not parsed; for example, both "%sTQ" and "%iQ" will suffix with a literal 'Q'.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `to` |  | A buffer to store the result in |
| `n` |  | Store up to n-1 characters, followed by an end 0 |
| `fmt` |  | printf-like format string |
| `to` |  | A buffer to store the result in |
| `n` |  | Store up to n-1 characters, followed by an end 0 |
| `fmt` |  | printf-like format string |

---

### my_vsnprintf

```cpp
#define my_vsnprintf my_snprintf_service->my_vsnprintf_type
```

Defined in service_my_snprintf.h:121

## Variables

| Return | Name | Description |
|--------|------|-------------|
| struct [`my_snprintf_service_st`](#my_snprintf_service_st) * | [`my_snprintf_service`](#my_snprintf_service)  |  |

---

### my_snprintf_service

```cpp
struct my_snprintf_service_st * my_snprintf_service
```

Type: struct [`my_snprintf_service_st`](#my_snprintf_service_st) *

Defined in service_my_snprintf.h:55


## Class Definitions



### my_snprintf_service_st

```cpp
#include <service_my_snprintf.h>
```

```cpp
struct my_snprintf_service_st
```

Defined in service_my_snprintf.h:50

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `size_t(*` | [`my_snprintf_type`](#my_snprintf_type)  |  |
| `size_t(*) size_t(*` | [`my_vsnprintf_type`](#my_vsnprintf_type)  |  |

---

#### my_snprintf_type

```cpp
size_t(* my_snprintf_type)(char *, size_t, const char *,...) ATTRIBUTE_FORMAT_FPTR(printf
```

Defined in service_my_snprintf.h:51

---

#### my_vsnprintf_type

```cpp
size_t(*) size_t(* my_vsnprintf_type)(char *, size_t, const char *, va_list) ATTRIBUTE_FORMAT_FPTR(printf
```

Defined in service_my_snprintf.h:53

