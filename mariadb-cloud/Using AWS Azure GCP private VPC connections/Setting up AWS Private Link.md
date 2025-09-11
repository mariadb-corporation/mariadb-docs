# Setting up AWS Private Link

AWS PrivateLink is an AWS service that enables secure and private connectivity between Virtual Private Clouds (VPCs) and third-party services. By using PrivateLink with SkySQL services, traffic does not traverse the public internet, which enhances security and reduces exposure to potential threats.

For detailed information about AWS PrivateLink, see ["AWS PrivateLink" (Amazon documentation)](https://aws.amazon.com/privatelink/).

## **Considerations**

* AWS PrivateLink is used for private connections within the same AWS region. The SkySQL service and the connection VPC must be in the same region.
* When using SkySQL with AWS PrivateLink, all connections occur through private endpoints. If you need to connect to the service from outside your VPC, you will need to use a VPN or other mechanism to go through the connected VPC. Alternatively, SkySQL can be configured to provide a second, public endpoint for an additional fee.
* A list of AWS Account IDs that will be allowed to connect to the SkySQL service must be provided when enabling AWS PrivateLink. This list can be updated at any time.
* The SkySQL IP Allowlist is not used with AWS PrivateLink connections. Access to the SkySQL service will be controlled by Security Groups in the connecting VPC. For detailed information, see ["Control traffic to resources using security groups"](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) (Amazon documentation).
* Connections to SkySQL services by features such as SkySQL backups, and monitoring do not depend on AWS PrivateLink.
* Query Editor is not supported when AWS PrivateLink is enabled.

### **Enable AWS PrivateLink on Service Launch**

<details>

<summary>Enable Privatelink via the SkySQL Portal</summary>

\


To enable AWS PrivateLink when launching a new service via the SkySQL Portal select the 'Enable Private link' option in the 'Security' section. After the service completes provisioning, you will see a new option to "Set up Private Link" in the service's context menu. Click this option to add one or more AWS account IDs to the allowlist.

</details>

<details>

<summary>Enable Privatelink via the SkySQL DBaaS API</summary>

\


To enable AWS PrivateLink when launching a new service via the SkySQL DBaaS API, add the `endpoint_mechanism` and `endpoint_allowed_accounts` attributes to service creation JSON payload.

```
{
  "name": "my-skysql-service",
  ...
  "endpoint_mechanism": "privateconnect",
  "allowed_accounts": [
    "AWS-ACCOUNT-ID-1",
    "AWS-ACCOUNT-ID-2"
  ]
}
```

* The `endpoint_mechanism` field must be set to `privateconnect`
* The `endpoint_allowed_accounts` field must be set to a JSON array of one or more customer account IDs in AWS that will be allowed to establish a private connection to the SkySQL service.

For more information on using the SkySQL DBaaS API, see ["SkySQL DBaaS API"](https://apidocs.skysql.com/#/Services/post_provisioning_v1_services).

</details>

<details>

<summary>Enable Privatelink via the SkySQL Terraform Provider</summary>

\


To enable AWS PrivateLink when launching a new service via the SkySQL DBaaS API, set the `endpoint_mechanism` and `endpoint_allowed_accounts` attributes on the `skysql_service` resource.

```hcl
resource "skysql_service" "example" {
  name                      = "my-skysql-service"
  ...
  endpoint_mechanism        = "privateconnect"
  endpoint_allowed_accounts = ["123456789012"]
}
```

* The `endpoint_mechanism` field must be set to `privateconnect`
* The `endpoint_allowed_accounts` field must be set to a list of one or more customer account IDs in AWS that will be allowed to establish a private connection to the SkySQL service.

A complete example Terraform template that creates a new SkySQL service with AWS PrivateLink enabled can be found in the [terraform provider examples](https://github.com/skysqlinc/terraform-provider-skysql/tree/main/examples/privateconnect).

For more information on using the SkySQL Terraform Provider, see ["SkySQL Terraform Provider"](https://registry.terraform.io/providers/skysqlinc/skysql/latest/docs).

</details>

**For the next step, see the** [**AWS Endpoint Setup**](<Setting up AWS Private Link.md#aws-endpoint-setup>) **section on this page.**

### **Enable AWS PrivateLink on an Existing SkySQL Service**

> \[!CAUTION] Enabling PrivateLink on an existing service will cause all existing connections to be dropped. The service will be unavailable for a short period of time while the public endpoint is replaced with the new PrivateLink endpoint.

<details>

<summary>Enable AWS PrivateLink on an existing service via the SkySQL Portal:</summary>

\


1. Log in to the SkySQL Portal
2. Click the "MANAGE" button (on the right) for the desired service.
3. In the context menu, choose the "Set up AWS PrivateLink" menu item.
4. In the popup window, add one or more AWS account IDs.
5. Click the "OK" button to confirm this operation.

</details>

<details>

<summary>Enable AWS PrivateLink on an existing service via the SkySQL DBaaS API:</summary>

\


To enable AWS PrivateLink on an existing service, you will need to update the service endpoints with a payload similar to the following:

```json
[
  {
    "mechanism": "privateconnect",
    "allowed_accounts": [
      "AWS-ACCOUNT-ID-1",
      "AWS-ACCOUNT-ID-2"
    ]
  }
]
```

This payload should then be sent to the API `PATCH` https://api.skysql.com/provisioning/v1/services/{SERVICE\_ID}/endpoints where `{SERVICE_ID}` is the ID of the service you are updating. For more information on using the SkySQL DBaaS API, see ["SkySQL DBaaS API"](https://apidocs.skysql.com/#/Services/patch_provisioning_v1_services__service_id__endpoints).

</details>

**For the next step, see the** [**AWS Endpoint Setup**](<Setting up AWS Private Link.md#aws-endpoint-setup>) **section on this page.**

## AWS Endpoint Setup

To connect to a SkySQL service using AWS PrivateLink, you must create an endpoint in your VPC that connects to the SkySQL service. The endpoint will be used by clients in your VPC to connect to the SkySQL service.

### Pre-requisites

* You must have a VPC in the same region as the SkySQL service.
* You must create a security group that will be used to control access to the SkySQL service endpoint.
  * This security group should contain rules to allow traffic from your client instances to the port of the SkySQL service (usually 3306).
  * You must create a rule in your security group for each IP range or other security group that will be allowed to connect to the SkySQL service.
  * The security group must be associated with the VPC that you will use to connect to the SkySQL service.
*   You will need to lookup the Endpoint Service ID that SkySQL provisioned for you when you created your SkySQL Service.

    * This ID can be found in the "Connect" window of the SkySQL portal.
    * If using the SkySQL DBaaS API, the ID can be found in the response of the service details API call.

    ```
    curl https://api.skysql.com/provisioning/v1/services/{SERVICE_ID} | jq ".endpoints[0].endpoint_service"
    ```

### VPC Endpoint Creation Steps

1. Log in to the AWS console.
2. Confirm the correct region is selected.
3. Navigate to the "VPC" page, then the "Endpoints" section.
4. Click the "Create Endpoint" button.
5. In the "Name tag" field, enter a name for the new endpoint. This name can be anything you like.
6. Set the Service category to "Other endpoint services".
7. The value for the "Service name" field must be set to the value of the Endpoint Service ID provided to you by SkySQL. See [Pre-requisites](<Setting up AWS Private Link.md#pre-requisites>) for more information on how to find this ID.
8. Click "Verify service". AWS should find the service and auto-populate the rest of the form.
9. In the VPC search field, find the VPC that you want to use for the interconnect between the clients and the SkySQL service.
10. In the Subnets section, it is suggested that you select all the Availability Zones in the list, entering the proper subnet ID for each one. If you are unsure, view the details of your running instances to see the Subnet ID that they have configured.
11. Select IPv4 for "IP address type".
12. For the "Security Groups" section, assign the security groups that will allow your client instance to connect to your VPC endpoint. See [Pre-requisites](<Setting up AWS Private Link.md#pre-requisites>) for more information on setting up security groups.
13. Press the "Create endpoint" button. Endpoint creation may take several minutes. When complete, status will change from "Pending" to "Available".

After creation, the Endpoint will be in `Pending` status while AWS provisions the new endpoint. Once the endpoint is `Available`, you can connect to your SkySQL service using the new endpoint. The newly created endpoint now authorizes the internal IPs or security groups that you specified in the Source values to access the SkySQL service's connection port. When testing a client connection, ensure that the client host is authorized by the security group's Source settings and that you're using the "`readwrite`" port plus the appropriate username and password (either the default values or the value for any user you have created).

### Connecting to your SkySQL Service

After creating your VPC endpoint, AWS will create a number of DNS records that will resolve to the private IP addresses of your Privatelink Endpoint.

* The first DNS name in the list can be used from any availability zone in your VPC and will resolve to the private IP address of the endpoint in the same availability zone.
* The following DNS names provided are availability zone specific and rely on the user to match the correct DNS name to the availability zone of the client instance.
* If connecting via these DNS names, we recommend using the first DNS name in the list to ensure that the connection is routed to the correct availability zone.

> \[!NOTE] The DNS names provided by AWS will always be in the domain `amazonaws.com`. If connecting to your SkySQL service using SSL/TLS, the database certificate will not match the VPC endpoint name. Due to this, we recommend [Enabling Private DNS for AWS PrivateLink](<Setting up AWS Private Link.md#enabling-private-dns-for-aws-privatelink>).

### Enabling Private DNS for AWS PrivateLink

In order to connect to your SkySQL service using the skysql.com service name provided in the SkySQL portal, you must enable Private DNS for the VPC endpoint. This will allow the service name to resolve to the private IP address of the SkySQL service.

The following requirements must be met to enable Private DNS for the VPC endpoint:

* Private DNS must be enabled for the VPC.
* Your client instances must use the default AWS DNS server provided by the VPC (this is usually turned on by default).

To enable Private DNS for the VPC endpoint:

1. Log in to the AWS console.
2. Confirm the correct region is selected.
3. Navigate to the "VPC" page, then the "Endpoints" section.
4. Select the VPC endpoint that you created for your SkySQL service.
5. Click the "Actions" button, then select "Modify Private DNS Name".
6. In the popup window, select the checkbox to "Enable Private DNS Name".
7. Click the "Save changes" button.

After a short period of time, the service name provided in the SkySQL portal should resolve to the private IP address of the SkySQL service via PrivateLink. You can test this by connecting to the service using the service name provided in the portal.

### **Disabling AWS PrivateLink**

> \[!CAUTION] Disabling PrivateLink on an existing service will cause all existing connections to be dropped. The service will be unavailable for a short period of time while the private endpoint is replaced with the new public endpoint.

<details>

<summary>Disable AWS PrivateLink via the SkySQL Portal</summary>

\


1. Visit the [SkySQL Portal](https://app.skysql.com/)
2. Find the service that you would like to modify.
3. Click "MANAGE" on the far right side of the service listing.
4. In the context menu, select "Manage PrivateLink".
5. In the popup window, click "I want to disconnect my Private Link".
6. In the popup window, select "Disconnect".
7. Since the service's allowlist was cleared when AWS PrivateLink was previously enabled, you will need to [update the allowlist](<../Security/Configuring Firewall.md>) to allow clients to connect after disabling PrivateLink.

</details>

<details>

<summary>Disable AWS PrivateLink via the SkySQL DBaaS API</summary>

\


To disable AWS PrivateLink on an existing service, you will need to update the service endpoints with a payload similar to the following:

```json
[
  {
    "mechanism": "nlb"
  }
]
```

This payload should then be sent to the API `PATCH` https://api.skysql.com/provisioning/v1/services/{SERVICE\_ID}/endpoints where `{SERVICE_ID}` is the ID of the service you are updating. For more information on using the SkySQL DBaaS API, see ["SkySQL DBaaS API"](https://apidocs.skysql.com/#/Services/patch_provisioning_v1_services__service_id__endpoints).

</details>
