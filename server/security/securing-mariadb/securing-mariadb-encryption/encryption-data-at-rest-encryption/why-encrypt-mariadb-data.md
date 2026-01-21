---
description: >-
  Explains the importance of data-at-rest encryption for mitigating physical
  theft risks and meeting regulatory compliance standards such as GDPR, HIPAA,
  and PCI DSS.
---

# Why Encrypt MariaDB Data?

Nearly everyone owns data of immense value: customer data, construction plans, recipes, product designs and other information. These data are stored in clear text on your storage media. Everyone with file system access is able to read and modify the data. If this data falls into the wrong hands (criminals or competitors) this may result in serious consequences.

With encryption you protect Data At Rest (see the [Wikipedia article](https://en.wikipedia.org/wiki/Data_at_Rest)). That way, the database files are protected against unauthorized access.

## When Does Encryption Help to Protect Your Data?

Encryption helps in case of threats against the database files:

* An attacker gains access to the system and copies the database files to avoid the MariaDB authorization check.
* MariaDB is operated by a service provider who should not gain access to the sensitive data.

## When is Encryption No Help?

Encryption provides no additional protection against threats caused by authorized database users. Specifically, SQL injections aren’t prevented.

## What to Encrypt?

All data that is not supposed to fall into possible attackers hands should be encrypted. Especially information, subject to strict data protection regulations, is to be protected by encryption (e.g. in the healthcare sector: patient records). Additionally, data being of interest for criminals should be protected. Data which should be encrypted are:

* Personal related information
* Customer details
* Financial and credit card data
* Public authorities' data
* Construction plans and research and development results

## How to Handle Key Management?

There are currently three options for key management:

* [File Key Management Plugin](../../encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin.md)
* [AWS Key Management Plugin](../../encryption/data-at-rest-encryption/key-management-and-encryption-plugins/aws-key-management-encryption-plugin.md)
* [Hashicorp Key Management Plugin](../../encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin.md)

See [Encryption Key Management](key-management-and-encryption-plugins/encryption-key-management.md) for details.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
