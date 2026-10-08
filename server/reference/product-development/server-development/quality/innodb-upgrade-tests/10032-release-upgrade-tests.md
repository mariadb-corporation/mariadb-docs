---
description: >-
  Dedicated testing results for verifying that the InnoDB storage engine can
  safely upgrade data from older server versions.
---

# 10.0.32 Release Upgrade Tests

## Upgrade from 10.0

### Tested revision

d85d6c9c416aab85f1ded344a5b870d4cc56f9f6

### Test date

2017-08-03 19:25:53

### Summary (PASS)

All tests passed

### Details

| #  | type   | pagesize | OLD version       | file format | encrypted | compressed |    | NEW version       | file format | encrypted | compressed | readonly | result | notes |
| -- | ------ | -------- | ----------------- | ----------- | --------- | ---------- | -- | ----------------- | ----------- | --------- | ---------- | -------- | ------ | ----- |
| 1  | crash  | 4        | 10.0.28 (inbuilt) | Antelope    | -         | -          | => | 10.0.32 (inbuilt) | Antelope    | -         | -          | -        | OK     |       |
| 2  | crash  | 4        | 10.0.28 (inbuilt) | Barracuda   | -         | -          | => | 10.0.32 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| 3  | crash  | 8        | 10.0.28 (inbuilt) | Antelope    | -         | -          | => | 10.0.32 (inbuilt) | Antelope    | -         | -          | -        | OK     |       |
| 4  | crash  | 8        | 10.0.28 (inbuilt) | Barracuda   | -         | -          | => | 10.0.32 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| 5  | crash  | 16       | 10.0.28 (inbuilt) | Antelope    | -         | -          | => | 10.0.32 (inbuilt) | Antelope    | -         | -          | -        | OK     |       |
| 6  | crash  | 16       | 10.0.28 (inbuilt) | Barracuda   | -         | -          | => | 10.0.32 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| 7  | normal | 4        | 10.0.28 (inbuilt) | Barracuda   | -         | -          | => | 10.0.32 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| 8  | normal | 4        | 10.0.28 (inbuilt) | Antelope    | -         | -          | => | 10.0.32 (inbuilt) | Antelope    | -         | -          | -        | OK     |       |
| 9  | normal | 8        | 10.0.28 (inbuilt) | Antelope    | -         | -          | => | 10.0.32 (inbuilt) | Antelope    | -         | -          | -        | OK     |       |
| 10 | normal | 8        | 10.0.28 (inbuilt) | Barracuda   | -         | -          | => | 10.0.32 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| 11 | normal | 16       | 10.0.28 (inbuilt) | Barracuda   | -         | -          | => | 10.0.32 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| 12 | normal | 16       | 10.0.28 (inbuilt) | Antelope    | -         | -          | => | 10.0.32 (inbuilt) | Antelope    | -         | -          | -        | OK     |       |

## Upgrade from MySQL 5.6

### Tested revision

d85d6c9c416aab85f1ded344a5b870d4cc56f9f6

### Test date

2017-08-03 19:45:21

### Summary (PASS)

All tests passed

### Details

| # | type   | pagesize | OLD version      | file format | encrypted | compressed |    | NEW version       | file format | encrypted | compressed | readonly | result | notes |
| - | ------ | -------- | ---------------- | ----------- | --------- | ---------- | -- | ----------------- | ----------- | --------- | ---------- | -------- | ------ | ----- |
| 1 | normal | 16       | 5.6.35 (inbuilt) | Antelope    | -         | -          | => | 10.0.32 (inbuilt) | Antelope    | -         | -          | -        | OK     |       |
| 2 | normal | 16       | 5.6.35 (inbuilt) | Barracuda   | -         | -          | => | 10.0.32 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| 3 | normal | 4        | 5.6.35 (inbuilt) | Barracuda   | -         | -          | => | 10.0.32 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| 4 | normal | 4        | 5.6.35 (inbuilt) | Antelope    | -         | -          | => | 10.0.32 (inbuilt) | Antelope    | -         | -          | -        | OK     |       |
| 5 | normal | 8        | 5.6.35 (inbuilt) | Antelope    | -         | -          | => | 10.0.32 (inbuilt) | Antelope    | -         | -          | -        | OK     |       |
| 6 | normal | 8        | 5.6.35 (inbuilt) | Barracuda   | -         | -          | => | 10.0.32 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |

## Crash Recovery

### Tested revision

d85d6c9c416aab85f1ded344a5b870d4cc56f9f6

### Test date

2017-08-03 19:55:23

### Summary (PASS)

All tests passed

### Details

| # | type  | pagesize | OLD version       | file format | encrypted | compressed |    | NEW version       | file format | encrypted | compressed | readonly | result | notes |
| - | ----- | -------- | ----------------- | ----------- | --------- | ---------- | -- | ----------------- | ----------- | --------- | ---------- | -------- | ------ | ----- |
| 1 | crash | 16       | 10.0.32 (inbuilt) | Antelope    | -         | -          | => | 10.0.32 (inbuilt) | Antelope    | -         | -          | -        | OK     |       |
| 2 | crash | 16       | 10.0.32 (inbuilt) | Barracuda   | -         | -          | => | 10.0.32 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| 3 | crash | 4        | 10.0.32 (inbuilt) | Barracuda   | -         | -          | => | 10.0.32 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| 4 | crash | 4        | 10.0.32 (inbuilt) | Antelope    | -         | -          | => | 10.0.32 (inbuilt) | Antelope    | -         | -          | -        | OK     |       |
| 5 | crash | 8        | 10.0.32 (inbuilt) | Antelope    | -         | -          | => | 10.0.32 (inbuilt) | Antelope    | -         | -          | -        | OK     |       |
| 6 | crash | 8        | 10.0.32 (inbuilt) | Barracuda   | -         | -          | => | 10.0.32 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
