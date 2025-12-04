# MariaDB Release Criteria

The MariaDB development release policy has the following project commitments for the maturity stages:

### Commitment for Alpha Releases

New features are being added. Some old features may be removed. Users can start trying Alpha versions out, but should not expect feature stability yet. Still, [Buildbot](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/general-info/tools/buildbot) should show no regressions and [Jira](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/general-info/tools/jira) should have no open [Blocker](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/community/bug-tracking/mariadb-community-bug-processing) level bugs for this release.

### Commitment for Beta Releases

Features can not be removed anymore. Users can start building applications using MariaDB Beta releases. Any application that works with MariaDB Beta release will continue to work with a RC and GA release. The syntax that was valid in Beta will stay valid, tables created in Beta will stay readable, Beta clients will be able to connect to GA servers, and so on.

### Commitment for Gamma/RC Releases

The server is feature complete. No new features, no changes in default settings are possible. From this point only bug fixes are accepted into the server.

### Commitment for Stable/GA Releases

We believe the code is ready for general usage (based on bug inflow).

### Plugins

Plugins generally follow the same rules, but they have [their own maturity levels](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/list-of-plugins). That is, a plugin is declared Gamma when it becomes feature complete. This happens independently from the server being Alpha, Beta, RC, or GA.

### Security Releases

See our [security policy](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/community/bug-tracking/mariadb-security-bug-fixing-policy) page for information of how and when emergency security releases are done.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
