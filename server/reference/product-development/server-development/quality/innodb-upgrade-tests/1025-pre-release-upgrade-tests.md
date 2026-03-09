---
description: >-
  Dedicated testing results for verifying that the InnoDB storage engine can
  safely upgrade data from older server versions.
---

# 10.2.5 Pre-release Upgrade Tests

## Upgrade from 10.0

### Tested revision

b56262f69677fdb158b3d19dd8848e5802b2dd27

### Test date

2017-03-27 02:05:09

### Summary (PASS)

All tests passed

### Details

| #  | type   | pagesize | OLD version             | encrypted | compressed |    | NEW version      | encrypted | compressed | readonly | result | notes |
| -- | ------ | -------- | ----------------------- | --------- | ---------- | -- | ---------------- | --------- | ---------- | -------- | ------ | ----- |
| 1  | normal | 4        | 10.0.29 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 2  | normal | 4        | 10.0.29 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |
| 3  | normal | 8        | 10.0.29 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 4  | normal | 8        | 10.0.29 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |
| 5  | normal | 16       | 10.0.29 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 6  | normal | 16       | 10.0.29 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |
| 7  | normal | 4        | 10.0.29 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |
| 8  | normal | 4        | 10.0.29 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 9  | normal | 8        | 10.0.29 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 10 | normal | 8        | 10.0.29 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |
| 11 | normal | 16       | 10.0.29 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |
| 12 | normal | 16       | 10.0.29 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |

## Upgrade from 10.1

### Tested revision

b56262f69677fdb158b3d19dd8848e5802b2dd27

### Test date

2017-03-27 02:31:34

### Summary (FAIL)

One test failed: [MDEV-12388](https://jira.mariadb.org/browse/MDEV-12388)

### Details

| #   | type   | pagesize | OLD version             | encrypted | compressed |    | NEW version      | encrypted | compressed | readonly | result | notes                                                    |
| --- | ------ | -------- | ----------------------- | --------- | ---------- | -- | ---------------- | --------- | ---------- | -------- | ------ | -------------------------------------------------------- |
| 1   | normal | 64       | 10.1.20 (InnoDB plugin) | on        | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 2   | normal | 64       | 10.1.20 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 3   | normal | 64       | 10.1.20 (InnoDB plugin) | on        | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 4   | normal | 64       | 10.1.20 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 5   | normal | 64       | 10.1.20 (InnoDB plugin) | -         | zlib       | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 6   | normal | 64       | 10.1.20 (InnoDB plugin) | on        | zlib       | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 7   | normal | 64       | 10.1.20 (InnoDB plugin) | -         | zlib       | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 8   | normal | 64       | 10.1.20 (InnoDB plugin) | on        | zlib       | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 9   | normal | 64       | 10.1.20 (InnoDB plugin) | on        | zlib       | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 10  | normal | 64       | 10.1.20 (InnoDB plugin) | -         | zlib       | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 11  | normal | 64       | 10.1.20 (InnoDB plugin) | -         | zlib       | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 12  | normal | 64       | 10.1.20 (InnoDB plugin) | on        | zlib       | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 13  | normal | 64       | 10.1.20 (InnoDB plugin) | on        | -          | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 14  | normal | 64       | 10.1.20 (InnoDB plugin) | on        | -          | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 15  | normal | 64       | 10.1.20 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 16  | normal | 64       | 10.1.20 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 17  | normal | 8        | 10.1.20 (InnoDB plugin) | -         | zlib       | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 18  | normal | 8        | 10.1.20 (InnoDB plugin) | on        | zlib       | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 19  | normal | 8        | 10.1.20 (InnoDB plugin) | on        | zlib       | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 20  | normal | 8        | 10.1.20 (InnoDB plugin) | -         | zlib       | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 21  | normal | 8        | 10.1.20 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 22  | normal | 8        | 10.1.20 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 23  | normal | 8        | 10.1.20 (InnoDB plugin) | on        | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 24  | normal | 8        | 10.1.20 (InnoDB plugin) | on        | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 25  | normal | 8        | 10.1.20 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 26  | normal | 8        | 10.1.20 (InnoDB plugin) | on        | -          | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 27  | normal | 8        | 10.1.20 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 28  | normal | 8        | 10.1.20 (InnoDB plugin) | on        | -          | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 29  | normal | 8        | 10.1.20 (InnoDB plugin) | -         | zlib       | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 30  | normal | 8        | 10.1.20 (InnoDB plugin) | -         | zlib       | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 31  | normal | 8        | 10.1.20 (InnoDB plugin) | on        | zlib       | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 32  | normal | 8        | 10.1.20 (InnoDB plugin) | on        | zlib       | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 33  | normal | 16       | 10.1.20 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 34  | normal | 16       | 10.1.20 (InnoDB plugin) | on        | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 35  | normal | 16       | 10.1.20 (InnoDB plugin) | on        | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 36  | normal | 16       | 10.1.20 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 37  | normal | 16       | 10.1.20 (InnoDB plugin) | on        | zlib       | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 38  | normal | 16       | 10.1.20 (InnoDB plugin) | -         | zlib       | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 39  | normal | 16       | 10.1.20 (InnoDB plugin) | -         | zlib       | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 40  | normal | 16       | 10.1.20 (InnoDB plugin) | on        | zlib       | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 41  | normal | 16       | 10.1.20 (InnoDB plugin) | -         | zlib       | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 42  | normal | 16       | 10.1.20 (InnoDB plugin) | on        | zlib       | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 43  | normal | 16       | 10.1.20 (InnoDB plugin) | on        | zlib       | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 44  | normal | 16       | 10.1.20 (InnoDB plugin) | -         | zlib       | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 45  | normal | 16       | 10.1.20 (InnoDB plugin) | on        | -          | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 46  | normal | 16       | 10.1.20 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 47  | normal | 16       | 10.1.20 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 48  | normal | 16       | 10.1.20 (InnoDB plugin) | on        | -          | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 49  | normal | 32       | 10.1.20 (InnoDB plugin) | on        | zlib       | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 50  | normal | 32       | 10.1.20 (InnoDB plugin) | -         | zlib       | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 51  | normal | 32       | 10.1.20 (InnoDB plugin) | -         | zlib       | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 52  | normal | 32       | 10.1.20 (InnoDB plugin) | on        | zlib       | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 53  | normal | 32       | 10.1.20 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 54  | normal | 32       | 10.1.20 (InnoDB plugin) | on        | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 55  | normal | 32       | 10.1.20 (InnoDB plugin) | on        | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 56  | normal | 32       | 10.1.20 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 57  | normal | 32       | 10.1.20 (InnoDB plugin) | on        | -          | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 58  | normal | 32       | 10.1.20 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 59  | normal | 32       | 10.1.20 (InnoDB plugin) | on        | -          | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 60  | normal | 32       | 10.1.20 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 61  | normal | 32       | 10.1.20 (InnoDB plugin) | -         | zlib       | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 62  | normal | 32       | 10.1.20 (InnoDB plugin) | on        | zlib       | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 63  | normal | 32       | 10.1.20 (InnoDB plugin) | on        | zlib       | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 64  | normal | 32       | 10.1.20 (InnoDB plugin) | -         | zlib       | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 65  | normal | 4        | 10.1.20 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 66  | normal | 4        | 10.1.20 (InnoDB plugin) | on        | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 67  | normal | 4        | 10.1.20 (InnoDB plugin) | on        | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 68  | normal | 4        | 10.1.20 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 69  | normal | 4        | 10.1.20 (InnoDB plugin) | on        | zlib       | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 70  | normal | 4        | 10.1.20 (InnoDB plugin) | -         | zlib       | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 71  | normal | 4        | 10.1.20 (InnoDB plugin) | on        | zlib       | => | 10.2.5 (inbuilt) | on        | zlib       | -        | FAIL   | [MDEV-12388](https://jira.mariadb.org/browse/MDEV-12388) |
| 72  | normal | 4        | 10.1.20 (InnoDB plugin) | -         | zlib       | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 73  | normal | 4        | 10.1.20 (InnoDB plugin) | on        | zlib       | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 74  | normal | 4        | 10.1.20 (InnoDB plugin) | -         | zlib       | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 75  | normal | 4        | 10.1.20 (InnoDB plugin) | on        | zlib       | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 76  | normal | 4        | 10.1.20 (InnoDB plugin) | -         | zlib       | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 77  | normal | 4        | 10.1.20 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 78  | normal | 4        | 10.1.20 (InnoDB plugin) | on        | -          | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 79  | normal | 4        | 10.1.20 (InnoDB plugin) | -         | -          | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 80  | normal | 4        | 10.1.20 (InnoDB plugin) | on        | -          | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 81  | normal | 8        | 10.1.20 (inbuilt)       | -         | zlib       | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 82  | normal | 8        | 10.1.20 (inbuilt)       | on        | zlib       | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 83  | normal | 8        | 10.1.20 (inbuilt)       | on        | zlib       | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 84  | normal | 8        | 10.1.20 (inbuilt)       | -         | zlib       | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 85  | normal | 8        | 10.1.20 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 86  | normal | 8        | 10.1.20 (inbuilt)       | on        | -          | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 87  | normal | 8        | 10.1.20 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 88  | normal | 8        | 10.1.20 (inbuilt)       | on        | -          | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 89  | normal | 8        | 10.1.20 (inbuilt)       | on        | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 90  | normal | 8        | 10.1.20 (inbuilt)       | on        | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 91  | normal | 8        | 10.1.20 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 92  | normal | 8        | 10.1.20 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 93  | normal | 8        | 10.1.20 (inbuilt)       | on        | zlib       | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 94  | normal | 8        | 10.1.20 (inbuilt)       | -         | zlib       | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 95  | normal | 8        | 10.1.20 (inbuilt)       | -         | zlib       | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 96  | normal | 8        | 10.1.20 (inbuilt)       | on        | zlib       | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 97  | normal | 64       | 10.1.20 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 98  | normal | 64       | 10.1.20 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 99  | normal | 64       | 10.1.20 (inbuilt)       | on        | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 100 | normal | 64       | 10.1.20 (inbuilt)       | on        | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 101 | normal | 64       | 10.1.20 (inbuilt)       | -         | zlib       | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 102 | normal | 64       | 10.1.20 (inbuilt)       | on        | zlib       | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 103 | normal | 64       | 10.1.20 (inbuilt)       | on        | zlib       | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 104 | normal | 64       | 10.1.20 (inbuilt)       | -         | zlib       | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 105 | normal | 64       | 10.1.20 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 106 | normal | 64       | 10.1.20 (inbuilt)       | on        | -          | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 107 | normal | 64       | 10.1.20 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 108 | normal | 64       | 10.1.20 (inbuilt)       | on        | -          | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 109 | normal | 64       | 10.1.20 (inbuilt)       | on        | zlib       | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 110 | normal | 64       | 10.1.20 (inbuilt)       | on        | zlib       | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 111 | normal | 64       | 10.1.20 (inbuilt)       | -         | zlib       | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 112 | normal | 64       | 10.1.20 (inbuilt)       | -         | zlib       | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 113 | normal | 16       | 10.1.20 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 114 | normal | 16       | 10.1.20 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 115 | normal | 16       | 10.1.20 (inbuilt)       | on        | -          | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 116 | normal | 16       | 10.1.20 (inbuilt)       | on        | -          | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 117 | normal | 16       | 10.1.20 (inbuilt)       | -         | zlib       | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 118 | normal | 16       | 10.1.20 (inbuilt)       | on        | zlib       | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 119 | normal | 16       | 10.1.20 (inbuilt)       | -         | zlib       | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 120 | normal | 16       | 10.1.20 (inbuilt)       | on        | zlib       | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 121 | normal | 16       | 10.1.20 (inbuilt)       | on        | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 122 | normal | 16       | 10.1.20 (inbuilt)       | on        | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 123 | normal | 16       | 10.1.20 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 124 | normal | 16       | 10.1.20 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 125 | normal | 16       | 10.1.20 (inbuilt)       | on        | zlib       | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 126 | normal | 16       | 10.1.20 (inbuilt)       | -         | zlib       | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 127 | normal | 16       | 10.1.20 (inbuilt)       | -         | zlib       | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 128 | normal | 16       | 10.1.20 (inbuilt)       | on        | zlib       | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 129 | normal | 4        | 10.1.20 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 130 | normal | 4        | 10.1.20 (inbuilt)       | on        | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 131 | normal | 4        | 10.1.20 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 132 | normal | 4        | 10.1.20 (inbuilt)       | on        | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 133 | normal | 4        | 10.1.20 (inbuilt)       | -         | zlib       | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 134 | normal | 4        | 10.1.20 (inbuilt)       | on        | zlib       | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 135 | normal | 4        | 10.1.20 (inbuilt)       | -         | zlib       | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 136 | normal | 4        | 10.1.20 (inbuilt)       | on        | zlib       | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 137 | normal | 4        | 10.1.20 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 138 | normal | 4        | 10.1.20 (inbuilt)       | on        | -          | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 139 | normal | 4        | 10.1.20 (inbuilt)       | on        | -          | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 140 | normal | 4        | 10.1.20 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 141 | normal | 4        | 10.1.20 (inbuilt)       | -         | zlib       | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 142 | normal | 4        | 10.1.20 (inbuilt)       | -         | zlib       | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 143 | normal | 4        | 10.1.20 (inbuilt)       | on        | zlib       | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 144 | normal | 4        | 10.1.20 (inbuilt)       | on        | zlib       | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 145 | normal | 32       | 10.1.20 (inbuilt)       | -         | zlib       | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 146 | normal | 32       | 10.1.20 (inbuilt)       | on        | zlib       | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 147 | normal | 32       | 10.1.20 (inbuilt)       | on        | zlib       | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 148 | normal | 32       | 10.1.20 (inbuilt)       | -         | zlib       | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 149 | normal | 32       | 10.1.20 (inbuilt)       | on        | zlib       | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 150 | normal | 32       | 10.1.20 (inbuilt)       | -         | zlib       | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 151 | normal | 32       | 10.1.20 (inbuilt)       | on        | zlib       | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 152 | normal | 32       | 10.1.20 (inbuilt)       | -         | zlib       | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 153 | normal | 32       | 10.1.20 (inbuilt)       | on        | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 154 | normal | 32       | 10.1.20 (inbuilt)       | on        | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 155 | normal | 32       | 10.1.20 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |                                                          |
| 156 | normal | 32       | 10.1.20 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |                                                          |
| 157 | normal | 32       | 10.1.20 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 158 | normal | 32       | 10.1.20 (inbuilt)       | -         | -          | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |
| 159 | normal | 32       | 10.1.20 (inbuilt)       | on        | -          | => | 10.2.5 (inbuilt) | -         | zlib       | -        | OK     |                                                          |
| 160 | normal | 32       | 10.1.20 (inbuilt)       | on        | -          | => | 10.2.5 (inbuilt) | on        | zlib       | -        | OK     |                                                          |

## Upgrade from MySQL 5.6

### Tested revision

b56262f69677fdb158b3d19dd8848e5802b2dd27

### Test date

2017-03-28 14:00:57

### Summary (PASS)

All tests passed

### Details

| # | type   | pagesize | OLD version      | encrypted | compressed |    | NEW version      | encrypted | compressed | readonly | result | notes |
| - | ------ | -------- | ---------------- | --------- | ---------- | -- | ---------------- | --------- | ---------- | -------- | ------ | ----- |
| 1 | normal | 16       | 5.6.35 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 2 | normal | 16       | 5.6.35 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |
| 3 | normal | 4        | 5.6.35 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |
| 4 | normal | 4        | 5.6.35 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 5 | normal | 8        | 5.6.35 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 6 | normal | 8        | 5.6.35 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |

## Upgrade from MySQL 5.7

### Tested revision

b56262f69677fdb158b3d19dd8848e5802b2dd27

### Test date

2017-03-28 23:04:16

### Summary (PASS)

All tests passed

### Details

| #  | type   | pagesize | OLD version      | encrypted | compressed |    | NEW version      | encrypted | compressed | readonly | result | notes |
| -- | ------ | -------- | ---------------- | --------- | ---------- | -- | ---------------- | --------- | ---------- | -------- | ------ | ----- |
| 1  | normal | 8        | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 2  | normal | 8        | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |
| 3  | normal | 64       | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 4  | normal | 64       | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |
| 5  | normal | 16       | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |
| 6  | normal | 16       | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 7  | normal | 32       | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 8  | normal | 32       | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |
| 9  | normal | 4        | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 10 | normal | 4        | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |
| 11 | crash  | 64       | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 12 | crash  | 64       | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |
| 13 | crash  | 16       | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |
| 14 | crash  | 16       | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 15 | crash  | 8        | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 16 | crash  | 8        | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |
| 17 | crash  | 32       | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |
| 18 | crash  | 32       | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 19 | crash  | 4        | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |
| 20 | crash  | 4        | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 21 | normal | 32       | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 22 | normal | 32       | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |
| 23 | normal | 4        | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 24 | normal | 4        | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |
| 25 | normal | 16       | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 26 | normal | 16       | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |
| 27 | normal | 64       | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |
| 28 | normal | 64       | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 29 | normal | 8        | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | -         | -          | -        | OK     |       |
| 30 | normal | 8        | 5.7.17 (inbuilt) | -         | -          | => | 10.2.5 (inbuilt) | on        | -          | -        | OK     |       |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
