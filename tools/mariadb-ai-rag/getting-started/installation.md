# Installation

## System Requirements

* **Operating System**: Linux (Debian/Ubuntu/RHEL), macOS 10.15+, or Windows 10/11
* **CPU**: 4+ cores recommended
* **RAM**: Minimum 8GB, 16GB+ recommended
* **Storage**: 10GB for installation, additional space for document storage
* **Database**: MariaDB 10.6+ or compatible MySQL 8.0+
* **Python**: Version 3.9+ (included in the installation package)

## Installation Procedure

{% tabs %}
{% tab title="Debian/Ubuntu" %}
#### Debian/Ubuntu Installation

1. Download the Debian / Ubuntu `.deb` installation package from:
   * [https://mariadb.com/downloads/enterprise-tooling/ai-rag/](https://mariadb.com/downloads/enterprise-tooling/ai-rag/)
2.  Install the package:

    ```bash
    sudo dpkg -i ai-rag-*.deb	
    ```
3.  Install dependencies:

    ```bash
    sudo apt-get install -f
    ```
{% endtab %}

{% tab title="RHEL" %}
#### RHEL (and equivalents) Installation

1. Download the RHEL `.rpm` installation package from:
   * [https://mariadb.com/downloads/enterprise-tooling/ai-rag/](https://mariadb.com/downloads/enterprise-tooling/ai-rag/)
2.  Install the package:

    ```bash
    sudo rpm -i ai-rag-*.rpm
    ```
{% endtab %}

{% tab title="Windows" %}
#### Windows Installation

1. Download the Windows `.msi` installation package from:
   * [https://mariadb.com/downloads/enterprise-tooling/ai-rag/](https://mariadb.com/downloads/enterprise-tooling/ai-rag/)
2. Run the `.msi` installer.
3. Follow the installation wizard instructions.
{% endtab %}
{% endtabs %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
