---
description: >-
  RMariaDB is a DBI-compliant R package that provides a MariaDB database
  interface for R, supporting connection, querying, and data manipulation
  through standard DBI methods.
icon: link
---

# RMariaDB: MariaDB Driver for R

RMariaDB is a database interface and MariaDB driver for R. This version is aimed at full compliance with R's DBI specification.

The link to the package on CRAN (R Package Repository) can be accessed from: [CRAN RMariaDB](https://cran.r-project.org/web/packages/RMariaDB/index.html)

The package can be installed in R with the following statement:

```r
install.packages("RMariaDB")
```

And loaded in the R environment executing:

```r
library(RMariaDB)
```

Basic notions on R Programming can be found in article:[R Statistical Programming Using MariaDB as the Background Database](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/mariadb-columnstore/use-cases/r-statistical-programming-using-mariadb-as-the-background-database)

## RMariaDB Package Function Examples

```r
library(RMariaDB)
library(DBI)
# Connect to my-db as defined in ~/.my.cnf
con <- dbConnect(RMariaDB::MariaDB(), group = "my-db")

dbListTables(con)
dbWriteTable(con, "mtcars", mtcars)
dbListTables(con)

dbListFields(con, "mtcars")
dbReadTable(con, "mtcars")

# You can fetch all results:
res <- dbSendQuery(con, "SELECT * FROM mtcars WHERE cyl = 4")
dbFetch(res)
dbClearResult(res)

# Or a chunk at a time
res <- dbSendQuery(con, "SELECT * FROM mtcars WHERE cyl = 4")
while(!dbHasCompleted(res)){
  chunk <- dbFetch(res, n = 5)
  print(nrow(chunk))
}
# Clear the result
dbClearResult(res)

# Disconnect from the database
dbDisconnect(con)
```

{% @marketo/form formId="4316" %}
