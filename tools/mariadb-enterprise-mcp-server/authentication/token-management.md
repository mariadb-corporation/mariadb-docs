---
description: >-
  The MCP Server issues JWT tokens on login, then validates each request by
  verifying the signature, checking token expiration, and confirming the
  user against the shared MariaDB database.
---

# Token Management

Token management is a critical part of the system's security, handled primarily by the RAG API.

## **Token Generation**

The process involves two main steps:

### **Step 1: User Registration**

```mermaid
graph TD
    A[User] -->|Sends Email & Password| B(POST /register)
    B --> C[Hash Password with bcrypt]
    C --> D[Store User in Database]
```

### **Step 2: User Login & Token Generation**

```mermaid
graph TD
    A[User] -->|Sends Credentials| B(POST /token)
    B --> C[Verify Credentials in DB]
    C --> D[Determine User Roles]
    D --> E[Generate JWT Token]
    E --> F[Return Token to User]
```

## **Token Usage**

Once a client has a JWT, it includes it in the `Authorization` header of every request to the MCP Server. The server then validates the token before processing the request.

```mermaid
sequenceDiagram
    participant Client
    participant MCP Server
    participant RAG API
    participant Database

    Client->>MCP Server: Tool Call + JWT Token
    
    Note over MCP Server: 1. Extract Token<br/>2. Verify JWT Signature
    
    MCP Server->>Database: 3. Validate User in DB
    Database-->>MCP Server: User Record
    
    Note over MCP Server: (If RAG tool is called)
    MCP Server->>RAG API: 4. Forward Request + Token
    Note over RAG API: 5. Verify Token Again
    RAG API-->>MCP Server: Processed Result
    
    MCP Server-->>Client: Response
```

## **Key Security Measures**

* **Signature Verification**: Prevents token tampering.
* **Expiration Check**: Tokens have a limited lifetime (e.g., 30 minutes).
* **Database Validation**: Ensures the user associated with the token still exists and is active.
* **Issuer/Audience Validation**: Prevents a token from one system from being used on another.
* **Not-Before Check**: Prevents a token from being used before it is valid

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
