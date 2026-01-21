---
description: >-
  Implementation guide specifically for developers creating logic to intercept
  and validate password changes in the server.
---

# Password Validation Plugin Development

{% include "../../../.gitbook/includes/this-page-contains-backgrou....md" %}

## Plugin API

Password validation plugin API is very simple. A plugin must implement only one method — `validate_password()`. This method takes two arguments — user name and the plain-text password. It returns `0` when the password has passed the validation; otherwise, `1`.

See also `mysql/plugin_password_validation.h` and password validation plugins in `plugin/simple_password_check/` and `plugins/cracklib_password_check/`.
