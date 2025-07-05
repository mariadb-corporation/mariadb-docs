# MariaDB Connector/J 1.5.1 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.5.1/)[Release Notes](../../1.5/mariadb-connector-j-151-release-notes.md)[Changelog](mariadb-connector-j-151-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 16 Aug 2016

For the highlights of this release, see the[release notes](../../1.5/mariadb-connector-j-151-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #0fcf874](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0fcf874) - \[misc] updating documentation - from kolzeq
* [Revision #fc156f5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/fc156f5) - \[[CONJ-329](https://jira.mariadb.org/browse/CONJ-329)] & \[[CONJ-330](https://jira.mariadb.org/browse/CONJ-330)] rewriteBatchedStatements single query correction - from kolzeq
* [Revision #4b1f278](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4b1f278) - \[misc] updating maven plugins versions - from kolzeq
* [Revision #eeddebb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/eeddebb) - \[misc] correction travis with .m2 corruption - from kolzeq
* [Revision #5f61b4a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5f61b4a) - \[misc] update checkstyle - from kolzeq
* [Revision #3480535](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3480535) - \[misc] java.lang.NoClassDefFoundError: org/apache/maven/shared/filtering/MavenFilteringException travis correction - from kolzeq
* [Revision #a8bd50e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a8bd50e) - \[misc] suppressing maven travis error "java.lang.NoClassDefFoundError: org/apache/maven/shared/filtering/MavenFilteringException" - from kolzeq
* [Revision #9a58957](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9a58957) - Merge branch 'feature/[CONJ-325](https://jira.mariadb.org/browse/CONJ-325)' into develop - from kolzeq
* [Revision #62cc603](https://github.com/mariadb-corporation/mariadb-connector-j/commit/62cc603) - Merge branch 'develop' into feature/[CONJ-325](https://jira.mariadb.org/browse/CONJ-325) - from kolzeq
* [Revision #037eab1](https://github.com/mariadb-corporation/mariadb-connector-j/commit/037eab1) - \[misc] timestamp default value test avoid NO\_ZERO\_DATE strict mode - from kolzeq
* [Revision #f2e734c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f2e734c) - \[misc] timestamp default value test avoid NO\_ZERO\_DATE strict mode - from kolzeq
* [Revision #415aa37](https://github.com/mariadb-corporation/mariadb-connector-j/commit/415aa37) - \[[CONJ-325](https://jira.mariadb.org/browse/CONJ-325)] implementation simplification - from kolzeq
* [Revision #52a25f6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/52a25f6) - Merge branch 'develop' into feature/[CONJ-325](https://jira.mariadb.org/browse/CONJ-325) - from kolzeq
* [Revision #346d0d7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/346d0d7) - \[misc] correcting test without using mariaDB test, since server tagged version can now be changed - from kolzeq
* [Revision #0748747](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0748747) - \[misc] correcting socketTimeout possible NPE - from kolzeq
* [Revision #e7e7d7e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e7e7d7e) - \[misc] correcting socketTimeout possible NPE - from kolzeq
* [Revision #20707ed](https://github.com/mariadb-corporation/mariadb-connector-j/commit/20707ed) - \[[CONJ-325](https://jira.mariadb.org/browse/CONJ-325)] merging PR-86 Aurora auto discovery - from kolzeq
* [Revision #0fefe45](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0fefe45) - Merge remote-tracking branch 'symbolic\_name\_origin\_or\_upstream/pr/86' into feature/[CONJ-325](https://jira.mariadb.org/browse/CONJ-325) - from kolzeq
* [Revision #8e067d0](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8e067d0) - \[[CONJ-320](https://jira.mariadb.org/browse/CONJ-320)] handling socketTimeout with solution to avoid synchronisation between write and read - from kolzeq
* [Revision #8122601](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8122601) - \[misc] updating revision tag to RC2-SNAPSHOT - from kolzeq
* [Revision #911fee9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/911fee9) - Handling connection string case since there is no more restriction: - In the case that the user uses the writer instance and the cluster endpoint as their connection string, set isFineIfOnlyMasterFound to true - Otherwise,
* [Revision #bcd734e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/bcd734e) - Changed urlParser size checks: - Since cluster endpoint is no longer included in the urlParser variable, all size checks of this variable must decrease by one - from Phan
* [Revision #c1259b0](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c1259b0) - Removed cluster host address from urlParser: - No need to have the cluster host address stored here since it is already stored in its own variable and is used when necessary - Tests need to know the cluster endpoint, not just
* [Revision #3d1519d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3d1519d) - Change for when the only known endpoint is the cluster endpoint: - Look for secondary so that setReadOnly is quicker. The change to not temporarily connect to the cluster endpoint required reconnectFailedConnection to be ca
* [Revision #ffc4dfe](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ffc4dfe) - Changes based on feedback regarding cluster endpoint use: - Cluster endpoint was previously temporarily connected to retrieve data; if the cluster endpoint can be connected, the driver will now use it as the connection w
* [Revision #dda8bf9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/dda8bf9) - Allow previous URL configuration: - Exception is no longer thrown if the URL is not a single cluster endpoint - Added checks to verify that there is a cluster endpoint before using it - Removed no longer appropriate tests - f
* [Revision #cea40ac](https://github.com/mariadb-corporation/mariadb-connector-j/commit/cea40ac) - Changes made based on feedback & improvements: - Removed use of TimeZone.setDefault - setTimeZone used instead on date formatter - Variable urlEndStr is set on AuroraListener initilization - Remains the same for a clus
* [Revision #a461945](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a461945) - Fix for Travis build fail: - Travis build would fail because it would unexpectedly continue outside of the catch block after throwing an exception, which it does not do when running the JUnit tests - from Phan
* [Revision #3e5ad47](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3e5ad47) - Import missing has been added - from Phan
* [Revision #82dd75c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/82dd75c) - Synchronized the array list in setUrlParserFromEndpoints - For thread safety - Change based on feedback - from Phan
* [Revision #0af765c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0af765c) - Removed automatic correction for 'java.sql.' by IntelliJ and remaining print out forgotten - from Phan
* [Revision #6c91d36](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6c91d36) - Implemented the self-discovery feature, wrote tests, simplified existing code and fixed typos. - from Phan

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
