# Code Coverage with dgcov

The dgcov tool helps you check the coverage for new code. The dgcov.pl script is part of the [mariadb-test](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-test) framework (and any packages that include mariadb-test).

## Overview

The dgcov program runs gcov for code coverage analysis, aggregates the coverage data,\
and (optionally) reports coverage only for those lines that are changed by the commit(s).\
Commits are specified in the `git diff` format.

If no commits are specified, the default is to work on all uncommitted changes, if any, otherwise on the last commit (in other words, on `git diff HEAD` or `git diff HEAD^`).

It's recommended that a developer [runs dgcov on their new code](code-coverage.md) before pushing it into a MariaDB repository.

## Usage

```
./dgcov.pl --help
./dgcov.pl [options] [<commit> [<commit>]]
```

## Options and Variables

| Short Option | Long Option | Description                                                               |
| ------------ | ----------- | ------------------------------------------------------------------------- |
| -h           | --help      | Print help and exit                                                       |
| -v           | --verbose   | Show commands run.                                                        |
| -p           | --purge     | Delete all test coverage information, to prepare for a new coverage test. |
| -o           | --only-gcov | Stop after running gcov, don't run git                                    |
| -s           | --skip-gcov | Do not run gcov, assume .gcov files are already in place                  |
| -g           | --generate  | Create .dgcov files for all source files                                  |

## How to Prepare the Code for dgcov

Prior to running this tool, MariaDB should be built with

```
cmake -DENABLE_GCOV=ON
```

and the testsuite should be run. dgcov will report the coverage\
for all lines modified in the specified commits.

## Output

Output .dgcov files have a conventional gcov format:\
lines not covered are prefixed with `#####`, lines without generated code are\
prefixed with `-`, and other lines are prefixed with the number of times they\
were executed. See `info gcov` for more information.

The patch-like coverage for commits uses gcov format (as above) for lines, changed in these commits, and no prefix at all for lines that were not changed.

## Examples

Checking the coverage for all unpushed commits:

```
dgcov.pl @{u} HEAD
```

Checking the coverate for all uncommitted changes:

```
dgcov.pl HEAD
```

Checking the coverage for a specific commit 1234567:

```
dgcov.pl 1234567^ 1234567
```

[mariadb-test-run](../../mariadb-internals/using-mariadb-with-your-programs-api/libmysqld/mariadb-test-and-mariadb-test-embedded.md) can invoke dgcov automatically:

```
./mtr --gcov
```

in the latter case the coverate for the uncommitted changes (or the last commit) will be not printed to the stdout, but will be put into `var/last_changes.dgcov` file.

## Caveats

Note that to be able to run gcov with the [mariadb-test](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-test) framework you need to have gcc version 4.8 or newer.

## References

* dgcov was created by Kristian Nielsen and was first [announced here](https://kristiannielsen.livejournal.com/1885.html).
* dgcov was re-implemented to aggregate the data and to work for git and cmake by Sergei Golubchik.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
