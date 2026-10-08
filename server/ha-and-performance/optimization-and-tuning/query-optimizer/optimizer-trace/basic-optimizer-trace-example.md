# Basic Optimizer Trace Example

```
MariaDB> set optimizer_trace='enabled=on';

MariaDB> select * from t1 where a<10;

MariaDB> select * from information_schema.optimizer_trace limit 1\G
*************************** 1. row ***************************
                            QUERY: select * from t1 where a<10
                            TRACE: {
  "steps": [
    {
      "join_preparation": {
        "select_id": 1,
        "steps": [
          {
            "expanded_query": "select t1.a AS a,t1.b AS b,t1.c AS c from t1 where t1.a < 10"
          }
        ]
      }
    },
    {
      "join_optimization": {
        "select_id": 1,
        "steps": [
          {
            "condition_processing": {
              "condition": "WHERE",
              "original_condition": "t1.a < 10",
              "steps": [
                {
                  "transformation": "equality_propagation",
                  "resulting_condition": "t1.a < 10"
                },
                {
                  "transformation": "constant_propagation",
                  "resulting_condition": "t1.a < 10"
                },
                {
                  "transformation": "trivial_condition_removal",
                  "resulting_condition": "t1.a < 10"
                }
              ]
            }
          },
          {
            "table_dependencies": [
              {
                "table": "t1",
                "row_may_be_null": false,
                "map_bit": 0,
                "depends_on_map_bits": []
              }
            ]
          },
          {
            "ref_optimizer_key_uses": []
          },
          {
            "rows_estimation": [
              {
                "table": "t1",
                "range_analysis": {
                  "table_scan": {
                    "rows": 1000,
                    "cost": 206.1
                  },
                  "potential_range_indexes": [
                    {
                      "index": "a",
                      "usable": true,
                      "key_parts": ["a"]
                    },
                    {
                      "index": "b",
                      "usable": false,
                      "cause": "not applicable"
                    }
                  ],
                  "setup_range_conditions": [],
                  "group_index_range": {
                    "chosen": false,
                    "cause": "no group by or distinct"
                  },
                  "analyzing_range_alternatives": {
                    "range_scan_alternatives": [
                      {
                        "index": "a",
                        "ranges": ["(NULL) < (a) < (10)"],
                        "rowid_ordered": false,
                        "using_mrr": false,
                        "index_only": false,
                        "rows": 10,
                        "cost": 13.751,
                        "chosen": true
                      }
                    ],
                    "analyzing_roworder_intersect": {
                      "cause": "too few roworder scans"
                    },
                    "analyzing_index_merge_union": []
                  },
                  "chosen_range_access_summary": {
                    "range_access_plan": {
                      "type": "range_scan",
                      "index": "a",
                      "rows": 10,
                      "ranges": ["(NULL) < (a) < (10)"]
                    },
                    "rows_for_plan": 10,
                    "cost_for_plan": 13.751,
                    "chosen": true
                  }
                }
              },
              {
                "selectivity_for_indexes": [
                  {
                    "index_name": "a",
                    "selectivity_from_index": 0.01
                  }
                ],
                "selectivity_for_columns": [],
                "cond_selectivity": 0.01
              }
            ]
          },
          {
            "considered_execution_plans": [
              {
                "plan_prefix": [],
                "table": "t1",
                "best_access_path": {
                  "considered_access_paths": [
                    {
                      "access_type": "range",
                      "resulting_rows": 10,
                      "cost": 13.751,
                      "chosen": true
                    }
                  ]
                }
              }
            ]
          },
          {
            "attaching_conditions_to_tables": {
              "original_condition": "t1.a < 10",
              "attached_conditions_computation": [],
              "attached_conditions_summary": [
                {
                  "table": "t1",
                  "attached": "t1.a < 10"
                }
              ]
            }
          }
        ]
      }
    },
    {
      "join_execution": {
        "select_id": 1,
        "steps": []
      }
    }
  ]
}
MISSING_BYTES_BEYOND_MAX_MEM_SIZE: 0
          INSUFFICIENT_PRIVILEGES: 0
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
