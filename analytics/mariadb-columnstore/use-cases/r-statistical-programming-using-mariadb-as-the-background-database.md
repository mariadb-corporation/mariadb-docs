# Using MariaDB With R

## Introduction to R

`R` is a language and environment for statistical computing and graphics.\
`R` provides a wide variety of statistical (linear and nonlinear modeling, classical statistical tests, time-series analysis, classification, clustering, …), graphical techniques, machine learning packages and is highly extensible.

One of `R’s` strengths is the ease with which well-designed publication-quality plots can be produced, including mathematical symbols and formulae where needed. Great care has been taken over the defaults for the minor design choices in graphics, but the user retains full control.

## The R Environment

`R` is an integrated suite of software facilities for data manipulation, calculation, and graphical display. 

It includes:

• an effective data handling and storage facility,

• a suite of operators for calculations on arrays, in particular matrices,

• a large, coherent, integrated collection of intermediate tools for data analysis,

• graphical facilities for data analysis and display either on-screen or on hardcopy, and

• a well-developed, simple and effective programming language which includes conditionals, loops, user-defined recursive functions and input and output facilities.

## Using R with MariaDB

### R Installation

Some basic notions / tips on how to use R along with MariaDB are the following:

A. The recommended R distribution is “Base R”: [CRAN](https://cran.r-project.org/bin/windows/base/)

B. The recommended R GUIs are RStudio Desktop, or RStudio Server: [RStudio](https://www.rstudio.com/products/rstudio/)

Alternative GUIs would be:

* RCode (PGM Solutions): [RCode](https://www.pgm-solutions.com/rcode).

“R” and “MariaDB Server” can be installed either in the same server, or in different servers, as an ODBC communication protocol will be used for the exchange of data between the two environments.

### Data Transfer between R and MariaDB

#### Package: "odbc"

For the transfer of data between MariaDB Server and R Environment, it is recommended R's "odbc" Package: [CRAN odbc](https://cran.r-project.org/web/packages/odbc/index.html)

* “odbc" is a new R package available on CRAN (Since 2017-02-05), and maintained by RStudio, which is designed to comply with the DBI specification.
* Tutorials on how to use R's "odbc" package can be found here:
  * Setting up ODBC Drivers: [DB RStudio Drivers](https://db.rstudio.com/drivers/)
  * "odbc" R Package: [DB RStudio odbc Usage](https://db.rstudio.com/odbc/#usage)

The "odbc" package requires to have previously installed the MariaDB or MySQL ODBC connector:

* [MariaDB ODBC Connector](https://downloads.mariadb.org/connector-odbc/)
* [MySQL ODBC Connector](https://dev.mysql.com/downloads/connector/odbc/5.3.html)

For installing the "odbc" package from CRAN, execute in R:

```sql
install.packages("odbc")
```

#### Package: "RMariaDB"

“RMariaDB” R library, is a modern 'MariaDB' client based on 'Rcpp'.

For installing RMariaDB package through CRAN, execute the following R statement:

```sql
install.packages("RMariaDB")
```

And for connecting to MariaDB:

```sql
library(RMariaDB)

con <- dbConnect(
  drv = RMariaDB::MariaDB(), 
  username = NULL,
  password = NULL, 
  host = NULL, 
  port = 3306
)
```

#### Other Packages: "readr", "RODBC"

There are other alternatives for data transfer between R and MariaDB:

* “readr” R package, for writing / reading CSV files. To be used in MariaDB along with “LOAD DATA INFILE”.
* "RODBC" R package: Robust and well-tested (Since 2000-05-24) package which enables data transfer between R and MariaDB by means of an ODBC connector: [CRAN RODBC](https://cran.r-project.org/web/packages/RODBC/index.html)
  * It is slightly slower than RStudio's new "odbc" package (See benchmarks): [RStudio odbc](https://db.rstudio.com/odbc/)
  * For bug report to the RODBC package maintainer, use the following R statement: bug.report(package = "RODBC")
  * A vignette on how to use the RODBC package can be found here: [RODBC CRAN Vignette](https://cran.r-project.org/web/packages/RODBC/vignettes/RODBC.pdf)

### R Programming Resources

#### A) Programming

Recommended resources for learning how to program in R are the following:

* [R Cookbook Second Edition (O’Reilly Media; Paul Teetor; James (JD) Long)](https://rc2e.com/)
* [R Graphics Cookbook Second Edition (O’Reilly Media; Winston Chang)](https://r-graphics.org/)
* [R for Data Science (O’Reilly Media; Garrett Grolemund, Hadley Wickham)](https://r4ds.had.co.nz/)
* [Advanced R Second Edition (CRC R Series; Hadley Wickham)](https://adv-r.hadley.nz/)
* [Mastering Spark with R (O'Reilly; Javier Luraschi, Kevin Kuo, Edgar Ruiz)](https://therinspark.com/)
* [R Packages (Hadley Wickham; O’Reilly)](https://r-pkgs.org/)

#### B) Statistics

A recommended book for understanding the underlying statistics in the R packages is:

* [Practical Statistics for Data Scientists (O’Reilly Media; Peter Bruce, Andrew Bruce)](https://shop.oreilly.com/product/0636920048992.do)

#### C) Cheatsheets: Concept Summary

* Rstudio Cheatsheets are a recommended and valuable resource: [RStudio Cheatsheets: Webpage](https://www.rstudio.com/resources/cheatsheets/)
* Along with the following Base R reference card: [R Reference Card v2](https://cran.r-project.org/doc/contrib/Baggott-refcard-v2.pdf)

#### D) Search Engine & R Package Spotlight

* Search Engines:
  * [RSeek: For searching any R related information (Based on Google).](https://rseek.org/)
  * [RPackages: Search and stats for CRAN packages.](https://www.rpackages.io/)
* Information on new R packages is regularly published in the following websites:
  * [R-bloggers](https://www.r-bloggers.com/)
  * [Towards Data Science](https://towardsdatascience.com/)
  * [MRAN: Package Spotlight](https://mran.microsoft.com/spotlight)

#### E) Statistical / Unsupervised Machine Learning, Deep Learning and Artificial Intelligence

**H2O.AI**

The R Programming language has support for the H2O.ai library ([h2o](https://cran.r-project.org/web/packages/h2o/index.html)), which enables to create in-memory multi-cluster GPU powered machine learning models.

For installing H2O.ai through CRAN, execute:

```sql
install.packages("h2o")
```

* [H2O.ai: Webpage](https://www.h2o.ai/)
* [H2O.ai Algorithms: Cheatsheet](https://github.com/h2oai/h2o-tutorials/raw/master/training/h2o_algos/h2o_algos_cheat_sheet_04_25_17.pdf)
* [h2o R Package Functions: Cheatsheet](https://github.com/rstudio/cheatsheets/raw/master/h2o.pdf)
* [Practical Machine Learning with H2O (O'Reilly Media; Darren Cook)](https://shop.oreilly.com/product/0636920053170.do)
* [Machine Learning with R and H2O (Mark Landry): Booklet Online Version](https://docs.h2o.ai/h2o/latest-stable/h2o-docs/booklets/RBooklet.pdf)
* [Deep Learning with H2O: Vignette](https://docs.h2o.ai/h2o/latest-stable/h2o-docs/booklets/DeepLearningBooklet.pdf)

The following R Statements can be used for importing a MariaDB table to H2O.ai using the R Front End:

* import\_sql\_table: "This function imports a SQL table to H2OFrame in memory".
* import\_sql\_select: "This function imports the SQL table that is the result of the specified SQL query to H2OFrame in memory".

```sql
connection_url <- "jdbc:mariadb://172.16.2.178:3306/ingestSQL?&useSSL=false"
username <- "root"
password <- "abc123"

# Whole Table:
table <- "citibike20k"
my_citibike_data <- h2o.import_sql_table(connection_url, table, username, password)

# SELECT Query:
select_query <-  "SELECT  bikeid  FROM citibike20k"
my_citibike_data <- h2o.import_sql_select(connection_url, select_query, username, password)
```

NOTE: Be sure to start the h2o.jar in the terminal with your downloaded JDBC driver in the classpath:

```sql
java -cp <path_to_h2o_jar>:<path_to_jdbc_driver_jar> water.H2OApp
```

**KERAS**

[R package keras](https://cran.r-project.org/web/packages/keras/index.html) offers an interface to [Python's 'Keras'](https://keras.io), a high-level neural networks 'API'.

'Keras' was developed with a focus on enabling fast experimentation, supports both convolution based networks and recurrent networks (as well as combinations of the two), and runs seamlessly on both 'CPU' and 'GPU' devices.

* [R interface to Keras: Webpage](https://keras.rstudio.com/)
* [Deep Learning With R (François Chollet with J. J. Allaire, Manning)](https://www.manning.com/books/deep-learning-with-r)
* [Keras Rstudio Cheatsheet](https://github.com/rstudio/cheatsheets/raw/master/keras.pdf)

**R LIBRARIES: CARET**

A book which introduces core Machine Learning concepts:

* [Introduction to Machine Learning with R (O'Reilly; Scott Burger)](https://shop.oreilly.com/product/0636920058885.do)

#### F) Text Mining

Documentation on how to perform Text Mining in R can be found in the book "Text Mining With R":

* [Text Mining With R: A Tidy Approach (O’Reilly Media; Julia Silge and David Robinson): Book Online Version](https://tidytextmining.com/)

#### G) Shiny Web Apps & RMarkdown Documents

**SHINY WEB APPS**

[Shiny](https://cran.r-project.org/web/packages/shiny/index.html) R Package makes it incredibly easy to build interactive web applications with R.

Automatic "reactive" binding between inputs and outputs and extensive prebuilt widgets make it possible to build beautiful, responsive, and powerful applications with minimal effort.

* [Shiny Written Tutorials](https://shiny.rstudio.com/tutorial/written-tutorial/lesson1/)
* [Shiny R Package Cheatsheet](https://github.com/rstudio/cheatsheets/raw/master/shiny.pdf)

For deploy Shiny Web Applications using Open Source Alternatives, you can either use:

* [RInno: CRAN Webpage (Windows)](https://cran.r-project.org/web/packages/RInno/index.html)
* [ShinyProxy: Webpage](https://www.shinyproxy.io/)
* [Shiny Server (Open Source Edition): Webpage](https://www.rstudio.com/products/shiny/shiny-server/)

**RMARKDOWN DOCUMENTS**

* [R Markdown: The Definitive Guide (Book).](https://bookdown.org/yihui/rmarkdown/)
* [R Markdown Cheatsheet.](https://github.com/rstudio/cheatsheets/raw/master/rmarkdown-2.0.pdf)

#### H) Advanced R Resources

Some of the most advanced R resources for fully understanding the internals and nuances of the R Programming Language are the following:

* [Chapman & Hall/CRC The R Series: Subject-specific Books](https://www.crcpress.com/Chapman--HallCRC-The-R-Series/book-series/crctherser)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
