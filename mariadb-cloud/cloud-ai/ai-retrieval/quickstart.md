---
description: >-
  Create a document knowledge base or a database knowledge base in MariaDB
  Cloud AI Retrieval with the default settings, and run your first query.
icon: rocket
hidden: true
---

<!-- DRAFT for DOCS-6592. Hidden until the Public Preview launch. One page with two sections, as Egor Ustinov asked on 2026-10-20: defaults only, no model names, no data sources. Built from the recording of that call and from the guide. Open items are marked TODO. -->

# Quickstart

This quickstart creates a knowledge base with the default settings and runs a first query. It has two sections: one for a document knowledge base, which answers questions about files that you upload, and one for a database knowledge base, which answers questions about the data in a MariaDB service. For every option and the reasons behind the defaults, see [Document Knowledge Bases](document-knowledge-bases.md) and the other pages in this section.

## Before You Begin

* You need a MariaDB Cloud account and a role that can create knowledge bases. The Viewer role cannot.
* Knowledge bases run on AWS.

## Create a Document Knowledge Base

1. In the portal, select **AI Retrieval** in the navigation, and then **Create Knowledge Base**.
2. For **Type**, select **Document Knowledge Base**.
3. Enter a **Name**.
4. Leave **AWS** and the region as they are.
5. Under **Vector Store Configuration**, select **Auto-provision new service**. MariaDB Cloud creates a MariaDB Serverless service to store the vectors.
6. Select **Create Knowledge Base**.

<figure><img src="../../.gitbook/assets/ai-retrieval-quickstart-create.png" alt="The Create Knowledge Base form with Document Knowledge Base, the name quickstart-docs, AWS in Frankfurt, and Auto-provision new service selected."><figcaption><p>The Create Knowledge Base form with the default settings</p></figcaption></figure>

The knowledge base shows the status **Provisioning**. This usually takes a few minutes.

<figure><img src="../../.gitbook/assets/ai-retrieval-quickstart-provisioning.png" alt="The page of the knowledge base quickstart-docs with the Provisioning status and the banner that says that the knowledge base is being provisioned."><figcaption><p>A knowledge base that is being provisioned</p></figcaption></figure> When the status is **Ready**, the knowledge base is ready for documents.


The knowledge base uses the default embedding model and generation model, and the reranker is on. You do not need to change them to continue.

### Upload a Document

1. On the knowledge base page, select **Upload Documents**.
2. Select a file, such as a PDF, a Word document, or a Markdown file, and select **Next**. A file can be up to 50 MB.
3. Leave the parsing and chunking options as they are, and select **Upload**.

<figure><img src="../../.gitbook/assets/ai-retrieval-upload-files.png" alt="The Files step of the Upload Files dialog with three files selected."><figcaption><p>The Files step of the Upload Files dialog</p></figcaption></figure>

The document appears in the **Documents** list. Wait until its status is **Ingested**. The **Chunks** column then shows how many chunks the document produced.

<figure><img src="../../.gitbook/assets/ai-retrieval-quickstart-ingested.png" alt="The page of the Ready knowledge base quickstart-docs, with the vector store quickstart-docs-vs and a Documents list that shows the file getting-started.md with the status Ingested and 4 chunks."><figcaption><p>A document with the status Ingested</p></figcaption></figure>

### Run a Query

1. Select **Test**.
2. On the **Retrieve & Generate** tab, enter a question about your document, and select **Test Query**.

The answer cites the chunks of your document that it uses. The **Retrieve** tab shows the matching chunks without a generated answer.

<figure><img src="../../.gitbook/assets/ai-retrieval-quickstart-answer.png" alt="The Test Knowledge Base drawer on the Retrieve and Generate tab with the question How do I create my first widget and a generated answer that ends with the citation marker 1."><figcaption><p>A generated answer with a citation</p></figcaption></figure>

To call the knowledge base from an application, see [Connect Your Application](document-knowledge-bases.md#connect-your-application).


## Create a Database Knowledge Base

A database knowledge base reads the tables of a MariaDB service that already holds your data.

1. Select **AI Retrieval** in the navigation, and then **Create Knowledge Base**.
2. For **Type**, select **Database Knowledge Base**.
3. Enter a **Name**.
4. Under **Datasource**, select your service. The hostname, the port, and the default user are filled in.
5. Enter the **Schema** that holds your tables.
6. Select **Create Knowledge Base**.
7. On the knowledge base page, select **Sync Now**. The sync reads the tables that the user can see and builds the semantic map, which AI Retrieval uses to turn a question into a query.
8. When the sync finishes, select **Test**, and ask a question about your data.

For access requirements, such as the IP allowlist and restricting what the knowledge base can read, see [Access and Security](access-and-security.md).

<!-- TODO: the database knowledge base UI is not merged yet (Egor, 2026-10-20), so these steps follow the test environment form in the recording: Datasource service, Hostname (FQDN), Port, Schema, Username, Password, Always include tables, Never include tables. Re-check every step, the sync button name, and the test steps against the final UI, and add screenshots then. -->
<!-- TODO: say where the IP address to allow is shown once Egor answers (see access-and-security.md). -->
<!-- TODO: Egor said a demo database will be available as a datasource. Mention it here when it ships. -->

## Next Steps

{% content-ref url="document-knowledge-bases.md" %}
[document-knowledge-bases.md](document-knowledge-bases.md)
{% endcontent-ref %}

{% content-ref url="parsing-and-chunking.md" %}
[parsing-and-chunking.md](parsing-and-chunking.md)
{% endcontent-ref %}

{% content-ref url="access-and-security.md" %}
[access-and-security.md](access-and-security.md)
{% endcontent-ref %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
