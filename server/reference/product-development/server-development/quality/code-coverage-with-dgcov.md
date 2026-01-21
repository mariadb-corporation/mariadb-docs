---
description: >-
  Technical instructions on using the dgcov tool to generate and analyze code
  coverage reports for the MariaDB server.
---

# Code Coverage With dgcov

{% include "../../../../.gitbook/includes/this-page-contains-backgrou....md" %}

The `dgcov` tool helps you check the coverage for new code. The `dgcov.pl` script is part of the [mariadb-test framework](../../../../clients-and-utilities/testing-tools/mariadb-test/) (and any packages that include mariadb-test).

### Overview <a href="#overview" id="overview"></a>

The `dgcov` program runs `gcov` for code coverage analysis aggregates the coverage data, and optionally reports coverage only for those lines that are changed by  commits. Commits are specified in the `git diff` format.

If no commits are specified, the default is to work on all uncommitted changes, if any, otherwise on the last commit (in other words, on `git diff HEAD` or `git diff HEAD^`).

It's recommended that a developer [runs dgcov on their new code](code-coverage.md) before pushing it into a MariaDB repository.

### Usage <a href="#usage" id="usage"></a>

```
./dgcov.pl --help
./dgcov.pl [options] [<commit> [<commit>]]
```

### Options and Variables <a href="#options-and-variables" id="options-and-variables"></a>

| Short Option | Long Option   | Description                                                               |
| ------------ | ------------- | ------------------------------------------------------------------------- |
| `-h`         | `--help`      | Print help and exit                                                       |
| `-v`         | `--verbose`   | Show commands run.                                                        |
| `-p`         | `--purge`     | Delete all test coverage information, to prepare for a new coverage test. |
| `-o`         | `--only-gcov` | Stop after running gcov, don't run git                                    |
| `-s`         | `--skip-gcov` | Do not run `gcov`, assume `.gcov` files are already in place              |
| `-g`         | `--generate`  | Create `.dgcov` files for all source files                                |

### How to Prepare Code for dgcov <a href="#how-to-prepare-the-code-for-dgcov" id="how-to-prepare-the-code-for-dgcov"></a>

Prior to running this tool, MariaDB should be built like this:

```cmake
cmake -DENABLE_GCOV=ON
```

In addition, the test suite should be run. `dgcov` reports the coverage for all lines modified in the specified commits.

### Output <a href="#output" id="output"></a>

Output `.dgcov` files have a conventional `gcov` format: Lines not covered are prefixed with `#####`, lines without generated code are prefixed with `-`, and other lines are prefixed with the number of times they were executed. See `info gcov` for more information.

The patch-like coverage for commits uses `gcov` format (as above) for lines, changed in these commits, and no prefix at all for lines that were not changed.

### Examples <a href="#examples" id="examples"></a>

Checking the coverage for all unpushed commits:

```perl
dgcov.pl @{u} HEAD
```

Checking the coverage for all uncommitted changes:

```perl
dgcov.pl HEAD
```

Checking the coverage for a specific commit _1234567_:

```
dgcov.pl 1234567^ 1234567
```

[mariadb-test-run](../../../../clients-and-utilities/testing-tools/mariadb-test/pausing-mariadb-test-run-pl.md) can invoke `dgcov` automatically:

```
./mtr --gcov
```

In the latter case, the coverage for uncommitted changes (or for the last commit) is not printed to `stdout`, but to the `var/last_changes.dgcov` file.

### Caveats <a href="#caveats" id="caveats"></a>

{% hint style="info" %}
To be able to run `gcov` with the [mariadb-test](../../../../clients-and-utilities/testing-tools/mariadb-test/) framework, you must have `gcc` version 4.8 or newer.
{% endhint %}

### References <a href="#references" id="references"></a>

* `dgcov` was created by Kristian Nielsen and [announced here](http://kristiannielsen.livejournal.com/1885.html).
* `dgcov` was reimplemented to aggregate the data, and to work for `git` and `cmake`, by Sergei Golubchik.
