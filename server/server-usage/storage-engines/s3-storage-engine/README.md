---
description: >-
  Integrate MariaDB Server with Amazon S3 using the S3 Storage Engine. Learn how
  to store and retrieve data directly from cloud object storage for scalability
  and cost efficiency.
---

# S3 Storage Engine

{% columns %}
{% column %}
{% content-ref url="using-the-s3-storage-engine.md" %}
[using-the-s3-storage-engine.md](using-the-s3-storage-engine.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This guide covers typical use cases for the S3 engine, such as archiving inactive tables, and details supported operations like ALTER TABLE and SELECT.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="s3-storage-engine-status-variables.md" %}
[s3-storage-engine-status-variables.md](s3-storage-engine-status-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A list of status variables for monitoring the S3 engine's interactions with the cloud service, although specific variables are not extensively documented here.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="s3-storage-engine-system-variables.md" %}
[s3-storage-engine-system-variables.md](s3-storage-engine-system-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This page lists system variables to configure the S3 engine, including AWS credentials, bucket names, page cache sizes, and connection protocols.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="s3-storage-engine-internals.md" %}
[s3-storage-engine-internals.md](s3-storage-engine-internals.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about the internal architecture of the S3 engine, which inherits from Aria code but redirects reads to S3, using a dedicated page cache.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="testing-the-connections-to-s3.md" %}
[testing-the-connections-to-s3.md](testing-the-connections-to-s3.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Instructions on how to verify your S3 configuration using tools like `aria_s3_copy` and the `mysql-test-run` suite to ensure proper connectivity.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="aria_s3_copy.md" %}
[aria_s3_copy.md](aria_s3_copy.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A reference for the `aria_s3_copy` tool, which is used to manually copy Aria tables to and from S3 storage for testing and data migration.
{% endcolumn %}
{% endcolumns %}
