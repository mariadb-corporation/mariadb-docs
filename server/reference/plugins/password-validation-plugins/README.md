---
description: >-
  Password validation plugins, like simple_password_check and cracklib, enforce
  strong password policies by checking new passwords against defined complexity
  rules.
---

# Password Validation Plugins

{% columns %}
{% column %}
{% content-ref url="password-validation.md" %}
[password-validation.md](password-validation.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
General introduction into plugins that enforce specific security policies and complexity rules for user passwords.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="cracklib-password-check-plugin.md" %}
[cracklib-password-check-plugin.md](cracklib-password-check-plugin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The Cracklib Password Check Plugin enforces password strength by validating new passwords against the CrackLib library and its dictionary.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="password-reuse-check-plugin.md" %}
[password-reuse-check-plugin.md](password-reuse-check-plugin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The Password Reuse Check Plugin prevents users from reusing previous passwords, with a retention policy controlled by the password_reuse_check_interval variable.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="password_reuse_check_interval.md" %}
[password_reuse_check_interval.md](password_reuse_check_interval.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This system variable defines the retention period in days for the password history used by the Password Reuse Check Plugin to prevent reuse.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="simple-password-check-plugin.md" %}
[simple-password-check-plugin.md](simple-password-check-plugin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The Simple Password Check Plugin enforces basic password complexity rules, such as minimum length and required numbers of digits, letters, and special characters.
{% endcolumn %}
{% endcolumns %}
