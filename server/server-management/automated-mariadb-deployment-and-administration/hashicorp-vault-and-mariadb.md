# HashiCorp Vault and MariaDB

Vault is open source software for secret management provided by HashiCorp. It is designed to avoid sharing secrets of various types, like passwords and private keys. When building automation, Vault is a good solution to avoid storing secrets in plain text in a repository.

{% hint style="danger" %}
**Unsafe Operations** \
It is unsafe to execute `vault secrets disable` or `vault token revoke` while MariaDB is running. Abruptly removing access to the Vault could prevent InnoDB from encrypting data pages during background flushes or log writes, which can lead to a server crash.
{% endhint %}

{% hint style="success" %}
Always ensure the MariaDB server has completed a clean shutdown before disabling Vault secrets or revoking access tokens.
{% endhint %}

MariaDB and Vault may relate to each other in several ways:

* MariaDB has a [Hashicorp Key Management plugin](../../security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin.md), to manage and rotate SSH keys.
* Users passwords can be stored in Vault.
* MariaDB (and MySQL) can be used as a secret engine, a component which stores, generates, or encrypts data.
* MariaDB (and MySQL) can be used as a backend storage, providing durability for Vault data.

For information about how to install Vault, see [Install Vault](https://developer.hashicorp.com/vault/install), as well as [MySQL/MariaDB Database Secrets Engine](https://developer.hashicorp.com/vault/docs/secrets/databases/mysql-maria).

{% hint style="info" %}
Namespace support is available as of MariaDB Enterprise Server 11.8.

See the [Hashicorp namespaces documentation](https://developer.hashicorp.com/vault/docs/enterprise/namespaces) for details.
{% endhint %}

## Vault Features

Vault is used via an HTTP/HTTPS API.

Vault is identity-based. Users login and Vault sends them a token that is valid for a certain amount of time, or until certain conditions occur. Users with a valid token may request to obtain secrets for which they have proper permissions.

Vault encrypts the secrets it stores.

Vault can optionally audit changes to secrets and secrets requests by the users.

## Vault Architecture

Vault is a server. This allows decoupling the secrets management logic from the clients, which only need to login and keep a token until it expires.

The sever can actually be a cluster of servers, to implement high availability.

The main Vault components are:

* Storage Backed: This is where the secrets are stored. Vault only send encrypted data to the backend storage.
* HTTP API: This API is used by the clients, and provides an access to Vault server.
* Barrier: Similarly to an actual barrier, it protects all inner Vault components. The HTTP API and the storage backend are outside of the barrier and could be accessed by anyone. All communications from and to these components have to pass through the barrier. The barrier verifies data and encrypts it. The barrier can have two states: sealed or unsealed. Data can only pass through when the barrier is unsealed. All the following components are located inside the barrier.
* Auth Method: Handles login attempts from clients. When a login succeeds, the auth method returns a list of security policies to Vault core.
* Token Store: Here the tokens generated as a result of a succeeded login are stored.
* Secrets Engines: These components manage secrets. They can have different levels of complexity. Some of them simply expect to receive a key, and return the corresponding secret. Others may generate secrets, including one-time-passwords.
* Audit Devices: These components log the requests received by Vault and the responses sent back to the clients.There may be multiple devices, in which case an Audit Broker sends the request or response to the proper device.

## Dev Mode

It is possible to start Vault in dev mode:

```bash
vault server -dev
```

Dev mode is useful for learning Vault, or running experiments on some particular features. It is extremely insecure, because dev mode is equivalent to starting Vault with several insecure options. This means that Vault should never run in production in dev mode. However, this also means that all the regular Vault features are available in dev mode.

Dev mode simplifies all operations. Actually, no configuration is necessary to get Vault up and running in dev mode. It makes it possible to communicate with the Vault API from the shell without any authentication. Data is stored in memory by default. Vault is unsealed by default, and if explicitly sealed, it can be unsealed using only one key.

For more details, see ["Dev" Server Mode](https://www.vaultproject.io/docs/concepts/dev-server) in Vault documentation.

## Vault Resources and References

* [Documentation](https://www.vaultproject.io/docs).
* [MySQL/MariaDB Database Secrets Engine](https://www.vaultproject.io/docs/secrets/databases/mysql-maria).
* [MySQL Storage Backend](https://www.vaultproject.io/docs/configuration/storage/mysql).

Content initially contributed by [Vettabase Ltd](https://vettabase.com/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
