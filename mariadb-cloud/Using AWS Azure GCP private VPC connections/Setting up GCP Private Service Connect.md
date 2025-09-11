# Setting up GCP Private Service Connect

Google Private Service Connect (PSC) is a Google Cloud service that enables secure and private connectivity between Virtual Private Clouds (VPCs) and third-party services. By using PSC with SkySQL services, traffic does not traverse the public internet, which enhances security and reduces exposure to potential threats.

For detailed information about Google PSC, see ["Private Service Connect" (Google documentation)](https://cloud.google.com/vpc/docs/private-service-connect).

## **Considerations**

* PSC is used for private connections within the same Google Cloud region. The SkySQL service and the connection VPC must be in the same region.
* When using SkySQL with PSC, all connections occur through private endpoints. If you need to connect to the service from outside your VPC, you will need to use a VPN or other mechanism to go through the connected VPC. Alternatively, SkySQL can be configured to provide a second, public endpoint for an additional fee.
* A list of Google Cloud project IDs that will be allowed to connect to the SkySQL service must be provided when enabling PSC. This list can be updated at any time.
* The SkySQL IP Allowlist is not used with PSC connections. Access to the SkySQL service can be controlled by setting up firewall rules inside the connecting VPC.
* Connections to SkySQL services by features such as SkySQL backups, and monitoring do not depend on PSC.
* Query Editor is not supported when PSC is enabled.
* PSC has connection limits which refer to the number of endpoints that can be created to a single PSC service within Google Cloud. Database connection limits are independent from PSC connection limits. The limit for PSC connections is 10.

### **Enable Private Service Connect on Service Launch**

<details>

<summary>Enable Google PSC via the SkySQL Portal</summary>

\


To enable PSC when launching a new service via the SkySQL Portal select the 'Google Private Service Connect' option in the 'Security' section. After the service completes provisioning, you will see a new option to "Manage Google Private Service Connect" in the service's context menu. Click this option to add one or more Google project IDs to the allowlist.

</details>

<details>

<summary>Enable Google PSC via the SkySQL DBaaS API</summary>

\


To enable Google PSC when launching a new service via the SkySQL DBaaS API, add the `endpoint_mechanism` and `endpoint_allowed_accounts` attributes to service creation JSON payload.

```
{
  "name": "my-skysql-service",
  ...
  "endpoint_mechanism": "privateconnect",
  "allowed_accounts": [
    "GCP-PROJECT-ID-1",
    "GCP-PROJECT-ID-2"
  ]
}
```

* The `endpoint_mechanism` field must be set to `privateconnect`
* The `endpoint_allowed_accounts` field must be set to a JSON array of one or more client project IDs in Google Cloud that will be allowed to establish a private connection to the SkySQL service.

For more information on using the SkySQL DBaaS API, see ["SkySQL DBaaS API"](https://apidocs.skysql.com/#/Services/post_provisioning_v1_services).

</details>

<details>

<summary>Enable Google PSC via the SkySQL Terraform Provider</summary>

\


To enable Google PSC when launching a new service via the SkySQL DBaaS API, set the `endpoint_mechanism` and `endpoint_allowed_accounts` attributes on the `skysql_service` resource.

```hcl
resource "skysql_service" "example" {
  name                      = "my-skysql-service"
  ...
  endpoint_mechanism        = "privateconnect"
  endpoint_allowed_accounts = ["GCP-PROJECT-ID-1", "GCP-PROJECT-ID-2"]
}
```

* The `endpoint_mechanism` field must be set to `privateconnect`
* The `endpoint_allowed_accounts` field must be set to a list of one or more customer project IDs in Google Cloud that will be allowed to establish a private connection to the SkySQL service.

A complete example Terraform template that creates a new SkySQL service with Google PSC enabled can be found in the [terraform provider examples](https://github.com/skysqlinc/terraform-provider-skysql/tree/main/examples/private-service-connect).

For more information on using the SkySQL Terraform Provider, see ["SkySQL Terraform Provider"](https://registry.terraform.io/providers/skysqlinc/skysql/latest/docs).

</details>

**For the next step, see the** [**PSC Endpoint Setup**](<Setting up GCP Private Service Connect.md#private-service-connect-endpoint-setup>) **section on this page.**

### **Enable Google PSC on an Existing SkySQL Service**

> \[!CAUTION] Enabling PSC on an existing service will cause all existing connections to be dropped. The service will be unavailable for a short period of time while the public endpoint is replaced with the new PSC endpoint.

<details>

<summary>Enable Google PSC on an existing service via the SkySQL Portal:</summary>

\


1. Log in to the SkySQL Portal
2. Click the "MANAGE" button (on the right) for the desired service.
3. In the context menu, choose the "Set up Google Private Service Connect" menu item.
4. In the popup window, add one or more GCP project IDs.
5. Click the "OK" button to confirm this operation.

</details>

<details>

<summary>Enable Google PSC on an existing service via the SkySQL DBaaS API:</summary>

\


To enable Google PSC on an existing service, you will need to update the service endpoints with a payload similar to the following:

```json
[
  {
    "mechanism": "privateconnect",
    "allowed_accounts": [
      "GOOGLE-PROJECT-ID-1",
      "GOOGLE-PROJECT-ID-2"
    ]
  }
]
```

This payload should then be sent to the API `PATCH` https://api.skysql.com/provisioning/v1/services/{SERVICE\_ID}/endpoints where `{SERVICE_ID}` is the ID of the service you are updating. For more information on using the SkySQL DBaaS API, see ["SkySQL DBaaS API"](https://apidocs.skysql.com/#/Services/patch_provisioning_v1_services__service_id__endpoints).

</details>

**For the next step, see the** [**PSC Endpoint Setup**](<Setting up GCP Private Service Connect.md#private-service-connect-endpoint-setup>) **section on this page.**

## Private Service Connect Endpoint Setup

To connect to a SkySQL service using Google PSC, you must create an endpoint in your VPC that connects to the SkySQL service. The endpoint will be used by clients in your VPC to connect to the SkySQL service.

### Pre-requisites

* You must have a VPC in the same region as the SkySQL service.
*   You will need to lookup the Endpoint Service ID that SkySQL provisioned for you when you created your SkySQL Service.

    * This ID can be found in the "Connect" window of the SkySQL portal.
    * If using the SkySQL DBaaS API, the ID can be found in the response of the service details API call.

    ```
    curl https://api.skysql.com/provisioning/v1/services/{SERVICE_ID} | jq ".endpoints[0].endpoint_service"
    ```

### Create a Subnet (optional)

We recommend use of a subnet dedicated to Private Service Connect endpoints in the same VPC where the application is running.

1. In the GCP console, navigate VPC network → VPC networks → → SUBNETS → ADD SUBNET.
   * Replace with the name of the VPC where the application is running.
2. Configure the subnet:
   * Name
   * Region: select the same region as the one where the application runs
   * Purpose: None
   * IP address range: Set a CIDR block that doesn't overlap with the CIDR blocks of the existing subnets in the same VPC.
   * Optionally configure Private Google Access
   * Optionally configure Flow logs
   * Click "ADD".

### Create a Static Internal IP Address

1. In the GCP console, navigate VPC network → VPC networks → → STATIC INTERNAL IP ADDRESSES → RESERVE STATIC ADDRESS.
   * Replace with the name of the VPC where the application is running.
2. Configure the static internal IP address:
   * Name: set to the Database ID (dbxxxxxxxx) from SkySQL.
   * Subnet: select the subnet where to reserve the static IP address.
   * Static IP address: optionally choose the address.
   * Purpose: Non-shared
   * Click "RESERVE".

### VPC Endpoint Creation Steps

1. In the GCP console, navigate Network services → Private Service Connect → CONNECTED ENDPOINTS → CONNECT ENDPOINT.
2. Configure the endpoint connection:
   * Target: Published service
   * Target service: the value of the Endpoint Service ID. See [Pre-requisites](<Setting up GCP Private Service Connect.md#pre-requisites>) for more information on how to find this ID.
   * Endpoint name: set to the Database ID from SkySQL (dbxxxxxxxx)
   * Network: select the VPC network where the application is running
   * Subnetwork: select the subnet where the static internal IP address is reserved
   * IP address: select the reserved internal IP address from the prior step
   * Click "ADD ENDPOINT".

After creation, the Endpoint should have a status of `Accepted`. If this status is not present, please ensure your Google Project ID is added to the list of allowed accounts in the SkySQL portal for this service.

### Connecting to your SkySQL Service

After creating your PSC endpoint, your service should be available within your VPC at the Private IP Address you assigned to the endpoint.

* DNS propagation from SkySQL to the Private IP address is not supported when using PSC.
* The hostname when connecting to your SkySQL service should always be the Private IP address of the PSC endpoint.

> \[!NOTE] When using PSC with SSL/TLS, there will be a hostname mismatch since the hostname provisioned by SkySQL will not match your internal IP Address. This can be ignored as the connection is still secure.

### **Disabling Google PSC**

> \[!CAUTION] Disabling PSC on an existing service will cause all existing connections to be dropped. The service will be unavailable for a short period of time while the private endpoint is replaced with the new public endpoint.

<details>

<summary>Disable Google PSC via the SkySQL Portal</summary>

\


1. Visit the [SkySQL Portal](https://app.skysql.com/)
2. Find the service that you would like to modify.
3. Click "MANAGE" on the far right side of the service listing.
4. In the context menu, select "Manage your Private Service Connect".
5. In the popup window, click "I want to disconnect my Private Service Connect".
6. In the popup window, select "Disconnect".
7. Since the service's allowlist was cleared when Goolge PSC was previously enabled, you will need to [update the allowlist](<../Security/Configuring Firewall.md>) to allow clients to connect after disabling PSC.

</details>

<details>

<summary>Disable Google PSC via the SkySQL DBaaS API</summary>

\


To disable Google PSC on an existing service, you will need to update the service endpoints with a payload similar to the following:

```json
[
  {
    "mechanism": "nlb"
  }
]
```

This payload should then be sent to the API `PATCH` https://api.skysql.com/provisioning/v1/services/{SERVICE\_ID}/endpoints where `{SERVICE_ID}` is the ID of the service you are updating. For more information on using the SkySQL DBaaS API, see ["SkySQL DBaaS API"](https://apidocs.skysql.com/#/Services/patch_provisioning_v1_services__service_id__endpoints).

</details>
