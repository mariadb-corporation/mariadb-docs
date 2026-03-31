# Secret Management

The MariaDB AI RAG system allows you to manage sensitive credentials (like API keys and database passwords) through the following configurations:

## **Standalone Mode**

* Configuration File: `config.env.secure.local`.
* Secret Management: Secrets are stored as direct environment variables within the local file.
* Best For: Local development, individual testing, and single-user setups where simplicity is preferred over external secret orchestration.

## **Vault Mode**

* Configuration File: `config.env.vault.local`.
* Secret Management: Integrates with a local HashiCorp Vault instance.
* Security: Secrets are stored securely in Vault and accessed via a root token and specific path (`secret/rag-in-a-box`).
* Best For: Team development environments and production-like local setups.

## **1Password Mode**

* Configuration File: `config.env.1password.employee`.
* Secret Management: Uses 1Password CLI references to pull secrets directly from an employee or team vault.
* Example Reference: `GEMINI_API_KEY=op://Employee/RAG-API-Keys/gemini`.
* Best For: Enterprises already using 1Password for credential management across their workforce.

## **HCP Vault Mode**

* Configuration File: `config.env.hcp.live`.
* Secret Management: Connects to the HashiCorp Cloud Platform (HCP) managed Vault service.
* Best For: Scalable, production cloud deployments where a managed secret service is required for high availability.

## Implementation Summary

| **Mode**   | **Target File**                 | **Security Method**   | **Primary Use Case**   |
| ---------- | ------------------------------- | --------------------- | ---------------------- |
| Standalone | `config.env.secure.local`       | Plaintext Env Vars    | Development / Solo     |
| Vault      | `config.env.vault.local`        | Local HashiCorp Vault | Team Dev / Pre-prod    |
| 1Password  | `config.env.1password.employee` | 1Password CLI         | Enterprise / Corporate |
| HCP Vault  | `config.env.hcp.live`           | Managed Cloud Vault   | Production Cloud       |

\{% @marketo/form formId="4316" %\}
