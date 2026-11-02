---
description: >-
  Instrumented mutex, rwlock, prlock, and condition structures and their
  wrappers, and the PSI_CALL_* thread macros that register threads and set their
  attributes.
---

# Thread Instrumentation

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Instrumentation Interface`](./)

## Classes

| Name                                                           | Description                                                                                                  |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| [`st_mysql_mutex`](thread_instrumentation.md#st_mysql_mutex)   | An instrumented mutex structure. **See also**: [mysql\_mutex\_t](thread_instrumentation.md#mysql_mutex_t)    |
| [`st_mysql_rwlock`](thread_instrumentation.md#st_mysql_rwlock) | An instrumented rwlock structure. **See also**: [mysql\_rwlock\_t](thread_instrumentation.md#mysql_rwlock_t) |
| [`st_mysql_prlock`](thread_instrumentation.md#st_mysql_prlock) | An instrumented prlock structure. **See also**: [mysql\_prlock\_t](thread_instrumentation.md#mysql_prlock_t) |
| [`st_mysql_cond`](thread_instrumentation.md#st_mysql_cond)     | An instrumented cond structure. **See also**: [mysql\_cond\_t](thread_instrumentation.md#mysql_cond_t)       |

## Macros

| Name                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`PSI_MUTEX_CALL`](thread_instrumentation.md#psi_mutex_call)                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`PSI_RWLOCK_CALL`](thread_instrumentation.md#psi_rwlock_call)                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`PSI_COND_CALL`](thread_instrumentation.md#psi_cond_call)                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`PSI_THREAD_CALL`](thread_instrumentation.md#psi_thread_call)                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`PSI_CALL_delete_current_thread`](thread_instrumentation.md#psi_call_delete_current_thread)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`PSI_CALL_get_thread`](thread_instrumentation.md#psi_call_get_thread)                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`PSI_CALL_new_thread`](thread_instrumentation.md#psi_call_new_thread)                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`PSI_CALL_register_thread`](thread_instrumentation.md#psi_call_register_thread)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`PSI_CALL_set_thread`](thread_instrumentation.md#psi_call_set_thread)                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`PSI_CALL_set_thread_THD`](thread_instrumentation.md#psi_call_set_thread_thd)                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`PSI_CALL_set_thread_connect_attrs`](thread_instrumentation.md#psi_call_set_thread_connect_attrs)     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`PSI_CALL_set_thread_db`](thread_instrumentation.md#psi_call_set_thread_db)                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`PSI_CALL_set_thread_id`](thread_instrumentation.md#psi_call_set_thread_id)                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`PSI_CALL_set_thread_os_id`](thread_instrumentation.md#psi_call_set_thread_os_id)                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`PSI_CALL_set_thread_info`](thread_instrumentation.md#psi_call_set_thread_info)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`PSI_CALL_set_thread_start_time`](thread_instrumentation.md#psi_call_set_thread_start_time)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`PSI_CALL_set_thread_account`](thread_instrumentation.md#psi_call_set_thread_account)                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`PSI_CALL_spawn_thread`](thread_instrumentation.md#psi_call_spawn_thread)                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`PSI_CALL_set_connection_type`](thread_instrumentation.md#psi_call_set_connection_type)               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`mysql_mutex_is_owner`](thread_instrumentation.md#mysql_mutex_is_owner)                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`mysql_mutex_assert_owner`](thread_instrumentation.md#mysql_mutex_assert_owner)                       | Wrapper, to use safe\_mutex\_assert\_owner with instrumented mutexes. `mysql_mutex_assert_owner` is a drop-in replacement for `safe_mutex_assert_owner`.                                                                                                                                                                                                                                                                                                                                                                                                |
| [`mysql_mutex_assert_not_owner`](thread_instrumentation.md#mysql_mutex_assert_not_owner)               | Wrapper, to use safe\_mutex\_assert\_not\_owner with instrumented mutexes. `mysql_mutex_assert_not_owner` is a drop-in replacement for `safe_mutex_assert_not_owner`.                                                                                                                                                                                                                                                                                                                                                                                   |
| [`mysql_mutex_setflags`](thread_instrumentation.md#mysql_mutex_setflags)                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`mysql_prlock_assert_write_owner`](thread_instrumentation.md#mysql_prlock_assert_write_owner)         | Drop-in replacement for `rw_pr_lock_assert_write_owner`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [`mysql_prlock_assert_not_write_owner`](thread_instrumentation.md#mysql_prlock_assert_not_write_owner) | Drop-in replacement for `rw_pr_lock_assert_not_write_owner`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [`mysql_mutex_register`](thread_instrumentation.md#mysql_mutex_register)                               | Mutex registration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [`mysql_mutex_init`](thread_instrumentation.md#mysql_mutex_init)                                       | Instrumented mutex\_init. `mysql_mutex_init` is a replacement for `pthread_mutex_init`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [`mysql_mutex_destroy`](thread_instrumentation.md#mysql_mutex_destroy)                                 | Instrumented mutex\_destroy. `mysql_mutex_destroy` is a drop-in replacement for `pthread_mutex_destroy`.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [`mysql_mutex_lock`](thread_instrumentation.md#mysql_mutex_lock)                                       | Instrumented mutex\_lock. `mysql_mutex_lock` is a drop-in replacement for `pthread_mutex_lock`.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`mysql_mutex_trylock`](thread_instrumentation.md#mysql_mutex_trylock)                                 | Instrumented mutex\_lock. `mysql_mutex_trylock` is a drop-in replacement for `pthread_mutex_trylock`.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [`mysql_mutex_unlock`](thread_instrumentation.md#mysql_mutex_unlock)                                   | Instrumented mutex\_unlock. `mysql_mutex_unlock` is a drop-in replacement for `pthread_mutex_unlock`.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [`mysql_rwlock_register`](thread_instrumentation.md#mysql_rwlock_register)                             | Rwlock registration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [`mysql_rwlock_init`](thread_instrumentation.md#mysql_rwlock_init)                                     | Instrumented rwlock\_init. `mysql_rwlock_init` is a replacement for `pthread_rwlock_init`. Note that pthread\_rwlockattr\_t is not supported in MySQL.                                                                                                                                                                                                                                                                                                                                                                                                  |
| [`mysql_prlock_init`](thread_instrumentation.md#mysql_prlock_init)                                     | Instrumented rw\_pr\_init. `mysql_prlock_init` is a replacement for `rw_pr_init`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [`mysql_rwlock_destroy`](thread_instrumentation.md#mysql_rwlock_destroy)                               | Instrumented rwlock\_destroy. `mysql_rwlock_destroy` is a drop-in replacement for `pthread_rwlock_destroy`.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [`mysql_prlock_destroy`](thread_instrumentation.md#mysql_prlock_destroy)                               | Instrumented rw\_pr\_destroy. `mysql_prlock_destroy` is a drop-in replacement for `rw_pr_destroy`.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [`mysql_rwlock_rdlock`](thread_instrumentation.md#mysql_rwlock_rdlock)                                 | Instrumented rwlock\_rdlock. `mysql_rwlock_rdlock` is a drop-in replacement for `pthread_rwlock_rdlock`.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [`mysql_prlock_rdlock`](thread_instrumentation.md#mysql_prlock_rdlock)                                 | Instrumented rw\_pr\_rdlock. `mysql_prlock_rdlock` is a drop-in replacement for `rw_pr_rdlock`.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`mysql_rwlock_wrlock`](thread_instrumentation.md#mysql_rwlock_wrlock)                                 | Instrumented rwlock\_wrlock. `mysql_rwlock_wrlock` is a drop-in replacement for `pthread_rwlock_wrlock`.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [`mysql_prlock_wrlock`](thread_instrumentation.md#mysql_prlock_wrlock)                                 | Instrumented rw\_pr\_wrlock. `mysql_prlock_wrlock` is a drop-in replacement for `rw_pr_wrlock`.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`mysql_rwlock_tryrdlock`](thread_instrumentation.md#mysql_rwlock_tryrdlock)                           | Instrumented rwlock\_tryrdlock. `mysql_rwlock_tryrdlock` is a drop-in replacement for `pthread_rwlock_tryrdlock`.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [`mysql_rwlock_trywrlock`](thread_instrumentation.md#mysql_rwlock_trywrlock)                           | Instrumented rwlock\_trywrlock. `mysql_rwlock_trywrlock` is a drop-in replacement for `pthread_rwlock_trywrlock`.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [`mysql_rwlock_unlock`](thread_instrumentation.md#mysql_rwlock_unlock)                                 | Instrumented rwlock\_unlock. `mysql_rwlock_unlock` is a drop-in replacement for `pthread_rwlock_unlock`.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [`mysql_prlock_unlock`](thread_instrumentation.md#mysql_prlock_unlock)                                 | Instrumented rw\_pr\_unlock. `mysql_prlock_unlock` is a drop-in replacement for `rw_pr_unlock`.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [`mysql_cond_register`](thread_instrumentation.md#mysql_cond_register)                                 | Cond registration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [`mysql_cond_init`](thread_instrumentation.md#mysql_cond_init)                                         | Instrumented cond\_init. `mysql_cond_init` is a replacement for `pthread_cond_init`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [`mysql_cond_destroy`](thread_instrumentation.md#mysql_cond_destroy)                                   | Instrumented cond\_destroy. `mysql_cond_destroy` is a drop-in replacement for `pthread_cond_destroy`.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [`mysql_cond_wait`](thread_instrumentation.md#mysql_cond_wait)                                         | Instrumented cond\_wait. `mysql_cond_wait` is a drop-in replacement for `pthread_cond_wait`.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [`mysql_cond_timedwait`](thread_instrumentation.md#mysql_cond_timedwait)                               | Instrumented cond\_timedwait. `mysql_cond_timedwait` is a drop-in replacement for `pthread_cond_timedwait`.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [`mysql_cond_signal`](thread_instrumentation.md#mysql_cond_signal)                                     | Instrumented cond\_signal. `mysql_cond_signal` is a drop-in replacement for `pthread_cond_signal`.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [`mysql_cond_broadcast`](thread_instrumentation.md#mysql_cond_broadcast)                               | Instrumented cond\_broadcast. `mysql_cond_broadcast` is a drop-in replacement for `pthread_cond_broadcast`.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [`mysql_thread_register`](thread_instrumentation.md#mysql_thread_register)                             | Thread registration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [`mysql_thread_create`](thread_instrumentation.md#mysql_thread_create)                                 | Instrumented pthread\_create. This function creates both the thread instrumentation and a thread. `mysql_thread_create` is a replacement for `pthread_create`. The parameter P4 (or, if it is NULL, P1) will be used as the instrumented thread "identity". Providing a P1 / P4 parameter with a different value for each call will on average improve performances, since this thread identity value is used internally to randomize access to data and prevent contention. This is optional, and the improvement is not guaranteed, only statistical. |
| [`mysql_thread_set_psi_id`](thread_instrumentation.md#mysql_thread_set_psi_id)                         | Set the thread identifier for the instrumentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [`mysql_thread_set_psi_THD`](thread_instrumentation.md#mysql_thread_set_psi_thd)                       | Set the thread sql session for the instrumentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

***

### PSI\_MUTEX\_CALL

```cpp
#define PSI_MUTEX_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql\_thread.h:79

***

### PSI\_RWLOCK\_CALL

```cpp
#define PSI_RWLOCK_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql\_thread.h:83

***

### PSI\_COND\_CALL

```cpp
#define PSI_COND_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql\_thread.h:87

***

### PSI\_THREAD\_CALL

```cpp
#define PSI_THREAD_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql\_thread.h:91

***

### PSI\_CALL\_delete\_current\_thread

```cpp
#define PSI_CALL_delete_current_thread() do { } while(0)
```

Defined in psi/mysql\_thread.h:111

***

### PSI\_CALL\_get\_thread

```cpp
#define PSI_CALL_get_thread() NULL
```

Defined in psi/mysql\_thread.h:112

***

### PSI\_CALL\_new\_thread

```cpp
#define PSI_CALL_new_thread(A1, A2, A3, A1, A2, A3) NULL
```

Defined in psi/mysql\_thread.h:113

***

### PSI\_CALL\_register\_thread

```cpp
#define PSI_CALL_register_thread(A1, A2, A3, A1, A2, A3) do { } while(0)
```

Defined in psi/mysql\_thread.h:114

***

### PSI\_CALL\_set\_thread

```cpp
#define PSI_CALL_set_thread(A1, A1) do { } while(0)
```

Defined in psi/mysql\_thread.h:115

***

### PSI\_CALL\_set\_thread\_THD

```cpp
#define PSI_CALL_set_thread_THD(A1, A2, A1, A2) do { } while(0)
```

Defined in psi/mysql\_thread.h:116

***

### PSI\_CALL\_set\_thread\_connect\_attrs

```cpp
#define PSI_CALL_set_thread_connect_attrs(A1, A2, A3, A1, A2, A3) 0
```

Defined in psi/mysql\_thread.h:117

***

### PSI\_CALL\_set\_thread\_db

```cpp
#define PSI_CALL_set_thread_db(A1, A2, A1, A2) do { } while(0)
```

Defined in psi/mysql\_thread.h:118

***

### PSI\_CALL\_set\_thread\_id

```cpp
#define PSI_CALL_set_thread_id(A1, A2, A1, A2) do { } while(0)
```

Defined in psi/mysql\_thread.h:119

***

### PSI\_CALL\_set\_thread\_os\_id

```cpp
#define PSI_CALL_set_thread_os_id(A1, A1) do { } while(0)
```

Defined in psi/mysql\_thread.h:120

***

### PSI\_CALL\_set\_thread\_info

```cpp
#define PSI_CALL_set_thread_info(A1, A2, A1, A2) do { } while(0)
```

Defined in psi/mysql\_thread.h:121

***

### PSI\_CALL\_set\_thread\_start\_time

```cpp
#define PSI_CALL_set_thread_start_time(A1, A1) do { } while(0)
```

Defined in psi/mysql\_thread.h:122

***

### PSI\_CALL\_set\_thread\_account

```cpp
#define PSI_CALL_set_thread_account(A1, A2, A3, A4, A1, A2, A3, A4) do { } while(0)
```

Defined in psi/mysql\_thread.h:123

***

### PSI\_CALL\_spawn\_thread

```cpp
#define PSI_CALL_spawn_thread(A1, A2, A3, A4, A5, A1, A2, A3, A4, A5) 0
```

Defined in psi/mysql\_thread.h:124

***

### PSI\_CALL\_set\_connection\_type

```cpp
#define PSI_CALL_set_connection_type(A, A) do { } while(0)
```

Defined in psi/mysql\_thread.h:125

***

### mysql\_mutex\_is\_owner

```cpp
#define mysql_mutex_is_owner(M, M) safe_mutex_is_owner(&(M)->m_mutex)
```

Defined in psi/mysql\_thread.h:266

***

### mysql\_mutex\_assert\_owner

```cpp
#define mysql_mutex_assert_owner(M, M) safe_mutex_assert_owner(&(M)->m_mutex)
```

Defined in psi/mysql\_thread.h:273

Wrapper, to use safe\_mutex\_assert\_owner with instrumented mutexes. `mysql_mutex_assert_owner` is a drop-in replacement for `safe_mutex_assert_owner`.

***

### mysql\_mutex\_assert\_not\_owner

```cpp
#define mysql_mutex_assert_not_owner(M, M) safe_mutex_assert_not_owner(&(M)->m_mutex)
```

Defined in psi/mysql\_thread.h:282

Wrapper, to use safe\_mutex\_assert\_not\_owner with instrumented mutexes. `mysql_mutex_assert_not_owner` is a drop-in replacement for `safe_mutex_assert_not_owner`.

***

### mysql\_mutex\_setflags

```cpp
#define mysql_mutex_setflags(M, F, M, F) safe_mutex_setflags(&(M)->m_mutex, (F))
```

Defined in psi/mysql\_thread.h:285

***

### mysql\_prlock\_assert\_write\_owner

```cpp
#define mysql_prlock_assert_write_owner(M, M) rw_pr_lock_assert_write_owner(&(M)->m_prlock)
```

Defined in psi/mysql\_thread.h:293

Drop-in replacement for `rw_pr_lock_assert_write_owner`.

***

### mysql\_prlock\_assert\_not\_write\_owner

```cpp
#define mysql_prlock_assert_not_write_owner(M, M) rw_pr_lock_assert_not_write_owner(&(M)->m_prlock)
```

Defined in psi/mysql\_thread.h:301

Drop-in replacement for `rw_pr_lock_assert_not_write_owner`.

***

### mysql\_mutex\_register

```cpp
#define mysql_mutex_register(P1, P2, P3, P1, P2, P3) inline_mysql_mutex_register(P1, P2, P3)
```

Defined in psi/mysql\_thread.h:308

Mutex registration.

***

### mysql\_mutex\_init

```cpp
#define mysql_mutex_init(K, M, A, K, M, A) inline_mysql_mutex_init(M, A)
```

Defined in psi/mysql\_thread.h:333

Instrumented mutex\_init. `mysql_mutex_init` is a replacement for `pthread_mutex_init`.

#### Parameters

| Parameter | Type | Description                                     |
| --------- | ---- | ----------------------------------------------- |
| `K`       |      | The PSI\_mutex\_key for this instrumented mutex |
| `M`       |      | The mutex to initialize                         |
| `A`       |      | Mutex attributes                                |
| `K`       |      | The PSI\_mutex\_key for this instrumented mutex |
| `M`       |      | The mutex to initialize                         |
| `A`       |      | Mutex attributes                                |

***

### mysql\_mutex\_destroy

```cpp
#define mysql_mutex_destroy(M, M) inline_mysql_mutex_destroy(M)
```

Defined in psi/mysql\_thread.h:348

Instrumented mutex\_destroy. `mysql_mutex_destroy` is a drop-in replacement for `pthread_mutex_destroy`.

***

### mysql\_mutex\_lock

```cpp
#define mysql_mutex_lock(M, M) inline_mysql_mutex_lock(M)
```

Defined in psi/mysql\_thread.h:363

Instrumented mutex\_lock. `mysql_mutex_lock` is a drop-in replacement for `pthread_mutex_lock`.

#### Parameters

| Parameter | Type | Description       |
| --------- | ---- | ----------------- |
| `M`       |      | The mutex to lock |
| `M`       |      | The mutex to lock |

***

### mysql\_mutex\_trylock

```cpp
#define mysql_mutex_trylock(M, M) inline_mysql_mutex_trylock(M)
```

Defined in psi/mysql\_thread.h:378

Instrumented mutex\_lock. `mysql_mutex_trylock` is a drop-in replacement for `pthread_mutex_trylock`.

***

### mysql\_mutex\_unlock

```cpp
#define mysql_mutex_unlock(M, M) inline_mysql_mutex_unlock(M)
```

Defined in psi/mysql\_thread.h:391

Instrumented mutex\_unlock. `mysql_mutex_unlock` is a drop-in replacement for `pthread_mutex_unlock`.

***

### mysql\_rwlock\_register

```cpp
#define mysql_rwlock_register(P1, P2, P3, P1, P2, P3) inline_mysql_rwlock_register(P1, P2, P3)
```

Defined in psi/mysql\_thread.h:399

Rwlock registration.

***

### mysql\_rwlock\_init

```cpp
#define mysql_rwlock_init(K, RW, K, RW) inline_mysql_rwlock_init(RW)
```

Defined in psi/mysql\_thread.h:413

Instrumented rwlock\_init. `mysql_rwlock_init` is a replacement for `pthread_rwlock_init`. Note that pthread\_rwlockattr\_t is not supported in MySQL.

#### Parameters

| Parameter | Type | Description                                       |
| --------- | ---- | ------------------------------------------------- |
| `K`       |      | The PSI\_rwlock\_key for this instrumented rwlock |
| `RW`      |      | The rwlock to initialize                          |
| `K`       |      | The PSI\_rwlock\_key for this instrumented rwlock |
| `RW`      |      | The rwlock to initialize                          |

***

### mysql\_prlock\_init

```cpp
#define mysql_prlock_init(K, RW, K, RW) inline_mysql_prlock_init(RW)
```

Defined in psi/mysql\_thread.h:426

Instrumented rw\_pr\_init. `mysql_prlock_init` is a replacement for `rw_pr_init`.

#### Parameters

| Parameter | Type | Description                                       |
| --------- | ---- | ------------------------------------------------- |
| `K`       |      | The PSI\_rwlock\_key for this instrumented prlock |
| `RW`      |      | The prlock to initialize                          |
| `K`       |      | The PSI\_rwlock\_key for this instrumented prlock |
| `RW`      |      | The prlock to initialize                          |

***

### mysql\_rwlock\_destroy

```cpp
#define mysql_rwlock_destroy(RW, RW) inline_mysql_rwlock_destroy(RW)
```

Defined in psi/mysql\_thread.h:435

Instrumented rwlock\_destroy. `mysql_rwlock_destroy` is a drop-in replacement for `pthread_rwlock_destroy`.

***

### mysql\_prlock\_destroy

```cpp
#define mysql_prlock_destroy(RW, RW) inline_mysql_prlock_destroy(RW)
```

Defined in psi/mysql\_thread.h:443

Instrumented rw\_pr\_destroy. `mysql_prlock_destroy` is a drop-in replacement for `rw_pr_destroy`.

***

### mysql\_rwlock\_rdlock

```cpp
#define mysql_rwlock_rdlock(RW, RW) inline_mysql_rwlock_rdlock(RW)
```

Defined in psi/mysql\_thread.h:455

Instrumented rwlock\_rdlock. `mysql_rwlock_rdlock` is a drop-in replacement for `pthread_rwlock_rdlock`.

***

### mysql\_prlock\_rdlock

```cpp
#define mysql_prlock_rdlock(RW, RW) inline_mysql_prlock_rdlock(RW)
```

Defined in psi/mysql\_thread.h:469

Instrumented rw\_pr\_rdlock. `mysql_prlock_rdlock` is a drop-in replacement for `rw_pr_rdlock`.

***

### mysql\_rwlock\_wrlock

```cpp
#define mysql_rwlock_wrlock(RW, RW) inline_mysql_rwlock_wrlock(RW)
```

Defined in psi/mysql\_thread.h:483

Instrumented rwlock\_wrlock. `mysql_rwlock_wrlock` is a drop-in replacement for `pthread_rwlock_wrlock`.

***

### mysql\_prlock\_wrlock

```cpp
#define mysql_prlock_wrlock(RW, RW) inline_mysql_prlock_wrlock(RW)
```

Defined in psi/mysql\_thread.h:497

Instrumented rw\_pr\_wrlock. `mysql_prlock_wrlock` is a drop-in replacement for `rw_pr_wrlock`.

***

### mysql\_rwlock\_tryrdlock

```cpp
#define mysql_rwlock_tryrdlock(RW, RW) inline_mysql_rwlock_tryrdlock(RW)
```

Defined in psi/mysql\_thread.h:511

Instrumented rwlock\_tryrdlock. `mysql_rwlock_tryrdlock` is a drop-in replacement for `pthread_rwlock_tryrdlock`.

***

### mysql\_rwlock\_trywrlock

```cpp
#define mysql_rwlock_trywrlock(RW, RW) inline_mysql_rwlock_trywrlock(RW)
```

Defined in psi/mysql\_thread.h:525

Instrumented rwlock\_trywrlock. `mysql_rwlock_trywrlock` is a drop-in replacement for `pthread_rwlock_trywrlock`.

***

### mysql\_rwlock\_unlock

```cpp
#define mysql_rwlock_unlock(RW, RW) inline_mysql_rwlock_unlock(RW)
```

Defined in psi/mysql\_thread.h:535

Instrumented rwlock\_unlock. `mysql_rwlock_unlock` is a drop-in replacement for `pthread_rwlock_unlock`.

***

### mysql\_prlock\_unlock

```cpp
#define mysql_prlock_unlock(RW, RW) inline_mysql_prlock_unlock(RW)
```

Defined in psi/mysql\_thread.h:543

Instrumented rw\_pr\_unlock. `mysql_prlock_unlock` is a drop-in replacement for `rw_pr_unlock`.

***

### mysql\_cond\_register

```cpp
#define mysql_cond_register(P1, P2, P3, P1, P2, P3) inline_mysql_cond_register(P1, P2, P3)
```

Defined in psi/mysql\_thread.h:549

Cond registration.

***

### mysql\_cond\_init

```cpp
#define mysql_cond_init(K, C, A, K, C, A) inline_mysql_cond_init(C, A)
```

Defined in psi/mysql\_thread.h:563

Instrumented cond\_init. `mysql_cond_init` is a replacement for `pthread_cond_init`.

#### Parameters

| Parameter | Type | Description                                   |
| --------- | ---- | --------------------------------------------- |
| `K`       |      | The PSI\_cond\_key for this instrumented cond |
| `C`       |      | The cond to initialize                        |
| `A`       |      | Condition attributes                          |
| `K`       |      | The PSI\_cond\_key for this instrumented cond |
| `C`       |      | The cond to initialize                        |
| `A`       |      | Condition attributes                          |

***

### mysql\_cond\_destroy

```cpp
#define mysql_cond_destroy(C, C) inline_mysql_cond_destroy(C)
```

Defined in psi/mysql\_thread.h:571

Instrumented cond\_destroy. `mysql_cond_destroy` is a drop-in replacement for `pthread_cond_destroy`.

***

### mysql\_cond\_wait

```cpp
#define mysql_cond_wait(C, M, C, M) inline_mysql_cond_wait(C, M)
```

Defined in psi/mysql\_thread.h:582

Instrumented cond\_wait. `mysql_cond_wait` is a drop-in replacement for `pthread_cond_wait`.

***

### mysql\_cond\_timedwait

```cpp
#define mysql_cond_timedwait(C, M, W, C, M, W) inline_mysql_cond_timedwait(C, M, W)
```

Defined in psi/mysql\_thread.h:596

Instrumented cond\_timedwait. `mysql_cond_timedwait` is a drop-in replacement for `pthread_cond_timedwait`.

***

### mysql\_cond\_signal

```cpp
#define mysql_cond_signal(C, C) inline_mysql_cond_signal(C)
```

Defined in psi/mysql\_thread.h:605

Instrumented cond\_signal. `mysql_cond_signal` is a drop-in replacement for `pthread_cond_signal`.

***

### mysql\_cond\_broadcast

```cpp
#define mysql_cond_broadcast(C, C) inline_mysql_cond_broadcast(C)
```

Defined in psi/mysql\_thread.h:613

Instrumented cond\_broadcast. `mysql_cond_broadcast` is a drop-in replacement for `pthread_cond_broadcast`.

***

### mysql\_thread\_register

```cpp
#define mysql_thread_register(P1, P2, P3, P1, P2, P3) inline_mysql_thread_register(P1, P2, P3)
```

Defined in psi/mysql\_thread.h:619

Thread registration.

***

### mysql\_thread\_create

```cpp
#define mysql_thread_create(K, P1, P2, P3, P4, K, P1, P2, P3, P4) pthread_create(P1, P2, P3, P4)
```

Defined in psi/mysql\_thread.h:643

Instrumented pthread\_create. This function creates both the thread instrumentation and a thread. `mysql_thread_create` is a replacement for `pthread_create`. The parameter P4 (or, if it is NULL, P1) will be used as the instrumented thread "identity". Providing a P1 / P4 parameter with a different value for each call will on average improve performances, since this thread identity value is used internally to randomize access to data and prevent contention. This is optional, and the improvement is not guaranteed, only statistical.

#### Parameters

| Parameter | Type | Description                                       |
| --------- | ---- | ------------------------------------------------- |
| `K`       |      | The PSI\_thread\_key for this instrumented thread |
| `P1`      |      | pthread\_create parameter 1                       |
| `P2`      |      | pthread\_create parameter 2                       |
| `P3`      |      | pthread\_create parameter 3                       |
| `P4`      |      | pthread\_create parameter 4                       |
| `K`       |      | The PSI\_thread\_key for this instrumented thread |
| `P1`      |      | pthread\_create parameter 1                       |
| `P2`      |      | pthread\_create parameter 2                       |
| `P3`      |      | pthread\_create parameter 3                       |
| `P4`      |      | pthread\_create parameter 4                       |

***

### mysql\_thread\_set\_psi\_id

```cpp
#define mysql_thread_set_psi_id(I, I) do {} while (0)
```

Defined in psi/mysql\_thread.h:655

Set the thread identifier for the instrumentation.

#### Parameters

| Parameter | Type | Description           |
| --------- | ---- | --------------------- |
| `I`       |      | The thread identifier |
| `I`       |      | The thread identifier |

***

### mysql\_thread\_set\_psi\_THD

```cpp
#define mysql_thread_set_psi_THD(T, T) do {} while (0)
```

Defined in psi/mysql\_thread.h:666

Set the thread sql session for the instrumentation.

#### Parameters

| Parameter | Type | Description           |
| --------- | ---- | --------------------- |
| `T`       |      | The thread identifier |
| `T`       |      | The thread identifier |

## Typedefs

| Return                                                                | Name                                                         | Description                                                                                                                                                                                                                               |
| --------------------------------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| struct [`st_mysql_mutex`](thread_instrumentation.md#st_mysql_mutex)   | [`mysql_mutex_t`](thread_instrumentation.md#mysql_mutex_t)   | Type of an instrumented mutex. `mysql_mutex_t` is a drop-in replacement for `pthread_mutex_t`. **See also**: [mysql\_mutex\_assert\_owner](thread_instrumentation.md#mysql_mutex_assert_owner)                                            |
| struct [`st_mysql_rwlock`](thread_instrumentation.md#st_mysql_rwlock) | [`mysql_rwlock_t`](thread_instrumentation.md#mysql_rwlock_t) | Type of an instrumented rwlock. `mysql_rwlock_t` is a drop-in replacement for `pthread_rwlock_t`. **See also**: [mysql\_rwlock\_init](thread_instrumentation.md#mysql_rwlock_init)                                                        |
| struct [`st_mysql_prlock`](thread_instrumentation.md#st_mysql_prlock) | [`mysql_prlock_t`](thread_instrumentation.md#mysql_prlock_t) | Type of an instrumented prlock. A prlock is a read write lock that 'prefers readers' (pr). `mysql_prlock_t` is a drop-in replacement for `rw_pr_lock_t`. **See also**: [mysql\_prlock\_init](thread_instrumentation.md#mysql_prlock_init) |
| struct [`st_mysql_cond`](thread_instrumentation.md#st_mysql_cond)     | [`mysql_cond_t`](thread_instrumentation.md#mysql_cond_t)     | Type of an instrumented condition. `mysql_cond_t` is a drop-in replacement for `pthread_cond_t`. **See also**: [mysql\_cond\_init](thread_instrumentation.md#mysql_cond_init)                                                             |

***

### mysql\_mutex\_t

```cpp
using mysql_mutex_t = struct st_mysql_mutex
```

Type: struct [`st_mysql_mutex`](thread_instrumentation.md#st_mysql_mutex)

Defined in psi/mysql\_thread.h:159

Type of an instrumented mutex. `mysql_mutex_t` is a drop-in replacement for `pthread_mutex_t`. **See also**: [mysql\_mutex\_assert\_owner](thread_instrumentation.md#mysql_mutex_assert_owner)

**See also**: [mysql\_mutex\_assert\_not\_owner](thread_instrumentation.md#mysql_mutex_assert_not_owner)

**See also**: [mysql\_mutex\_init](thread_instrumentation.md#mysql_mutex_init)

**See also**: [mysql\_mutex\_lock](thread_instrumentation.md#mysql_mutex_lock)

**See also**: [mysql\_mutex\_unlock](thread_instrumentation.md#mysql_mutex_unlock)

**See also**: [mysql\_mutex\_destroy](thread_instrumentation.md#mysql_mutex_destroy)

***

### mysql\_rwlock\_t

```cpp
using mysql_rwlock_t = struct st_mysql_rwlock
```

Type: struct [`st_mysql_rwlock`](thread_instrumentation.md#st_mysql_rwlock)

Defined in psi/mysql\_thread.h:204

Type of an instrumented rwlock. `mysql_rwlock_t` is a drop-in replacement for `pthread_rwlock_t`. **See also**: [mysql\_rwlock\_init](thread_instrumentation.md#mysql_rwlock_init)

**See also**: [mysql\_rwlock\_rdlock](thread_instrumentation.md#mysql_rwlock_rdlock)

**See also**: [mysql\_rwlock\_tryrdlock](thread_instrumentation.md#mysql_rwlock_tryrdlock)

**See also**: [mysql\_rwlock\_wrlock](thread_instrumentation.md#mysql_rwlock_wrlock)

**See also**: [mysql\_rwlock\_trywrlock](thread_instrumentation.md#mysql_rwlock_trywrlock)

**See also**: [mysql\_rwlock\_unlock](thread_instrumentation.md#mysql_rwlock_unlock)

**See also**: [mysql\_rwlock\_destroy](thread_instrumentation.md#mysql_rwlock_destroy)

***

### mysql\_prlock\_t

```cpp
using mysql_prlock_t = struct st_mysql_prlock
```

Type: struct [`st_mysql_prlock`](thread_instrumentation.md#st_mysql_prlock)

Defined in psi/mysql\_thread.h:216

Type of an instrumented prlock. A prlock is a read write lock that 'prefers readers' (pr). `mysql_prlock_t` is a drop-in replacement for `rw_pr_lock_t`. **See also**: [mysql\_prlock\_init](thread_instrumentation.md#mysql_prlock_init)

**See also**: [mysql\_prlock\_rdlock](thread_instrumentation.md#mysql_prlock_rdlock)

**See also**: [mysql\_prlock\_wrlock](thread_instrumentation.md#mysql_prlock_wrlock)

**See also**: [mysql\_prlock\_unlock](thread_instrumentation.md#mysql_prlock_unlock)

**See also**: [mysql\_prlock\_destroy](thread_instrumentation.md#mysql_prlock_destroy)

***

### mysql\_cond\_t

```cpp
using mysql_cond_t = struct st_mysql_cond
```

Type: struct [`st_mysql_cond`](thread_instrumentation.md#st_mysql_cond)

Defined in psi/mysql\_thread.h:244

Type of an instrumented condition. `mysql_cond_t` is a drop-in replacement for `pthread_cond_t`. **See also**: [mysql\_cond\_init](thread_instrumentation.md#mysql_cond_init)

**See also**: [mysql\_cond\_wait](thread_instrumentation.md#mysql_cond_wait)

**See also**: [mysql\_cond\_timedwait](thread_instrumentation.md#mysql_cond_timedwait)

**See also**: [mysql\_cond\_signal](thread_instrumentation.md#mysql_cond_signal)

**See also**: [mysql\_cond\_broadcast](thread_instrumentation.md#mysql_cond_broadcast)

**See also**: [mysql\_cond\_destroy](thread_instrumentation.md#mysql_cond_destroy)

## Functions

| Return | Name                                                                                                         | Description |
| ------ | ------------------------------------------------------------------------------------------------------------ | ----------- |
| `void` | [`inline_mysql_mutex_register`](thread_instrumentation.md#inline_mysql_mutex_register) `static` `inline`     |             |
| `int`  | [`inline_mysql_mutex_init`](thread_instrumentation.md#inline_mysql_mutex_init) `static` `inline`             |             |
| `int`  | [`inline_mysql_mutex_destroy`](thread_instrumentation.md#inline_mysql_mutex_destroy) `static` `inline`       |             |
| `int`  | [`inline_mysql_mutex_lock`](thread_instrumentation.md#inline_mysql_mutex_lock) `static` `inline`             |             |
| `int`  | [`inline_mysql_mutex_trylock`](thread_instrumentation.md#inline_mysql_mutex_trylock) `static` `inline`       |             |
| `int`  | [`inline_mysql_mutex_unlock`](thread_instrumentation.md#inline_mysql_mutex_unlock) `static` `inline`         |             |
| `void` | [`inline_mysql_rwlock_register`](thread_instrumentation.md#inline_mysql_rwlock_register) `static` `inline`   |             |
| `int`  | [`inline_mysql_rwlock_init`](thread_instrumentation.md#inline_mysql_rwlock_init) `static` `inline`           |             |
| `int`  | [`inline_mysql_prlock_init`](thread_instrumentation.md#inline_mysql_prlock_init) `static` `inline`           |             |
| `int`  | [`inline_mysql_rwlock_destroy`](thread_instrumentation.md#inline_mysql_rwlock_destroy) `static` `inline`     |             |
| `int`  | [`inline_mysql_prlock_destroy`](thread_instrumentation.md#inline_mysql_prlock_destroy) `static` `inline`     |             |
| `int`  | [`inline_mysql_rwlock_rdlock`](thread_instrumentation.md#inline_mysql_rwlock_rdlock) `static` `inline`       |             |
| `int`  | [`inline_mysql_prlock_rdlock`](thread_instrumentation.md#inline_mysql_prlock_rdlock) `static` `inline`       |             |
| `int`  | [`inline_mysql_rwlock_wrlock`](thread_instrumentation.md#inline_mysql_rwlock_wrlock) `static` `inline`       |             |
| `int`  | [`inline_mysql_prlock_wrlock`](thread_instrumentation.md#inline_mysql_prlock_wrlock) `static` `inline`       |             |
| `int`  | [`inline_mysql_rwlock_tryrdlock`](thread_instrumentation.md#inline_mysql_rwlock_tryrdlock) `static` `inline` |             |
| `int`  | [`inline_mysql_rwlock_trywrlock`](thread_instrumentation.md#inline_mysql_rwlock_trywrlock) `static` `inline` |             |
| `int`  | [`inline_mysql_rwlock_unlock`](thread_instrumentation.md#inline_mysql_rwlock_unlock) `static` `inline`       |             |
| `int`  | [`inline_mysql_prlock_unlock`](thread_instrumentation.md#inline_mysql_prlock_unlock) `static` `inline`       |             |
| `void` | [`inline_mysql_cond_register`](thread_instrumentation.md#inline_mysql_cond_register) `static` `inline`       |             |
| `int`  | [`inline_mysql_cond_init`](thread_instrumentation.md#inline_mysql_cond_init) `static` `inline`               |             |
| `int`  | [`inline_mysql_cond_destroy`](thread_instrumentation.md#inline_mysql_cond_destroy) `static` `inline`         |             |
| `int`  | [`inline_mysql_cond_wait`](thread_instrumentation.md#inline_mysql_cond_wait) `static` `inline`               |             |
| `int`  | [`inline_mysql_cond_timedwait`](thread_instrumentation.md#inline_mysql_cond_timedwait) `static` `inline`     |             |
| `int`  | [`inline_mysql_cond_signal`](thread_instrumentation.md#inline_mysql_cond_signal) `static` `inline`           |             |
| `int`  | [`inline_mysql_cond_broadcast`](thread_instrumentation.md#inline_mysql_cond_broadcast) `static` `inline`     |             |
| `void` | [`inline_mysql_thread_register`](thread_instrumentation.md#inline_mysql_thread_register) `static` `inline`   |             |

***

### inline\_mysql\_mutex\_register

`static` `inline`

```cpp
static inline void inline_mysql_mutex_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql\_thread.h:669

***

### inline\_mysql\_mutex\_init

`static` `inline`

```cpp
static inline int inline_mysql_mutex_init(mysql_mutex_t * that, const pthread_mutexattr_t * attr, mysql_mutex_t * that, const pthread_mutexattr_t * attr)
```

Defined in psi/mysql\_thread.h:686

***

### inline\_mysql\_mutex\_destroy

`static` `inline`

```cpp
static inline int inline_mysql_mutex_destroy(mysql_mutex_t * that, mysql_mutex_t * that)
```

Defined in psi/mysql\_thread.h:709

***

### inline\_mysql\_mutex\_lock

`static` `inline`

```cpp
static inline int inline_mysql_mutex_lock(mysql_mutex_t * that, mysql_mutex_t * that)
```

Defined in psi/mysql\_thread.h:737

***

### inline\_mysql\_mutex\_trylock

`static` `inline`

```cpp
static inline int inline_mysql_mutex_trylock(mysql_mutex_t * that, mysql_mutex_t * that)
```

Defined in psi/mysql\_thread.h:756

***

### inline\_mysql\_mutex\_unlock

`static` `inline`

```cpp
static inline int inline_mysql_mutex_unlock(mysql_mutex_t * that, mysql_mutex_t * that)
```

Defined in psi/mysql\_thread.h:775

***

### inline\_mysql\_rwlock\_register

`static` `inline`

```cpp
static inline void inline_mysql_rwlock_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql\_thread.h:798

***

### inline\_mysql\_rwlock\_init

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_init(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql\_thread.h:815

***

### inline\_mysql\_prlock\_init

`static` `inline`

```cpp
static inline int inline_mysql_prlock_init(mysql_prlock_t * that, mysql_prlock_t * that)
```

Defined in psi/mysql\_thread.h:833

***

### inline\_mysql\_rwlock\_destroy

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_destroy(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql\_thread.h:848

***

### inline\_mysql\_prlock\_destroy

`static` `inline`

```cpp
static inline int inline_mysql_prlock_destroy(mysql_prlock_t * that, mysql_prlock_t * that)
```

Defined in psi/mysql\_thread.h:862

***

### inline\_mysql\_rwlock\_rdlock

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_rdlock(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql\_thread.h:893

***

### inline\_mysql\_prlock\_rdlock

`static` `inline`

```cpp
static inline int inline_mysql_prlock_rdlock(mysql_prlock_t * that, mysql_prlock_t * that)
```

Defined in psi/mysql\_thread.h:908

***

### inline\_mysql\_rwlock\_wrlock

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_wrlock(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql\_thread.h:923

***

### inline\_mysql\_prlock\_wrlock

`static` `inline`

```cpp
static inline int inline_mysql_prlock_wrlock(mysql_prlock_t * that, mysql_prlock_t * that)
```

Defined in psi/mysql\_thread.h:938

***

### inline\_mysql\_rwlock\_tryrdlock

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_tryrdlock(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql\_thread.h:953

***

### inline\_mysql\_rwlock\_trywrlock

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_trywrlock(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql\_thread.h:967

***

### inline\_mysql\_rwlock\_unlock

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_unlock(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql\_thread.h:981

***

### inline\_mysql\_prlock\_unlock

`static` `inline`

```cpp
static inline int inline_mysql_prlock_unlock(mysql_prlock_t * that, mysql_prlock_t * that)
```

Defined in psi/mysql\_thread.h:994

***

### inline\_mysql\_cond\_register

`static` `inline`

```cpp
static inline void inline_mysql_cond_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql\_thread.h:1007

***

### inline\_mysql\_cond\_init

`static` `inline`

```cpp
static inline int inline_mysql_cond_init(mysql_cond_t * that, const pthread_condattr_t * attr, mysql_cond_t * that, const pthread_condattr_t * attr)
```

Defined in psi/mysql\_thread.h:1024

***

### inline\_mysql\_cond\_destroy

`static` `inline`

```cpp
static inline int inline_mysql_cond_destroy(mysql_cond_t * that, mysql_cond_t * that)
```

Defined in psi/mysql\_thread.h:1039

***

### inline\_mysql\_cond\_wait

`static` `inline`

```cpp
static inline int inline_mysql_cond_wait(mysql_cond_t * that, mysql_mutex_t * mutex, mysql_cond_t * that, mysql_mutex_t * mutex)
```

Defined in psi/mysql\_thread.h:1060

***

### inline\_mysql\_cond\_timedwait

`static` `inline`

```cpp
static inline int inline_mysql_cond_timedwait(mysql_cond_t * that, mysql_mutex_t * mutex, const struct timespec * abstime, mysql_cond_t * that, mysql_mutex_t * mutex, const struct timespec * abstime)
```

Defined in psi/mysql\_thread.h:1075

***

### inline\_mysql\_cond\_signal

`static` `inline`

```cpp
static inline int inline_mysql_cond_signal(mysql_cond_t * that, mysql_cond_t * that)
```

Defined in psi/mysql\_thread.h:1091

***

### inline\_mysql\_cond\_broadcast

`static` `inline`

```cpp
static inline int inline_mysql_cond_broadcast(mysql_cond_t * that, mysql_cond_t * that)
```

Defined in psi/mysql\_thread.h:1103

***

### inline\_mysql\_thread\_register

`static` `inline`

```cpp
static inline void inline_mysql_thread_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql\_thread.h:1115

## Class Definitions

### st\_mysql\_mutex

```cpp
#include <mysql_thread.h>
```

```cpp
struct st_mysql_mutex
```

Defined in psi/mysql\_thread.h:133

An instrumented mutex structure. **See also**: [mysql\_mutex\_t](thread_instrumentation.md#mysql_mutex_t)

#### Public Attributes

| Return                                | Name                                           | Description                                                                                                                            |
| ------------------------------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `pthread_mutex_t`                     | [`m_mutex`](thread_instrumentation.md#m_mutex) | The real mutex.                                                                                                                        |
| struct [`PSI_mutex`](./#psi_mutex) \* | [`m_psi`](thread_instrumentation.md#m_psi-2)   | The instrumentation hook. Note that this hook is not conditionally defined, for binary compatibility of the `mysql_mutex_t` interface. |

***

#### m\_mutex

```cpp
pthread_mutex_t m_mutex
```

Defined in psi/mysql\_thread.h:139

The real mutex.

***

#### m\_psi

```cpp
struct PSI_mutex * m_psi
```

Type: struct [`PSI_mutex`](./#psi_mutex) \*

Defined in psi/mysql\_thread.h:146

The instrumentation hook. Note that this hook is not conditionally defined, for binary compatibility of the `mysql_mutex_t` interface.

### st\_mysql\_rwlock

```cpp
#include <mysql_thread.h>
```

```cpp
struct st_mysql_rwlock
```

Defined in psi/mysql\_thread.h:165

An instrumented rwlock structure. **See also**: [mysql\_rwlock\_t](thread_instrumentation.md#mysql_rwlock_t)

#### Public Attributes

| Return                                  | Name                                             | Description                                                                                                                             |
| --------------------------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| `rw_lock_t`                             | [`m_rwlock`](thread_instrumentation.md#m_rwlock) | The real rwlock                                                                                                                         |
| struct [`PSI_rwlock`](./#psi_rwlock) \* | [`m_psi`](thread_instrumentation.md#m_psi-3)     | The instrumentation hook. Note that this hook is not conditionally defined, for binary compatibility of the `mysql_rwlock_t` interface. |

***

#### m\_rwlock

```cpp
rw_lock_t m_rwlock
```

Defined in psi/mysql\_thread.h:168

The real rwlock

***

#### m\_psi

```cpp
struct PSI_rwlock * m_psi
```

Type: struct [`PSI_rwlock`](./#psi_rwlock) \*

Defined in psi/mysql\_thread.h:174

The instrumentation hook. Note that this hook is not conditionally defined, for binary compatibility of the `mysql_rwlock_t` interface.

### st\_mysql\_prlock

```cpp
#include <mysql_thread.h>
```

```cpp
struct st_mysql_prlock
```

Defined in psi/mysql\_thread.h:181

An instrumented prlock structure. **See also**: [mysql\_prlock\_t](thread_instrumentation.md#mysql_prlock_t)

#### Public Attributes

| Return                                  | Name                                             | Description                                                                                                                             |
| --------------------------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| `rw_pr_lock_t`                          | [`m_prlock`](thread_instrumentation.md#m_prlock) | The real prlock                                                                                                                         |
| struct [`PSI_rwlock`](./#psi_rwlock) \* | [`m_psi`](thread_instrumentation.md#m_psi-2)     | The instrumentation hook. Note that this hook is not conditionally defined, for binary compatibility of the `mysql_rwlock_t` interface. |

***

#### m\_prlock

```cpp
rw_pr_lock_t m_prlock
```

Defined in psi/mysql\_thread.h:184

The real prlock

***

#### m\_psi

```cpp
struct PSI_rwlock * m_psi
```

Type: struct [`PSI_rwlock`](./#psi_rwlock) \*

Defined in psi/mysql\_thread.h:190

The instrumentation hook. Note that this hook is not conditionally defined, for binary compatibility of the `mysql_rwlock_t` interface.

### st\_mysql\_cond

```cpp
#include <mysql_thread.h>
```

```cpp
struct st_mysql_cond
```

Defined in psi/mysql\_thread.h:222

An instrumented cond structure. **See also**: [mysql\_cond\_t](thread_instrumentation.md#mysql_cond_t)

#### Public Attributes

| Return                              | Name                                         | Description                                                                                                                           |
| ----------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `pthread_cond_t`                    | [`m_cond`](thread_instrumentation.md#m_cond) | The real condition                                                                                                                    |
| struct [`PSI_cond`](./#psi_cond) \* | [`m_psi`](thread_instrumentation.md#m_psi-3) | The instrumentation hook. Note that this hook is not conditionally defined, for binary compatibility of the `mysql_cond_t` interface. |

***

#### m\_cond

```cpp
pthread_cond_t m_cond
```

Defined in psi/mysql\_thread.h:225

The real condition

***

#### m\_psi

```cpp
struct PSI_cond * m_psi
```

Type: struct [`PSI_cond`](./#psi_cond) \*

Defined in psi/mysql\_thread.h:231

The instrumentation hook. Note that this hook is not conditionally defined, for binary compatibility of the `mysql_cond_t` interface.
