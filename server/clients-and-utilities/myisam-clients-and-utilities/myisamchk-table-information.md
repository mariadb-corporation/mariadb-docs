# myisamchk Table Information

[myisamchk](myisamchk.md) can be used to obtain information about MyISAM tables, particularly with the _-d_, _-e_, _-i_ and _-v_ options.

Common options for gathering information include:

* myisamchk -d
* myisamchk -dv
* myisamchk -dvv
* myisamchk -ei
* myisamchk -eiv

The _-d_ option returns a short description of the table and its keys. Running the option while the table is being updated, and with external locking disabled, may result in an error, but no damage is done to the table. Each extra _v_ adds more output. _-e_ checks the table thoroughly (but slowly), and the _-i_ options adds statistical information,

## -dvv output

The following table describes the output from the running myisamchk with the _-dvv_ option:

| Heading             | Description                                                                                                                                                                                                             |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MyISAM file         | Name and path of the MyISAM index file (without the extension)                                                                                                                                                          |
| Record format       | [Storage format](../../server-usage/storage-engines/myisam-storage-engine/myisam-storage-formats.md). One of packed (dynamic), fixed or compressed.                                                                     |
| Character set     | Default [character set](../../reference/data-types/string-data-types/character-sets/) for the table.                                                                                                                    |
| File-version        | Always 1.                                                                                                                                                                                                               |
| Creation time       | Time the data file was created                                                                                                                                                                                          |
| Recover time        | Most recent time the file was reconstructed.                                                                                                                                                                            |
| Status              | Table status. One or more of analyzed, changed, crashed, open, optimized keys and sorted index pages.                                                                                                                   |
| Auto increment key  | Index number of the table's [auto-increment](../../reference/data-types/auto_increment.md) column. Not shown if no auto-increment column exists.                                                                        |
| Last value          | Most recently generated auto-increment value. Not shown if no auto-increment column exists.                                                                                                                             |
| Data records        | Number of records in the table.                                                                                                                                                                                         |
| Deleted blocks      | Number of deleted blocks that are still reserving space. Use [OPTIMIZE TABLE](../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md) to defragment.                                      |
| Datafile parts      | For [dynamic tables](../../server-usage/storage-engines/myisam-storage-engine/myisam-storage-formats.md), the number of data blocks. If the table is optimized, this will match the number of data records.             |
| Deleted data        | Number of bytes of unreclaimed deleted data, Use [OPTIMIZE TABLE](../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md) to reclaim the space.                                           |
| Datafile pointer    | Size in bytes of the data file pointer. The size of the data file pointer, in bytes.                                                                                                                                    |
| Keyfile pointer     | Size in bytes of the index file pointer.                                                                                                                                                                                |
| Max datafile length | Maximum length, in bytes, that the data file could become.                                                                                                                                                              |
| Max keyfile length  | Maximum length, in bytes, that the index file could become.                                                                                                                                                             |
| Recordlength        | Space, in bytes, that each row takes.                                                                                                                                                                                   |
| table description   | Description of all indexes in the table, followed by all columns                                                                                                                                                        |
| Key                 | Index number, starting with one. If not shown, the index is part of a multiple-column index.                                                                                                                            |
| Start               | Where the index part starts in the row.                                                                                                                                                                                 |
| Len                 | Length of the index or index part. The length of a multiple-column index is the sum of the component lengths. Indexes of string columns is shorter than the full column length if only a string prefix is indexed. |
| Index               | Whether an index value is unique or not. Either multip. or unique.                                                                                                                                                      |
| Type                | Data type of the index of index part.                                                                                                                                                                                   |
| Rec/key             | Record of the number of rows per value for the index or index part. Used by the optimizer to calculate query plans. Can be updated with [myisamchk-a](myisamchk.md). If not present, defaults to 30.                    |
| Root                | Root index block address.                                                                                                                                                                                               |
| Blocksize           | Index block size, in bytes.                                                                                                                                                                                             |
| Field               | Column number, starting with one. The first line will contain the position and number of bytes used to store NULL flags, if any (see Nullpos and Nullbit, below).                                                       |
| Start               | Column's byte position within the table row.                                                                                                                                                                            |
| Length              | Column length, in bytes.                                                                                                                                                                                                |
| Nullpos             | Byte containing the flag for NULL values. Empty if column cannot be NULL.                                                                                                                                               |
| Nullbit             | Bit containing the flag for NULL values. Empty if column cannot be NULL.                                                                                                                                                |
| Type                | Data type - see the table below for a list of possible values.                                                                                                                                                          |
| Huff tree           | Only present for packed tables, contains the Huffman tree number associated with the column.                                                                                                                            |
| Bits                | Only present for packed tables, contains the number of bits used in the Huffman tree.                                                                                                                                   |

| Data type                | Description                                                                              |
| ------------------------ | ---------------------------------------------------------------------------------------- |
| constant                 | All rows contain the same value.                                                         |
| no endspace              | No endspace is stored.                                                                   |
| no endspace, not\_always | No endspace is stored, and endspace compression is not always performed for all values.  |
| no endspace, no empty    | No endspace is stored, no empty values are stored.                                       |
| table-lookup             | Column was converted to an [ENUM](../../reference/data-types/string-data-types/enum.md). |
| zerofill(N)              | Most significant N bytes of the value are not stored, as they are always zero.           |
| no zeros                 | Zeros are not stored.                                                                    |
| always zero              | Zero values are stored with one bit.                                                     |

## -eiv output

The following table describes the output from the running myisamchk with the _-eiv_ option:

| Heading          | Description                                                                                                                                                                                                                   |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data records     | Number of records in the table.                                                                                                                                                                                               |
| Deleted blocks   | Number of deleted blocks that are still reserving space. Use [OPTIMIZE TABLE](../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md) to defragment.                                            |
| Key              | Index number, starting with one.                                                                                                                                                                                              |
| Keyblocks used   | Percentage of the keyblocks that are used. Percentages is higher for optimized tables.                                                                                                                                   |
| Packed           | Percentage space saved from packing key values with a common suffix.                                                                                                                                                          |
| Max levels       | Depth of the [b-tree index](../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/storage-engine-index-types.md#b-tree-indexes) for the key. Larger tables and longer key values result in higher values. |
| Records          | Number of records in the table.                                                                                                                                                                                               |
| M.recordlength   | Average row length. For fixed rows, is the actual length of each row.                                                                                                                                                    |
| Packed           | Percentage saving from stripping spaces from the end of strings.                                                                                                                                                              |
| Recordspace used | Percentage of the data file used.                                                                                                                                                                                             |
| Empty space      | Percentage of the data file unused.                                                                                                                                                                                           |
| Blocks/Record    | Average number of blocks per record. Values higher than one indicate fragmentation. Use [OPTIMIZE TABLE](../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md) to defragment.                 |
| Recordblocks     | Number of used blocks. Will match the number of rows for fixed or optimized tables.                                                                                                                                           |
| Deleteblocks     | Number of deleted blocks                                                                                                                                                                                                      |
| Recorddata       | Used bytes in the data file.                                                                                                                                                                                                  |
| Deleted data     | Unused bytes in the data file.                                                                                                                                                                                                |
| Lost space       | Total bytes lost, such as when a row is updated to a shorter length.                                                                                                                                                          |
| Linkdata         | Sum of the bytes used for pointers linking disconnected blocks. Each is four to seven bytes in size.                                                                                                                          |

## Examples

```
myisamchk -d /var/lib/mysql/test/posts

MyISAM file:         /var/lib/mysql/test/posts
Record format:       Compressed
Character set:       utf8mb4_unicode_ci (224)
Data records:                 1680  Deleted blocks:                 0
Recordlength:                 2758
Using only keys '0' of 5 possibly keys

table description:
Key Start Len Index   Type
1   1     8   unique  ulonglong            
2   2265  80  multip. varchar prefix       
    63    80          varchar              
    17    5           binary               
    1     8           ulonglong            
3   1231  8   multip. ulonglong            
4   9     8   multip. ulonglong            
5   387   764 multip. ? prefix
```

```
myisamchk -dvv /var/lib/mysql/test/posts

MyISAM file:         /var/lib/mysql/test/posts
Record format:       Compressed
Character set:       utf8mb4_unicode_ci (224)
File-version:        1
Creation time:       2015-08-10 16:26:54
Recover time:        2015-08-10 16:26:54
Status:              checked,analyzed,optimized keys
Auto increment key:              1  Last value:                  1811
Checksum:               2299272165
Data records:                 1680  Deleted blocks:                 0
Datafile parts:               1680  Deleted data:                   0
Datafile pointer (bytes):        6  Keyfile pointer (bytes):        6
Datafile length:           4298092  Keyfile length:            156672
Max datafile length: 281474976710654  Max keyfile length: 288230376151710719
Recordlength:                 2758
Using only keys '0' of 5 possibly keys

table description:
Key Start Len Index   Type                     Rec/key         Root  Blocksize
1   1     8   unique  ulonglong                      1                    1024
2   2265  80  multip. varchar prefix               336                    1024
    63    80          varchar                      187
    17    5           binary                         1
    1     8           ulonglong                      1
3   1231  8   multip. ulonglong                     10                    1024
4   9     8   multip. ulonglong                    840                    1024
5   387   764 multip. ? prefix                       1                    4096

Field Start Length Nullpos Nullbit Type                         Huff tree  Bits
1     1     8                      zerofill(6)                          1     9
2     9     8                      zerofill(7)                          1     9
3     17    5                                                           1     9
4     22    5                                                           1     9
5     27    12                     blob                                 2     9
6     39    10                     blob                                 3     9
7     49    4                      always zero                          1     9
8     53    10                     blob                                 1     9
9     63    81                     varchar                              4     9
10    144   81                     varchar                              5     5
11    225   81                     varchar                              5     5
12    306   81                     varchar                              1     9
13    387   802                    varchar                              6     9
14    1189  10                     blob                                 1     9
15    1199  10                     blob                                 7     9
16    1209  5                                                           1     9
17    1214  5                                                           1     9
18    1219  12                     blob                                 1     9
19    1231  8                      no zeros, zerofill(6)                1     9
20    1239  1022                   varchar                              7     9
21    2261  4                      always zero                          1     9
22    2265  81                     varchar                              8     8
23    2346  402                    varchar                              2     9
24    2748  8                      no zeros, zerofill(7)                1     9
```

```
myisamchk -eiv /var/lib/mysql/test/posts
Checking MyISAM file: /var/lib/mysql/test/posts
Data records:    1680   Deleted blocks:       0
- check file-size
- check record delete-chain
No recordlinks
- check key delete-chain
block_size 1024:
block_size 2048:
block_size 3072:
block_size 4096:
- check index reference
- check data record references index: 1
Key:  1:  Keyblocks used:  92%  Packed:    0%  Max levels:  2
- check data record references index: 2
Key:  2:  Keyblocks used:  93%  Packed:   90%  Max levels:  2
- check data record references index: 3
Key:  3:  Keyblocks used:  92%  Packed:    0%  Max levels:  2
- check data record references index: 4
Key:  4:  Keyblocks used:  92%  Packed:    0%  Max levels:  2
- check data record references index: 5
Key:  5:  Keyblocks used:  88%  Packed:   97%  Max levels:  2
Total:    Keyblocks used:  91%  Packed:   91%

- check records and index references
Records:              1680    M.recordlength:     4102   Packed:             0%
Recordspace used:      100%   Empty space:           0%  Blocks/Record:   1.00
Record blocks:        1680    Delete blocks:         0
Record data:       6892064    Deleted data:          0
Lost space:           1284    Linkdata:           6264

User time 0.11, System time 0.00
Maximum resident set size 3036, Integral resident set size 0
Non-physical pagefaults 925, Physical pagefaults 0, Swaps 0
Blocks in 0 out 0, Messages in 0 out 0, Signals 0
Voluntary context switches 0, Involuntary context switches 74
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
