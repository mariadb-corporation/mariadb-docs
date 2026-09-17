---
description: >-
  Performance benchmark results for Spider, demonstrating its throughput and
  latency characteristics under various workloads compared to other
  configurations.
---

# Spider Benchmarks

This is best run on a cluster of 3 nodes intel NUC servers 12 virtual cores model name : Intel® Core(TM) i3-3217U CPU @ 1.80GHz

All nodes have been running a mysqlslap client attached to the local spider node in the best run.

```
/usr/local/skysql/mysql-client/bin/mysqlslap --user=skysql --password=skyvodka --host=192.168.0.201 --port=5012 -i1000000 -c32 -q "insert into test(c) values('0-31091-138522330')" --create-schema=test
```

`spider_conn_recycle_mode=1;`

```mermaid
flowchart TD
  accTitle: Spider sharding architecture with XA two-phase commit
  accDescr { A client fans out to three Spider nodes, each holding the full partition map for TABLE1 (PART1, PART2, PART3). One Spider node routes to three backend shards, each storing a single partition of TABLE1. The three backends coordinate distributed writes with each other using XA two-phase commit (XA 2PC). }

  CLIENT[CLIENT]
  SPIDER1["SPIDER<br/>TABLE1: PART1, PART2, PART3"]
  SPIDER2["SPIDER<br/>TABLE1: PART1, PART2, PART3"]
  SPIDER3["SPIDER<br/>TABLE1: PART1, PART2, PART3"]
  BACKEND1[("BACKEND<br/>TABLE1: PART1")]
  BACKEND2[("BACKEND<br/>TABLE1: PART2")]
  BACKEND3[("BACKEND<br/>TABLE1: PART3")]

  CLIENT --> SPIDER1
  CLIENT --> SPIDER2
  CLIENT --> SPIDER3

  SPIDER1 --> BACKEND1
  SPIDER1 --> BACKEND2
  SPIDER1 --> BACKEND3

  BACKEND1 -->|XA 2PC| BACKEND2
  BACKEND2 -->|XA 2PC| BACKEND3
  BACKEND1 -->|XA 2PC| BACKEND3

  linkStyle 6 stroke:#c07000,stroke-width:2px,stroke-dasharray:5 5;
  linkStyle 7 stroke:#c07000,stroke-width:2px,stroke-dasharray:5 5;
  linkStyle 8 stroke:#c07000,stroke-width:2px,stroke-dasharray:5 5;

  classDef client fill:#e8908a,stroke:#7a2a20,stroke-width:2px,color:#111;
  classDef spider fill:#f0a030,stroke:#7a4a00,stroke-width:2px,color:#111;
  classDef backend fill:#e8908a,stroke:#7a2a20,stroke-width:2px,color:#111;

  class CLIENT client
  class SPIDER1,SPIDER2,SPIDER3 spider
  class BACKEND1,BACKEND2,BACKEND3 backend
```

_Spider sharding architecture: three Spider nodes route to three backend shards, each holding one partition of TABLE1, coordinated across backends by XA two-phase commit._

The read point select is produce with a 10M rows sysbench table

```mermaid
flowchart TD
  accTitle: Single Spider node fan-out to three backends
  accDescr { A client connects to a single Spider node holding TABLE1. The Spider node forwards queries to three backend nodes, each holding a copy of TABLE1, with no partitioning or cross-backend coordination shown. }

  CLIENT[CLIENT]
  SPIDER["SPIDER<br/>TABLE1"]
  BACKEND1[("BACKEND<br/>TABLE1")]
  BACKEND2[("BACKEND<br/>TABLE1")]
  BACKEND3[("BACKEND<br/>TABLE1")]

  CLIENT --> SPIDER
  SPIDER --> BACKEND1
  SPIDER --> BACKEND2
  SPIDER --> BACKEND3

  classDef client fill:#e8908a,stroke:#7a2a20,stroke-width:2px,color:#111;
  classDef spider fill:#f0a030,stroke:#7a4a00,stroke-width:2px,color:#111;
  classDef backend fill:#e8908a,stroke:#7a2a20,stroke-width:2px,color:#111;

  class CLIENT client
  class SPIDER spider
  class BACKEND1,BACKEND2,BACKEND3 backend
```

_Single Spider node distributing client queries to three backend nodes, each holding a full copy of TABLE1._

The write insert a single string into a memory table

![spbench6](../../../.gitbook/assets/spbench6.png)

Before Engine Condition Push Down patch .

![benchspider7](../../../.gitbook/assets/benchspider7.png)

Spider can benefit by 10% additional performance with Independent Storage Engine Statistics.

```sql
SET global use_stat_tables='preferably';
USE backend; 
ANALYZE TABLE sbtest;
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
