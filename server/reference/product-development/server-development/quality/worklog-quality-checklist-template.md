---
description: >-
  Provides a standardized template for developers to ensure every new feature
  meets mandatory quality and documentation requirements.
---

# Worklog Quality Checklist Template

{% include "../../../../.gitbook/includes/this-page-contains-backgrou....md" %}

The purpose of this template is to produce individual checklists for testing individual Worklogs. Using a checklist ensures that all WLs[^1] are treated equally and that all important points are addressed and tested, or at least considered when clearing the WL[^2] for merging into a stable release.

## Inputs <a href="#inputs" id="inputs"></a>

This page lists all sources of information which can be used as inputs to the testing process. The goal is to gather comprehensive information before creating a testing plan.

### Usage Scenario <a href="#usage-scenario" id="usage-scenario"></a>

_TODO: Summarize here the intended use for the feature._

### Design, Architecture, Specification <a href="#design-architecture-and-specification" id="design-architecture-and-specification"></a>

* **WorkLog number and title:**
  * _If there is no Worklog, create one or ask one to be created_
* **Are HLS and LLS present?**
  * _If the HLS or LLS sections are missing, add them or ask that they are created_
* **Reviewer name:**
  * _Testing suggestions and concerns should be obtained by the reviewer_
* **Customer requirements:**
  * _Make yourself familiar with any requirements or documents supplied by the customer_
* **Other implementations:**
  * _Make yourself familiar with other implementations of the feature in other database products or flavors of MySQL_

### Testability and Observability <a href="#testability-and-observability" id="testability-and-observability"></a>

* **Does the feature have an on/off switch?**
  * _An on/off switch is required in at least the following situations:_
    * _A RQG comparison test will be performed in order to validate the feature;_
    * _The feature may cause a performance degradation for certain queries or usage scenarios;_
    * _The feature is experimental or of interest to a small number of users;_
* **Is the operation of the feature observable?**
  * _Does the feature leave any traces in `SHOW STATUS` or `EXPLAIN`, or in the logs?_

### The Patch <a href="#the-patch" id="the-patch"></a>

* **List of modified files:**
  * _Obtain a list of all modified files from the version control system, to serve as a starting point for identifying areas of risk within the server or potential interactions with other features. A larger number of modified files may indicate larger risk of unforeseen interactions_
* **Review comments:**
  * _Paste a link to the review and read it for any concerns that the reviewer may have raised_
* **MTR tests:**
  * _Does the patch include enough MTR tests?_
* **DGCov output:**
  * _Generate a report or obtain it from a developer and make sure it is acceptable for all parties_

### Feedback From Interested Parties <a href="#feedback-from-interested-parties" id="feedback-from-interested-parties"></a>

* **Feedback from developer:**
  * _Paste here any useful information provided by the developer in informal discussions, emails or chat_
  * _Make sure any concerns raised by the developer are recorded in this document_
* **Feedback from reviewer:**
  * _Paste here any discussions with the reviewer related to concerns, risks or testing, if not included in the formal review comments for the patch itself_
* **Feedback from customer:**
  * _Summarize here any relevant discussions with the customer_

### Query Patterns <a href="#query-patterns" id="query-patterns"></a>

_If the feature relates to the optimization of a particular set of queries, provide here examples that were extracted from the sources of information listed above, in particular the Worklog and any MTR test cases provided with the patch._

## Risks <a href="#risks" id="risks"></a>

_This section lists any risks inherent to the Worklog, as identified by reviewing the inputs mentioned_

### Refactoring <a href="#refactoring" id="refactoring"></a>

* **Areas that have been refactored:**
  * _List areas that have been refactored in order to accommodate the new functionality_

### Interactions <a href="#interactions" id="interactions"></a>

* **Areas of potential interaction:**
  * _List areas in the server that may have an interaction with the feature_
* **Does the feature contain engine-specific code, hooks or hacks?**
  * _List any engine-specific considerations there may be_
* **Does the feature define a new API?**
* **Does the feature relate to transactions or transactional integrity?**
  * _If yes, is testing required on all storage engines, or using cross-engine transactions or binlog involvement?_
* **Does the feature relate to any of the core server features?**
  * _Do we need to test with views, triggers, stored procedures, functions, events, partitions, foreign keys, time zones_

### Upgrade or Downgrade <a href="#upgradedowngrade" id="upgradedowngrade"></a>

* **Does the feature change any on-disk formats?**
  * _If yes, testing would be required that upgrading to the new format works properly_
* **Does the feature change the format of the system tables in the `mysql` database?**
  * _If yes, testing would be required to make sure that any upgrade/downgrade scripts are able to handle the change gracefully_
* **Does the feature change or retire or deprecate any mysqld configuration options?**
  * _List options here_
* **Is downgrade to be supported?**
  * _If using the new feature makes the database non-downgradable, this must be a conscious design decision_

### User-Visible Changes <a href="#user-visible-changes" id="user-visible-changes"></a>

* **Does the feature change the mysql protocol?**
  * _If yes, full connectors testing is required to make sure the change is compatible_
* **Does the feature change any result formatting or data types?**
  * _If yes, testing via the `mysql` client is required to verify that the new format or data type properly arrives at the client_
* **Does the feature change the syntax or the output of a `SHOW` command?**
  * _If yes, clients, connectors and tools that issue that `SHOW` command and process its output should be tested_
* **Does the feature change anything with respect to `INFORMATION_SCHEMA` and `PERFORMANCE_SCHEMA` ?**

### Performance and Optimizer <a href="#performance-and-optimizer" id="performance-and-optimizer"></a>

* **Does the feature have any performance implications?**
  * _Is the feature expected to deliver any performance improvement?_
  * _Is the feature feared to have a performance impact?_
* **Does the feature interact with the Optimizer or indexes?**
  * _Does the feature change anything related to indexes or data stored in them?_
  * _Does the feature change anything with respect to any optimizations?_

### Replication <a href="#replication" id="replication"></a>

_Does the feature generate or transmit data that may be sent or processed by the slave or tools such as `mysqlbinlog`?_

* **Which binary log formats should be tested?**
  * _Certain optimizations or scenarios may only trigger for a particular binary log mode_
* **Are existing replication RQG grammars sufficient to trigger the new code?**
* **Do we need to test DDL in replication, log rotation and such?**
* **Does the change affect the master as well, or just the slave? Is a transactional integrity test indicated?**
* **Do we need to simulate replication failures, server restarts and such?**
* **Do we need to test cloning new slaves from scratch, binary log replay and other replication maintenance activities?**
* **Do we need to cover exotic data types, overly large records, statements that are only safe in a particular binlog mode, etc?**

### Extreme Conditions and Corner Cases <a href="#extreme-conditions-and-corner-case" id="extreme-conditions-and-corner-case"></a>

* **Does the feature deal with extreme conditions and corner cases?**
  * _e.g. huge values, huge tables, huge row lengths, blobs, high concurrencies_
* **Is any form of stress testing indicated for the feature?**
  * _Does the feature have any thread interactions, locking or concurrency mechanisms?_

## Testing Plan <a href="#testing-plan" id="testing-plan"></a>

_This section identifies the testing that will be performed based on the risks identified above_

### Additional MTR Tests <a href="#additional-mtr-tests" id="additional-mtr-tests"></a>

_Describe any MTR tests that will be implemented in addition to the ones already present in the patch_

### RQG Tests <a href="#rqg-tests" id="rqg-tests"></a>

* **Are new Random Query Generator grammars required?**
  * _If existing grammars do not cover the new feature_
* **Are new Validators or Reporters required?**
  * _If the existing RQG validation code can not verify the proper operation of the feature_
* **RQG tests lines to run:**
  * _provide actual RQG command lines, along with a description of the desired effect_

### Manual Testing <a href="#manual-testing" id="manual-testing"></a>

_Describe any manual testing that will be performed involving connectors, clients or installers_

### Benchmarks and Stress Tests <a href="#benchmarks-and-stress-tests" id="benchmarks-and-stress-tests"></a>

_Describe any benchmarks and stress tests that will be performed. Include the exact parameters and command lines that will be used_

## Hand-Off <a href="#hand-off" id="hand-off"></a>

_This section identifies final checks to be performed on the test content when it is delivered._

### Requirements for MTR Tests <a href="#requirements-for-mtr-tests" id="requirements-for-mtr-tests"></a>

* Are all new mysqld options, `SHOW STATUS` variables, [`I_S`](#user-content-fn-3)[^3] tables and such covered with an MTR test?
* Are all new error messages covered with a test?
* Is code coverage acceptable to all parties involved?

### Requirements for Random Query Generator Tests <a href="#requirements-for-random-query-generator-tests" id="requirements-for-random-query-generator-tests"></a>

* Has the proper set of RQG grammars been chosen or created?
* Do we have a .CC file listing all interesting mysqld options and RQG variants, in order to run a combinations test? Was the CC file pushed into RQG's LP repository?
* Has an at least 24-hour combination test been run?
* Was code coverage run on the RQG test?
* Were all new grammars and Perl modules pushed into the RQG LP repository?
* Were the RQG tests prepared to be buildbot-ready, as opposed to manually-monitored?
* Does the test include any safeguards against false negatives?
  * _e.g. all queries generated are bad, which causes no actual replication, which is still reported as test success_
* Are the tests running stably and green in the feature tree's BuildBot?
* Are any bug reports missing reproducible test cases, core files, RQG command lines and the like?

### Requirements for Code Coverage <a href="#requirements-for-code-coverage" id="requirements-for-code-coverage"></a>

_This makes it much faster to review code as one knows what it tested and what one needs to review more carefully_

* Ideally all code should be tested by MTR;
* If code can only be reproduced by an RQG test or other external test, sufficient information must be provided in the Worklog for the test to be reproducible;
* All code should either be tested or reviewed and marked with `/* purecov inspected */`
* Code that is suspected to be unreachable should have an DBUG\_ASSERT(0) and be marked with /\* purecov: deadcode \*/.
* Was an MTR code coverage report for the feature tree generated by i7.stoev.org/lcov?
* Has the dgcov coverage tool been run?
* Are there any notable regressions in the code coverage?
* Was code coverage run on the RQG tests alone, along with an effort to increase it?
* Is the code covered by comments?

### Requirements for Code Trees <a href="#requirements-for-the-code-trees" id="requirements-for-the-code-trees"></a>

* Was the stable tree merged **into** the feature tree recently?
* Were all RQG tests pushed into lp:randgen and documented on the RQG manual pages?
* Were all RQG or other automatable tests installed in BuildBot?
* Is the feature tree BuildBot green?

### Requirements for Closing the Worklog as Complete <a href="#requirements-for-closing-the-worklog-as-complete" id="requirements-for-closing-the-worklog-as-complete"></a>

* Was the Worklog updated with information on the testing performed?
* Was the QA check box in the Worklog ticked?
* Were all related bugs on Launchpad closed? This includes A) bugs that were tagged to belong to the feature tree, B) bugs assigned to the developer regardless of tree, C) bugs assigned to the tester and D) and orphan bugs just hanging around the same theme or time frame;
* Did the WL complete the entire review procedure, including any back-and-forth emails?
* Has the new feature been documented?

## See Also <a href="#see-also" id="see-also"></a>

* [RQG Documentation](http://github.com/RQG/RQG-Documentation/wiki/Category:RandomQueryGenerator)
* [RQG Performance Comparisons](benchmarks-and-long-running-tests/benchmarks/rqg-performance-comparisons.md)
* [RQG Extensions for MariaDB Features](rqg-extensions-for-mariadb.md)
* [Optimizer Quality](optimizer-quality.md)
* [QA Tools](qa-tools.md)

[^1]: WorkLogs

[^2]: WorkLog

[^3]: Information Schema
