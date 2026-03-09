# MariaDB 5.2.0 Changelog

[Download](https://askmonty.org/wiki/MariaDB:Download:MariaDB_5.2.0-beta) | [Release Notes](../../old-releases/5.2/5.2.0.md) | **Changelog** |[Overview of 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md)

**Release date:** 10 Apr 2010

### Changelog

The revision number links will take you to the revision's page on Launchpad. On Launchpad you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #2783](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2783): \[merge] merged
* [Revision #2782](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2782): fixes for buildbot:
* [Revision #2781](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2781): fix dialog plugin to work again
* [Revision #2780](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2780): \[merge] Merge with local tree
* [Revision #2779](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2779): [MWL#43](https://askmonty.org/worklog/?tid=43) CREATE TABLE options (by Sanja)
* [Revision #2778](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2778): test fix for sol-sparc-32
* [Revision #2777](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2777): more fixes for buildbot failures
* [Revision #2776](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2776): fixes for builbot failures
* [Revision #2775](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2775): keep acl\_user->auth\_string and acl\_user->salt always in sync
* [Revision #2774](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2774): fix a warning
* [Revision #2773](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2773): \[merge] Merge of the code for segmented key cache ([MWL#85](https://askmonty.org/worklog/?tid=85)) into 5.2.
* [Revision #2772](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2772): fixed a bug in handling mysql\_native\_password specified explicitly:
* [Revision #2771](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2771): embedded builds used to refer to undefined functions inside if(0) { }
* [Revision #2770](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2770): more fixes for windows and status\_user.test
* [Revision #2769](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2769): fixes for windows builds
* [Revision #2768](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2768): Fixed the test according to the new plugin information
* [Revision #2767](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2767): Fied problem with of compilation without dynamic plugin loading.
* [Revision #2766](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2766): Maria \[\[MWL:61]]
* [Revision #2765](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2765): \[merge] Auto merge with 5.1
* [Revision #2764](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2764): \[merge] Auto merge with 5.1
* [Revision #2763](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2763): \[merge] Auto merge with 5.1
* [Revision #2762](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2762): \[merge] Merge with 5.1
* [Revision #2761](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2761): Fixed some compiler warnings
* [Revision #2760](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2760): Compiler warnings removed.
* [Revision #2759](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2759): Remove compiler warning
* [Revision #2758](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2758): Atomic operation removed because we do not need it.
* [Revision #2757](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2757): tell autoconf about `--with-plugin` options to avoid
* [Revision #2756](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2756): pluggable auth with plugin examples
* [Revision #2755](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2755): yet another valgrind suppression for nptl\_pthread\_exit\_hack\_handler
* [Revision #2754](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2754): mtr: it's not silent if you say it.
* [Revision #2753](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2753): bugfix: change\_user should only take the password
* [Revision #2752](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2752): make force really force
* [Revision #2751](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2751): simple speed & space optimization:
* [Revision #2750](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2750): portability fix for vcol.vcol\_partition\_myisam test
* [Revision #2749](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2749): status\_user.test fix for rbr
* [Revision #2748](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2748): flush tables before the crash in the crashing test
* [Revision #2747](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2747): fixes for the status\_user.test in ps protocol
* [Revision #2746](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2746): \[merge] Merge
* [Revision #2745](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2745): Made the vcol suite independent on time zone.
* [Revision #2744](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2744): Fixed bug [Bug #539643](https://bugs.launchpad.net/bugs/539643)
* [Revision #2743](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2743): \[merge] merged
* [Revision #2742](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2742): [MWL#98](https://askmonty.org/worklog/?tid=98) - libservices
* [Revision #2741](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2741): Group commit for maria engine.
* [Revision #2740](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2740): \[merge] merged
* [Revision #2739](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2739): Fix bad 5.1->5.2 merge: timezone must now be set explicitly for test cases that depend on it.
* [Revision #2738](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2738): \[merge] merge 5.1->5.2
* [Revision #2737](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2737): Applied Antony T Curtis patch for declaring many CHARSET objects as const
* [Revision #2736](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2736): \[merge] Merge bug fixes from 5.1
* [Revision #2735](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2735): \[merge] Merge with 5.1
* [Revision #2734](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2734): \[merge] auto-merge
* [Revision #2733](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2733): \[merge] merge 5.1-> 5.2
* [Revision #2732](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2732): \[merge] Merge of the patch introducing virtual columns into maria-5.2
* [Revision #2731](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2731): \[merge] [MWL#36](https://askmonty.org/worklog/?tid=36): Add a mysqlbinlog option to change the used database
* [Revision #2730](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2730): \[merge] Merge with 5.1 (Faster test cases)
* [Revision #2729](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2729): \[merge] Automatic merge with 5.1
* [Revision #2728](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2728): Updated test suite results with new information schemas
* [Revision #2727](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2727): Fixed version number
* [Revision #2726](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2726): userstatv2 patch from Percona and OurDelta.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
