# MariaDB 5.2.1 Changelog

[Download](https://askmonty.org/wiki/MariaDB:Download:MariaDB_5.2.1-beta) | [Release Notes](../../old-releases/5.2/5.2.1.md) | **Changelog** |[Overview of 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md)

**Release date:** 18 Jun 2010

For the highlights of this release, see the [release notes](../../old-releases/5.2/5.2.1.md).

The revision number links will take you to the revision's page on Launchpad. On Launchpad you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #2784](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2784): don't hide old\_password\_plugin from embedded, it may be compiled with grant support
* [Revision #2785](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2785): Automerge [mariadb 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md) -> [mariadb 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md)
* [Revision #2786](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2786): Merge OQGraph into [MariaDB 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md).
* [Revision #2787](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2787): small changes to \[\[mwl:43]]:
  * consistency: don't use "index" and "key" interchangeably
    * rename "key" to "index"
  * consistency: all option types are logical, besides ULL
    * rename ULL to NUMBER
  * don't accept floats where integers are expected
  * accept hexadecimal where integers are expected
* [Revision #2788](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2788): create table options bug: alter table does not reset HA\_OPTION\_TEXT\_CREATE\_OPTIONS when the last option value is removed
* [Revision #2789](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2789): create table options bug: parse\_engine\_table\_options() was only called when there was at least option with a non-default value. otherwise it was not called and option structure was not allocated at all. NULL pointer dereference in ::open().
* [Revision #2790](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2790): A temporary solution to make CREATE TABLE attributes to work when a table is partitioned
* [Revision #2791](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2791): make table option reader more future-proof
* [Revision #2792](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2792): don't error out on unknown options in the replication thread or when opening a table
* [Revision #2793](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2793): crash on `--with-embedded-privilege-control` builds:
  1. fix broken change user handling (no restart should happen in the normal case)
  2. add assert to guarantee that we never send a request to change to the same plugin
  3. "fix" plugin string as sent by the client to be able to compare native plugins by pointers
  4. more complete MYSQL initialization in the embedded case
  5. change\_user.test updated to handle -with-embedded-privilege-control builds
* [Revision #2794](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2794): oqgraph fix: not all gcc versions support -fvisibility-inlines-hidden
* [Revision #2795](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2795): merge 5.1->5.2
* [Revision #2796](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2796): mysql: don't crash when `--show-warnings` is enabled and the server suddenly goes away
* [Revision #2797](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2797): rename "partitioned key cache" to "segmented"
* [Revision #2798](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2798): first initialize variable, then use it, not the other way around
* [Revision #2799](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2799): only run maria tests if maria is compiled in
* [Revision #2800](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2800): [MWL#43](https://askmonty.org/worklog/?tid=43): initialize lex->option\_list for foreign keys
* [Revision #2801](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2801): merge 5.1->5.2
* [Revision #2802](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2802): handle a case when a user connects with a password to a passwordless account
* [Revision #2803](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2803): fixes for test suite
* [Revision #2804](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2804): include guards
* [Revision #2805](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2805): fixes for a few small MySQL bugs/issues that impact the engines, as discussed in the [Storage Engine summit](https://mariadb.com/docs/server/server-usage/storage-engines)
  * remove handler::index\_read\_last()
  * create handler::keyread\_read\_time() (was get\_index\_only\_read\_time() in opt\_range.cc)
  * ha\_show\_status() allows engine's show\_status() to fail
  * remove HTON\_FLUSH\_AFTER\_RENAME
  * fix key\_cmp\_if\_same() to work for floats and doubles
  * set table->status in the server, don't force engines to do it
  * increment status vars in the server, don't force engines to do it
* [Revision #2811](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2811): innodb\_plugin needs to be built with -lmysqlservices
* [Revision #2812](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2812): bug in converting st\_mysql\_plugin to st\_maria\_plugin - all but the last plugins in a dl were lost
* [Revision #2814](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2814): `--plugin-maturity` command-line option
* [Revision #2815](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2815): fix for valgrind warning
* [Revision #2816](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2816): plugin\_maturity.test needs example plugin to be built

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
