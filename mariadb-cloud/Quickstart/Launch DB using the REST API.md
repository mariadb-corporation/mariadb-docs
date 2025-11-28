# Launch DB Using REST API

This walkthrough explains how to launch database services and manage the lifecycle of database services using the [MariaDB Cloud DBaaS REST API](https://apidocs.skysql.com/).

## Launch a Service

{% stepper %}
{% step %}
### **Generate API Key**

1. Go to the [MariaDB Cloud API Key management page](https://app.skysql.com/user-profile/api-keys) and generate an API key
2.  Export the value from the token field to an environment variable $API\_KEY

    ```bash
    export API_KEY='... key data ...'
    ```

    The `API_KEY` environment variable will be used in the subsequent steps.

Use it on subsequent requests, for example:

```bash
 curl --request GET 'https://api.skysql.com/provisioning/v1/services' \
    --header "X-API-Key: $API_KEY"
```
{% endstep %}

{% step %}
### **Use the API Reference Guide to try out the APIs**

You can use the API Documentation here and directly try out the APIs in your browser.

All you need is to click ‘Authorize’ and type in `<supply your API key here>`

{% hint style="info" %}
Pre-requisites for code below.

The examples below use `curl` as the REST client, available on Linux, macOS, and Windows. You may use any language client supporting REST over HTTP. Examples also use `jq`, a JSON parsing tool, and both utilities should be installed on your system.

Using `tee`, you can save response JSON data to a file while piping it to `jq` for display. Linux and macOS support `tee` as shown. In Windows PowerShell, use the `-filepath` option with `tee`.

The `chmod` command makes files private to the user. If not supported, adjust file permissions accordingly.

Examples employ exported variables and `${VARIABLE_NAME}` syntax, compatible with Bourne-like shells (e.g., sh, bash, zsh). Windows users not using a Bourne-like shell should adjust by running the `jq` portion separately and manually assigning it to a variable.

Backslashes are used to indicate a command spans multiple lines. Remove them if your shell doesn't support this and join lines together.
{% endhint %}
{% endstep %}

{% step %}
### **Determine the Client IP Address**

When your new service is created, your client can only connect through the service's firewall if the client's IP address is in the service's IP allowlist.

Before creating the new service, determine the public IP address of your client host and save it to the `SKYSQL_CLIENT_IP` environment variable.

If you are not sure of your public IP address, you can use a lookup service, such as `checkip.amazonaws.com`:

```bash
export SKYSQL_CLIENT_IP=`curl -sS checkip.amazonaws.com`
```
{% endstep %}

{% step %}
### **Launch a Service**

To launch a service:

1. Prepare a request body containing the desired service options in a file called `request-service.json`:

```bash
cat > request-service.json <<EOF
{
  "service_type": "transactional",
  "topology": "es-single",
  "provider": "gcp",
  "region": "us-central1",
  "architecture": "amd64",
  "size": "sky-2x8",
  "storage": 100,
  "nodes": 1,
  "name": "skysql-quickstart",
  "ssl_enabled": true,
  "allow_list": [
     {
        "comment": "Describe the IP address",
        "ip": "${SKYSQL_CLIENT_IP}/32"
     }
  ]
}
EOF
```

This configuration is suitable for a quick test, but a more customized configuration should be selected for performance testing or for alignment to the needs of production workloads:

* For `service_type`, choose a [Service Type Selection](https://apidocs.skysql.com/#/Offering/get_provisioning_v1_service_types)
* For `topology`, choose a [Topology Selection](https://apidocs.skysql.com/#/Offering/get_provisioning_v1_topologies)
* For `provider`, choose a [Cloud Provider Selection](https://apidocs.skysql.com/#/Offering/get_provisioning_v1_providers) (`aws`,`gcp` or `azure`)
* For `region`, choose a [Region Selection](https://apidocs.skysql.com/#/Offering/get_provisioning_v1_regions)
* For `architecture`, choose a [Hardware Architecture Selection](https://apidocs.skysql.com/#/CPU-Architectures/get_provisioning_v1_cpu_architectures)
* For `size`, choose an [Instance Size Selection](https://apidocs.skysql.com/#/Offering/get_provisioning_v1_sizes)
* For `storage`, choose a [Transactional Storage Size Selection](https://apidocs.skysql.com/#/Offering/get_provisioning_v1_topologies__topology_name__storage_sizes)
* For `nodes`, choose a node count
* For `version`, choose the [Software Version Selection](https://apidocs.skysql.com/#/Offering/get_provisioning_v1_versions)
* For `name`, choose a name between 4-24 characters for the new service
* For `allow_list`, set the client IP address using CIDR notation, so that the client can connect through the firewall

1. Provide the request to the [`/provisioning/v1/services` API endpoint](https://apidocs.skysql.com/#/Services/post_provisioning_v1_services) to create (launch) a new database service and save the response to the `response-service.json` file:

```bash
curl -sS --location --request POST \
   --header "X-API-Key: ${API_KEY}" \
   --header "Accept: application/json" \
   --header "Content-type: application/json" \
   --data '@request-service.json' \
   https://api.skysql.com/provisioning/v1/services \
   | tee response-service.json | jq .
```

Upon success, the command will return JSON with details about the new service.

1.  Read the service ID for the new service and save the value in the `SKYSQL_SERVICE` environment variable:

    ```bash
    $ export SKYSQL_SERVICE=`jq -r .id response-service.json`
    ```
{% endstep %}

{% step %}
### **Check Service State**

Before advancing, check the service state using the `/provisioning/v1/services/${SKYSQL_SERVICE}` [API endpoint](https://apidocs.skysql.com/#/allowed_roles%3AADMIN%3BMEMBER%3BVIEWER/get_provisioning_v1_services__service_id_):

```bash
curl -sS --location --request GET \
   --header "X-API-Key: ${API_KEY}" \
   --header "Accept: application/json" \
   https://api.skysql.com/provisioning/v1/services/${SKYSQL_SERVICE} \
   | tee response-state.json | jq .status
```

When the service is still being launched, the JSON payload will contain `"pending_create"` or `"pending_modifying"` as the service status.

When the service has been launched, the JSON payload contains `"ready"`, and you can continue with the next steps. Keep in mind that some of the following values will not be populated in the JSON data until this ready status has been achieved.
{% endstep %}

{% step %}
### **Obtain Connection Details**

Obtain the connection credentials for the new MariaDB Cloud service by executing the following commands:

1. Obtain the hostname and port of the service and save them to the `SKYSQL_FQDN` and `SKYSQL_PORT` environment variables:
   *   The hostname is specified with the `"fqdn"` key.

       ```bash
       export SKYSQL_FQDN=`jq -r .fqdn response-state.json`
       ```
   *   Available TCP ports are specified in the `"endpoints"` array. For this test, connect to the `"port"` where `"name"` is `"readwrite"`.

       ```bash
       export SKYSQL_PORT=`jq '.endpoints[0].ports[] | select(.name=="readwrite") | .port' response-state.json`
       ```
2. Obtain the default username and password for the service using the `/provisioning/v1/services/${SKYSQL_SERVICE}/security/credentials` [API endpoint](https://apidocs.skysql.com/#/allowed_roles%3AADMIN%3BMEMBER%3BVIEWER/get_provisioning_v1_services__service_id__security_credentials) and save the response to the `response-credentials.json` file:

```bash
curl -sS --location --request GET \
   --header "X-API-Key: ${API_KEY}" \
   --header "Accept: application/json" \
   --header "Content-type: application/json" \
   https://api.skysql.com/provisioning/v1/services/${SKYSQL_SERVICE}/security/credentials \
   | tee response-credentials.json | jq .
```

The default username and password will not be available until the service state is `"ready"`.

1.  Set the file's mode to only allow the current user to read its contents:

    ```bash
    $ chmod 600 response-credentials.json
    ```
2.  Read the username and password from `response-credentials.json` and save them to the `SKYSQL_USERNAME` and `SKYSQL_PASSWORD` environment variables:

    ```bash
    $ export SKYSQL_USERNAME=`jq -r .username response-credentials.json`
    $ export SKYSQL_PASSWORD=`jq -r .password response-credentials.json`
    ```
{% endstep %}

{% step %}
### **Connect**

Connect to the database using the host, port, and default credentials using the [mariadb client](https://mariadb.com/docs/server/connect/clients/mariadb-client/):

```bash
mariadb --host ${SKYSQL_FQDN} --port ${SKYSQL_PORT} \
   --user ${SKYSQL_USERNAME} --password="${SKYSQL_PASSWORD}" \
   --ssl-verify-server-cert 
```

If you don't want the password to appear on the command-line, specify the `--password` command-line option without an argument to be prompted for a password.
{% endstep %}

{% step %}
### **Save Connection Information**

{% hint style="info" %}
This step is optional.
{% endhint %}

To connect to your MariaDB Cloud service easily, it is possible to create a `.my.cnf` file in your home directory that contains all the details of your connection.

1. Use the following command to create a new `.my.cnf` file or overwrite an existing one and populates it with the connection information that was collected in the previous steps:

```ini
cat > ~/.my.cnf <<EOF
[client]
host=${SKYSQL_FQDN}
port=${SKYSQL_PORT}
user=${SKYSQL_USERNAME}
password="${SKYSQL_PASSWORD}"
EOF
```

1.  Set the file system permissions for the `.my.cnf` file to ensure that other users can't read it:

    ```bash
    $ chmod 600 ~/.my.cnf
    ```
2.  When all the connection parameters are in your `~/.my.cnf` file, the mariadb client can connect without specifying any command-line options:

    ```bash
    $ mariadb
    ```
{% endstep %}
{% endstepper %}

## Resources

* [API Documentation](https://apidocs.skysql.com/)
* [API Reference Documentation](../reference-guide/rest-api-reference.md)
