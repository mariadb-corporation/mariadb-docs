---
hidden: true
noIndex: true
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: false
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
---

# Basic Support

MariaDB Community Server provides a strong foundation for your applications, offering the flexibility and ease of use essential for modern environments. Our Basic Support offering provides direct access to the expertise you need to maximize your MariaDB Community Server deployment.

#### Support Package Details

This support package is specifically structured for companies with up to 150 employees, providing focused and efficient expert assistance.

* Pricing: $600 USD / €520 per core, per year
* Core coverage: Minimum 2 cores, maximum 16 cores
* Support tickets: 12 support tickets annually&#x20;
* SLA: 24-hour Standard Priority Issue First Response
* User access: 1 authorized user for ticketing system access
* Scope: Support applies exclusively to MariaDB Community Server, including the InnoDB, MyISAM and Aria storage engines.

#### Eligibility Requirements

To ensure we can provide the most focused and effective support, this MariaDB Community Server support package is available for:

* Companies with 150 or fewer employees.
* Database deployments utilizing between 2-16 database cores.

For more information about Basic Support and how to purchase, see [here](https://mariadb.com/services/technical-support-services/basic-support/).&#x20;

### Open a Basic Support ticket

1. Log into the [MariaDB Customer Portal](https://support.mariadb.com/)
2. Select "Submit Ticket" or "Open Ticket" button on Customer Portal dashboard

<figure><img src=".gitbook/assets/customer-portal-submit-ticket (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/mariadb-customer-portal-open ticket.png" alt=""><figcaption></figcaption></figure>

3. Fill out ticket request form
4. **Important:** Attach support script output to ticket. It is **required for all Basic Support tickets**. Instructions to obtain the output can be found [below](basic-support.md#run-required-support-script).
5. Submit ticket

### Run required support script

**Step 1:** Download the support script:

```
wget https://dlm.mariadb.com/mariadb-support-script/mdb-support.sh
```

**Step 2:** Make the script executable:

```
chmod +x ./mdb-support.sh
```

**Step 3:** Execute the script:

```
./mdb-support.sh --caseno {{ticket.id}}
```

**Step 4:** Attach the file created by the script to this ticket. The file name will end with "\*-support.tgz".

**Note:** If you have questions about running this support script or run into any issues, please add a comment with details to your open support ticket.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
