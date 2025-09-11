# Setting up Azure Private Link

Azure Private Link is an Azure service that enables secure and private connectivity between Virtual Networks (VNet) and third-party services. By using Private Link with SkySQL services, traffic does not traverse the public internet, which enhances security and reduces exposure to potential threats.

For detailed information about Azure Private Link, see ["Azure Private Link" (Azure documentation)](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview).

## **Considerations**

* Azure Private Link is used for private connections within the same Azure region. The SkySQL service and the connecting VNet must be in the same region.
* When using SkySQL with Azure Private Link, all connections occur through private endpoints. If you need to connect to the service from outside your VNET, you will need to use a VPN or other mechanism to go through the connected VNet. Alternatively, SkySQL can be configured to provide a second, public endpoint for an additional fee.
* A list of Azure Subscription IDs that will be allowed to connect to the SkySQL service must be provided when enabling Azure Private Link. This list can be updated at any time.
* The SkySQL IP Allowlist is not used with Azure Private Link connections. Access to the SkySQL service will be controlled by Security Groups in the connecting VNet. For detailed information, see ["Manage network policies for private endpoints"](https://learn.microsoft.com/en-us/azure/private-link/disable-private-endpoint-network-policy?tabs=network-policy-portal) (Azure documentation).
* Connections to SkySQL services by features such as SkySQL backups, and monitoring do not depend on Azure Private Link.
* The IP address of the SkySQL service will be a private IP address in the range of the VNet that the Private Link endpoint is created in. Because of this, SSL certificates will not match the IP address of the service. To avoid this issue, you can either disable SSL on the SkySQL service, or setup Private DNS within your Azure VNet. See ["Enabling DNS for Azure Private Link"](<Setting up Azure Private Link.md#enabling-dns-for-azure-private-link>) for more information.
* Query Editor is not supported when Azure Private Link is enabled.

### **Enable Azure Private Link on Service Launch**

<details>

<summary>Enable Private Link via the SkySQL Portal</summary>

\


To enable Azure Private Link when launching a new service via the SkySQL Portal select the 'Enable Private link' option in the 'Security' section. After the service completes provisioning, you will see a new option to "Set up Private Link" in the service's context menu. Click this option to add one or more Azure Subscription IDs to the allowlist.

</details>

<details>

<summary>Enable Private Link via the SkySQL DBaaS API</summary>

\


To enable Azure Private Link when launching a new service via the SkySQL DBaaS API, add the `endpoint_mechanism` and `endpoint_allowed_accounts` attributes to service creation JSON payload.

```
{
  "name": "my-skysql-service",
  ...
  "endpoint_mechanism": "privateconnect",
  "allowed_accounts": [
    "AZURE-SUBSCRIPTION-ID-1",
    "AZURE-SUBSCRIPTION-ID-2"
  ]
}
```

* The `endpoint_mechanism` field must be set to `privateconnect`
* The `endpoint_allowed_accounts` field must be set to a JSON array of one or more customer subscription IDs in Azure that will be allowed to establish a private connection to the SkySQL service. These IDs should be in the guid format.

For more information on using the SkySQL DBaaS API, see ["SkySQL DBaaS API"](https://apidocs.skysql.com/#/Services/post_provisioning_v1_services).

</details>

<details>

<summary>Enable Private Link via the SkySQL Terraform Provider</summary>

\


To enable Azure Private Link when launching a new service via the SkySQL DBaaS API, set the `endpoint_mechanism` and `endpoint_allowed_accounts` attributes on the `skysql_service` resource.

```hcl
resource "skysql_service" "example" {
  name                      = "my-skysql-service"
  ...
  endpoint_mechanism        = "privateconnect"
  endpoint_allowed_accounts = ["123456789012"]
}
```

* The `endpoint_mechanism` field must be set to `privateconnect`
* The `endpoint_allowed_accounts` field must be set to a list of one or more customer subscription IDs in Azure that will be allowed to establish a private connection to the SkySQL service. These IDs should be in the guid format.

A complete example Terraform template that creates a new SkySQL service with Azure Private Link enabled can be found in the [terraform provider examples](https://github.com/skysqlinc/terraform-provider-skysql/tree/main/examples/azure-private-link).

For more information on using the SkySQL Terraform Provider, see ["SkySQL Terraform Provider"](https://registry.terraform.io/providers/skysqlinc/skysql/latest/docs).

</details>

**For the next step, see the** [**Azure Endpoint Setup**](<Setting up Azure Private Link.md#azure-endpoint-setup>) **section on this page.**

### **Enable Azure Private Link on an Existing SkySQL Service**

> \[!CAUTION] Enabling Private Link on an existing service will cause all existing connections to be dropped. The service will be unavailable for a short period of time while the public endpoint is replaced with the new Private Link endpoint.

<details>

<summary>Enable Azure Private Link on an existing service via the SkySQL Portal:</summary>

\


1. Log in to the SkySQL Portal
2. Click the "MANAGE" button (on the right) for the desired service.
3. In the context menu, choose the "Set up Azure Private Link" menu item.
4. In the popup window, add one or more Azure account IDs.
5. Click the "OK" button to confirm this operation.

</details>

<details>

<summary>Enable Azure Private Link on an existing service via the SkySQL DBaaS API:</summary>

\


To enable Azure Private Link on an existing service, you will need to update the service endpoints with a payload similar to the following:

```json
[
  {
    "mechanism": "privateconnect",
    "allowed_accounts": [
      "AZURE-SUBSCRIPTION-ID-1",
      "AZURE-SUBSCRIPTION-ID-2"
    ]
  }
]
```

This payload should then be sent to the API `PATCH` https://api.skysql.com/provisioning/v1/services/{SERVICE\_ID}/endpoints where `{SERVICE_ID}` is the ID of the service you are updating. For more information on using the SkySQL DBaaS API, see ["SkySQL DBaaS API"](https://apidocs.skysql.com/#/Services/patch_provisioning_v1_services__service_id__endpoints).

</details>

**For the next step, see the** [**Azure Endpoint Setup**](<Setting up Azure Private Link.md#azure-endpoint-setup>) **section on this page.**

## Azure Endpoint Setup

To connect to a SkySQL service using Azure Private Link, you must create an endpoint in your VNet that connects to the SkySQL service. The endpoint will be used by clients in your VNet to connect to the SkySQL service.

### Pre-requisites

* You must have a Virtual Network in the same region as the SkySQL service.
*   You will need to look up the Endpoint Service ID that SkySQL provisioned for you when you created your SkySQL Service.

    * This ID can be found in the "Connect" window of the SkySQL portal.
    * This ID references the "Alias" field of the Azure created Private Link service.
    * If using the SkySQL DBaaS API, the ID can be found in the response of the service details API call.

    ```bash
    curl https://api.skysql.com/provisioning/v1/services/{SERVICE_ID} \
         | jq ".endpoints[0].endpoint_service"
    ```

### Private Link Endpoint Creation Steps

1. Log in to the Azure console.
2. Navigate to the "Private Link" page, then the "Private endpoints" section.

* The easiest way to get here is to enter "Private Link" in the search bar at the top of the Azure console and then select "Private endpoints" on the left navigation bar.

3. Click the "Create" button on the "Private Link Center | Private endpoints" page.
4. In the "Basics" tab, update the following:

* Subscription: Select the subscription that contains the VNet you want to use.
* Resource group: Select the resource group that will host the Private Link endpoint.
* Name: Enter a name for the Private Link endpoint. This can be anything you like.
* Network Interface Name: Enter a name for the network interface or leave the default value.
* Region: Select the region where the Virtual Network and the SkySQL service are located.

5. Click the "Next: Resource" button.
6. In the "Resource" tab, update the following:

* Connection Method: "Connect to an Azure resource by resource ID or alias."
* Resource ID or alias: Enter the value of the Endpoint Service ID provided to you by SkySQL. See [Pre-requisites](<Setting up Azure Private Link.md#pre-requisites>) for more information on how to find this ID.
* You should see a little green check mark in the "Resource ID or alias" field if the value is correct.
* Request message: You can leave this blank as SkySQL will automatically approve connections from your allowlisted Azure Subscription.

7. Click the "Next: Virtual Network" button.
8. In the "Virtual Network" tab, update the following:

* Virtual Network: Select the VNet that you want to use to connect to the SkySQL service.
* Subnet: Select the subnet within the VNet that you want to use to connect to the SkySQL service. Any service that will connect to the SkySQL service must be able to route to this subnet.

9. Click the "Next: DNS" button.

* Leave this section as the default settings.

10. Click the "Next: Tags" button.

* You can add any tags that you wish to help identify the endpoint. This is completely optional.

11. Click the "Review + create" button.
12. After reviewing the settings, click the "Create" button.

After creation, Azure will begin provisioning the new Endpoint. Once the provisioning is complete, you can inspect the details of your newly created endpoint by clicking the "Go to Resource" button, or by navigating again to the "Private Link Center | Private endpoints" page. On the details page, you will see a link to the "Network Interface" that was created for the endpoint. This network interface will have a private IP address that you can use to connect to the SkySQL service.

### Connecting to your SkySQL Service

After creating your Private Link endpoint, you will need to find the IP address associated with that endpoint. This IP address can be found in the properties of the network interface that was created for the endpoint.

* The hostname when connecting to your SkySQL service should always be the Private IP address of the Private Endpoint.
* The SSL certificate provided by SkySQL will not match the IP address of the service. To avoid this issue, you can either disable SSL on the SkySQL service, or setup Private DNS within your Azure VNet. See ["Enabling DNS for Azure Private Link"](<Setting up Azure Private Link.md#enabling-dns-for-azure-private-link>) for more information.

### Enabling Private DNS for Azure Private Link

Enabling Private DNS for Azure Private Link is optional. However, if you wish to use a verified SSL connection to the SkySQL service, you will need to create a Private DNS record in your Azure account that maps the service name provided by SkySQL to the private IP address of the Private Link endpoint.

The following links will help guide you through the process of setting up Private DNS in Azure:

* [Creating a Private DNS Zone in Microsoft Azure](https://learn.microsoft.com/en-us/azure/dns/private-dns-getstarted-portal)
* [Linking a Private DNS Zone to a Virtual Network](https://learn.microsoft.com/en-us/azure/dns/private-dns-getstarted-portal#link-the-virtual-network)
* [Adding DNS Records to a Private DNS Zone](https://learn.microsoft.com/en-us/azure/dns/private-dns-getstarted-portal#create-another-dns-record)

> \[!CAUTION] When linking a DNS zone for your skysql.com domain, you will delegate all DNS resolution for that domain to Azure. This means that all DNS queries for that domain will be resolved by Azure DNS servers. If you have other public services that use the same domain, these hostnames will no longer resolve to services inside your linked VNet.

Since Private DNS setup is a complex process, we have provided a terraform example that can help with the process. We highly advise that you explore this example if your organization requires this type of setup. The example can be found in the [terraform provider examples](https://github.com/skysqlinc/terraform-provider-skysql/tree/main/examples/azure-private-link)

### **Disabling Azure Private Link**

> \[!CAUTION] Disabling Private Link on an existing service will cause all existing connections to be dropped. The service will be unavailable for a short period of time while the private endpoint is replaced with the new public endpoint.

<details>

<summary>Disable Azure Private Link via the SkySQL Portal</summary>

\


1. Visit the [SkySQL Portal](https://app.skysql.com/)
2. Find the service that you would like to modify.
3. Click "MANAGE" on the far right side of the service listing.
4. In the context menu, select "Manage Private Link".
5. In the popup window, click "I want to disconnect my Private Link".
6. In the popup window, select "Disconnect".
7. Since the service's allowlist was cleared when Azure Private Link was previously enabled, you will need to [update the allowlist](<../Security/Configuring Firewall.md>) to allow clients to connect after disabling Private Link.

</details>

<details>

<summary>Disable Azure Private Link via the SkySQL DBaaS API</summary>

\


To disable Azure Private Link on an existing service, you will need to update the service endpoints with a payload similar to the following:

```json
[
  {
    "mechanism": "nlb"
  }
]
```

This payload should then be sent to the API `PATCH` https://api.skysql.com/provisioning/v1/services/{SERVICE\_ID}/endpoints where `{SERVICE_ID}` is the ID of the service you are updating. For more information on using the SkySQL DBaaS API, see ["SkySQL DBaaS API"](https://apidocs.skysql.com/#/Services/patch_provisioning_v1_services__service_id__endpoints).

</details>
