# MCS Backup and Restore Commands

This page documents how to create and restore MariaDB Enterprise ColumnStore backups using the `mcs` CLI.

The `mcs backup` and `mcs restore` commands support the same workflows as the `mcs_backup_manager.sh` script, including:

* Full and incremental backups
* Local/shared storage and S3 storage topologies
* Optional compression and parallelism
* Separate DBRM (metadata) backup/restore workflows

{% hint style="info" %}
The examples in this page assume the `mcs` command is available on the host and you run the backup/restore operations as `root`.
{% endhint %}

## Before You Start

### Identify Your Storage Topology

On a ColumnStore node, determine which StorageManager service is configured:

```bash
grep "service" /etc/columnstore/storagemanager.cnf
```

Example output:

* `service = LocalStorage`
* `service = S3`

{% hint style="tip" %}
Use `service = LocalStorage` when ColumnStore data lives on local/shared storage, and `service = S3` when ColumnStore data is stored in object storage.
{% endhint %}

### Estimate Backup Size

LocalStorage:

```bash
du -sh /var/lib/columnstore/
```

S3:

```bash
du -sh /var/lib/columnstore/storagemanager/ ;
aws s3 ls s3://<bucketname> --recursive | grep -v -E "(Bucket: |Prefix: |LastWriteTime|^$|--)" | awk 'BEGIN {total=0}{total+=$3}END{print total/1024/1024/1024" GB"}'
```

## Backups

## LocalStorage Topology Backups

### Instructions

1. Run `mcs backup` as `root` on **each node**, starting with the primary node.
2. Use the same backup location on each node.

### List Your Backups

```bash
mcs backup --backup-location /tmp/backups/ --list
```

Example output:

```text
Existing Backups
--------------------------------------------------------------------------
Options                                       Last-Updated  Extent Map      EM-Size      Journal-Size VBBM-Size  VSS-Size   Days Old
12-03-2024                                    Dec 3 21:05   BRM_saves_em    77228        0            1884       2792       12
11-21-2024                                    Nov 21 21:05   BRM_saves_em    77228        0            1884       2792       12
--------------------------------------------------------------------------
Restore with mcs restore --path /tmp/backups/ --directory <backup_folder_from_above>
```

### Quick Examples

Full backup:

```bash
mcs backup
```

Parallel backup:

```bash
mcs backup --parallel 8
```

Compressed backup:

```bash
mcs backup --parallel 8 --compress pigz
```

Incremental backup (auto-select most recent full backup):

```bash
mcs backup --incremental auto_most_recent
```

Save the backup to a remote host (SCP):

```bash
mcs backup --backup-destination Remote --scp root@192.68.0.1
```

### Online Backup Example

When you run a backup, by default the tooling performs polling checks and attempts to obtain a consistent point-in-time backup by:

* checking for active writes
* checking for running `cpimport` jobs
* issuing write locks
* saving BRM prior to copying

You can skip these safety mechanisms with:

* `--skip-polls`
* `--skip-locks`
* `--skip-save-brm`

{% hint style="warning" %}
Skipping polls/locks/BRM saving can be useful for certain workflows, but it increases the risk of capturing a partially-written state that complicates restore.
{% endhint %}

```bash
mcs backup -P 8
```

#### Incremental Backup Example
{% hint style="warning" %}
Before you can run an incremental backup, you need a full backup taken.
{% endhint %}
Then taking an incremental backup you need to define the full backup name to increment via flag `--incremental xxxxx`.
```bash
# Run Full Backup
mcs backup -P 8
# Backup Complete @ /tmp/backups/12-03-2025
# Run the incremental backup - updating the full backup 12-03-2025
mcs backup --incremental 12-03-2025
```

Incremental backups add ColumnStore deltas to an existing full backup. You can either:

* specify the full backup folder name explicitly, or
* use `auto_most_recent` will select the most recent directory defined in `--backup-location` to apply the incremental backup to the most recent full backup

Apply to the most recent full backup:

```bash
mcs backup --incremental auto_most_recent
```

Apply to a specific full backup folder:

```bash
mcs backup --incremental <full-backup-folder>
```

### Cron Backup Example

Create a cron job (run as root) that takes periodic backups and appends logs:

```bash
sudo crontab -e
```

Every Night Full Backup retaining the last 14 days:

```text
*/60 */24 * * *  mcs backup --parallel 4 -r 14 >> /tmp/cs_backup.log  2>&1
```

Full backup once a week (Saturday night) w/ incremental backups all the other nights (keep 21 days)
```text
59 23 * * 6 mcs backup -P 8 -r 21 >> /root/cs_backup.log 2>&1
59 23 * * 0-5 mcs backup --incremental auto_most_recent -r 21 >> /root/cs_backup.log 2>&1
59 23 * * 7 mcs backup --incremental auto_most_recent -r 21 >> /root/cs_backup.log 2>&1
```

### LocalStorage Backup Flags

The most commonly used options are:

| Flag / Option | Description | Notes |
| --- | --- | --- |
| `--backup-location` (`-bl`) | Defines the path where the backup should be saved to. A date based folder under this path will be created per backup run automatically. You can change the name of the folders with `-nb` | Typical default in tooling: `/tmp/backups/` |
| `--backup-destination` (`-bd`) | Where backups are stored relative to the node running the command. Two possible values: `Local` or `Remote`. Determines if the backup requires ssh thus `-scp` needs to be defined too or if the `-bl` path is relative to the script| `Local` or `Remote` |
| `--secure-copy-protocol` (`-scp`) | if `--backup-destination` is defined as `Remote` , then you need to define `-scp` . This defines the ssh connection to remotely rsync to | Example: `-bd Remote -scp root@192.168.0.1` |
| `--incremental` (`-i`) | Creates an incremental backup based on an existing full backup | Value can be `<folder>` or `auto_most_recent` |
| `--parallel` (`-P`) | Enables parallel rsync and defines the number of parallel rsync threads to run. If combined with `--compress` this flag defines the number of compression threads to run. Default is `4` | Example: `--parallel 8` |
| `--compress` (`-c`) | Compress backup in X format | Supported: `pigz` |
| `--quiet` (`-q`) | Silence verbose copy command outputs | Useful for cron jobs |
| `--name-backup` (`-nb`) | Define the name of the backup - default: `date +%m-%d-%Y` | Example: `-nb before-upgrade-backup` |
| `--retention-days` (`-r`) | Retain backups created within the last X days; delete older ones | `0` means keep all |
| `--apply-retention-only` (`-aro`) | Only apply retention policy; do not run a backup | Works with `--retention-days` |
| `--list` (`-li`) | List backups | Lists backups in the configured location |

## S3 Topology Backups

### Instructions

1. Ensure the node has access to your S3 endpoint and credentials.
2. Run `mcs backup` with `--storage S3` and a backup bucket (`--backup-bucket`).
3. Run it as `root` on **each node**, starting with the primary node.

{% hint style="info" %}
If you're using an on-premise S3-compatible solution, you may need `--endpoint-url` (and sometimes `--no-verify-ssl`).
{% endhint %}

### Quick Examples

Full backup:

```bash
mcs backup --storage S3 --backup-bucket s3://my-cs-backups
```

Compressed backup (and skip copying bucket data if you only want local artifacts):

```bash
mcs backup --storage S3 --backup-bucket s3://my-cs-backups --compress pigz --quiet --skip-bucket-data
```

Incremental backup:

```bash
mcs backup --storage S3 --backup-bucket gs://my-cs-backups --incremental 12-18-2023
```

On-premise S3 endpoint:
Key Flags for on premise buckets are the following:

* `-url` - the local/ip address of the S3 provider. For example, minio defaults to port 9000, 127.0.0.1 would be used if minio is installed on the same machine running columnstore
* `--no-verify-ssl` - used when ssl certs are not used/defined for the S3 provider/endpoint

```bash
mcs backup --storage S3 --backup-bucket s3://my-on-premise-bucket --endpoint-url http://127.0.0.1:8000
```

### Cron Backup Example

As with LocalStorage, you can schedule `mcs backup` in cron. Consider including `--name-backup` to avoid collisions.

### S3 Backup Flags

The most commonly used S3-specific options are:

| Flag / Option | Description | Notes |
| --- | --- | --- |
| `--storage S3` (`-s`) | Use S3 storage topology | Must be set to `S3` for object storage workflows |
| `--backup-bucket` (`-bb`) | Bucket where backups are stored | Example: `s3://my-cs-backups` |
| `--endpoint-url` (`-url`) | Custom S3 endpoint URL | For on-premise S3 vendors (MinIO, etc.) |
| `--no-verify-ssl` (`-nv-ssl`) | Skip verifying SSL certificates | Use with caution; primarily for test/non-standard TLS |

## Restore

## LocalStorage Topology Restore

### Instructions
{% hint style="tip" %}
If Backup made only on Primary node on Clusters that do NOT save the backup to an NFS share, copy the primary nodes backup mysql & configs directory to all nodes.
```bash
scp /tmp/backups/12-03-2024/mysql root@pm2:/tmp/backups/12-03-2024/mysql
scp /tmp/backups/12-03-2024/configs root@pm2:/tmp/backups/12-03-2024/configs

scp /tmp/backups/12-03-2024/mysql root@pm3:/tmp/backups/12-03-2024/mysql
scp /tmp/backups/12-03-2024/configs root@pm3:/tmp/backups/12-03-2024/configs
```
{% endhint %}

1. List backups to find the folder name you want.
2. Restore on each node, starting with the primary node.
{% hint style="tip" %}
When running a columnstore backup, a restore.job file is created with a command compatible to run on each node to restore the backup.
{% endhint %}

### List Your Backups to Restore

```bash
mcs restore --backup-location /tmp/backups/ --list
```

### Quick Examples

Standard restore:

```bash
# on primary
mcs cluster stop

# on every node
systemctl stop mariadb
systemctl stop mariadb-columnstore-cmapi
mcs restore -l 12-03-2024 -bl /mnt/custom/path/
```

Compressed backup restore:

```bash
mcs restore -l 11-21-2024 -bl /mnt/custom/path/ -c pigz
```

### LocalStorage Restore Flags

Common options:

| Flag / Option | Description | Notes |
| --- | --- | --- |
| `--load` (`-l`) | Backup folder name to restore | Required for restore |
| `--backup-location` (`-bl`) | Where backups are located | Example: `/tmp/backups/` |
| `--backup_destination` (`-bd`) | Whether the backup is on the local server or a remote server | `Local` or `Remote` |
| `--scp` (`-scp`) | SCP source used when `--backup_destination Remote` | Format: `user@host` |
| `--skip-mariadb-backup` (`-smdb`) | Skip restoring MariaDB server data | Use when restoring ColumnStore only |

## S3 Topology Restore

### Instructions

1. Use the same backup bucket that contains the backup.
2. Restore on each node, starting with the primary node.

{% hint style="danger" %}
When running a columnstore backup, a restoreS3.job file is created with a command compatible to run on each node to restore the backup.
{% endhint %}

### Quick Examples
```bash
mcs restore -s S3 -bb s3://my-cs-backups  -l 12-03-2025
mcs restore -s S3 -bb gs://on-premise-bucket -l 12-03-2025 -url http://127.0.0.1:8000
mcs restore -s S3 -bb s3://my-cs-backups -l 11-21-2022 -nb s3://new-data-bucket -nr us-east-1 -nk AKIAxxxxxxx3FHCADF -ns GGGuxxxxxxxxxxnqa72csk5 -ha
```

#### Standard Restore:

```bash
# on primary
mcs cluster stop

# on every node
systemctl stop mariadb
systemctl stop mariadb-columnstore-cmapi
mcs restore -s S3 -bb s3://my-cs-backups -l 11-21-2024
```

#### On-premise S3 Endpoint:

```bash
mcs restore -s S3 -bb gs://on-premise-bucket -l 12-03-2021 -url http://127.0.0.1:9000
```

#### Restoring to a New Bucket:
Key Flags for restoring to a new bucket

* `-nb` - the name of the new bucket to copy the backup into and configure columnstore to use post restore
* `-nr` - the name of the region of the new bucket to  configure columnstore to use post restore
* `-nk` - the key of the new bucket to configure columnstore to use post restore
* `-ns` - the secret of the new bucket to configure columnstore to use post restore


```bash
mcs restore -s S3 -bb s3://my-cs-backups -l 11-21-2022 -nb s3://new-data-bucket -nr us-east-1 -nk AKIAxxxxxxx3FHCADF -ns GGGuxxxxxxxxxxnqa72csk5
```

### S3 Restore Flags

Common options:

| Flag / Option | Description | Notes |
| --- | --- | --- |
| `--backup-bucket` (`-bb`) | Backup bucket to restore from | Example: `s3://my-cs-backups` |
| `--endpoint-url` (`-url`) | Custom S3 endpoint URL | For on-premise S3 vendors |
| `--no-verify-ssl` (`-nv-ssl`) | Skip verifying SSL certificates | Use with caution |
| `--new-bucket` (`-nb`) | New bucket to restore data into | Use when restoring into a different bucket |
| `--new-region` (`-nr`) | Region for `--new-bucket` | S3 only |
| `--new-key` (`-nk`) | Access key for `--new-bucket` | S3 only |
| `--new-secret` (`-ns`) | Secret for `--new-bucket` | S3 only |
| `--continue` (`-cont`) | Allow deleting data in `--new-bucket` during restore | S3 only; dangerous if bucket contains important data |

## DBRM Backups
Both S3 and LocalStorage use the same commands for dbrm backups
{% hint style="danger" %}
DBRM backups are intended for backing up **internal ColumnStore metadata only**.
{% endhint %}

### Instructions
Run `mcs dbrm_backup` as root with the appropriate flags as you need **ONLY on the primary node**

### List Your dbrm Backups

```bash
mcs dbrm_backup --list
```

### Quick Examples
```bash
mcs dbrm_backup --mode loop --interval 90 --retention-days 7 --backup-location /mnt/dbrm_backups
mcs dbrm_backup --mode once --retention-days 7 --backup-location /mnt/dbrm_backups -nb my-one-off-backup
```

#### Standard `dbrm_backup`:

```bash
mcs dbrm_backup
```

`dbrm_backup` before upgrade:

```bash
mcs dbrm_backup -nb before_upgrade_11.21.2024_dbrm_backup
```

### dbrm_backup Flags

Common options:

| Flag / Option | Description | Notes |
| --- | --- | --- |
| `--backup-location` (`-bl`) | Where DBRM backups are written | Default example: `/tmp/dbrm_backups` |
| `--retention-days` (`-r`) | Retain DBRM backups created within last X days | Older backups are deleted |
| `--mode` (`-m`) | Run mode | `once` or `loop` |
| `--interval` (`-i`) | Sleep interval (minutes) when `--mode loop` | Only used in loop mode |
| `--skip-storage-manager` (`-ssm`) | Skip backing up the storagemanager directory | Support-guided workflows |
| `--skip-save-brm` (`-sbrm`) | Skip saving BRM prior to DBRM backup | Can produce a dirtier backup |
| `--skip-locks` (`-slock`) | Skip issuing read locks | Support-guided workflows |
| `--skip-polls` (`-spoll`) | Skip polling to confirm locks are released | Support-guided workflows |
| `--quiet` (`-q`) | Silence verbose copy output | Useful for cron |

## DBRM Restore

### Instructions
Both S3 and LocalStorage use the same commands for dbrm restore.
{% hint style="danger" %}
DBRM backups are intended for backing up **internal ColumnStore metadata only**.
{% endhint %}

1. List available DBRM backups.
2. Restore from the selected folder.

### List Your dbrm Restore Options

```bash
mcs dbrm_restore --list
```

### Quick Examples

```bash
./mcs_backup_manager.sh dbrm_restore --backup-location /tmp/dbrm_backups --load dbrm_backup_20241203_172842
./mcs_backup_manager.sh dbrm_restore --backup-location /tmp/dbrm_backups --load dbrm_backup_20241203_172842 --no-start
```

#### Standard `dbrm_restore`:

```bash
mcs dbrm-restore --backup-location /tmp/dbrm_backups --load <dbrm_backup_folder>
```

### `dbrm_restore` Flags

Common options:

| Flag / Option | Description | Notes |
| --- | --- | --- |
| `--backup-location` (`-bl`) | Where DBRM backups exist on disk | Example: `/tmp/dbrm_backups` |
| `--load` (`-l`) | Backup directory name to restore | Required for restore |
| `--no-start` (`-ns`) | Do not attempt ColumnStore startup after restore | Useful for manual recovery steps |
| `--skip-dbrm-backup` (`-sdbk`) | Skip taking a safety backup before restoring | Use with caution |
| `--skip-storage-manager` (`-ssm`) | Skip backing up/restoring storagemanager directory | Support-guided workflows |
| `--list` (`-li`) | List backups | Lists available DBRM backups |
