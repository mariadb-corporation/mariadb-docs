---
description: >-
  Write dumps to and load them from local disk, Amazon S3 and S3-compatible
  storage, OCI Object Storage, and Azure Blob Storage, and where each provider's
  credentials and settings come from.
---

# Object Storage

The dump, load, and table export and import utilities read and write files through a storage layer. By default that is the local file system, but a dump can also go to a cloud object store and be loaded directly from it. The object storage options are the same for every utility that writes or reads files: `util.dump_instance()`, `util.dump_schemas()`, `util.dump_tables()`, `util.load_dump()`, `util.export_table()`, and `util.import_table()`. The copy utilities need no storage, because they pass data in memory.

{% hint style="warning" %}
The object storage backends are shared with MySQL Shell and only transfer files, so they do not depend on the database server. They have not been validated against MariaDB, however, because their test suites require cloud accounts. Local and network file systems are fully tested. Test a backup and restore with your provider before you rely on it.
{% endhint %}

You choose a provider with one option, the bucket or container name. The first argument of the function, `outputUrl` for a dump or `url` for a load, is then a path inside that bucket or container. Object stores have no directories, so the path becomes a prefix of each object name. Only one provider can be used per call. In the shell, `\? remote storage` describes all storage options.

| Storage | Selected by | Location argument |
| --- | --- | --- |
| Local or network file system | Default | `/backups/shop` or `file:///backups/shop` |
| Amazon S3 or S3-compatible storage | `s3BucketName` | A prefix in the bucket, such as `backups/shop` |
| OCI Object Storage | `osBucketName` | A prefix in the bucket, such as `backups/shop` |
| OCI Object Storage, through a pre-authenticated request | No option | The PAR URL |
| Azure Blob Storage | `azureContainerName` | A prefix in the container, such as `backups/shop` |

The bucket or container must exist. A dump requires its target directory or prefix to be empty, or not to exist yet. Each object written to cloud storage can be at most 1.2 TiB. All providers support loading a dump while it is still being written, with `waitDumpTimeout`.

## Local and Network File Systems

A plain path, or a `file://` URL, writes to the file system of the machine where MariaDB Shell runs. Relative paths are relative to the current working directory of the shell. If the target directory does not exist but its parent does, the dump creates it. Directories are created with permissions `rwxr-x---` and files with `rw-r-----`, on systems that support permissions.

```python
util.dump_schemas(["shop"], "file:///mnt/nfs/backups/shop")
```

## Amazon S3 and S3-Compatible Storage

| Option | Description |
| --- | --- |
| `s3BucketName` | The name of the S3 bucket. Enables S3 storage. |
| `s3Profile` | The profile to use from the AWS credentials and config files. |
| `s3CredentialsFile` | The AWS credentials file to use. |
| `s3ConfigFile` | The AWS config file to use. |
| `s3Region` | The region of the bucket. |
| `s3EndpointOverride` | The endpoint URL of the S3 API, for S3-compatible services. |

The other `s3*` options can only be used together with `s3BucketName`.

```python
util.dump_instance("prod/2026-10-05", {
    "s3BucketName": "acme-db-backups",
    "s3Profile": "backup",
    "s3Region": "eu-central-1",
})
```

For an S3-compatible service, such as MinIO or the object storage of another cloud provider, set `s3EndpointOverride` to the service's endpoint:

```python
util.dump_instance("prod/2026-10-05", {
    "s3BucketName": "db-backups",
    "s3EndpointOverride": "https://minio.example.com:9000",
})
```

### Where S3 Settings Come From

Each setting comes from the first source in this list that provides it:

| Setting | Sources, in order |
| --- | --- |
| Profile | `s3Profile`, `AWS_PROFILE`, `AWS_DEFAULT_PROFILE`, then `default` |
| Credentials file | `s3CredentialsFile`, `AWS_SHARED_CREDENTIALS_FILE`, then `~/.aws/credentials` |
| Config file | `s3ConfigFile`, `AWS_CONFIG_FILE`, then `~/.aws/config` |
| Region | `s3Region`, `AWS_REGION`, `AWS_DEFAULT_REGION`, the `region` of the profile in the config file, then `us-east-1` |
| Endpoint | `s3EndpointOverride`, then `https://<bucket>.s3.<region>.amazonaws.com` |

The credentials (access key, secret key, and optional session token) come from the first of these providers that has an access key or a secret key:

1. The environment variables `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN`. They are skipped when `s3Profile` is set.
2. A role assumed with the `role_arn`, `source_profile`, `credential_source`, `external_id`, `role_session_name`, and `duration_seconds` settings of the profile in the config file. Multi-factor authentication is not supported.
3. The `aws_access_key_id`, `aws_secret_access_key`, and `aws_session_token` settings of the profile in the credentials file.
4. A program named by the `credential_process` setting of the profile in the config file, which prints the credentials as JSON.
5. The same three key settings in the profile of the config file.
6. Amazon ECS container credentials.
7. Amazon EC2 instance metadata (IMDS) credentials.

If the selected provider has only one of the two keys, the operation fails. Credentials with an expiration time are refreshed before they expire. Failed requests are retried three times.

## OCI Object Storage

| Option | Description |
| --- | --- |
| `osBucketName` | The name of the OCI Object Storage bucket. Enables OCI storage. |
| `osNamespace` | The namespace of the bucket. By default it is looked up from the tenancy in the OCI configuration. |
| `ociConfigFile` | The OCI configuration file to use. |
| `ociProfile` | The profile to use from the OCI configuration file. |
| `ociAuth` | The authentication method: `api_key` (default), `security_token`, `instance_principal`, `instance_obo_user`, or `resource_principal`. |

The other `os*` and `oci*` options can only be used together with `osBucketName`.

```python
util.dump_schemas(["shop"], "shop/2026-10-05", {
    "osBucketName": "db-backups",
    "ociProfile": "BACKUP",
})
```

### Where OCI Settings Come From

| Setting | Sources, in order |
| --- | --- |
| Configuration file | `ociConfigFile`, `OCI_CLI_CONFIG_FILE`, then the `oci.configFile` shell option (default `~/.oci/config`) |
| Profile | `ociProfile`, `OCI_CLI_PROFILE`, then the `oci.profile` shell option (default `DEFAULT`) |
| Authentication method | `ociAuth`, `OCI_CLI_AUTH`, then `api_key` |

With API key and session token authentication, the `OCI_CLI_*` environment variables override the matching entries of the configuration file: `OCI_CLI_USER`, `OCI_CLI_TENANCY`, `OCI_CLI_REGION`, `OCI_CLI_FINGERPRINT`, `OCI_CLI_KEY_FILE` or `OCI_CLI_KEY_CONTENT`, `OCI_CLI_PASSPHRASE`, and, for session tokens, `OCI_CLI_SECURITY_TOKEN_FILE`.

### Pre-Authenticated Requests

A pre-authenticated request (PAR) gives access to a bucket or a prefix without an OCI configuration. Pass the PAR URL as the location and leave out `osBucketName`. A PAR URL for a prefix must end with a slash; without one, it is treated as a PAR for a single object.

| Operation | PAR type | Required access |
| --- | --- | --- |
| Dump | Bucket or prefix | Object reads and writes, and object listing |
| Load | Bucket or prefix | Object reads, and object listing |
| Export a table | Single object | Object writes |
| Import a table | Single object | Object reads |

When a load reads through a PAR, it cannot write its progress file next to the dump, so `progressFile` is required:

```python
util.load_dump(
    "https://abc123.objectstorage.eu-frankfurt-1.oci.customer-oci.com/p/TOKEN/n/acme/b/db-backups/o/shop/",
    {"progressFile": "/var/tmp/shop-load-progress.json"},
)
```

## Azure Blob Storage

| Option | Description |
| --- | --- |
| `azureContainerName` | The name of the Azure container. Enables Azure storage. |
| `azureConfigFile` | The Azure configuration file to use instead of `~/.azure/config`. |
| `azureStorageAccount` | The storage account to use. |
| `azureStorageSasToken` | A shared access signature (SAS) token to authenticate with, instead of an account key. |

The other `azure*` options can only be used together with `azureContainerName`.

```python
util.dump_schemas(["shop"], "shop/2026-10-05", {
    "azureContainerName": "db-backups",
    "azureStorageAccount": "acmebackups",
})
```

### Where Azure Settings Come From

Settings are taken from the options first, then from environment variables, then from the `[storage]` section of the configuration file:

| Setting | Environment variable | Configuration file entry |
| --- | --- | --- |
| Connection string | `AZURE_STORAGE_CONNECTION_STRING` | `connection_string` |
| Storage account | `AZURE_STORAGE_ACCOUNT` | `account` |
| Account key | `AZURE_STORAGE_KEY` | `key` |
| SAS token | `AZURE_STORAGE_SAS_TOKEN` | `sas_token` |

A connection string takes precedence over a separate account and key. A SAS token, when present, is used instead of the account key. The endpoint is `https://<account>.blob.core.windows.net` unless the connection string names another one.
