---
description: >-
  Plugin API reference: Thread Instrumentation. Generated from the MariaDB server headers by doxygen and moxygen.
---

{#threadinstrumentation}

# Thread Instrumentation

> [`Instrumentation Interface`](Instrumentation_interface.md#instrumentationinterface)

## Classes

| Name | Description |
|------|-------------|
| [`st_mysql_mutex`](#st_mysql_mutex) | An instrumented mutex structure. **See also**: [mysql_mutex_t](api.md#mysql_mutex_t) |
| [`st_mysql_rwlock`](#st_mysql_rwlock) | An instrumented rwlock structure. **See also**: [mysql_rwlock_t](api.md#mysql_rwlock_t) |
| [`st_mysql_prlock`](#st_mysql_prlock) | An instrumented prlock structure. **See also**: [mysql_prlock_t](api.md#mysql_prlock_t) |
| [`st_mysql_cond`](#st_mysql_cond) | An instrumented cond structure. **See also**: [mysql_cond_t](api.md#mysql_cond_t) |

## Macros

| Name | Description |
|------|-------------|
| [`PSI_CALL_delete_current_thread`](#psi_call_delete_current_thread)  |  |
| [`PSI_CALL_get_thread`](#psi_call_get_thread)  |  |
| [`PSI_CALL_new_thread`](#psi_call_new_thread)  |  |
| [`PSI_CALL_register_thread`](#psi_call_register_thread)  |  |
| [`PSI_CALL_set_thread`](#psi_call_set_thread)  |  |
| [`PSI_CALL_set_thread_THD`](#psi_call_set_thread_thd)  |  |
| [`PSI_CALL_set_thread_connect_attrs`](#psi_call_set_thread_connect_attrs)  |  |
| [`PSI_CALL_set_thread_db`](#psi_call_set_thread_db)  |  |
| [`PSI_CALL_set_thread_id`](#psi_call_set_thread_id)  |  |
| [`PSI_CALL_set_thread_os_id`](#psi_call_set_thread_os_id)  |  |
| [`PSI_CALL_set_thread_info`](#psi_call_set_thread_info)  |  |
| [`PSI_CALL_set_thread_start_time`](#psi_call_set_thread_start_time)  |  |
| [`PSI_CALL_set_thread_account`](#psi_call_set_thread_account)  |  |
| [`PSI_CALL_spawn_thread`](#psi_call_spawn_thread)  |  |
| [`PSI_CALL_set_connection_type`](#psi_call_set_connection_type)  |  |
| [`mysql_mutex_is_owner`](#mysql_mutex_is_owner)  |  |
| [`mysql_mutex_assert_owner`](#mysql_mutex_assert_owner)  | Wrapper, to use safe_mutex_assert_owner with instrumented mutexes. `mysql_mutex_assert_owner` is a drop-in replacement for `safe_mutex_assert_owner`. |
| [`mysql_mutex_assert_not_owner`](#mysql_mutex_assert_not_owner)  | Wrapper, to use safe_mutex_assert_not_owner with instrumented mutexes. `mysql_mutex_assert_not_owner` is a drop-in replacement for `safe_mutex_assert_not_owner`. |
| [`mysql_mutex_setflags`](#mysql_mutex_setflags)  |  |
| [`mysql_prlock_assert_write_owner`](#mysql_prlock_assert_write_owner)  | Drop-in replacement for `rw_pr_lock_assert_write_owner`. |
| [`mysql_prlock_assert_not_write_owner`](#mysql_prlock_assert_not_write_owner)  | Drop-in replacement for `rw_pr_lock_assert_not_write_owner`. |
| [`mysql_mutex_register`](#mysql_mutex_register)  | Mutex registration. |
| [`mysql_mutex_init`](#mysql_mutex_init)  | Instrumented mutex_init. `mysql_mutex_init` is a replacement for `pthread_mutex_init`. |
| [`mysql_mutex_destroy`](#mysql_mutex_destroy)  | Instrumented mutex_destroy. `mysql_mutex_destroy` is a drop-in replacement for `pthread_mutex_destroy`. |
| [`mysql_mutex_lock`](#mysql_mutex_lock)  | Instrumented mutex_lock. `mysql_mutex_lock` is a drop-in replacement for `pthread_mutex_lock`. |
| [`mysql_mutex_trylock`](#mysql_mutex_trylock)  | Instrumented mutex_lock. `mysql_mutex_trylock` is a drop-in replacement for `pthread_mutex_trylock`. |
| [`mysql_mutex_unlock`](#mysql_mutex_unlock)  | Instrumented mutex_unlock. `mysql_mutex_unlock` is a drop-in replacement for `pthread_mutex_unlock`. |
| [`mysql_rwlock_register`](#mysql_rwlock_register)  | Rwlock registration. |
| [`mysql_rwlock_init`](#mysql_rwlock_init)  | Instrumented rwlock_init. `mysql_rwlock_init` is a replacement for `pthread_rwlock_init`. Note that pthread_rwlockattr_t is not supported in MySQL. |
| [`mysql_prlock_init`](#mysql_prlock_init)  | Instrumented rw_pr_init. `mysql_prlock_init` is a replacement for `rw_pr_init`. |
| [`mysql_rwlock_destroy`](#mysql_rwlock_destroy)  | Instrumented rwlock_destroy. `mysql_rwlock_destroy` is a drop-in replacement for `pthread_rwlock_destroy`. |
| [`mysql_prlock_destroy`](#mysql_prlock_destroy)  | Instrumented rw_pr_destroy. `mysql_prlock_destroy` is a drop-in replacement for `rw_pr_destroy`. |
| [`mysql_rwlock_rdlock`](#mysql_rwlock_rdlock)  | Instrumented rwlock_rdlock. `mysql_rwlock_rdlock` is a drop-in replacement for `pthread_rwlock_rdlock`. |
| [`mysql_prlock_rdlock`](#mysql_prlock_rdlock)  | Instrumented rw_pr_rdlock. `mysql_prlock_rdlock` is a drop-in replacement for `rw_pr_rdlock`. |
| [`mysql_rwlock_wrlock`](#mysql_rwlock_wrlock)  | Instrumented rwlock_wrlock. `mysql_rwlock_wrlock` is a drop-in replacement for `pthread_rwlock_wrlock`. |
| [`mysql_prlock_wrlock`](#mysql_prlock_wrlock)  | Instrumented rw_pr_wrlock. `mysql_prlock_wrlock` is a drop-in replacement for `rw_pr_wrlock`. |
| [`mysql_rwlock_tryrdlock`](#mysql_rwlock_tryrdlock)  | Instrumented rwlock_tryrdlock. `mysql_rwlock_tryrdlock` is a drop-in replacement for `pthread_rwlock_tryrdlock`. |
| [`mysql_rwlock_trywrlock`](#mysql_rwlock_trywrlock)  | Instrumented rwlock_trywrlock. `mysql_rwlock_trywrlock` is a drop-in replacement for `pthread_rwlock_trywrlock`. |
| [`mysql_rwlock_unlock`](#mysql_rwlock_unlock)  | Instrumented rwlock_unlock. `mysql_rwlock_unlock` is a drop-in replacement for `pthread_rwlock_unlock`. |
| [`mysql_prlock_unlock`](#mysql_prlock_unlock)  | Instrumented rw_pr_unlock. `mysql_prlock_unlock` is a drop-in replacement for `rw_pr_unlock`. |
| [`mysql_cond_register`](#mysql_cond_register)  | Cond registration. |
| [`mysql_cond_init`](#mysql_cond_init)  | Instrumented cond_init. `mysql_cond_init` is a replacement for `pthread_cond_init`. |
| [`mysql_cond_destroy`](#mysql_cond_destroy)  | Instrumented cond_destroy. `mysql_cond_destroy` is a drop-in replacement for `pthread_cond_destroy`. |
| [`mysql_cond_wait`](#mysql_cond_wait)  | Instrumented cond_wait. `mysql_cond_wait` is a drop-in replacement for `pthread_cond_wait`. |
| [`mysql_cond_timedwait`](#mysql_cond_timedwait)  | Instrumented cond_timedwait. `mysql_cond_timedwait` is a drop-in replacement for `pthread_cond_timedwait`. |
| [`mysql_cond_signal`](#mysql_cond_signal)  | Instrumented cond_signal. `mysql_cond_signal` is a drop-in replacement for `pthread_cond_signal`. |
| [`mysql_cond_broadcast`](#mysql_cond_broadcast)  | Instrumented cond_broadcast. `mysql_cond_broadcast` is a drop-in replacement for `pthread_cond_broadcast`. |
| [`mysql_thread_register`](#mysql_thread_register)  | Thread registration. |
| [`mysql_thread_create`](#mysql_thread_create)  | Instrumented pthread_create. This function creates both the thread instrumentation and a thread. `mysql_thread_create` is a replacement for `pthread_create`. The parameter P4 (or, if it is NULL, P1) will be used as the instrumented thread "identity". Providing a P1 / P4 parameter with a different value for each call will on average improve performances, since this thread identity value is used internally to randomize access to data and prevent contention. This is optional, and the improvement is not guaranteed, only statistical. |
| [`mysql_thread_set_psi_id`](#mysql_thread_set_psi_id)  | Set the thread identifier for the instrumentation. |
| [`mysql_thread_set_psi_THD`](#mysql_thread_set_psi_thd)  | Set the thread sql session for the instrumentation. |

---

{#psi_call_delete_current_thread}

### PSI_CALL_delete_current_thread

```cpp
#define PSI_CALL_delete_current_thread() do { } while(0)
```

Defined in psi/mysql_thread.h:111

---

{#psi_call_get_thread}

### PSI_CALL_get_thread

```cpp
#define PSI_CALL_get_thread() NULL
```

Defined in psi/mysql_thread.h:112

---

{#psi_call_new_thread}

### PSI_CALL_new_thread

```cpp
#define PSI_CALL_new_thread(A1, A2, A3, A1, A2, A3) NULL
```

Defined in psi/mysql_thread.h:113

---

{#psi_call_register_thread}

### PSI_CALL_register_thread

```cpp
#define PSI_CALL_register_thread(A1, A2, A3, A1, A2, A3) do { } while(0)
```

Defined in psi/mysql_thread.h:114

---

{#psi_call_set_thread}

### PSI_CALL_set_thread

```cpp
#define PSI_CALL_set_thread(A1, A1) do { } while(0)
```

Defined in psi/mysql_thread.h:115

---

{#psi_call_set_thread_thd}

### PSI_CALL_set_thread_THD

```cpp
#define PSI_CALL_set_thread_THD(A1, A2, A1, A2) do { } while(0)
```

Defined in psi/mysql_thread.h:116

---

{#psi_call_set_thread_connect_attrs}

### PSI_CALL_set_thread_connect_attrs

```cpp
#define PSI_CALL_set_thread_connect_attrs(A1, A2, A3, A1, A2, A3) 0
```

Defined in psi/mysql_thread.h:117

---

{#psi_call_set_thread_db}

### PSI_CALL_set_thread_db

```cpp
#define PSI_CALL_set_thread_db(A1, A2, A1, A2) do { } while(0)
```

Defined in psi/mysql_thread.h:118

---

{#psi_call_set_thread_id}

### PSI_CALL_set_thread_id

```cpp
#define PSI_CALL_set_thread_id(A1, A2, A1, A2) do { } while(0)
```

Defined in psi/mysql_thread.h:119

---

{#psi_call_set_thread_os_id}

### PSI_CALL_set_thread_os_id

```cpp
#define PSI_CALL_set_thread_os_id(A1, A1) do { } while(0)
```

Defined in psi/mysql_thread.h:120

---

{#psi_call_set_thread_info}

### PSI_CALL_set_thread_info

```cpp
#define PSI_CALL_set_thread_info(A1, A2, A1, A2) do { } while(0)
```

Defined in psi/mysql_thread.h:121

---

{#psi_call_set_thread_start_time}

### PSI_CALL_set_thread_start_time

```cpp
#define PSI_CALL_set_thread_start_time(A1, A1) do { } while(0)
```

Defined in psi/mysql_thread.h:122

---

{#psi_call_set_thread_account}

### PSI_CALL_set_thread_account

```cpp
#define PSI_CALL_set_thread_account(A1, A2, A3, A4, A1, A2, A3, A4) do { } while(0)
```

Defined in psi/mysql_thread.h:123

---

{#psi_call_spawn_thread}

### PSI_CALL_spawn_thread

```cpp
#define PSI_CALL_spawn_thread(A1, A2, A3, A4, A5, A1, A2, A3, A4, A5) 0
```

Defined in psi/mysql_thread.h:124

---

{#psi_call_set_connection_type}

### PSI_CALL_set_connection_type

```cpp
#define PSI_CALL_set_connection_type(A, A) do { } while(0)
```

Defined in psi/mysql_thread.h:125

---

{#mysql_mutex_is_owner}

### mysql_mutex_is_owner

```cpp
#define mysql_mutex_is_owner(M, M) safe_mutex_is_owner(&(M)->m_mutex)
```

Defined in psi/mysql_thread.h:266

---

{#mysql_mutex_assert_owner}

### mysql_mutex_assert_owner

```cpp
#define mysql_mutex_assert_owner(M, M) safe_mutex_assert_owner(&(M)->m_mutex)
```

Defined in psi/mysql_thread.h:273

Wrapper, to use safe_mutex_assert_owner with instrumented mutexes. `mysql_mutex_assert_owner` is a drop-in replacement for `safe_mutex_assert_owner`.

---

{#mysql_mutex_assert_not_owner}

### mysql_mutex_assert_not_owner

```cpp
#define mysql_mutex_assert_not_owner(M, M) safe_mutex_assert_not_owner(&(M)->m_mutex)
```

Defined in psi/mysql_thread.h:282

Wrapper, to use safe_mutex_assert_not_owner with instrumented mutexes. `mysql_mutex_assert_not_owner` is a drop-in replacement for `safe_mutex_assert_not_owner`.

---

{#mysql_mutex_setflags}

### mysql_mutex_setflags

```cpp
#define mysql_mutex_setflags(M, F, M, F) safe_mutex_setflags(&(M)->m_mutex, (F))
```

Defined in psi/mysql_thread.h:285

---

{#mysql_prlock_assert_write_owner}

### mysql_prlock_assert_write_owner

```cpp
#define mysql_prlock_assert_write_owner(M, M) rw_pr_lock_assert_write_owner(&(M)->m_prlock)
```

Defined in psi/mysql_thread.h:293

Drop-in replacement for `rw_pr_lock_assert_write_owner`.

---

{#mysql_prlock_assert_not_write_owner}

### mysql_prlock_assert_not_write_owner

```cpp
#define mysql_prlock_assert_not_write_owner(M, M) rw_pr_lock_assert_not_write_owner(&(M)->m_prlock)
```

Defined in psi/mysql_thread.h:301

Drop-in replacement for `rw_pr_lock_assert_not_write_owner`.

---

{#mysql_mutex_register}

### mysql_mutex_register

```cpp
#define mysql_mutex_register(P1, P2, P3, P1, P2, P3) inline_mysql_mutex_register(P1, P2, P3)
```

Defined in psi/mysql_thread.h:308

Mutex registration.

---

{#mysql_mutex_init}

### mysql_mutex_init

```cpp
#define mysql_mutex_init(K, M, A, K, M, A) inline_mysql_mutex_init(M, A)
```

Defined in psi/mysql_thread.h:333

Instrumented mutex_init. `mysql_mutex_init` is a replacement for `pthread_mutex_init`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` |  | The PSI_mutex_key for this instrumented mutex |
| `M` |  | The mutex to initialize |
| `A` |  | Mutex attributes |
| `K` |  | The PSI_mutex_key for this instrumented mutex |
| `M` |  | The mutex to initialize |
| `A` |  | Mutex attributes |

---

{#mysql_mutex_destroy}

### mysql_mutex_destroy

```cpp
#define mysql_mutex_destroy(M, M) inline_mysql_mutex_destroy(M)
```

Defined in psi/mysql_thread.h:348

Instrumented mutex_destroy. `mysql_mutex_destroy` is a drop-in replacement for `pthread_mutex_destroy`.

---

{#mysql_mutex_lock}

### mysql_mutex_lock

```cpp
#define mysql_mutex_lock(M, M) inline_mysql_mutex_lock(M)
```

Defined in psi/mysql_thread.h:363

Instrumented mutex_lock. `mysql_mutex_lock` is a drop-in replacement for `pthread_mutex_lock`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `M` |  | The mutex to lock |
| `M` |  | The mutex to lock |

---

{#mysql_mutex_trylock}

### mysql_mutex_trylock

```cpp
#define mysql_mutex_trylock(M, M) inline_mysql_mutex_trylock(M)
```

Defined in psi/mysql_thread.h:378

Instrumented mutex_lock. `mysql_mutex_trylock` is a drop-in replacement for `pthread_mutex_trylock`.

---

{#mysql_mutex_unlock}

### mysql_mutex_unlock

```cpp
#define mysql_mutex_unlock(M, M) inline_mysql_mutex_unlock(M)
```

Defined in psi/mysql_thread.h:391

Instrumented mutex_unlock. `mysql_mutex_unlock` is a drop-in replacement for `pthread_mutex_unlock`.

---

{#mysql_rwlock_register}

### mysql_rwlock_register

```cpp
#define mysql_rwlock_register(P1, P2, P3, P1, P2, P3) inline_mysql_rwlock_register(P1, P2, P3)
```

Defined in psi/mysql_thread.h:399

Rwlock registration.

---

{#mysql_rwlock_init}

### mysql_rwlock_init

```cpp
#define mysql_rwlock_init(K, RW, K, RW) inline_mysql_rwlock_init(RW)
```

Defined in psi/mysql_thread.h:413

Instrumented rwlock_init. `mysql_rwlock_init` is a replacement for `pthread_rwlock_init`. Note that pthread_rwlockattr_t is not supported in MySQL.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` |  | The PSI_rwlock_key for this instrumented rwlock |
| `RW` |  | The rwlock to initialize |
| `K` |  | The PSI_rwlock_key for this instrumented rwlock |
| `RW` |  | The rwlock to initialize |

---

{#mysql_prlock_init}

### mysql_prlock_init

```cpp
#define mysql_prlock_init(K, RW, K, RW) inline_mysql_prlock_init(RW)
```

Defined in psi/mysql_thread.h:426

Instrumented rw_pr_init. `mysql_prlock_init` is a replacement for `rw_pr_init`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` |  | The PSI_rwlock_key for this instrumented prlock |
| `RW` |  | The prlock to initialize |
| `K` |  | The PSI_rwlock_key for this instrumented prlock |
| `RW` |  | The prlock to initialize |

---

{#mysql_rwlock_destroy}

### mysql_rwlock_destroy

```cpp
#define mysql_rwlock_destroy(RW, RW) inline_mysql_rwlock_destroy(RW)
```

Defined in psi/mysql_thread.h:435

Instrumented rwlock_destroy. `mysql_rwlock_destroy` is a drop-in replacement for `pthread_rwlock_destroy`.

---

{#mysql_prlock_destroy}

### mysql_prlock_destroy

```cpp
#define mysql_prlock_destroy(RW, RW) inline_mysql_prlock_destroy(RW)
```

Defined in psi/mysql_thread.h:443

Instrumented rw_pr_destroy. `mysql_prlock_destroy` is a drop-in replacement for `rw_pr_destroy`.

---

{#mysql_rwlock_rdlock}

### mysql_rwlock_rdlock

```cpp
#define mysql_rwlock_rdlock(RW, RW) inline_mysql_rwlock_rdlock(RW)
```

Defined in psi/mysql_thread.h:455

Instrumented rwlock_rdlock. `mysql_rwlock_rdlock` is a drop-in replacement for `pthread_rwlock_rdlock`.

---

{#mysql_prlock_rdlock}

### mysql_prlock_rdlock

```cpp
#define mysql_prlock_rdlock(RW, RW) inline_mysql_prlock_rdlock(RW)
```

Defined in psi/mysql_thread.h:469

Instrumented rw_pr_rdlock. `mysql_prlock_rdlock` is a drop-in replacement for `rw_pr_rdlock`.

---

{#mysql_rwlock_wrlock}

### mysql_rwlock_wrlock

```cpp
#define mysql_rwlock_wrlock(RW, RW) inline_mysql_rwlock_wrlock(RW)
```

Defined in psi/mysql_thread.h:483

Instrumented rwlock_wrlock. `mysql_rwlock_wrlock` is a drop-in replacement for `pthread_rwlock_wrlock`.

---

{#mysql_prlock_wrlock}

### mysql_prlock_wrlock

```cpp
#define mysql_prlock_wrlock(RW, RW) inline_mysql_prlock_wrlock(RW)
```

Defined in psi/mysql_thread.h:497

Instrumented rw_pr_wrlock. `mysql_prlock_wrlock` is a drop-in replacement for `rw_pr_wrlock`.

---

{#mysql_rwlock_tryrdlock}

### mysql_rwlock_tryrdlock

```cpp
#define mysql_rwlock_tryrdlock(RW, RW) inline_mysql_rwlock_tryrdlock(RW)
```

Defined in psi/mysql_thread.h:511

Instrumented rwlock_tryrdlock. `mysql_rwlock_tryrdlock` is a drop-in replacement for `pthread_rwlock_tryrdlock`.

---

{#mysql_rwlock_trywrlock}

### mysql_rwlock_trywrlock

```cpp
#define mysql_rwlock_trywrlock(RW, RW) inline_mysql_rwlock_trywrlock(RW)
```

Defined in psi/mysql_thread.h:525

Instrumented rwlock_trywrlock. `mysql_rwlock_trywrlock` is a drop-in replacement for `pthread_rwlock_trywrlock`.

---

{#mysql_rwlock_unlock}

### mysql_rwlock_unlock

```cpp
#define mysql_rwlock_unlock(RW, RW) inline_mysql_rwlock_unlock(RW)
```

Defined in psi/mysql_thread.h:535

Instrumented rwlock_unlock. `mysql_rwlock_unlock` is a drop-in replacement for `pthread_rwlock_unlock`.

---

{#mysql_prlock_unlock}

### mysql_prlock_unlock

```cpp
#define mysql_prlock_unlock(RW, RW) inline_mysql_prlock_unlock(RW)
```

Defined in psi/mysql_thread.h:543

Instrumented rw_pr_unlock. `mysql_prlock_unlock` is a drop-in replacement for `rw_pr_unlock`.

---

{#mysql_cond_register}

### mysql_cond_register

```cpp
#define mysql_cond_register(P1, P2, P3, P1, P2, P3) inline_mysql_cond_register(P1, P2, P3)
```

Defined in psi/mysql_thread.h:549

Cond registration.

---

{#mysql_cond_init}

### mysql_cond_init

```cpp
#define mysql_cond_init(K, C, A, K, C, A) inline_mysql_cond_init(C, A)
```

Defined in psi/mysql_thread.h:563

Instrumented cond_init. `mysql_cond_init` is a replacement for `pthread_cond_init`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` |  | The PSI_cond_key for this instrumented cond |
| `C` |  | The cond to initialize |
| `A` |  | Condition attributes |
| `K` |  | The PSI_cond_key for this instrumented cond |
| `C` |  | The cond to initialize |
| `A` |  | Condition attributes |

---

{#mysql_cond_destroy}

### mysql_cond_destroy

```cpp
#define mysql_cond_destroy(C, C) inline_mysql_cond_destroy(C)
```

Defined in psi/mysql_thread.h:571

Instrumented cond_destroy. `mysql_cond_destroy` is a drop-in replacement for `pthread_cond_destroy`.

---

{#mysql_cond_wait}

### mysql_cond_wait

```cpp
#define mysql_cond_wait(C, M, C, M) inline_mysql_cond_wait(C, M)
```

Defined in psi/mysql_thread.h:582

Instrumented cond_wait. `mysql_cond_wait` is a drop-in replacement for `pthread_cond_wait`.

---

{#mysql_cond_timedwait}

### mysql_cond_timedwait

```cpp
#define mysql_cond_timedwait(C, M, W, C, M, W) inline_mysql_cond_timedwait(C, M, W)
```

Defined in psi/mysql_thread.h:596

Instrumented cond_timedwait. `mysql_cond_timedwait` is a drop-in replacement for `pthread_cond_timedwait`.

---

{#mysql_cond_signal}

### mysql_cond_signal

```cpp
#define mysql_cond_signal(C, C) inline_mysql_cond_signal(C)
```

Defined in psi/mysql_thread.h:605

Instrumented cond_signal. `mysql_cond_signal` is a drop-in replacement for `pthread_cond_signal`.

---

{#mysql_cond_broadcast}

### mysql_cond_broadcast

```cpp
#define mysql_cond_broadcast(C, C) inline_mysql_cond_broadcast(C)
```

Defined in psi/mysql_thread.h:613

Instrumented cond_broadcast. `mysql_cond_broadcast` is a drop-in replacement for `pthread_cond_broadcast`.

---

{#mysql_thread_register}

### mysql_thread_register

```cpp
#define mysql_thread_register(P1, P2, P3, P1, P2, P3) inline_mysql_thread_register(P1, P2, P3)
```

Defined in psi/mysql_thread.h:619

Thread registration.

---

{#mysql_thread_create}

### mysql_thread_create

```cpp
#define mysql_thread_create(K, P1, P2, P3, P4, K, P1, P2, P3, P4) pthread_create(P1, P2, P3, P4)
```

Defined in psi/mysql_thread.h:643

Instrumented pthread_create. This function creates both the thread instrumentation and a thread. `mysql_thread_create` is a replacement for `pthread_create`. The parameter P4 (or, if it is NULL, P1) will be used as the instrumented thread "identity". Providing a P1 / P4 parameter with a different value for each call will on average improve performances, since this thread identity value is used internally to randomize access to data and prevent contention. This is optional, and the improvement is not guaranteed, only statistical.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` |  | The PSI_thread_key for this instrumented thread |
| `P1` |  | pthread_create parameter 1 |
| `P2` |  | pthread_create parameter 2 |
| `P3` |  | pthread_create parameter 3 |
| `P4` |  | pthread_create parameter 4 |
| `K` |  | The PSI_thread_key for this instrumented thread |
| `P1` |  | pthread_create parameter 1 |
| `P2` |  | pthread_create parameter 2 |
| `P3` |  | pthread_create parameter 3 |
| `P4` |  | pthread_create parameter 4 |

---

{#mysql_thread_set_psi_id}

### mysql_thread_set_psi_id

```cpp
#define mysql_thread_set_psi_id(I, I) do {} while (0)
```

Defined in psi/mysql_thread.h:655

Set the thread identifier for the instrumentation.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `I` |  | The thread identifier |
| `I` |  | The thread identifier |

---

{#mysql_thread_set_psi_thd}

### mysql_thread_set_psi_THD

```cpp
#define mysql_thread_set_psi_THD(T, T) do {} while (0)
```

Defined in psi/mysql_thread.h:666

Set the thread sql session for the instrumentation.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `T` |  | The thread identifier |
| `T` |  | The thread identifier |

## Typedefs

| Return | Name | Description |
|--------|------|-------------|
| struct [`st_mysql_mutex`](#st_mysql_mutex) | [`mysql_mutex_t`](#mysql_mutex_t)  | Type of an instrumented mutex. `mysql_mutex_t` is a drop-in replacement for `pthread_mutex_t`. **See also**: [mysql_mutex_assert_owner](api.md#mysql_mutex_assert_owner) |
| struct [`st_mysql_rwlock`](#st_mysql_rwlock) | [`mysql_rwlock_t`](#mysql_rwlock_t)  | Type of an instrumented rwlock. `mysql_rwlock_t` is a drop-in replacement for `pthread_rwlock_t`. **See also**: [mysql_rwlock_init](api.md#mysql_rwlock_init) |
| struct [`st_mysql_prlock`](#st_mysql_prlock) | [`mysql_prlock_t`](#mysql_prlock_t)  | Type of an instrumented prlock. A prlock is a read write lock that 'prefers readers' (pr). `mysql_prlock_t` is a drop-in replacement for `rw_pr_lock_t`. **See also**: [mysql_prlock_init](api.md#mysql_prlock_init) |
| struct [`st_mysql_cond`](#st_mysql_cond) | [`mysql_cond_t`](#mysql_cond_t)  | Type of an instrumented condition. `mysql_cond_t` is a drop-in replacement for `pthread_cond_t`. **See also**: [mysql_cond_init](api.md#mysql_cond_init) |

---

{#mysql_mutex_t}

### mysql_mutex_t

```cpp
using mysql_mutex_t = struct st_mysql_mutex
```

Type: struct [`st_mysql_mutex`](#st_mysql_mutex)

Defined in psi/mysql_thread.h:159

Type of an instrumented mutex. `mysql_mutex_t` is a drop-in replacement for `pthread_mutex_t`. **See also**: [mysql_mutex_assert_owner](api.md#mysql_mutex_assert_owner)

**See also**: [mysql_mutex_assert_not_owner](api.md#mysql_mutex_assert_not_owner)

**See also**: [mysql_mutex_init](api.md#mysql_mutex_init)

**See also**: [mysql_mutex_lock](api.md#mysql_mutex_lock)

**See also**: [mysql_mutex_unlock](api.md#mysql_mutex_unlock)

**See also**: [mysql_mutex_destroy](api.md#mysql_mutex_destroy)

---

{#mysql_rwlock_t}

### mysql_rwlock_t

```cpp
using mysql_rwlock_t = struct st_mysql_rwlock
```

Type: struct [`st_mysql_rwlock`](#st_mysql_rwlock)

Defined in psi/mysql_thread.h:204

Type of an instrumented rwlock. `mysql_rwlock_t` is a drop-in replacement for `pthread_rwlock_t`. **See also**: [mysql_rwlock_init](api.md#mysql_rwlock_init)

**See also**: [mysql_rwlock_rdlock](api.md#mysql_rwlock_rdlock)

**See also**: [mysql_rwlock_tryrdlock](api.md#mysql_rwlock_tryrdlock)

**See also**: [mysql_rwlock_wrlock](api.md#mysql_rwlock_wrlock)

**See also**: [mysql_rwlock_trywrlock](api.md#mysql_rwlock_trywrlock)

**See also**: [mysql_rwlock_unlock](api.md#mysql_rwlock_unlock)

**See also**: [mysql_rwlock_destroy](api.md#mysql_rwlock_destroy)

---

{#mysql_prlock_t}

### mysql_prlock_t

```cpp
using mysql_prlock_t = struct st_mysql_prlock
```

Type: struct [`st_mysql_prlock`](#st_mysql_prlock)

Defined in psi/mysql_thread.h:216

Type of an instrumented prlock. A prlock is a read write lock that 'prefers readers' (pr). `mysql_prlock_t` is a drop-in replacement for `rw_pr_lock_t`. **See also**: [mysql_prlock_init](api.md#mysql_prlock_init)

**See also**: [mysql_prlock_rdlock](api.md#mysql_prlock_rdlock)

**See also**: [mysql_prlock_wrlock](api.md#mysql_prlock_wrlock)

**See also**: [mysql_prlock_unlock](api.md#mysql_prlock_unlock)

**See also**: [mysql_prlock_destroy](api.md#mysql_prlock_destroy)

---

{#mysql_cond_t}

### mysql_cond_t

```cpp
using mysql_cond_t = struct st_mysql_cond
```

Type: struct [`st_mysql_cond`](#st_mysql_cond)

Defined in psi/mysql_thread.h:244

Type of an instrumented condition. `mysql_cond_t` is a drop-in replacement for `pthread_cond_t`. **See also**: [mysql_cond_init](api.md#mysql_cond_init)

**See also**: [mysql_cond_wait](api.md#mysql_cond_wait)

**See also**: [mysql_cond_timedwait](api.md#mysql_cond_timedwait)

**See also**: [mysql_cond_signal](api.md#mysql_cond_signal)

**See also**: [mysql_cond_broadcast](api.md#mysql_cond_broadcast)

**See also**: [mysql_cond_destroy](api.md#mysql_cond_destroy)

## Functions

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`inline_mysql_mutex_register`](#inline_mysql_mutex_register) `static` `inline` |  |
| `int` | [`inline_mysql_mutex_init`](#inline_mysql_mutex_init) `static` `inline` |  |
| `int` | [`inline_mysql_mutex_destroy`](#inline_mysql_mutex_destroy) `static` `inline` |  |
| `int` | [`inline_mysql_mutex_lock`](#inline_mysql_mutex_lock) `static` `inline` |  |
| `int` | [`inline_mysql_mutex_trylock`](#inline_mysql_mutex_trylock) `static` `inline` |  |
| `int` | [`inline_mysql_mutex_unlock`](#inline_mysql_mutex_unlock) `static` `inline` |  |
| `void` | [`inline_mysql_rwlock_register`](#inline_mysql_rwlock_register) `static` `inline` |  |
| `int` | [`inline_mysql_rwlock_init`](#inline_mysql_rwlock_init) `static` `inline` |  |
| `int` | [`inline_mysql_prlock_init`](#inline_mysql_prlock_init) `static` `inline` |  |
| `int` | [`inline_mysql_rwlock_destroy`](#inline_mysql_rwlock_destroy) `static` `inline` |  |
| `int` | [`inline_mysql_prlock_destroy`](#inline_mysql_prlock_destroy) `static` `inline` |  |
| `int` | [`inline_mysql_rwlock_rdlock`](#inline_mysql_rwlock_rdlock) `static` `inline` |  |
| `int` | [`inline_mysql_prlock_rdlock`](#inline_mysql_prlock_rdlock) `static` `inline` |  |
| `int` | [`inline_mysql_rwlock_wrlock`](#inline_mysql_rwlock_wrlock) `static` `inline` |  |
| `int` | [`inline_mysql_prlock_wrlock`](#inline_mysql_prlock_wrlock) `static` `inline` |  |
| `int` | [`inline_mysql_rwlock_tryrdlock`](#inline_mysql_rwlock_tryrdlock) `static` `inline` |  |
| `int` | [`inline_mysql_rwlock_trywrlock`](#inline_mysql_rwlock_trywrlock) `static` `inline` |  |
| `int` | [`inline_mysql_rwlock_unlock`](#inline_mysql_rwlock_unlock) `static` `inline` |  |
| `int` | [`inline_mysql_prlock_unlock`](#inline_mysql_prlock_unlock) `static` `inline` |  |
| `void` | [`inline_mysql_cond_register`](#inline_mysql_cond_register) `static` `inline` |  |
| `int` | [`inline_mysql_cond_init`](#inline_mysql_cond_init) `static` `inline` |  |
| `int` | [`inline_mysql_cond_destroy`](#inline_mysql_cond_destroy) `static` `inline` |  |
| `int` | [`inline_mysql_cond_wait`](#inline_mysql_cond_wait) `static` `inline` |  |
| `int` | [`inline_mysql_cond_timedwait`](#inline_mysql_cond_timedwait) `static` `inline` |  |
| `int` | [`inline_mysql_cond_signal`](#inline_mysql_cond_signal) `static` `inline` |  |
| `int` | [`inline_mysql_cond_broadcast`](#inline_mysql_cond_broadcast) `static` `inline` |  |
| `void` | [`inline_mysql_thread_register`](#inline_mysql_thread_register) `static` `inline` |  |

---

{#inline_mysql_mutex_register}

### inline_mysql_mutex_register

`static` `inline`

```cpp
static inline void inline_mysql_mutex_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql_thread.h:669

---

{#inline_mysql_mutex_init}

### inline_mysql_mutex_init

`static` `inline`

```cpp
static inline int inline_mysql_mutex_init(mysql_mutex_t * that, const pthread_mutexattr_t * attr, mysql_mutex_t * that, const pthread_mutexattr_t * attr)
```

Defined in psi/mysql_thread.h:686

---

{#inline_mysql_mutex_destroy}

### inline_mysql_mutex_destroy

`static` `inline`

```cpp
static inline int inline_mysql_mutex_destroy(mysql_mutex_t * that, mysql_mutex_t * that)
```

Defined in psi/mysql_thread.h:709

---

{#inline_mysql_mutex_lock}

### inline_mysql_mutex_lock

`static` `inline`

```cpp
static inline int inline_mysql_mutex_lock(mysql_mutex_t * that, mysql_mutex_t * that)
```

Defined in psi/mysql_thread.h:737

---

{#inline_mysql_mutex_trylock}

### inline_mysql_mutex_trylock

`static` `inline`

```cpp
static inline int inline_mysql_mutex_trylock(mysql_mutex_t * that, mysql_mutex_t * that)
```

Defined in psi/mysql_thread.h:756

---

{#inline_mysql_mutex_unlock}

### inline_mysql_mutex_unlock

`static` `inline`

```cpp
static inline int inline_mysql_mutex_unlock(mysql_mutex_t * that, mysql_mutex_t * that)
```

Defined in psi/mysql_thread.h:775

---

{#inline_mysql_rwlock_register}

### inline_mysql_rwlock_register

`static` `inline`

```cpp
static inline void inline_mysql_rwlock_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql_thread.h:798

---

{#inline_mysql_rwlock_init}

### inline_mysql_rwlock_init

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_init(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql_thread.h:815

---

{#inline_mysql_prlock_init}

### inline_mysql_prlock_init

`static` `inline`

```cpp
static inline int inline_mysql_prlock_init(mysql_prlock_t * that, mysql_prlock_t * that)
```

Defined in psi/mysql_thread.h:833

---

{#inline_mysql_rwlock_destroy}

### inline_mysql_rwlock_destroy

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_destroy(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql_thread.h:848

---

{#inline_mysql_prlock_destroy}

### inline_mysql_prlock_destroy

`static` `inline`

```cpp
static inline int inline_mysql_prlock_destroy(mysql_prlock_t * that, mysql_prlock_t * that)
```

Defined in psi/mysql_thread.h:862

---

{#inline_mysql_rwlock_rdlock}

### inline_mysql_rwlock_rdlock

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_rdlock(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql_thread.h:893

---

{#inline_mysql_prlock_rdlock}

### inline_mysql_prlock_rdlock

`static` `inline`

```cpp
static inline int inline_mysql_prlock_rdlock(mysql_prlock_t * that, mysql_prlock_t * that)
```

Defined in psi/mysql_thread.h:908

---

{#inline_mysql_rwlock_wrlock}

### inline_mysql_rwlock_wrlock

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_wrlock(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql_thread.h:923

---

{#inline_mysql_prlock_wrlock}

### inline_mysql_prlock_wrlock

`static` `inline`

```cpp
static inline int inline_mysql_prlock_wrlock(mysql_prlock_t * that, mysql_prlock_t * that)
```

Defined in psi/mysql_thread.h:938

---

{#inline_mysql_rwlock_tryrdlock}

### inline_mysql_rwlock_tryrdlock

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_tryrdlock(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql_thread.h:953

---

{#inline_mysql_rwlock_trywrlock}

### inline_mysql_rwlock_trywrlock

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_trywrlock(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql_thread.h:967

---

{#inline_mysql_rwlock_unlock}

### inline_mysql_rwlock_unlock

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_unlock(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql_thread.h:981

---

{#inline_mysql_prlock_unlock}

### inline_mysql_prlock_unlock

`static` `inline`

```cpp
static inline int inline_mysql_prlock_unlock(mysql_prlock_t * that, mysql_prlock_t * that)
```

Defined in psi/mysql_thread.h:994

---

{#inline_mysql_cond_register}

### inline_mysql_cond_register

`static` `inline`

```cpp
static inline void inline_mysql_cond_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql_thread.h:1007

---

{#inline_mysql_cond_init}

### inline_mysql_cond_init

`static` `inline`

```cpp
static inline int inline_mysql_cond_init(mysql_cond_t * that, const pthread_condattr_t * attr, mysql_cond_t * that, const pthread_condattr_t * attr)
```

Defined in psi/mysql_thread.h:1024

---

{#inline_mysql_cond_destroy}

### inline_mysql_cond_destroy

`static` `inline`

```cpp
static inline int inline_mysql_cond_destroy(mysql_cond_t * that, mysql_cond_t * that)
```

Defined in psi/mysql_thread.h:1039

---

{#inline_mysql_cond_wait}

### inline_mysql_cond_wait

`static` `inline`

```cpp
static inline int inline_mysql_cond_wait(mysql_cond_t * that, mysql_mutex_t * mutex, mysql_cond_t * that, mysql_mutex_t * mutex)
```

Defined in psi/mysql_thread.h:1060

---

{#inline_mysql_cond_timedwait}

### inline_mysql_cond_timedwait

`static` `inline`

```cpp
static inline int inline_mysql_cond_timedwait(mysql_cond_t * that, mysql_mutex_t * mutex, const struct timespec * abstime, mysql_cond_t * that, mysql_mutex_t * mutex, const struct timespec * abstime)
```

Defined in psi/mysql_thread.h:1075

---

{#inline_mysql_cond_signal}

### inline_mysql_cond_signal

`static` `inline`

```cpp
static inline int inline_mysql_cond_signal(mysql_cond_t * that, mysql_cond_t * that)
```

Defined in psi/mysql_thread.h:1091

---

{#inline_mysql_cond_broadcast}

### inline_mysql_cond_broadcast

`static` `inline`

```cpp
static inline int inline_mysql_cond_broadcast(mysql_cond_t * that, mysql_cond_t * that)
```

Defined in psi/mysql_thread.h:1103

---

{#inline_mysql_thread_register}

### inline_mysql_thread_register

`static` `inline`

```cpp
static inline void inline_mysql_thread_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql_thread.h:1115


## Class Definitions

{#st_mysql_mutex}

### st_mysql_mutex

```cpp
#include <mysql_thread.h>
```

```cpp
struct st_mysql_mutex
```

Defined in psi/mysql_thread.h:133

An instrumented mutex structure. **See also**: [mysql_mutex_t](api.md#mysql_mutex_t)

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `pthread_mutex_t` | [`m_mutex`](#m_mutex)  | The real mutex. |
| struct [`PSI_mutex`](api.md#psi_mutex) * | [`m_psi`](#m_psi-2)  | The instrumentation hook. Note that this hook is not conditionally defined, for binary compatibility of the `mysql_mutex_t` interface. |

---

{#m_mutex}

##### m_mutex

```cpp
pthread_mutex_t m_mutex
```

Defined in psi/mysql_thread.h:139

The real mutex.

---

{#m_psi-2}

##### m_psi

```cpp
struct PSI_mutex * m_psi
```

Type: struct [`PSI_mutex`](api.md#psi_mutex) *

Defined in psi/mysql_thread.h:146

The instrumentation hook. Note that this hook is not conditionally defined, for binary compatibility of the `mysql_mutex_t` interface.

{#st_mysql_rwlock}

### st_mysql_rwlock

```cpp
#include <mysql_thread.h>
```

```cpp
struct st_mysql_rwlock
```

Defined in psi/mysql_thread.h:165

An instrumented rwlock structure. **See also**: [mysql_rwlock_t](api.md#mysql_rwlock_t)

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `rw_lock_t` | [`m_rwlock`](#m_rwlock)  | The real rwlock |
| struct [`PSI_rwlock`](api.md#psi_rwlock) * | [`m_psi`](#m_psi-3)  | The instrumentation hook. Note that this hook is not conditionally defined, for binary compatibility of the `mysql_rwlock_t` interface. |

---

{#m_rwlock}

##### m_rwlock

```cpp
rw_lock_t m_rwlock
```

Defined in psi/mysql_thread.h:168

The real rwlock

---

{#m_psi-3}

##### m_psi

```cpp
struct PSI_rwlock * m_psi
```

Type: struct [`PSI_rwlock`](api.md#psi_rwlock) *

Defined in psi/mysql_thread.h:174

The instrumentation hook. Note that this hook is not conditionally defined, for binary compatibility of the `mysql_rwlock_t` interface.

{#st_mysql_prlock}

### st_mysql_prlock

```cpp
#include <mysql_thread.h>
```

```cpp
struct st_mysql_prlock
```

Defined in psi/mysql_thread.h:181

An instrumented prlock structure. **See also**: [mysql_prlock_t](api.md#mysql_prlock_t)

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `rw_pr_lock_t` | [`m_prlock`](#m_prlock)  | The real prlock |
| struct [`PSI_rwlock`](api.md#psi_rwlock) * | [`m_psi`](#m_psi-4)  | The instrumentation hook. Note that this hook is not conditionally defined, for binary compatibility of the `mysql_rwlock_t` interface. |

---

{#m_prlock}

##### m_prlock

```cpp
rw_pr_lock_t m_prlock
```

Defined in psi/mysql_thread.h:184

The real prlock

---

{#m_psi-4}

##### m_psi

```cpp
struct PSI_rwlock * m_psi
```

Type: struct [`PSI_rwlock`](api.md#psi_rwlock) *

Defined in psi/mysql_thread.h:190

The instrumentation hook. Note that this hook is not conditionally defined, for binary compatibility of the `mysql_rwlock_t` interface.

{#st_mysql_cond}

### st_mysql_cond

```cpp
#include <mysql_thread.h>
```

```cpp
struct st_mysql_cond
```

Defined in psi/mysql_thread.h:222

An instrumented cond structure. **See also**: [mysql_cond_t](api.md#mysql_cond_t)

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `pthread_cond_t` | [`m_cond`](#m_cond)  | The real condition |
| struct [`PSI_cond`](api.md#psi_cond) * | [`m_psi`](#m_psi-5)  | The instrumentation hook. Note that this hook is not conditionally defined, for binary compatibility of the `mysql_cond_t` interface. |

---

{#m_cond}

##### m_cond

```cpp
pthread_cond_t m_cond
```

Defined in psi/mysql_thread.h:225

The real condition

---

{#m_psi-5}

##### m_psi

```cpp
struct PSI_cond * m_psi
```

Type: struct [`PSI_cond`](api.md#psi_cond) *

Defined in psi/mysql_thread.h:231

The instrumentation hook. Note that this hook is not conditionally defined, for binary compatibility of the `mysql_cond_t` interface.

