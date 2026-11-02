---
description: >-
  The MYSQL_FILE structure and the mysql_file_* wrappers for opening, reading,
  writing, seeking, syncing, renaming, and deleting files with Performance
  Schema instrumentation.
---

# File Instrumentation

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Instrumentation Interface`](./)

## Classes

| Name                                                     | Description                                                                                     |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| [`st_mysql_file`](file_instrumentation.md#st_mysql_file) | An instrumented FILE structure. **See also**: [MYSQL\_FILE](file_instrumentation.md#mysql_file) |

## Macros

| Name                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`PSI_FILE_CALL`](file_instrumentation.md#psi_file_call)                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [`mysql_file_register`](file_instrumentation.md#mysql_file_register)                       | File registration.                                                                                                                                                                                                                                                                                                                                                                                                                |
| [`mysql_file_fgets`](file_instrumentation.md#mysql_file_fgets)                             | Instrumented fgets. `mysql_file_fgets` is a replacement for `fgets`.                                                                                                                                                                                                                                                                                                                                                              |
| [`mysql_file_fgetc`](file_instrumentation.md#mysql_file_fgetc)                             | Instrumented fgetc. `mysql_file_fgetc` is a replacement for `fgetc`.                                                                                                                                                                                                                                                                                                                                                              |
| [`mysql_file_fputs`](file_instrumentation.md#mysql_file_fputs)                             | Instrumented fputs. `mysql_file_fputs` is a replacement for `fputs`.                                                                                                                                                                                                                                                                                                                                                              |
| [`mysql_file_fputc`](file_instrumentation.md#mysql_file_fputc)                             | Instrumented fputc. `mysql_file_fputc` is a replacement for `fputc`.                                                                                                                                                                                                                                                                                                                                                              |
| [`mysql_file_fprintf`](file_instrumentation.md#mysql_file_fprintf)                         | Instrumented fprintf. `mysql_file_fprintf` is a replacement for `fprintf`.                                                                                                                                                                                                                                                                                                                                                        |
| [`mysql_file_vfprintf`](file_instrumentation.md#mysql_file_vfprintf)                       | Instrumented vfprintf. `mysql_file_vfprintf` is a replacement for `vfprintf`.                                                                                                                                                                                                                                                                                                                                                     |
| [`mysql_file_fflush`](file_instrumentation.md#mysql_file_fflush)                           | Instrumented fflush. `mysql_file_fflush` is a replacement for `fflush`.                                                                                                                                                                                                                                                                                                                                                           |
| [`mysql_file_feof`](file_instrumentation.md#mysql_file_feof)                               | Instrumented feof. `mysql_file_feof` is a replacement for `feof`.                                                                                                                                                                                                                                                                                                                                                                 |
| [`mysql_file_fstat`](file_instrumentation.md#mysql_file_fstat)                             | Instrumented fstat. `mysql_file_fstat` is a replacement for `my_fstat`.                                                                                                                                                                                                                                                                                                                                                           |
| [`mysql_file_stat`](file_instrumentation.md#mysql_file_stat)                               | Instrumented stat. `mysql_file_stat` is a replacement for `my_stat`.                                                                                                                                                                                                                                                                                                                                                              |
| [`mysql_file_chsize`](file_instrumentation.md#mysql_file_chsize)                           | Instrumented chsize. `mysql_file_chsize` is a replacement for `my_chsize`.                                                                                                                                                                                                                                                                                                                                                        |
| [`mysql_file_fopen`](file_instrumentation.md#mysql_file_fopen)                             | Instrumented fopen. `mysql_file_fopen` is a replacement for `my_fopen`.                                                                                                                                                                                                                                                                                                                                                           |
| [`mysql_file_fclose`](file_instrumentation.md#mysql_file_fclose)                           | Instrumented fclose. `mysql_file_fclose` is a replacement for `my_fclose`. Without the instrumentation, this call will have the same behavior as the undocumented and possibly platform specific my\_fclose(NULL, ...) behavior. With the instrumentation, mysql\_fclose(NULL, ...) will safely return 0, which is an extension compared to my\_fclose and is therefore compliant. mysql\_fclose is on purpose _not_ implementing |
| [`mysql_file_fread`](file_instrumentation.md#mysql_file_fread)                             | Instrumented fread. `mysql_file_fread` is a replacement for `my_fread`.                                                                                                                                                                                                                                                                                                                                                           |
| [`mysql_file_fwrite`](file_instrumentation.md#mysql_file_fwrite)                           | Instrumented fwrite. `mysql_file_fwrite` is a replacement for `my_fwrite`.                                                                                                                                                                                                                                                                                                                                                        |
| [`mysql_file_fseek`](file_instrumentation.md#mysql_file_fseek)                             | Instrumented fseek. `mysql_file_fseek` is a replacement for `my_fseek`.                                                                                                                                                                                                                                                                                                                                                           |
| [`mysql_file_ftell`](file_instrumentation.md#mysql_file_ftell)                             | Instrumented ftell. `mysql_file_ftell` is a replacement for `my_ftell`.                                                                                                                                                                                                                                                                                                                                                           |
| [`mysql_file_create`](file_instrumentation.md#mysql_file_create)                           | Instrumented create. `mysql_file_create` is a replacement for `my_create`.                                                                                                                                                                                                                                                                                                                                                        |
| [`mysql_file_create_temp`](file_instrumentation.md#mysql_file_create_temp)                 | Instrumented create\_temp\_file. `mysql_file_create_temp` is a replacement for `create_temp_file`.                                                                                                                                                                                                                                                                                                                                |
| [`mysql_file_open`](file_instrumentation.md#mysql_file_open)                               | Instrumented open. `mysql_file_open` is a replacement for `my_open`.                                                                                                                                                                                                                                                                                                                                                              |
| [`mysql_file_close`](file_instrumentation.md#mysql_file_close)                             | Instrumented close. `mysql_file_close` is a replacement for `my_close`.                                                                                                                                                                                                                                                                                                                                                           |
| [`mysql_file_read`](file_instrumentation.md#mysql_file_read)                               | Instrumented read. `mysql_read` is a replacement for `my_read`.                                                                                                                                                                                                                                                                                                                                                                   |
| [`mysql_file_write`](file_instrumentation.md#mysql_file_write)                             | Instrumented write. `mysql_file_write` is a replacement for `my_write`.                                                                                                                                                                                                                                                                                                                                                           |
| [`mysql_file_pread`](file_instrumentation.md#mysql_file_pread)                             | Instrumented pread. `mysql_pread` is a replacement for `my_pread`.                                                                                                                                                                                                                                                                                                                                                                |
| [`mysql_file_pwrite`](file_instrumentation.md#mysql_file_pwrite)                           | Instrumented pwrite. `mysql_file_pwrite` is a replacement for `my_pwrite`.                                                                                                                                                                                                                                                                                                                                                        |
| [`mysql_file_seek`](file_instrumentation.md#mysql_file_seek)                               | Instrumented seek. `mysql_file_seek` is a replacement for `my_seek`.                                                                                                                                                                                                                                                                                                                                                              |
| [`mysql_file_tell`](file_instrumentation.md#mysql_file_tell)                               | Instrumented tell. `mysql_file_tell` is a replacement for `my_tell`.                                                                                                                                                                                                                                                                                                                                                              |
| [`mysql_file_delete`](file_instrumentation.md#mysql_file_delete)                           | Instrumented delete. `mysql_file_delete` is a replacement for `my_delete`.                                                                                                                                                                                                                                                                                                                                                        |
| [`mysql_file_rename`](file_instrumentation.md#mysql_file_rename)                           | Instrumented rename. `mysql_file_rename` is a replacement for `my_rename`.                                                                                                                                                                                                                                                                                                                                                        |
| [`mysql_file_create_with_symlink`](file_instrumentation.md#mysql_file_create_with_symlink) | Instrumented create with symbolic link. `mysql_file_create_with_symlink` is a replacement for `my_create_with_symlink`.                                                                                                                                                                                                                                                                                                           |
| [`mysql_file_delete_with_symlink`](file_instrumentation.md#mysql_file_delete_with_symlink) | Instrumented delete with symbolic link. `mysql_file_delete_with_symlink` is a replacement for `my_handler_delete_with_symlink`.                                                                                                                                                                                                                                                                                                   |
| [`mysql_file_rename_with_symlink`](file_instrumentation.md#mysql_file_rename_with_symlink) | Instrumented rename with symbolic link. `mysql_file_rename_with_symlink` is a replacement for `my_rename_with_symlink`.                                                                                                                                                                                                                                                                                                           |
| [`mysql_file_sync`](file_instrumentation.md#mysql_file_sync)                               | Instrumented file sync. `mysql_file_sync` is a replacement for `my_sync`.                                                                                                                                                                                                                                                                                                                                                         |

***

### PSI\_FILE\_CALL

```cpp
#define PSI_FILE_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql\_file.h:58

***

### mysql\_file\_register

```cpp
#define mysql_file_register(P1, P2, P3, P1, P2, P3) inline_mysql_file_register(P1, P2, P3)
```

Defined in psi/mysql\_file.h:65

File registration.

***

### mysql\_file\_fgets

```cpp
#define mysql_file_fgets(P1, P2, F, P1, P2, F) inline_mysql_file_fgets(P1, P2, F)
```

Defined in psi/mysql\_file.h:77

Instrumented fgets. `mysql_file_fgets` is a replacement for `fgets`.

***

### mysql\_file\_fgetc

```cpp
#define mysql_file_fgetc(F, F) inline_mysql_file_fgetc(F)
```

Defined in psi/mysql\_file.h:89

Instrumented fgetc. `mysql_file_fgetc` is a replacement for `fgetc`.

***

### mysql\_file\_fputs

```cpp
#define mysql_file_fputs(P1, F, P1, F) inline_mysql_file_fputs(P1, F)
```

Defined in psi/mysql\_file.h:101

Instrumented fputs. `mysql_file_fputs` is a replacement for `fputs`.

***

### mysql\_file\_fputc

```cpp
#define mysql_file_fputc(P1, F, P1, F) inline_mysql_file_fputc(P1, F)
```

Defined in psi/mysql\_file.h:114

Instrumented fputc. `mysql_file_fputc` is a replacement for `fputc`.

***

### mysql\_file\_fprintf

```cpp
#define mysql_file_fprintf inline_mysql_file_fprintf
```

Defined in psi/mysql\_file.h:123

Instrumented fprintf. `mysql_file_fprintf` is a replacement for `fprintf`.

***

### mysql\_file\_vfprintf

```cpp
#define mysql_file_vfprintf(F, P1, P2, F, P1, P2) inline_mysql_file_vfprintf(F, P1, P2)
```

Defined in psi/mysql\_file.h:134

Instrumented vfprintf. `mysql_file_vfprintf` is a replacement for `vfprintf`.

***

### mysql\_file\_fflush

```cpp
#define mysql_file_fflush(F, F) inline_mysql_file_fflush(F)
```

Defined in psi/mysql\_file.h:147

Instrumented fflush. `mysql_file_fflush` is a replacement for `fflush`.

***

### mysql\_file\_feof

```cpp
#define mysql_file_feof(F, F) inline_mysql_file_feof(F)
```

Defined in psi/mysql\_file.h:156

Instrumented feof. `mysql_file_feof` is a replacement for `feof`.

***

### mysql\_file\_fstat

```cpp
#define mysql_file_fstat(FN, S, FL, FN, S, FL) inline_mysql_file_fstat(FN, S, FL)
```

Defined in psi/mysql\_file.h:167

Instrumented fstat. `mysql_file_fstat` is a replacement for `my_fstat`.

***

### mysql\_file\_stat

```cpp
#define mysql_file_stat(K, FN, S, FL, K, FN, S, FL) inline_mysql_file_stat(FN, S, FL)
```

Defined in psi/mysql\_file.h:180

Instrumented stat. `mysql_file_stat` is a replacement for `my_stat`.

***

### mysql\_file\_chsize

```cpp
#define mysql_file_chsize(F, P1, P2, P3, F, P1, P2, P3) inline_mysql_file_chsize(F, P1, P2, P3)
```

Defined in psi/mysql\_file.h:193

Instrumented chsize. `mysql_file_chsize` is a replacement for `my_chsize`.

***

### mysql\_file\_fopen

```cpp
#define mysql_file_fopen(K, N, F1, F2, K, N, F1, F2) inline_mysql_file_fopen(N, F1, F2)
```

Defined in psi/mysql\_file.h:206

Instrumented fopen. `mysql_file_fopen` is a replacement for `my_fopen`.

***

### mysql\_file\_fclose

```cpp
#define mysql_file_fclose(FD, FL, FD, FL) inline_mysql_file_fclose(FD, FL)
```

Defined in psi/mysql\_file.h:226

Instrumented fclose. `mysql_file_fclose` is a replacement for `my_fclose`. Without the instrumentation, this call will have the same behavior as the undocumented and possibly platform specific my\_fclose(NULL, ...) behavior. With the instrumentation, mysql\_fclose(NULL, ...) will safely return 0, which is an extension compared to my\_fclose and is therefore compliant. mysql\_fclose is on purpose _not_ implementing

```cpp
assert(file != NULL) 
```

, since doing so could introduce regressions.

***

### mysql\_file\_fread

```cpp
#define mysql_file_fread(FD, P1, P2, P3, FD, P1, P2, P3) inline_mysql_file_fread(FD, P1, P2, P3)
```

Defined in psi/mysql\_file.h:239

Instrumented fread. `mysql_file_fread` is a replacement for `my_fread`.

***

### mysql\_file\_fwrite

```cpp
#define mysql_file_fwrite(FD, P1, P2, P3, FD, P1, P2, P3) inline_mysql_file_fwrite(FD, P1, P2, P3)
```

Defined in psi/mysql\_file.h:252

Instrumented fwrite. `mysql_file_fwrite` is a replacement for `my_fwrite`.

***

### mysql\_file\_fseek

```cpp
#define mysql_file_fseek(FD, P, W, F, FD, P, W, F) inline_mysql_file_fseek(FD, P, W, F)
```

Defined in psi/mysql\_file.h:265

Instrumented fseek. `mysql_file_fseek` is a replacement for `my_fseek`.

***

### mysql\_file\_ftell

```cpp
#define mysql_file_ftell(FD, F, FD, F) inline_mysql_file_ftell(FD, F)
```

Defined in psi/mysql\_file.h:278

Instrumented ftell. `mysql_file_ftell` is a replacement for `my_ftell`.

***

### mysql\_file\_create

```cpp
#define mysql_file_create(K, N, F1, F2, F3, K, N, F1, F2, F3) inline_mysql_file_create(N, F1, F2, F3)
```

Defined in psi/mysql\_file.h:291

Instrumented create. `mysql_file_create` is a replacement for `my_create`.

***

### mysql\_file\_create\_temp

```cpp
#define mysql_file_create_temp(K, T, D, P, M, F, K, T, D, P, M, F) inline_mysql_file_create_temp(T, D, P, M, F)
```

Defined in psi/mysql\_file.h:304

Instrumented create\_temp\_file. `mysql_file_create_temp` is a replacement for `create_temp_file`.

***

### mysql\_file\_open

```cpp
#define mysql_file_open(K, N, F1, F2, K, N, F1, F2) inline_mysql_file_open(N, F1, F2)
```

Defined in psi/mysql\_file.h:317

Instrumented open. `mysql_file_open` is a replacement for `my_open`.

***

### mysql\_file\_close

```cpp
#define mysql_file_close(FD, F, FD, F) inline_mysql_file_close(FD, F)
```

Defined in psi/mysql\_file.h:330

Instrumented close. `mysql_file_close` is a replacement for `my_close`.

***

### mysql\_file\_read

```cpp
#define mysql_file_read(FD, B, S, F, FD, B, S, F) inline_mysql_file_read(FD, B, S, F)
```

Defined in psi/mysql\_file.h:343

Instrumented read. `mysql_read` is a replacement for `my_read`.

***

### mysql\_file\_write

```cpp
#define mysql_file_write(FD, B, S, F, FD, B, S, F) inline_mysql_file_write(FD, B, S, F)
```

Defined in psi/mysql\_file.h:356

Instrumented write. `mysql_file_write` is a replacement for `my_write`.

***

### mysql\_file\_pread

```cpp
#define mysql_file_pread(FD, B, S, O, F, FD, B, S, O, F) inline_mysql_file_pread(FD, B, S, O, F)
```

Defined in psi/mysql\_file.h:369

Instrumented pread. `mysql_pread` is a replacement for `my_pread`.

***

### mysql\_file\_pwrite

```cpp
#define mysql_file_pwrite(FD, B, S, O, F, FD, B, S, O, F) inline_mysql_file_pwrite(FD, B, S, O, F)
```

Defined in psi/mysql\_file.h:382

Instrumented pwrite. `mysql_file_pwrite` is a replacement for `my_pwrite`.

***

### mysql\_file\_seek

```cpp
#define mysql_file_seek(FD, P, W, F, FD, P, W, F) inline_mysql_file_seek(FD, P, W, F)
```

Defined in psi/mysql\_file.h:395

Instrumented seek. `mysql_file_seek` is a replacement for `my_seek`.

***

### mysql\_file\_tell

```cpp
#define mysql_file_tell(FD, F, FD, F) inline_mysql_file_tell(FD, F)
```

Defined in psi/mysql\_file.h:408

Instrumented tell. `mysql_file_tell` is a replacement for `my_tell`.

***

### mysql\_file\_delete

```cpp
#define mysql_file_delete(K, P1, P2, K, P1, P2) inline_mysql_file_delete(P1, P2)
```

Defined in psi/mysql\_file.h:421

Instrumented delete. `mysql_file_delete` is a replacement for `my_delete`.

***

### mysql\_file\_rename

```cpp
#define mysql_file_rename(K, P1, P2, P3, K, P1, P2, P3) inline_mysql_file_rename(P1, P2, P3)
```

Defined in psi/mysql\_file.h:434

Instrumented rename. `mysql_file_rename` is a replacement for `my_rename`.

***

### mysql\_file\_create\_with\_symlink

```cpp
#define mysql_file_create_with_symlink(K, P1, P2, P3, P4, P5, K, P1, P2, P3, P4, P5) inline_mysql_file_create_with_symlink(P1, P2, P3, P4, P5)
```

Defined in psi/mysql\_file.h:449

Instrumented create with symbolic link. `mysql_file_create_with_symlink` is a replacement for `my_create_with_symlink`.

***

### mysql\_file\_delete\_with\_symlink

```cpp
#define mysql_file_delete_with_symlink(K, P1, P2, P3, K, P1, P2, P3) inline_mysql_file_delete_with_symlink(P1, P2, P3)
```

Defined in psi/mysql\_file.h:463

Instrumented delete with symbolic link. `mysql_file_delete_with_symlink` is a replacement for `my_handler_delete_with_symlink`.

***

### mysql\_file\_rename\_with\_symlink

```cpp
#define mysql_file_rename_with_symlink(K, P1, P2, P3, K, P1, P2, P3) inline_mysql_file_rename_with_symlink(P1, P2, P3)
```

Defined in psi/mysql\_file.h:477

Instrumented rename with symbolic link. `mysql_file_rename_with_symlink` is a replacement for `my_rename_with_symlink`.

***

### mysql\_file\_sync

```cpp
#define mysql_file_sync(P1, P2, P1, P2) inline_mysql_file_sync(P1, P2)
```

Defined in psi/mysql\_file.h:490

Instrumented file sync. `mysql_file_sync` is a replacement for `my_sync`.

## Typedefs

| Return                                                          | Name                                               | Description                                                                                                                                                |
| --------------------------------------------------------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| struct [`st_mysql_file`](file_instrumentation.md#st_mysql_file) | [`MYSQL_FILE`](file_instrumentation.md#mysql_file) | Type of an instrumented file. `MYSQL_FILE` is a drop-in replacement for `FILE`. **See also**: [mysql\_file\_open](file_instrumentation.md#mysql_file_open) |

***

### MYSQL\_FILE

```cpp
using MYSQL_FILE = struct st_mysql_file
```

Type: struct [`st_mysql_file`](file_instrumentation.md#st_mysql_file)

Defined in psi/mysql\_file.h:515

Type of an instrumented file. `MYSQL_FILE` is a drop-in replacement for `FILE`. **See also**: [mysql\_file\_open](file_instrumentation.md#mysql_file_open)

## Functions

| Return                                                | Name                                                                                                                       | Description |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `void`                                                | [`inline_mysql_file_register`](file_instrumentation.md#inline_mysql_file_register) `static` `inline`                       |             |
| `char *`                                              | [`inline_mysql_file_fgets`](file_instrumentation.md#inline_mysql_file_fgets) `static` `inline`                             |             |
| `int`                                                 | [`inline_mysql_file_fgetc`](file_instrumentation.md#inline_mysql_file_fgetc) `static` `inline`                             |             |
| `int`                                                 | [`inline_mysql_file_fputs`](file_instrumentation.md#inline_mysql_file_fputs) `static` `inline`                             |             |
| `int`                                                 | [`inline_mysql_file_fputc`](file_instrumentation.md#inline_mysql_file_fputc) `static` `inline`                             |             |
| `int`                                                 | [`inline_mysql_file_fprintf`](file_instrumentation.md#inline_mysql_file_fprintf) `static` `inline`                         |             |
| `int`                                                 | [`inline_mysql_file_vfprintf`](file_instrumentation.md#inline_mysql_file_vfprintf) `static` `inline`                       |             |
| `int`                                                 | [`inline_mysql_file_fflush`](file_instrumentation.md#inline_mysql_file_fflush) `static` `inline`                           |             |
| `int`                                                 | [`inline_mysql_file_feof`](file_instrumentation.md#inline_mysql_file_feof) `static` `inline`                               |             |
| `int`                                                 | [`inline_mysql_file_fstat`](file_instrumentation.md#inline_mysql_file_fstat) `static` `inline`                             |             |
| `MY_STAT *`                                           | [`inline_mysql_file_stat`](file_instrumentation.md#inline_mysql_file_stat) `static` `inline`                               |             |
| `int`                                                 | [`inline_mysql_file_chsize`](file_instrumentation.md#inline_mysql_file_chsize) `static` `inline`                           |             |
| [`MYSQL_FILE`](file_instrumentation.md#mysql_file) \* | [`inline_mysql_file_fopen`](file_instrumentation.md#inline_mysql_file_fopen) `static` `inline`                             |             |
| `int`                                                 | [`inline_mysql_file_fclose`](file_instrumentation.md#inline_mysql_file_fclose) `static` `inline`                           |             |
| `size_t`                                              | [`inline_mysql_file_fread`](file_instrumentation.md#inline_mysql_file_fread) `static` `inline`                             |             |
| `size_t`                                              | [`inline_mysql_file_fwrite`](file_instrumentation.md#inline_mysql_file_fwrite) `static` `inline`                           |             |
| `my_off_t`                                            | [`inline_mysql_file_fseek`](file_instrumentation.md#inline_mysql_file_fseek) `static` `inline`                             |             |
| `my_off_t`                                            | [`inline_mysql_file_ftell`](file_instrumentation.md#inline_mysql_file_ftell) `static` `inline`                             |             |
| `File`                                                | [`inline_mysql_file_create`](file_instrumentation.md#inline_mysql_file_create) `static` `inline`                           |             |
| `File`                                                | [`inline_mysql_file_create_temp`](file_instrumentation.md#inline_mysql_file_create_temp) `static` `inline`                 |             |
| `File`                                                | [`inline_mysql_file_open`](file_instrumentation.md#inline_mysql_file_open) `static` `inline`                               |             |
| `int`                                                 | [`inline_mysql_file_close`](file_instrumentation.md#inline_mysql_file_close) `static` `inline`                             |             |
| `size_t`                                              | [`inline_mysql_file_read`](file_instrumentation.md#inline_mysql_file_read) `static` `inline`                               |             |
| `size_t`                                              | [`inline_mysql_file_write`](file_instrumentation.md#inline_mysql_file_write) `static` `inline`                             |             |
| `size_t`                                              | [`inline_mysql_file_pread`](file_instrumentation.md#inline_mysql_file_pread) `static` `inline`                             |             |
| `size_t`                                              | [`inline_mysql_file_pwrite`](file_instrumentation.md#inline_mysql_file_pwrite) `static` `inline`                           |             |
| `my_off_t`                                            | [`inline_mysql_file_seek`](file_instrumentation.md#inline_mysql_file_seek) `static` `inline`                               |             |
| `my_off_t`                                            | [`inline_mysql_file_tell`](file_instrumentation.md#inline_mysql_file_tell) `static` `inline`                               |             |
| `int`                                                 | [`inline_mysql_file_delete`](file_instrumentation.md#inline_mysql_file_delete) `static` `inline`                           |             |
| `int`                                                 | [`inline_mysql_file_rename`](file_instrumentation.md#inline_mysql_file_rename) `static` `inline`                           |             |
| `File`                                                | [`inline_mysql_file_create_with_symlink`](file_instrumentation.md#inline_mysql_file_create_with_symlink) `static` `inline` |             |
| `int`                                                 | [`inline_mysql_file_delete_with_symlink`](file_instrumentation.md#inline_mysql_file_delete_with_symlink) `static` `inline` |             |
| `int`                                                 | [`inline_mysql_file_rename_with_symlink`](file_instrumentation.md#inline_mysql_file_rename_with_symlink) `static` `inline` |             |
| `int`                                                 | [`inline_mysql_file_sync`](file_instrumentation.md#inline_mysql_file_sync) `static` `inline`                               |             |

***

### inline\_mysql\_file\_register

`static` `inline`

```cpp
static inline void inline_mysql_file_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql\_file.h:517

***

### inline\_mysql\_file\_fgets

`static` `inline`

```cpp
static inline char * inline_mysql_file_fgets(char * str, int size, MYSQL_FILE * file, char * str, int size, MYSQL_FILE * file)
```

Defined in psi/mysql\_file.h:535

***

### inline\_mysql\_file\_fgetc

`static` `inline`

```cpp
static inline int inline_mysql_file_fgetc(MYSQL_FILE * file, MYSQL_FILE * file)
```

Defined in psi/mysql\_file.h:563

***

### inline\_mysql\_file\_fputs

`static` `inline`

```cpp
static inline int inline_mysql_file_fputs(const char * str, MYSQL_FILE * file, const char * str, MYSQL_FILE * file)
```

Defined in psi/mysql\_file.h:591

***

### inline\_mysql\_file\_fputc

`static` `inline`

```cpp
static inline int inline_mysql_file_fputc(char c, MYSQL_FILE * file, char c, MYSQL_FILE * file)
```

Defined in psi/mysql\_file.h:621

***

### inline\_mysql\_file\_fprintf

`static` `inline`

```cpp
static inline int inline_mysql_file_fprintf(MYSQL_FILE * file, const char * format, ..., MYSQL_FILE * file, const char * format, ...)
```

Defined in psi/mysql\_file.h:649

***

### inline\_mysql\_file\_vfprintf

`static` `inline`

```cpp
static inline int inline_mysql_file_vfprintf(MYSQL_FILE * file, const char * format, va_list args, MYSQL_FILE * file, const char * format, va_list args)
```

Defined in psi/mysql\_file.h:681

***

### inline\_mysql\_file\_fflush

`static` `inline`

```cpp
static inline int inline_mysql_file_fflush(MYSQL_FILE * file, MYSQL_FILE * file)
```

Defined in psi/mysql\_file.h:709

***

### inline\_mysql\_file\_feof

`static` `inline`

```cpp
static inline int inline_mysql_file_feof(MYSQL_FILE * file, MYSQL_FILE * file)
```

Defined in psi/mysql\_file.h:736

***

### inline\_mysql\_file\_fstat

`static` `inline`

```cpp
static inline int inline_mysql_file_fstat(int filenr, MY_STAT * stat_area, myf flags, int filenr, MY_STAT * stat_area, myf flags)
```

Defined in psi/mysql\_file.h:743

***

### inline\_mysql\_file\_stat

`static` `inline`

```cpp
static inline MY_STAT * inline_mysql_file_stat(const char * path, MY_STAT * stat_area, myf flags, const char * path, MY_STAT * stat_area, myf flags)
```

Defined in psi/mysql\_file.h:768

***

### inline\_mysql\_file\_chsize

`static` `inline`

```cpp
static inline int inline_mysql_file_chsize(File file, my_off_t newlength, int filler, myf flags, File file, my_off_t newlength, int filler, myf flags)
```

Defined in psi/mysql\_file.h:793

***

### inline\_mysql\_file\_fopen

`static` `inline`

```cpp
static inline MYSQL_FILE * inline_mysql_file_fopen(const char * filename, int flags, myf myFlags, const char * filename, int flags, myf myFlags)
```

Defined in psi/mysql\_file.h:819

***

### inline\_mysql\_file\_fclose

`static` `inline`

```cpp
static inline int inline_mysql_file_fclose(MYSQL_FILE * file, myf flags, MYSQL_FILE * file, myf flags)
```

Defined in psi/mysql\_file.h:861

***

### inline\_mysql\_file\_fread

`static` `inline`

```cpp
static inline size_t inline_mysql_file_fread(MYSQL_FILE * file, uchar * buffer, size_t count, myf flags, MYSQL_FILE * file, uchar * buffer, size_t count, myf flags)
```

Defined in psi/mysql\_file.h:895

***

### inline\_mysql\_file\_fwrite

`static` `inline`

```cpp
static inline size_t inline_mysql_file_fwrite(MYSQL_FILE * file, const uchar * buffer, size_t count, myf flags, MYSQL_FILE * file, const uchar * buffer, size_t count, myf flags)
```

Defined in psi/mysql\_file.h:928

***

### inline\_mysql\_file\_fseek

`static` `inline`

```cpp
static inline my_off_t inline_mysql_file_fseek(MYSQL_FILE * file, my_off_t pos, int whence, myf flags, MYSQL_FILE * file, my_off_t pos, int whence, myf flags)
```

Defined in psi/mysql\_file.h:961

***

### inline\_mysql\_file\_ftell

`static` `inline`

```cpp
static inline my_off_t inline_mysql_file_ftell(MYSQL_FILE * file, myf flags, MYSQL_FILE * file, myf flags)
```

Defined in psi/mysql\_file.h:989

***

### inline\_mysql\_file\_create

`static` `inline`

```cpp
static inline File inline_mysql_file_create(const char * filename, mode_t create_flags, int access_flags, myf myFlags, const char * filename, mode_t create_flags, int access_flags, myf myFlags)
```

Defined in psi/mysql\_file.h:1017

***

### inline\_mysql\_file\_create\_temp

`static` `inline`

```cpp
static inline File inline_mysql_file_create_temp(char * to, const char * dir, const char * pfx, int mode, myf myFlags, char * to, const char * dir, const char * pfx, int mode, myf myFlags)
```

Defined in psi/mysql\_file.h:1043

***

### inline\_mysql\_file\_open

`static` `inline`

```cpp
static inline File inline_mysql_file_open(const char * filename, int flags, myf myFlags, const char * filename, int flags, myf myFlags)
```

Defined in psi/mysql\_file.h:1070

***

### inline\_mysql\_file\_close

`static` `inline`

```cpp
static inline int inline_mysql_file_close(File file, myf flags, File file, myf flags)
```

Defined in psi/mysql\_file.h:1096

***

### inline\_mysql\_file\_read

`static` `inline`

```cpp
static inline size_t inline_mysql_file_read(File file, uchar * buffer, size_t count, myf flags, File file, uchar * buffer, size_t count, myf flags)
```

Defined in psi/mysql\_file.h:1121

***

### inline\_mysql\_file\_write

`static` `inline`

```cpp
static inline size_t inline_mysql_file_write(File file, const uchar * buffer, size_t count, myf flags, File file, const uchar * buffer, size_t count, myf flags)
```

Defined in psi/mysql\_file.h:1151

***

### inline\_mysql\_file\_pread

`static` `inline`

```cpp
static inline size_t inline_mysql_file_pread(File file, uchar * buffer, size_t count, my_off_t offset, myf flags, File file, uchar * buffer, size_t count, my_off_t offset, myf flags)
```

Defined in psi/mysql\_file.h:1181

***

### inline\_mysql\_file\_pwrite

`static` `inline`

```cpp
static inline size_t inline_mysql_file_pwrite(File file, const uchar * buffer, size_t count, my_off_t offset, myf flags, File file, const uchar * buffer, size_t count, my_off_t offset, myf flags)
```

Defined in psi/mysql\_file.h:1211

***

### inline\_mysql\_file\_seek

`static` `inline`

```cpp
static inline my_off_t inline_mysql_file_seek(File file, my_off_t pos, int whence, myf flags, File file, my_off_t pos, int whence, myf flags)
```

Defined in psi/mysql\_file.h:1241

***

### inline\_mysql\_file\_tell

`static` `inline`

```cpp
static inline my_off_t inline_mysql_file_tell(File file, myf flags, File file, myf flags)
```

Defined in psi/mysql\_file.h:1266

***

### inline\_mysql\_file\_delete

`static` `inline`

```cpp
static inline int inline_mysql_file_delete(const char * name, myf flags, const char * name, myf flags)
```

Defined in psi/mysql\_file.h:1291

***

### inline\_mysql\_file\_rename

`static` `inline`

```cpp
static inline int inline_mysql_file_rename(const char * from, const char * to, myf flags, const char * from, const char * to, myf flags)
```

Defined in psi/mysql\_file.h:1316

***

### inline\_mysql\_file\_create\_with\_symlink

`static` `inline`

```cpp
static inline File inline_mysql_file_create_with_symlink(const char * linkname, const char * filename, mode_t create_flags, int access_flags, myf flags, const char * linkname, const char * filename, mode_t create_flags, int access_flags, myf flags)
```

Defined in psi/mysql\_file.h:1343

***

### inline\_mysql\_file\_delete\_with\_symlink

`static` `inline`

```cpp
static inline int inline_mysql_file_delete_with_symlink(const char * name, const char * ext, myf flags, const char * name, const char * ext, myf flags)
```

Defined in psi/mysql\_file.h:1373

***

### inline\_mysql\_file\_rename\_with\_symlink

`static` `inline`

```cpp
static inline int inline_mysql_file_rename_with_symlink(const char * from, const char * to, myf flags, const char * from, const char * to, myf flags)
```

Defined in psi/mysql\_file.h:1402

***

### inline\_mysql\_file\_sync

`static` `inline`

```cpp
static inline int inline_mysql_file_sync(File fd, myf flags, File fd, myf flags)
```

Defined in psi/mysql\_file.h:1428

## Class Definitions

### st\_mysql\_file

```cpp
#include <mysql_file.h>
```

```cpp
struct st_mysql_file
```

Defined in psi/mysql\_file.h:498

An instrumented FILE structure. **See also**: [MYSQL\_FILE](file_instrumentation.md#mysql_file)

#### Public Attributes

| Return                              | Name                                       | Description                                                                                                                         |
| ----------------------------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| `FILE *`                            | [`m_file`](file_instrumentation.md#m_file) | The real file.                                                                                                                      |
| struct [`PSI_file`](./#psi_file) \* | [`m_psi`](file_instrumentation.md#m_psi)   | The instrumentation hook. Note that this hook is not conditionally defined, for binary compatibility of the `MYSQL_FILE` interface. |

***

#### m\_file

```cpp
FILE * m_file
```

Defined in psi/mysql\_file.h:501

The real file.

***

#### m\_psi

```cpp
struct PSI_file * m_psi
```

Type: struct [`PSI_file`](./#psi_file) \*

Defined in psi/mysql\_file.h:507

The instrumentation hook. Note that this hook is not conditionally defined, for binary compatibility of the `MYSQL_FILE` interface.
