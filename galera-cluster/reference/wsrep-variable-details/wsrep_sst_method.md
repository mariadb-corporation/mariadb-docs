---
description: >-
  wsrep_sst_method selects the State Snapshot Transfer method used by Galera
  Cluster, with rsync as the default; it is dynamic and global, and should
  match between donor and joiner nodes.
---

# wsrep\_sst\_method

### Overview <a href="#overview_h2" id="overview_h2"></a>

State snapshot transfer method.

### DETAILS

#### PARAMETERS

| Command-line          | --wsrep\_sst\_method=arg |
| --------------------- | ------------------------ |
| Configuration file    | Supported                |
| Dynamic               | Yes                      |
| Scope                 | Global                   |
| Data Type             | VARCHAR                  |
| Product Default Value | rsync                    |
