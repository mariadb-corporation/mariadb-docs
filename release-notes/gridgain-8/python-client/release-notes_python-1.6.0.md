---
description: >-
  PyGridGain 1.6.0 lets you choose the similarity function used by vector search,
  adding DOT_PRODUCT, EUCLIDEAN, and MAXIMUM_INNER_PRODUCT alongside the default
  COSINE.
hidden: true
---

# PyGridGain 1.6.0 Release Notes

## New Features

PyGridGain 1.6.0 provides access to improved vector search.

### Vector Search Similarity Functions

You can now choose the similarity function used by vector search. Prior to this release, `COSINE` similarity was always used. Now, you can choose the preferred similarity function between `COSINE`, `DOT_PRODUCT`, `EUCLIDEAN`, and `MAXIMUM_INNER_PRODUCT`. `COSINE` similarity is still used by default. For more information about advantages and drawbacks of each similarity function, see [Function Comparison](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/vector#function-comparison) section in vector search documentation.

The example below shows how you can specify the similarity function:

```python
def cache_config(cache_name):
    return {
        PROP_NAME: cache_name,
        PROP_CACHE_MODE: CacheMode.REPLICATED,
        PROP_CACHE_ATOMICITY_MODE: CacheAtomicityMode.TRANSACTIONAL,
        PROP_WRITE_SYNCHRONIZATION_MODE: WriteSynchronizationMode.FULL_SYNC,
        PROP_QUERY_ENTITIES: [{
            'table_name': cache_name,
            'key_field_name': 'id',
            'key_type_name': 'java.lang.Long',
            'value_field_name': None,
            'value_type_name': Article.type_name,
            'field_name_aliases': [],
            'query_fields': [
                {
                    'name': 'id',
                    'type_name': 'java.lang.Long'
                },
                {
                    'name': 'title',
                    'type_name': 'java.lang.String'
                },
                {
                    'name': 'vec',
                    'type_name': '[F'
                }
            ],
            'query_indexes': [
                {
                    'index_name': 'vec',
                    'index_type': IndexType.VECTOR,
                    'inline_size': 1024,

                    #- Set `similarity_function: 0` for COSINE
                    #- Set `similarity_function: 1` for DOT_PRODUCT
                    #- Set `similarity_function: 2` for EUCLIDEAN
                    #- Set `similarity_function: 3` for MAXIMUM_INNER_PRODUCT
                    'similarity_function': 0,   # defaults to COSINE
                    'fields': [
                        {
                            'name': 'vec'
                        }
                    ]
                }
            ]
        }],
    }
```

## Improvements and Fixed Issues

| Issue ID | Description |
|---|---|
| GG-43272 | Vector Search now supports EUCLIDEAN, DOT_PRODUCT and MAXIMUM_INNER_PRODUCT similarity functions for vector search in addition to the COSINE. |

## Installation and Upgrade Information

To upgrade an existing package, use the following command:

```shell
pip install --upgrade pygridgain
```

To install the latest version of a package:

```shell
pip install pygridgain
```

To install a specific version:

```shell
pip install pygridgain==1.6.0
```

## Previous Releases

- [PyGridGain 1.5.0](release-notes_python-1.5.0.md)
- [PyGridGain 1.4.0](release-notes_python-1.4.0.md)
- [PyGridGain 1.3.1](release-notes_python-1.3.1.md)
- [PyGridGain 1.2.0](release-notes_python-1.2.0.md)

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
