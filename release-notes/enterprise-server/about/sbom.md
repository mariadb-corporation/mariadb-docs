---
description: MariaDB Enterprise Server Software Bill of Materials (SBOM) information
---

# SBOM

MariaDB publishes a Software Bill of Materials (SBOM) for each MariaDB Enterprise Server release. An SBOM lists the components that make up a build (libraries, packages, versions, licenses, and hashes); enabling customers to meet compliance requirements, perform vulnerability management, and understand supply chain risk.

## About

**Coverage:** Core MariaDB Enterprise Server binaries and packages for each supported platform/release

**Formats:** CycloneDX JSON (.json)

**Contents:** Component names & versions, suppliers, licenses, purls/CPEs (when available), cryptographic hashes, and dependencies

**Availability:** SBOM files are provided alongside each release’s download artifacts in the customer portal, or from the "Software Bill of Materials (SBOM)" link on the [Enterprise Server download page](https://mariadb.com/downloads/enterprise/)

**Updates:** A new SBOM is published for every release; compare SBOMs across versions to see component deltas

## **Recommended Uses**

* **Vulnerability management:** Import the SBOM into a scanner or platform to match against advisories (e.g., OSV/CVE feeds)
* **Compliance & audits:** Produce component/license reports and demonstrate software composition controls
* **Change analysis:** Diff SBOMs between versions to identify updated/deprecated components

## Viewing SBOM Files

The recommended viewer for the MariaDB SBOM files is the CycloneDX Web Tool (hosted by the CycloneDX project), which can be found at [https://cyclonedx.github.io/cyclonedx-web-tool](https://cyclonedx.github.io/cyclonedx-web-tool?utm_source=chatgpt.com)

Advantages of the CycloneDX Web Tool include:

* Our SBOM files are explicitly built for CycloneDX including upload/view functionality for both XML and JSON
* The CycloneDX Web Tool is maintained by the CycloneDX project so it aligns with the standard and will remain compatible
* The CycloneDX Web Tool works via browser so you do not need to install anything

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
