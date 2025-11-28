# Feature Deprecation Policy

From time to time some features in MariaDB will be marked something as deprecated. This is done to warn MariaDB users that the feature is likely to disappear in some upcoming major version and give them time to adapt to the change.

The policy is that "It is unacceptable for a user to upgrade from a supported version `A` where a feature works normally to a version `B` where a feature doesn't exist without an advanced warning."

Thus, when a feature is removed for some reason, the sequence of steps is as follows:

1. the feature is marked as deprecated.
2. we wait until all releases where the feature is not deprecated have reached EOL.
3. now the feature can be removed in the next major version before GA. It will not be removed in a minor update!

With an LTS lifetime of 5 years, step 2 normally means that a feature cannot be removed until it's marked deprecated for 5 years.

Typical things that are deprecated:

* Variables, options or status variables that have lost their meaning or have been renamed.
* Features/behavior that have been replaced with better functionality.
* Features that conflicts with the SQL standard.
* Features that are depending on outside contributors that are not active anymore and no new developers have stepped in to take over and that the MariaDB team is not able to keep developing or keeping up to date.
  * This includes storage engines and plugins that are not being used or developed.
* Features that depend on libraries that are no longer available in newer OS versions.

We do our best to ensure that upgrading to a new major version of MariaDB is as smooth and uneventful as possible. This means that we go to great lengths to keep things compatibility, even when removing deprecated features:

* MariaDB server will keep old startup variables around even after they are removed (deprecation has taken effect). Assigning a value to a removed variable will produce a warning in the error log.
* Some removed features/behavior that we know is still important for some users, we still keep available behind a dedicated [old-mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/old_mode) option, which will give it at least 5 more years until disappearance.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
