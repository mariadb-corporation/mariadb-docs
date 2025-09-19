# Hashicorp Key Management Plugin

The [Hashicorp Key Management Pugin](../../../server/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin.md) is used to implement encryption using keys stored in the Hashicorp Vault KMS.

{% hint style="info" %}
For more information about configuring the plugin as well as different capabilities, please check the [documentation](../../../server/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin.md). This guide will cover a minimal example for configuring the plugin with the operator.
{% endhint %}

## Configuring TDE in MariaDB Using Hashicorp Key Management Plugin

MariaDB can be configured to encrypt all of it's components 

### Requirements

- Running and accessible Vault KMS setup with a valid SSL certificate.
- Vault is unsealed and you've logged in to it with `vault login $AUTH_TOKEN`, where $AUTH_TOKEN is an authentication token given to you by an administrator
- `openssl` for generating secrets

### Steps 

1. **Creating A New Key-Value Store In Vault.**
    Create a new key-value store and take note of the `path`. In our example we will use `mariadb`.
    ```sh
    vault secrets enable -path /mariadb -version=2 kv
    ```

2. **Adding necessary secrets.**
    We will put 2 secrets with ids `1` and `2`. `2` will be used for temporary files, while `1` will be used for everything else. It is not
    neccessary to create 2 of them and in that case, temporary files will use `1`.

    Note: Here you should use the `path` we chose in the previous step.
    ```sh
    vault kv put /mariadb/1 data="$(openssl rand -hex 32)"
    vault kv put /mariadb/2 data="$(openssl rand -hex 32)"
    ```

3. **(Optional) Create An Authentication Token With Policy.**
    This step can be skipped if you want to use your own token. Consult with a Vault administrator regarding this.
    Policies are Vault's way to restrict access to what you are allowed to do. The following is a policy that should be used by the token following the least permission principle.
    ```sh
    cat <<'EOF' | vault policy write -non-interactive mariadb -
    # Allow access to MariaDB secrets
    path "mariadb/*" {
      capabilities = ["create", "read", "update", "delete", "list"]
    }

    # Allow reading the mount configuration
    path "sys/mounts/mariadb/tune" {
      capabilities = ["read"]
    }
    EOF
    ```
    After which, we can create a new token with the given policy.
    ```sh
    vault token create -policy mariadb
    ```
    You will see output similar to:
    ```
    Key                  Value
    ---                  -----
    token                EXAMPLE_TOKEN
    token_accessor       utFtmh98YAAJyYdxEVN3SFQA
    token_duration       768h
    token_renewable      true
    token_policies       ["default" "mariadb"]
    identity_policies    []
    policies             ["default" "mariadb"]
    ```
    Your new token is: `EXAMPLE_TOKEN`.

4. **Create A `Secret` For the vault token.**
    Now that you've either created a new token, or are using an existing one, we need to create a secret with it.
    ```sh
    export TOKEN="EXAMPLE_TOKEN"
    kubeclt create secret generic mariadb-vault-token --from-literal=token="$TOKEN"
    ```

5. **Create a Secret for the ca.**
    For which certificate is needed, consult [the docs](../../../server/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin.md#hashicorp-key-management-vault-ca)
    If you have the certificate locally in a file called `ca.crt` you can run:

    ```sh
    kubectl create secret generic vault-tls --from-file=./ca.crt
    ```

5. **Create A MariaDB Custom Resource.**
    The final step is creating a new MariaDB instance.

    **mariadb-vault.yaml**
    ```yaml
    ---
    apiVersion: v1
    kind: Secret
    metadata:
      name: mariadb # Used to hold the mariadb and root user passwords
      labels:
        enterprise.mariadb.com/watch: ""
    stringData:
      password: MariaDB11!
      root-password: MariaDB11!
    ---
    apiVersion: enterprise.mariadb.com/v1alpha1
    kind: MariaDB
    metadata:
      name: mariadb
    spec:
      image: docker.mariadb.com/enterprise-server:11.4.7-4.3
      rootPasswordSecretKeyRef:
        name: mariadb
        key: password

      username: mariadb
      passwordSecretKeyRef:
        name: mariadb-password
        key: password
        generate: true
      database: mariadb

      port: 3306

      storage:
        size: 1Gi
        # storageClassName: csi-hostpath-sc

      myCnf: |
        [mariadb]
        bind-address=*
        default_storage_engine=InnoDB
        binlog_format=row
        innodb_autoinc_lock_mode=2
        innodb_buffer_pool_size=800M
        max_allowed_packet=256M

        plugin_load_add = hashicorp_key_management
        hashicorp-key-management-vault-url=https://vault-0.vault-internal.default.svc.cluster.local:8200/v1/mariadb
        hashicorp-key-management-caching-enabled=ON
        hashicorp-key-management-vault-ca=/etc/vault/certs/ca.crt

        innodb_encrypt_tables = FORCE
        innodb_encrypt_log = ON
        innodb_encrypt_temporary_tables = ON
        encrypt_tmp_disk_tables = ON
        encrypt_tmp_files = ON
        encrypt_binlog = ON
        aria_encrypt_tables = ON

        innodb_encryption_threads = 4
        innodb_encryption_rotation_iops = 2000

      env:
        - name: VAULT_TOKEN # This is where our token is defined!
          valueFrom:
            secretKeyRef:
              name: mariadb-vault-token
              key: token

      resources:
        requests:
          cpu: 100m
          memory: 128Mi
        limits:
          memory: 1Gi

      metrics:
        enabled: true

      volumes:
        - name: vault-certificates
          secret:
            secretName: vault-tls
            defaultMode: 0600
      volumeMounts:
        - name: vault-certificates
          mountPath: /etc/vault/certs/
    ```
    `kubectl apply -f mariadb-vault.yaml`

6. **Verify Encryption Works.**
    ```sh
    kubectl run mariadb-connect --rm -it --image=mariadb:11.4 -- bash -c "mariadb -u root -p'MariaDB11!' --ssl=false -h mariadb"
    ```

    You should see something along the lines of:

    ```
    If you don't see a command prompt, try pressing enter.
    Welcome to the MariaDB monitor.  Commands end with ; or \g.
    Your MariaDB connection id is 95
    Server version: 11.4.7-4-MariaDB-enterprise MariaDB Enterprise Server

    Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    MariaDB [(none)]>
    ```

    At this point, you can check the encryption status:
    ```sql
    SELECT * from information_schema.INNODB_TABLESPACES_ENCRYPTION;
    ```

    If you create a new database and then table, the above query should return additional information about them. Something like:
    ```sql
    MariaDB [my_db]> SELECT * from information_schema.INNODB_TABLESPACES_ENCRYPTION;
    +-----------------+-------------------+-----------------+---------------------+----------------+----------------------+
    | NAME            | ENCRYPTION_SCHEME | MIN_KEY_VERSION | CURRENT_KEY_VERSION | CURRENT_KEY_ID | ROTATING_OR_FLUSHING |
    +-----------------+-------------------+-----------------+---------------------+----------------+----------------------+
    | innodb_system   |                 1 |               1 |                   1 |              1 |                    0 |
    | innodb_undo001  |                 1 |               1 |                   1 |              1 |                    0 |
    | innodb_undo002  |                 1 |               1 |                   1 |              1 |                    0 |
    | innodb_undo003  |                 1 |               1 |                   1 |              1 |                    0 |
    | mysql/innodb_ta |                 1 |               1 |                   1 |              1 |                    0 |
    | mysql/innodb_in |                 1 |               1 |                   1 |              1 |                    0 |
    | mysql/gtid_slav |                 1 |               1 |                   1 |              1 |                    0 |
    | mysql/transacti |                 1 |               1 |                   1 |              1 |                    0 |
    | my_db/people    |                 1 |               1 |                   1 |              1 |                    0 |
    +-----------------+-------------------+-----------------+---------------------+----------------+----------------------+
    ```
    Note: The above query is truncated, so it will be readable in the docs. In reality, you will see a few more columns.

## Day-2 Operations

### Rotating Secrets

1. **Put A New Secret In Vault.**
    After logging in to vault, you can run again:
    ```sh
    vault kv put /mariadb/1 data="$(openssl rand -hex 32)"
    vault kv put /mariadb/2 data="$(openssl rand -hex 32)"
    ```
    This will start re-encrypting data.

2. **Monitor Re-Encryption.**
    ```sh
    kubectl run mariadb-connect --rm -it --image=mariadb:11.4 -- bash -c "mariadb -u root -p'MariaDB11!' --ssl=false -h mariadb"
    ```
    If you check the encrpytion status again:
    ```sql
    SELECT * from information_schema.INNODB_TABLESPACES_ENCRYPTION;
    ```
    You should see `CURRENT_KEY_VERSION` column start getting updated to point to the new key version.
    ```sql
    MariaDB [my_db]> SELECT * from information_schema.INNODB_TABLESPACES_ENCRYPTION;
    +-----------------+-------------------+-----------------+---------------------+----------------+----------------------+
    | NAME            | ENCRYPTION_SCHEME | MIN_KEY_VERSION | CURRENT_KEY_VERSION | CURRENT_KEY_ID | ROTATING_OR_FLUSHING |
    +-----------------+-------------------+-----------------+---------------------+----------------+----------------------+
    | innodb_system   |                 1 |               1 |                   2 |              1 |                    0 |
    | innodb_undo001  |                 1 |               1 |                   2 |              1 |                    0 |
    | innodb_undo002  |                 1 |               1 |                   2 |              1 |                    0 |
    | innodb_undo003  |                 1 |               1 |                   2 |              1 |                    0 |
    | mysql/innodb_ta |                 1 |               1 |                   2 |              1 |                    0 |
    | mysql/innodb_in |                 1 |               1 |                   2 |              1 |                    0 |
    | mysql/gtid_slav |                 1 |               1 |                   2 |              1 |                    0 |
    | mysql/transacti |                 1 |               1 |                   2 |              1 |                    0 |
    | my_db/people    |                 1 |               1 |                   2 |              1 |                    0 |
    +-----------------+-------------------+-----------------+---------------------+----------------+----------------------+
    ```

### Rotating Token
Make sure when rotating the token, to do so in advance of the token expiring.

1. **Acquire a new token and update the secret.**

    ```sh
    export TOKEN="EXAMPLE_TOKEN"
    kubeclt create secret generic mariadb-vault-token --from-literal=token="$TOKEN"
    ```

2. **Restart The MariaDB StatefullSet.**
    MariaDB will continue using the old token until the statefulset is restart. If the name of the database CRD is `mariadb` (as per the example above), then:
    ```sh
    kubectl rollout restart statefulset mariadb
    ```

## Known Issues/Limitations

### **Vault Not Being Accessible Will Result In MariaDB Not Working**

As MariaDB uses vault to fetch it's decryption key, in the case where vault is not accessible due to it being down, network issues, secret
not existing, will result in MariaDB not being able to fetch the decryption key and hence stop working. While the Hashicorp plugin has a
configurable cache, that should be set and will result in MariaDB still working for a few seconds to minutes, depending on configuration,
the cache is not reliable as it's ephemeral and short lived.

### **Deleting The Decryption Key Will Make Your Data Inaccessible.**

It is recommended to back up the decryption key so accidental deletions will not result in issues.

### **Decryption Key Must Be Hexadecimal**

Use the following to generate correct decryption keys.
```sh
openssl rand -hex 32
```

### **Rotating The Decryption Key Before A Previous Re-Encryption Has Finished, Will Result In Data Corruption.**
To check the re-encryption progress, you can run:

```sql
SELECT * from information_schema.INNODB_TABLESPACES_ENCRYPTION;
```

Look for the `CURRENT_KEY_VERSION` and make sure they are in sync with the latest version you have in Vault.
