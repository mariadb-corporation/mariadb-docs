---
description: >-
  Dedicated testing results for verifying that the InnoDB storage engine can
  safely upgrade data from older server versions.
---

# 10.1.36 Release Upgrade Tests

### Tested revision

38e5dc0f772daecca1d2681885d3d85414eb6826

### Test date

2018-10-03 11:54:43

### Summary

Tests passed

### Details

| type          | pagesize | OLD version       | file format | encrypted | compressed |    | NEW version       | file format | encrypted | compressed | readonly | result | notes |
| ------------- | -------- | ----------------- | ----------- | --------- | ---------- | -- | ----------------- | ----------- | --------- | ---------- | -------- | ------ | ----- |
| recovery      | 16       | 10.1.36 (inbuilt) | Barracuda   | on        | -          | => | 10.1.36 (inbuilt) | Barracuda   | on        | -          | -        | OK     |       |
| recovery      | 16       | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| recovery      | 4        | 10.1.36 (inbuilt) | Barracuda   | on        | -          | => | 10.1.36 (inbuilt) | Barracuda   | on        | -          | -        | OK     |       |
| recovery      | 4        | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| recovery      | 32       | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| recovery      | 32       | 10.1.36 (inbuilt) | Barracuda   | on        | -          | => | 10.1.36 (inbuilt) | Barracuda   | on        | -          | -        | OK     |       |
| recovery      | 64       | 10.1.36 (inbuilt) | Barracuda   | on        | -          | => | 10.1.36 (inbuilt) | Barracuda   | on        | -          | -        | OK     |       |
| recovery      | 64       | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| recovery      | 8        | 10.1.36 (inbuilt) | Barracuda   | on        | -          | => | 10.1.36 (inbuilt) | Barracuda   | on        | -          | -        | OK     |       |
| recovery      | 8        | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| recovery      | 16       | 10.1.36 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| recovery      | 16       | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | -        | OK     |       |
| recovery      | 4        | 10.1.36 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| recovery      | 4        | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | -        | OK     |       |
| recovery      | 32       | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | -        | OK     |       |
| recovery      | 32       | 10.1.36 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| recovery      | 64       | 10.1.36 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| recovery      | 64       | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | -        | OK     |       |
| recovery      | 8        | 10.1.36 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| recovery      | 8        | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | -        | OK     |       |
| undo-recovery | 16       | 10.1.36 (inbuilt) | Barracuda   | on        | -          | => | 10.1.36 (inbuilt) | Barracuda   | on        | -          | -        | OK     |       |
| undo-recovery | 4        | 10.1.36 (inbuilt) | Barracuda   | on        | -          | => | 10.1.36 (inbuilt) | Barracuda   | on        | -          | -        | OK     |       |
| undo-recovery | 32       | 10.1.36 (inbuilt) | Barracuda   | on        | -          | => | 10.1.36 (inbuilt) | Barracuda   | on        | -          | -        | OK     |       |
| undo-recovery | 64       | 10.1.36 (inbuilt) | Barracuda   | on        | -          | => | 10.1.36 (inbuilt) | Barracuda   | on        | -          | -        | OK     |       |
| undo-recovery | 8        | 10.1.36 (inbuilt) | Barracuda   | on        | -          | => | 10.1.36 (inbuilt) | Barracuda   | on        | -          | -        | OK     |       |
| undo-recovery | 16       | 10.1.36 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| undo-recovery | 4        | 10.1.36 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| undo-recovery | 32       | 10.1.36 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| undo-recovery | 64       | 10.1.36 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| undo-recovery | 8        | 10.1.36 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| undo-recovery | 16       | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| undo-recovery | 4        | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| undo-recovery | 32       | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| undo-recovery | 64       | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| undo-recovery | 8        | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| undo-recovery | 16       | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | -        | OK     |       |
| undo-recovery | 4        | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | -        | OK     |       |
| undo-recovery | 32       | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | -        | OK     |       |
| undo-recovery | 64       | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | -        | OK     |       |
| undo-recovery | 8        | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | -        | OK     |       |
| normal        | 16       | 10.1.35 (inbuilt) | Barracuda   | on        | -          | => | 10.1.36 (inbuilt) | Barracuda   | on        | -          | -        | OK     |       |
| normal        | 16       | 10.1.35 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| normal        | 4        | 10.1.35 (inbuilt) | Barracuda   | on        | -          | => | 10.1.36 (inbuilt) | Barracuda   | on        | -          | -        | OK     |       |
| normal        | 4        | 10.1.35 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| normal        | 32       | 10.1.35 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| normal        | 32       | 10.1.35 (inbuilt) | Barracuda   | on        | -          | => | 10.1.36 (inbuilt) | Barracuda   | on        | -          | -        | OK     |       |
| normal        | 64       | 10.1.35 (inbuilt) | Barracuda   | on        | -          | => | 10.1.36 (inbuilt) | Barracuda   | on        | -          | -        | OK     |       |
| normal        | 64       | 10.1.35 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| normal        | 8        | 10.1.35 (inbuilt) | Barracuda   | on        | -          | => | 10.1.36 (inbuilt) | Barracuda   | on        | -          | -        | OK     |       |
| normal        | 8        | 10.1.35 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| normal        | 16       | 10.1.35 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| normal        | 16       | 10.1.35 (inbuilt) | Barracuda   | -         | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | -        | OK     |       |
| normal        | 4        | 10.1.35 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| normal        | 4        | 10.1.35 (inbuilt) | Barracuda   | -         | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | -        | OK     |       |
| normal        | 32       | 10.1.35 (inbuilt) | Barracuda   | -         | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | -        | OK     |       |
| normal        | 32       | 10.1.35 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| normal        | 64       | 10.1.35 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| normal        | 64       | 10.1.35 (inbuilt) | Barracuda   | -         | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | -        | OK     |       |
| normal        | 8        | 10.1.35 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| normal        | 8        | 10.1.35 (inbuilt) | Barracuda   | -         | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | -        | OK     |       |
| crash         | 16       | 10.1.35 (inbuilt) | Barracuda   | on        | -          | => | 10.1.36 (inbuilt) | Barracuda   | on        | -          | -        | OK     |       |
| crash         | 16       | 10.1.35 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| crash         | 4        | 10.1.35 (inbuilt) | Barracuda   | on        | -          | => | 10.1.36 (inbuilt) | Barracuda   | on        | -          | -        | OK     |       |
| crash         | 4        | 10.1.35 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| crash         | 32       | 10.1.35 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| crash         | 32       | 10.1.35 (inbuilt) | Barracuda   | on        | -          | => | 10.1.36 (inbuilt) | Barracuda   | on        | -          | -        | OK     |       |
| crash         | 64       | 10.1.35 (inbuilt) | Barracuda   | on        | -          | => | 10.1.36 (inbuilt) | Barracuda   | on        | -          | -        | OK     |       |
| crash         | 64       | 10.1.35 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| crash         | 8        | 10.1.35 (inbuilt) | Barracuda   | on        | -          | => | 10.1.36 (inbuilt) | Barracuda   | on        | -          | -        | OK     |       |
| crash         | 8        | 10.1.35 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| crash         | 16       | 10.1.35 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| crash         | 16       | 10.1.35 (inbuilt) | Barracuda   | -         | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | -        | OK     |       |
| crash         | 4        | 10.1.35 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| crash         | 4        | 10.1.35 (inbuilt) | Barracuda   | -         | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | -        | OK     |       |
| crash         | 32       | 10.1.35 (inbuilt) | Barracuda   | -         | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | -        | OK     |       |
| crash         | 32       | 10.1.35 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| crash         | 64       | 10.1.35 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| crash         | 64       | 10.1.35 (inbuilt) | Barracuda   | -         | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | -        | OK     |       |
| crash         | 8        | 10.1.35 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| crash         | 8        | 10.1.35 (inbuilt) | Barracuda   | -         | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | -         | zlib       | -        | OK     |       |
| undo          | 16       | 10.1.35 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| undo          | 4        | 10.1.35 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| undo          | 32       | 10.1.35 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| undo          | 64       | 10.1.35 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| undo          | 8        | 10.1.35 (inbuilt) | Barracuda   | -         | -          | => | 10.1.36 (inbuilt) | Barracuda   | -         | -          | -        | OK     |       |
| undo          | 16       | 10.1.35 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| undo          | 4        | 10.1.35 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| undo          | 32       | 10.1.35 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| undo          | 64       | 10.1.35 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| undo          | 8        | 10.1.35 (inbuilt) | Barracuda   | on        | zlib       | => | 10.1.36 (inbuilt) | Barracuda   | on        | zlib       | -        | OK     |       |
| normal        | 4        | 10.0.36 (inbuilt) |             | -         | -          | => | 10.1.36 (inbuilt) |             | -         | -          | -        | OK     |       |
| normal        | 8        | 10.0.36 (inbuilt) |             | -         | -          | => | 10.1.36 (inbuilt) |             | -         | -          | -        | OK     |       |
| normal        | 16       | 10.0.36 (inbuilt) |             | -         | -          | => | 10.1.36 (inbuilt) |             | -         | -          | -        | OK     |       |
| normal        | 16       | 10.0.36 (inbuilt) |             | -         | -          | => | 10.1.36 (inbuilt) |             | on        | -          | -        | OK     |       |
| normal        | 4        | 10.0.36 (inbuilt) |             | -         | -          | => | 10.1.36 (inbuilt) |             | on        | -          | -        | OK     |       |
| normal        | 8        | 10.0.36 (inbuilt) |             | -         | -          | => | 10.1.36 (inbuilt) |             | on        | -          | -        | OK     |       |
| crash         | 4        | 10.0.36 (inbuilt) |             | -         | -          | => | 10.1.36 (inbuilt) |             | -         | -          | -        | OK     |       |
| crash         | 8        | 10.0.36 (inbuilt) |             | -         | -          | => | 10.1.36 (inbuilt) |             | -         | -          | -        | OK     |       |
| crash         | 16       | 10.0.36 (inbuilt) |             | -         | -          | => | 10.1.36 (inbuilt) |             | -         | -          | -        | OK     |       |
| crash         | 16       | 10.0.36 (inbuilt) |             | -         | -          | => | 10.1.36 (inbuilt) |             | on        | -          | -        | OK     |       |
| crash         | 4        | 10.0.36 (inbuilt) |             | -         | -          | => | 10.1.36 (inbuilt) |             | on        | -          | -        | OK     |       |
| crash         | 8        | 10.0.36 (inbuilt) |             | -         | -          | => | 10.1.36 (inbuilt) |             | on        | -          | -        | OK     |       |
| undo          | 16       | 10.0.36 (inbuilt) |             | -         | -          | => | 10.1.36 (inbuilt) |             | -         | -          | -        | OK     |       |
| undo          | 4        | 10.0.36 (inbuilt) |             | -         | -          | => | 10.1.36 (inbuilt) |             | -         | -          | -        | OK     |       |
| undo          | 8        | 10.0.36 (inbuilt) |             | -         | -          | => | 10.1.36 (inbuilt) |             | -         | -          | -        | OK     |       |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
