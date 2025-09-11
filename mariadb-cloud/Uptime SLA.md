# Uptime SLA

SkySQL customers should assess the availability requirements of their application and choose an appropriate service tier to meet their objectives. SkySQL customers are on the Foundation Tier unless they have specifically purchased and paid for Power Tier service.

## **Performance Standard**

| Tier | Performance Standard |
| --- | --- |
| SkySQL Foundation Tier | Multi-node configurations will deliver a 99.95% service availability on a per-billing-month basis. For example, with this availability target in a 30 day calendar month the maximum service downtime is 21 minutes and 54 seconds. |
| SkySQL Power Tier | Multi-node configurations will deliver a 99.995% service availability on a per-billing-month basis. For example, with this availability target in a 30 day calendar month the maximum service downtime is 2 minutes and 11 seconds. |

## **Service Downtime**

**Service Downtime** is measured at each SkySQL database endpoint as the total number of full minutes, outside of scheduled downtime for maintenance and upgrades, where continuous attempts to establish a connection within the minute fail as reflected in minute-by-minute logs.

## **Monthly Uptime Percentage**

**Monthly Uptime Percentage** is calculated on a per-billing-month basis as the total number of minutes in a month, minus the number of minutes of measured [Service Downtime](https://skysql.com/sla/) within the month, divided by the number of minutes in that month. When a service is deployed for only part of a month, it is assumed to be 100% available for the portion of the month that it is not deployed.

## **Service Credit**

**Service Credit** is the percentage of the total fees paid by you for a given SkySQL service during the month in which the downtime occurred to be credited if SkySQL approves your claim. The percentage used in calculating Service Credit is dependent on whether the customer is on Foundation Tier or Power Tier, and is dependent on the calculated [Monthly Uptime Percentage](https://skysql.com/sla/).

| Tier | Monthly Uptime Percentage | Percentage Applied |
| --- | --- | --- |
| Foundation Tier | Less than 99.95%, but greater than or equal to 99.0% | 10% |
| Foundation Tier | Less than 99.0% | 25% |
| Power Tier | Less than 99.995%, but greater than or equal to 99.0% | 10% |
| Power Tier | Less than 99.0% | 25% |

SkySQL will grant and process claims, provided the customer has satisfied its [Customer Obligations](https://skysql.com/sla/) and that none of the [Exclusions](https://skysql.com/sla/) listed apply to the claim. [Service Credits](https://skysql.com/sla/) will be issued only upon request within 60 days of the end of the billing period of the month of impact to service availability, and upon confirmation of outage. [Service Credits](https://skysql.com/sla/) will be issued in the form of a monetary credit applied to future use of the service that experienced the [Service Downtime](https://skysql.com/sla/). [Service Credits](https://skysql.com/sla/) will not be applied to fees for any other SkySQL instance.

The aggregate maximum number of [Service Credits](https://skysql.com/sla/) to be issued by SkySQL to customers for any and all [Service Downtime](https://skysql.com/sla/) that occurs in a single billing month will not exceed 50% of the amount due from the customer for the covered service for the applicable month.

## **Customer Obligations**

A customer will forfeit their right to receive a [Service Credit](https://skysql.com/sla/) unless they:

- Log a support ticket with SkySQL Support within 60 minutes of first becoming aware of an event that impacts service availability.
- Submit a claim and all required information by the end of the month immediately following the month when the [Service Downtime](https://skysql.com/sla/) occurred.
- Submit necessary information for SkySQL to validate the claim, including:
    - a description of the events resulting in the [Service Downtime](https://skysql.com/sla/), and related request logs
    - the date, time, and duration of the [Service Downtime](https://skysql.com/sla/)
    - the number and location(s) of affected users
    - descriptions of customer attempts to fix the [Service Downtime](https://skysql.com/sla/) as it occurred
- Provide reasonable assistance to SkySQL in investigating the cause of the [Service Downtime](https://skysql.com/sla/) and investigating your claim.

## **Exclusions**

- **Out-of-scope configurations**
    
    The [Performance Standard](https://skysql.com/sla/) does not apply to single instance SkySQL service configuration or services in Technical Preview. Customers requiring High Availability should deploy instead in production-ready multi-node service configuration.
        
- **Underlying infrastructure**
    
    Impact to service availability caused by availability or performance of cloud services used to operate SkySQL is excluded. This includes any such outages in Amazon Web Services (AWS) and Amazon Elastic Kubernetes Service (EKS), and Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE).
    
- **Network interruption**
    
    Impact to service availability caused by blocking of network traffic by ISPs, network providers, governments, or third parties is excluded.
    
- **External factors**
    
    Impact to your use of service based on factors outside SkySQL are excluded. This includes periods of downtime for your applications.
    
- **Uncorroborated impacts**
    
    Only impacts to service availability detected at [point of measurement](https://skysql.com/sla/) are subject when determining the uptime percentage. Service availability impacts measured through any other means, such as application instrumentation, are excluded except as also measured as [Service Downtime](https://skysql.com/sla/) by SkySQL.
    
- **Portal access**
    
    Impact to your ability to access or use the SkySQL portal, an interface provided to manage services, is excluded. This includes any component and content linked from the SkySQL portal, including Documentation, the Customer Support portal, Monitoring, and Workload Analysis. These components operate independently from database services and do not impact database availability.
    
- **Resource usage**
    
    Impact to service availability caused by usage of system resources, such as problems caused by excessive workload consumption of CPU, disk I/O, disk capacity, memory, and other system resources, are excluded.
    
- **Clients and connectors**
    
    Impact to service availability caused by the use of unsupported third-party clients and connectors is excluded.
    
- **Non-paying customers**
    
    The [Performance Standard](https://skysql.com/sla/) applies only to paying SkySQL customers who are paid-in-full. All other SkySQL customers, including those not paid-in-full and those customers participating in a free or credited service trial, are excluded.
    
- **Customer-directed maintenance**
    
    When a customer directs that SkySQL conduct a maintenance operation on a service, any resulting impact to service availability is excluded.
    
- **Customer-approved maintenance**
    
    When a customer approves SkySQL-recommended maintenance on a service, any resulting impact to service availability is excluded.
    
- **Customer-initiated changes**
    
    When a customer initiates changes to their SkySQL services, e.g., via access to the database or via the SkySQL portal, any resulting impact to service availability is excluded.
    
- **Initial provisioning**
    
    Availability of services during initial provisioning, e.g., before a service becomes online, healthy, and available, is excluded.
