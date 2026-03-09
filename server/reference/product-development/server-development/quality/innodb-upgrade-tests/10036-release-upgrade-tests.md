---
description: >-
  Dedicated testing results for verifying that the InnoDB storage engine can
  safely upgrade data from older server versions.
---

# 10.0.36 Release Upgrade Tests

### Tested revision

e023f9a4d5a620b54d7f7132567150d80b630692

### Test date

2018-08-05 19:08:18

### Summary

Two tests failed due to problems in previous versions (unrelated to the release)

### Details

| type            | pagesize | OLD version       | file format | encrypted | compressed |    | NEW version       | file format | encrypted | compressed | readonly | result | notes         |
| --------------- | -------- | ----------------- | ----------- | --------- | ---------- | -- | ----------------- | ----------- | --------- | ---------- | -------- | ------ | ------------- |
| undo-recovery   | 4        | 10.0.36 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| undo-recovery   | 8        | 10.0.36 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| undo-recovery   | 16       | 10.0.36 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| recovery        | 16       | 10.0.36 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| recovery        | 4        | 10.0.36 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| recovery        | 8        | 10.0.36 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| crash           | 4        | 10.0.35 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| crash           | 8        | 10.0.35 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| crash           | 16       | 10.0.35 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| normal          | 16       | 10.0.35 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| normal          | 4        | 10.0.35 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| normal          | 8        | 10.0.35 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| undo            | 16       | 10.0.35 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| undo            | 4        | 10.0.35 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| undo            | 8        | 10.0.35 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| crash           | 4        | 10.0.14 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| crash           | 8        | 10.0.14 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| crash           | 16       | 10.0.14 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| normal          | 16       | 10.0.14 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| normal          | 4        | 10.0.14 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| normal          | 8        | 10.0.14 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| undo            | 16       | 10.0.18 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| undo            | 4        | 10.0.18 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| undo            | 8        | 10.0.18 (inbuilt) |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | FAIL   | TEST\_FAILURE |
| crash           | 4        | 5.6.41 (inbuilt)  |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| crash           | 8        | 5.6.41 (inbuilt)  |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| crash           | 16       | 5.6.41 (inbuilt)  |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| normal          | 16       | 5.6.41 (inbuilt)  |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| normal          | 4        | 5.6.41 (inbuilt)  |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| normal          | 8        | 5.6.41 (inbuilt)  |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| undo            | 16       | 5.6.41 (inbuilt)  |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | FAIL   | TEST\_FAILURE |
| undo            | 4        | 5.6.41 (inbuilt)  |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| undo            | 8        | 5.6.41 (inbuilt)  |             | -         | -          | => | 10.0.36 (inbuilt) |             | -         | -          | -        | OK     |               |
| crash-downgrade | 4        | 10.0.36 (inbuilt) |             | -         | -          | => | 10.0.35 (inbuilt) |             | -         | -          | -        | OK     |               |
| crash-downgrade | 8        | 10.0.36 (inbuilt) |             | -         | -          | => | 10.0.35 (inbuilt) |             | -         | -          | -        | OK     |               |
| crash-downgrade | 16       | 10.0.36 (inbuilt) |             | -         | -          | => | 10.0.35 (inbuilt) |             | -         | -          | -        | OK     |               |
| downgrade       | 16       | 10.0.36 (inbuilt) |             | -         | -          | => | 10.0.35 (inbuilt) |             | -         | -          | -        | OK     |               |
| downgrade       | 4        | 10.0.36 (inbuilt) |             | -         | -          | => | 10.0.35 (inbuilt) |             | -         | -          | -        | OK     |               |
| downgrade       | 8        | 10.0.36 (inbuilt) |             | -         | -          | => | 10.0.35 (inbuilt) |             | -         | -          | -        | OK     |               |
| crash-downgrade | 4        | 10.0.36 (inbuilt) |             | -         | -          | => | 10.0.14 (inbuilt) |             | -         | -          | -        | OK     |               |
| crash-downgrade | 8        | 10.0.36 (inbuilt) |             | -         | -          | => | 10.0.14 (inbuilt) |             | -         | -          | -        | OK     |               |
| crash-downgrade | 16       | 10.0.36 (inbuilt) |             | -         | -          | => | 10.0.14 (inbuilt) |             | -         | -          | -        | OK     |               |
| downgrade       | 16       | 10.0.36 (inbuilt) |             | -         | -          | => | 10.0.14 (inbuilt) |             | -         | -          | -        | OK     |               |
| downgrade       | 4        | 10.0.36 (inbuilt) |             | -         | -          | => | 10.0.14 (inbuilt) |             | -         | -          | -        | OK     |               |
| downgrade       | 8        | 10.0.36 (inbuilt) |             | -         | -          | => | 10.0.14 (inbuilt) |             | -         | -          | -        | OK     |               |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
