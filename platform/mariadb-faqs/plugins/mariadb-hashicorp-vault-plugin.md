# MariaDB HashiCorp Vault Plugin

* Q: What is the MariaDB HashiCorp Vault Plugin and its purpose?\
  A: The MariaDB HashiCorp Vault Plugin is an enterprise-grade feature designed to integrate MariaDB Enterprise Server with HashiCorp Vault. Its primary purpose is to enable MariaDB to use HashiCorp Vault as an external, centralized Key Management System (KMS) for securely managing the encryption keys used for MariaDB's Data-at-Rest Encryption (TDE) features.
* Q: What security problem does the MariaDB HashiCorp Vault Plugin address?\
  A: This plugin addresses a significant security challenge by decoupling the management of sensitive encryption keys from the database server itself. Instead of storing encryption keys locally on the database server (which could be a security risk if the server is compromised), the keys are securely stored, managed, and versioned within HashiCorp Vault, a dedicated secrets management tool designed for high security.
* Q: What are the main benefits of using HashiCorp Vault for MariaDB key management via this plugin?\
  A: The main benefits include:
  * Centralized Key Management: All encryption keys are managed in one secure, external location.
  * Enhanced Security: Vault provides robust access control, authentication, and detailed audit trails for key usage.
  * Simplified Key Rotation: Vault facilitates easier and more secure key rotation policies.
  * Improved Compliance: Helps meet security and compliance policies that often mandate the use of external key management systems and separation of duties.
  * Reduced Risk: Minimizes the risk of encryption key compromise even if the database server itself is breached.
* Q: How does MariaDB Enterprise Server access encryption keys from HashiCorp Vault using the plugin?\
  A: The MariaDB HashiCorp Vault Plugin enables MariaDB Enterprise Server to securely connect to a configured HashiCorp Vault instance. It authenticates with Vault using appropriate credentials or tokens and then retrieves the necessary encryption keys on demand when MariaDB needs to encrypt new data or decrypt existing encrypted data.
* Q: Is the MariaDB HashiCorp Vault Plugin a commercial or open-source feature?\
  A: The MariaDB HashiCorp Vault Plugin for Data-at-Rest Encryption is a commercial, enterprise feature. It is available as part of the MariaDB Enterprise Server subscription offered by MariaDB plc.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
