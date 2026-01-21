---
description: >-
  Dedicated testing results for verifying that the InnoDB storage engine can
  safely upgrade data from older server versions.
---

# 10.0.34 Release Upgrade Tests

### Tested revision

d01dbe66a8bf9cb6031f95159c49100f9299a768

### Test date

2018-02-01 07:13:41

### Summary

All tests passed

### Details

| type            | pagesize | OLD version       | file format | encrypted | compressed |    | NEW version       | file format | encrypted | compressed | readonly | result | notes |
| --------------- | -------- | ----------------- | ----------- | --------- | ---------- | -- | ----------------- | ----------- | --------- | ---------- | -------- | ------ | ----- |
| undo-recovery   | 4        | 10.0.34 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| undo-recovery   | 8        | 10.0.34 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| undo-recovery   | 16       | 10.0.34 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| recovery        | 16       | 10.0.34 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| recovery        | 4        | 10.0.34 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| recovery        | 8        | 10.0.34 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| crash           | 4        | 10.0.33 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| crash           | 8        | 10.0.33 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| crash           | 16       | 10.0.33 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| normal          | 16       | 10.0.33 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| normal          | 4        | 10.0.33 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| normal          | 8        | 10.0.33 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| undo            | 16       | 10.0.33 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| undo            | 4        | 10.0.33 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| undo            | 8        | 10.0.33 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| crash           | 4        | 10.0.14 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| crash           | 8        | 10.0.14 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| crash           | 16       | 10.0.14 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| normal          | 16       | 10.0.14 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| normal          | 4        | 10.0.14 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| normal          | 8        | 10.0.14 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| undo            | 16       | 10.0.18 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| undo            | 4        | 10.0.18 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| undo            | 8        | 10.0.18 (inbuilt) |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| crash           | 4        | 5.6.39 (inbuilt)  |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| crash           | 8        | 5.6.39 (inbuilt)  |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| crash           | 16       | 5.6.39 (inbuilt)  |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| normal          | 16       | 5.6.39 (inbuilt)  |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| normal          | 4        | 5.6.39 (inbuilt)  |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| normal          | 8        | 5.6.39 (inbuilt)  |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| undo            | 16       | 5.6.39 (inbuilt)  |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| undo            | 4        | 5.6.39 (inbuilt)  |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| undo            | 8        | 5.6.39 (inbuilt)  |             | -         | -          | => | 10.0.34 (inbuilt) |             | -         | -          | -        | OK     |       |
| crash-downgrade | 4        | 10.0.34 (inbuilt) |             | -         | -          | => | 10.0.33 (inbuilt) |             | -         | -          | -        | OK     |       |
| crash-downgrade | 8        | 10.0.34 (inbuilt) |             | -         | -          | => | 10.0.33 (inbuilt) |             | -         | -          | -        | OK     |       |
| crash-downgrade | 16       | 10.0.34 (inbuilt) |             | -         | -          | => | 10.0.33 (inbuilt) |             | -         | -          | -        | OK     |       |
| downgrade       | 16       | 10.0.34 (inbuilt) |             | -         | -          | => | 10.0.33 (inbuilt) |             | -         | -          | -        | OK     |       |
| downgrade       | 4        | 10.0.34 (inbuilt) |             | -         | -          | => | 10.0.33 (inbuilt) |             | -         | -          | -        | OK     |       |
| downgrade       | 8        | 10.0.34 (inbuilt) |             | -         | -          | => | 10.0.33 (inbuilt) |             | -         | -          | -        | OK     |       |
| crash-downgrade | 4        | 10.0.34 (inbuilt) |             | -         | -          | => | 10.0.14 (inbuilt) |             | -         | -          | -        | OK     |       |
| crash-downgrade | 8        | 10.0.34 (inbuilt) |             | -         | -          | => | 10.0.14 (inbuilt) |             | -         | -          | -        | OK     |       |
| crash-downgrade | 16       | 10.0.34 (inbuilt) |             | -         | -          | => | 10.0.14 (inbuilt) |             | -         | -          | -        | OK     |       |
| downgrade       | 16       | 10.0.34 (inbuilt) |             | -         | -          | => | 10.0.14 (inbuilt) |             | -         | -          | -        | OK     |       |
| downgrade       | 4        | 10.0.34 (inbuilt) |             | -         | -          | => | 10.0.14 (inbuilt) |             | -         | -          | -        | OK     |       |
| downgrade       | 8        | 10.0.34 (inbuilt) |             | -         | -          | => | 10.0.14 (inbuilt) |             | -         | -          | -        | OK     |       |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
