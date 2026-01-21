---
description: >-
  Dedicated testing results for verifying that the InnoDB storage engine can
  safely upgrade data from older server versions.
---

# 10.2.7 Release Upgrade Tests

## Upgrade from 10.0

### Tested revision

5ff2db7f67401511b30dbd3fc69a1ea87d7e8cc4

### Test date

2017-07-10 07:11:04

### Summary (PASS)

All tests passed

### Details

| #  | type   | pagesize | OLD version       | file format | encrypted | compressed |    | NEW version      | file format | encrypted | compressed | readonly | result | notes |
| -- | ------ | -------- | ----------------- | ----------- | --------- | ---------- | -- | ---------------- | ----------- | --------- | ---------- | -------- | ------ | ----- |
| 1  | normal | 16       | 10.0.28 (inbuilt) | Antelope    | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 2  | normal | 16       | 10.0.28 (inbuilt) | Barracuda   | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 3  | normal | 16       | 10.0.28 (inbuilt) | Antelope    | -         | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 4  | normal | 16       | 10.0.28 (inbuilt) | Barracuda   | -         | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 5  | normal | 4        | 10.0.28 (inbuilt) | Barracuda   | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 6  | normal | 4        | 10.0.28 (inbuilt) | Antelope    | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 7  | normal | 4        | 10.0.28 (inbuilt) | Antelope    | -         | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 8  | normal | 4        | 10.0.28 (inbuilt) | Barracuda   | -         | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 9  | normal | 8        | 10.0.28 (inbuilt) | Antelope    | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 10 | normal | 8        | 10.0.28 (inbuilt) | Barracuda   | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 11 | normal | 8        | 10.0.28 (inbuilt) | Barracuda   | -         | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 12 | normal | 8        | 10.0.28 (inbuilt) | Antelope    | -         | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |

## Upgrade from 10.1

### Tested revision

5ff2db7f67401511b30dbd3fc69a1ea87d7e8cc4

### Test date

2017-07-10 07:29:38

### Summary (PASS)

All tests passed

### Details

| #  | type   | pagesize | OLD version       | file format | encrypted | compressed |    | NEW version      | file format | encrypted | compressed | readonly | result | notes |
| -- | ------ | -------- | ----------------- | ----------- | --------- | ---------- | -- | ---------------- | ----------- | --------- | ---------- | -------- | ------ | ----- |
| 1  | normal | 64       | 10.1.24 (inbuilt) | Antelope    | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | OK     |       |
| 2  | normal | 64       | 10.1.24 (inbuilt) | Barracuda   | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | OK     |       |
| 3  | normal | 64       | 10.1.24 (inbuilt) | Barracuda   | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | OK     |       |
| 4  | normal | 64       | 10.1.24 (inbuilt) | Antelope    | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | OK     |       |
| 5  | normal | 64       | 10.1.24 (inbuilt) | Barracuda   | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 6  | normal | 64       | 10.1.24 (inbuilt) | Antelope    | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 7  | normal | 64       | 10.1.24 (inbuilt) | Antelope    | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 8  | normal | 64       | 10.1.24 (inbuilt) | Barracuda   | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 9  | normal | 8        | 10.1.24 (inbuilt) | Antelope    | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | OK     |       |
| 10 | normal | 8        | 10.1.24 (inbuilt) | Barracuda   | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | OK     |       |
| 11 | normal | 8        | 10.1.24 (inbuilt) | Antelope    | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | OK     |       |
| 12 | normal | 8        | 10.1.24 (inbuilt) | Barracuda   | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | OK     |       |
| 13 | normal | 8        | 10.1.24 (inbuilt) | Barracuda   | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 14 | normal | 8        | 10.1.24 (inbuilt) | Antelope    | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 15 | normal | 8        | 10.1.24 (inbuilt) | Barracuda   | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 16 | normal | 8        | 10.1.24 (inbuilt) | Antelope    | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 17 | normal | 16       | 10.1.24 (inbuilt) | Barracuda   | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | OK     |       |
| 18 | normal | 16       | 10.1.24 (inbuilt) | Antelope    | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | OK     |       |
| 19 | normal | 16       | 10.1.24 (inbuilt) | Barracuda   | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | OK     |       |
| 20 | normal | 16       | 10.1.24 (inbuilt) | Antelope    | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | OK     |       |
| 21 | normal | 16       | 10.1.24 (inbuilt) | Antelope    | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 22 | normal | 16       | 10.1.24 (inbuilt) | Barracuda   | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 23 | normal | 16       | 10.1.24 (inbuilt) | Antelope    | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 24 | normal | 16       | 10.1.24 (inbuilt) | Barracuda   | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 25 | normal | 32       | 10.1.24 (inbuilt) | Barracuda   | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 26 | normal | 32       | 10.1.24 (inbuilt) | Antelope    | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 27 | normal | 32       | 10.1.24 (inbuilt) | Barracuda   | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 28 | normal | 32       | 10.1.24 (inbuilt) | Antelope    | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 29 | normal | 32       | 10.1.24 (inbuilt) | Barracuda   | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | OK     |       |
| 30 | normal | 32       | 10.1.24 (inbuilt) | Antelope    | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | OK     |       |
| 31 | normal | 32       | 10.1.24 (inbuilt) | Barracuda   | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | OK     |       |
| 32 | normal | 32       | 10.1.24 (inbuilt) | Antelope    | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | OK     |       |
| 33 | normal | 4        | 10.1.24 (inbuilt) | Barracuda   | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | OK     |       |
| 34 | normal | 4        | 10.1.24 (inbuilt) | Antelope    | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | OK     |       |
| 35 | normal | 4        | 10.1.24 (inbuilt) | Barracuda   | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | OK     |       |
| 36 | normal | 4        | 10.1.24 (inbuilt) | Antelope    | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | OK     |       |
| 37 | normal | 4        | 10.1.24 (inbuilt) | Antelope    | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 38 | normal | 4        | 10.1.24 (inbuilt) | Barracuda   | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 39 | normal | 4        | 10.1.24 (inbuilt) | Antelope    | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 40 | normal | 4        | 10.1.24 (inbuilt) | Barracuda   | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 41 | normal | 8        | 10.1.20 (inbuilt) | Antelope    | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 42 | normal | 8        | 10.1.20 (inbuilt) | Barracuda   | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 43 | normal | 8        | 10.1.20 (inbuilt) | Antelope    | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 44 | normal | 8        | 10.1.20 (inbuilt) | Barracuda   | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 45 | normal | 8        | 10.1.20 (inbuilt) | Barracuda   | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | OK     |       |
| 46 | normal | 8        | 10.1.20 (inbuilt) | Antelope    | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | OK     |       |
| 47 | normal | 8        | 10.1.20 (inbuilt) | Barracuda   | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | OK     |       |
| 48 | normal | 8        | 10.1.20 (inbuilt) | Antelope    | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | OK     |       |
| 49 | normal | 64       | 10.1.20 (inbuilt) | Antelope    | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | OK     |       |
| 50 | normal | 64       | 10.1.20 (inbuilt) | Barracuda   | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | OK     |       |
| 51 | normal | 64       | 10.1.20 (inbuilt) | Barracuda   | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | OK     |       |
| 52 | normal | 64       | 10.1.20 (inbuilt) | Antelope    | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | OK     |       |
| 53 | normal | 64       | 10.1.20 (inbuilt) | Barracuda   | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 54 | normal | 64       | 10.1.20 (inbuilt) | Antelope    | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 55 | normal | 64       | 10.1.20 (inbuilt) | Antelope    | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 56 | normal | 64       | 10.1.20 (inbuilt) | Barracuda   | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 57 | normal | 32       | 10.1.20 (inbuilt) | Antelope    | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | OK     |       |
| 58 | normal | 32       | 10.1.20 (inbuilt) | Barracuda   | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | OK     |       |
| 59 | normal | 32       | 10.1.20 (inbuilt) | Antelope    | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | OK     |       |
| 60 | normal | 32       | 10.1.20 (inbuilt) | Barracuda   | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | OK     |       |
| 61 | normal | 32       | 10.1.20 (inbuilt) | Barracuda   | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 62 | normal | 32       | 10.1.20 (inbuilt) | Antelope    | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 63 | normal | 32       | 10.1.20 (inbuilt) | Antelope    | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 64 | normal | 32       | 10.1.20 (inbuilt) | Barracuda   | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 65 | normal | 16       | 10.1.20 (inbuilt) | Antelope    | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | OK     |       |
| 66 | normal | 16       | 10.1.20 (inbuilt) | Barracuda   | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | OK     |       |
| 67 | normal | 16       | 10.1.20 (inbuilt) | Antelope    | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | OK     |       |
| 68 | normal | 16       | 10.1.20 (inbuilt) | Barracuda   | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | OK     |       |
| 69 | normal | 16       | 10.1.20 (inbuilt) | Barracuda   | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 70 | normal | 16       | 10.1.20 (inbuilt) | Antelope    | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 71 | normal | 16       | 10.1.20 (inbuilt) | Antelope    | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 72 | normal | 16       | 10.1.20 (inbuilt) | Barracuda   | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 73 | normal | 4        | 10.1.20 (inbuilt) | Barracuda   | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 74 | normal | 4        | 10.1.20 (inbuilt) | Antelope    | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 75 | normal | 4        | 10.1.20 (inbuilt) | Antelope    | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 76 | normal | 4        | 10.1.20 (inbuilt) | Barracuda   | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 77 | normal | 4        | 10.1.20 (inbuilt) | Antelope    | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | OK     |       |
| 78 | normal | 4        | 10.1.20 (inbuilt) | Barracuda   | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | OK     |       |
| 79 | normal | 4        | 10.1.20 (inbuilt) | Antelope    | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | OK     |       |
| 80 | normal | 4        | 10.1.20 (inbuilt) | Barracuda   | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | OK     |       |

## Upgrade from 10.2

### Tested revision

5ff2db7f67401511b30dbd3fc69a1ea87d7e8cc4

### Test date

2017-07-10 09:34:15

### Summary (FAIL)

[MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094), [MDEV-13103](https://jira.mariadb.org/browse/MDEV-13103)

### Details

| #  | type   | pagesize | OLD version      | file format | encrypted | compressed |    | NEW version      | file format | encrypted | compressed | readonly | result | notes                                                                   |
| -- | ------ | -------- | ---------------- | ----------- | --------- | ---------- | -- | ---------------- | ----------- | --------- | ---------- | -------- | ------ | ----------------------------------------------------------------------- |
| 1  | crash  | 64       | 10.2.6 (inbuilt) |             | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 2  | crash  | 64       | 10.2.6 (inbuilt) |             | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13103](https://jira.mariadb.org/browse/MDEV-13103)(1) |
| 3  | crash  | 64       | 10.2.6 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(2) |
| 4  | crash  | 64       | 10.2.6 (inbuilt) |             | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 5  | crash  | 8        | 10.2.6 (inbuilt) |             | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 6  | crash  | 8        | 10.2.6 (inbuilt) |             | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13103](https://jira.mariadb.org/browse/MDEV-13103)(1) |
| 7  | crash  | 8        | 10.2.6 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(2) |
| 8  | crash  | 8        | 10.2.6 (inbuilt) |             | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 9  | crash  | 16       | 10.2.6 (inbuilt) |             | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(2) |
| 10 | crash  | 16       | 10.2.6 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(2) |
| 11 | crash  | 16       | 10.2.6 (inbuilt) |             | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(2) |
| 12 | crash  | 16       | 10.2.6 (inbuilt) |             | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13103](https://jira.mariadb.org/browse/MDEV-13103)(1) |
| 13 | crash  | 32       | 10.2.6 (inbuilt) |             | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13103](https://jira.mariadb.org/browse/MDEV-13103)(1) |
| 14 | crash  | 32       | 10.2.6 (inbuilt) |             | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 15 | crash  | 32       | 10.2.6 (inbuilt) |             | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 16 | crash  | 32       | 10.2.6 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |                                                                         |
| 17 | crash  | 4        | 10.2.6 (inbuilt) |             | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 18 | crash  | 4        | 10.2.6 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |                                                                         |
| 19 | crash  | 4        | 10.2.6 (inbuilt) |             | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13103](https://jira.mariadb.org/browse/MDEV-13103)(1) |
| 20 | crash  | 4        | 10.2.6 (inbuilt) |             | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(2) |
| 21 | normal | 32       | 10.2.6 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(2) |
| 22 | normal | 32       | 10.2.6 (inbuilt) |             | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(2) |
| 23 | normal | 32       | 10.2.6 (inbuilt) |             | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 24 | normal | 32       | 10.2.6 (inbuilt) |             | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 25 | normal | 4        | 10.2.6 (inbuilt) |             | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 26 | normal | 4        | 10.2.6 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 27 | normal | 4        | 10.2.6 (inbuilt) |             | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(2) |
| 28 | normal | 4        | 10.2.6 (inbuilt) |             | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 29 | normal | 16       | 10.2.6 (inbuilt) |             | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 30 | normal | 16       | 10.2.6 (inbuilt) |             | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(2) |
| 31 | normal | 16       | 10.2.6 (inbuilt) |             | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 32 | normal | 16       | 10.2.6 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(2) |
| 33 | normal | 64       | 10.2.6 (inbuilt) |             | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 34 | normal | 64       | 10.2.6 (inbuilt) |             | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | OK     |                                                                         |
| 35 | normal | 64       | 10.2.6 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(2) |
| 36 | normal | 64       | 10.2.6 (inbuilt) |             | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 37 | normal | 8        | 10.2.6 (inbuilt) |             | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | OK     |                                                                         |
| 38 | normal | 8        | 10.2.6 (inbuilt) |             | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | OK     |                                                                         |
| 39 | normal | 8        | 10.2.6 (inbuilt) |             | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |                                                                         |
| 40 | normal | 8        | 10.2.6 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |                                                                         |

## Upgrade from MySQL 5.6

### Tested revision

5ff2db7f67401511b30dbd3fc69a1ea87d7e8cc4

### Test date

2017-07-10 10:34:00

### Summary (PASS)

All tests passed

### Details

| #  | type   | pagesize | OLD version      | file format | encrypted | compressed |    | NEW version      | file format | encrypted | compressed | readonly | result | notes |
| -- | ------ | -------- | ---------------- | ----------- | --------- | ---------- | -- | ---------------- | ----------- | --------- | ---------- | -------- | ------ | ----- |
| 1  | normal | 16       | 5.6.35 (inbuilt) | Antelope    | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 2  | normal | 16       | 5.6.35 (inbuilt) | Barracuda   | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 3  | normal | 16       | 5.6.35 (inbuilt) | Antelope    | -         | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 4  | normal | 16       | 5.6.35 (inbuilt) | Barracuda   | -         | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 5  | normal | 4        | 5.6.35 (inbuilt) | Barracuda   | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 6  | normal | 4        | 5.6.35 (inbuilt) | Antelope    | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 7  | normal | 4        | 5.6.35 (inbuilt) | Antelope    | -         | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 8  | normal | 4        | 5.6.35 (inbuilt) | Barracuda   | -         | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 9  | normal | 8        | 5.6.35 (inbuilt) | Antelope    | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 10 | normal | 8        | 5.6.35 (inbuilt) | Barracuda   | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 11 | normal | 8        | 5.6.35 (inbuilt) | Barracuda   | -         | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 12 | normal | 8        | 5.6.35 (inbuilt) | Antelope    | -         | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |

## Upgrade from MySQL 5.7

### Tested revision

5ff2db7f67401511b30dbd3fc69a1ea87d7e8cc4

### Test date

2017-07-10 10:52:42

### Summary (PASS)

All tests passed

### Details

| #  | type   | pagesize | OLD version      | file format | encrypted | compressed |    | NEW version      | file format | encrypted | compressed | readonly | result | notes |
| -- | ------ | -------- | ---------------- | ----------- | --------- | ---------- | -- | ---------------- | ----------- | --------- | ---------- | -------- | ------ | ----- |
| 1  | crash  | 64       | 5.7.17 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 2  | crash  | 64       | 5.7.17 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 3  | crash  | 8        | 5.7.17 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 4  | crash  | 8        | 5.7.17 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 5  | crash  | 16       | 5.7.17 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 6  | crash  | 16       | 5.7.17 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 7  | crash  | 32       | 5.7.17 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 8  | crash  | 32       | 5.7.17 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 9  | crash  | 4        | 5.7.17 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 10 | crash  | 4        | 5.7.17 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 11 | normal | 16       | 5.7.17 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 12 | normal | 16       | 5.7.17 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 13 | normal | 32       | 5.7.17 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 14 | normal | 32       | 5.7.17 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 15 | normal | 64       | 5.7.17 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 16 | normal | 64       | 5.7.17 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 17 | normal | 8        | 5.7.17 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 18 | normal | 8        | 5.7.17 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |
| 19 | normal | 4        | 5.7.17 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | OK     |       |
| 20 | normal | 4        | 5.7.17 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | OK     |       |

## Crash recovery

### Tested revision

5ff2db7f67401511b30dbd3fc69a1ea87d7e8cc4

### Test date

2017-07-10 11:23:26

### Summary (FAIL)

[MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094), [MDEV-13103](https://jira.mariadb.org/browse/MDEV-13103)

### Details

| #  | type  | pagesize | OLD version      | file format | encrypted | compressed |    | NEW version      | file format | encrypted | compressed | readonly | result | notes                                                                   |
| -- | ----- | -------- | ---------------- | ----------- | --------- | ---------- | -- | ---------------- | ----------- | --------- | ---------- | -------- | ------ | ----------------------------------------------------------------------- |
| 1  | crash | 16       | 10.2.7 (inbuilt) |             | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 2  | crash | 16       | 10.2.7 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(3) |
| 3  | crash | 16       | 10.2.7 (inbuilt) |             | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 4  | crash | 16       | 10.2.7 (inbuilt) |             | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13103](https://jira.mariadb.org/browse/MDEV-13103)(1) |
| 5  | crash | 4        | 10.2.7 (inbuilt) |             | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(2) |
| 6  | crash | 4        | 10.2.7 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(3) |
| 7  | crash | 4        | 10.2.7 (inbuilt) |             | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 8  | crash | 4        | 10.2.7 (inbuilt) |             | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13103](https://jira.mariadb.org/browse/MDEV-13103)(1) |
| 9  | crash | 32       | 10.2.7 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 10 | crash | 32       | 10.2.7 (inbuilt) |             | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 11 | crash | 32       | 10.2.7 (inbuilt) |             | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 12 | crash | 32       | 10.2.7 (inbuilt) |             | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13103](https://jira.mariadb.org/browse/MDEV-13103)(1) |
| 13 | crash | 64       | 10.2.7 (inbuilt) |             | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 14 | crash | 64       | 10.2.7 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(1) |
| 15 | crash | 64       | 10.2.7 (inbuilt) |             | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13103](https://jira.mariadb.org/browse/MDEV-13103)(1) |
| 16 | crash | 64       | 10.2.7 (inbuilt) |             | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(2) |
| 17 | crash | 8        | 10.2.7 (inbuilt) |             | -         | zlib       | => | 10.2.7 (inbuilt) |             | -         | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(2) |
| 18 | crash | 8        | 10.2.7 (inbuilt) |             | on        | zlib       | => | 10.2.7 (inbuilt) |             | on        | zlib       | -        | FAIL   | KNOWN\_BUGS [MDEV-13103](https://jira.mariadb.org/browse/MDEV-13103)(1) |
| 19 | crash | 8        | 10.2.7 (inbuilt) |             | -         | -          | => | 10.2.7 (inbuilt) |             | -         | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(2) |
| 20 | crash | 8        | 10.2.7 (inbuilt) |             | on        | -          | => | 10.2.7 (inbuilt) |             | on        | -          | -        | FAIL   | KNOWN\_BUGS [MDEV-13094](https://jira.mariadb.org/browse/MDEV-13094)(2) |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
