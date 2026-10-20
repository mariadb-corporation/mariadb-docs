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
%%{init: {"themeVariables": {"edgeLabelBackground": "#eef2ff"}}}%%
graph TD
    accTitle: User registration flow
    accDescr {
        A top-to-bottom chain of four boxes joined by one-way arrows. User leads
        to POST /register, labelled Sends Email & Password. POST /register leads
        to Hash Password with bcrypt, which leads to Store User in Database.
    }
    A[User] -->|Sends Email & Password| B(POST /register)
    B --> C[Hash Password with bcrypt]
    C --> D[Store User in Database]
    linkStyle default color:#111111
```

### **Step 2: User Login & Token Generation**

```mermaid
%%{init: {"themeVariables": {"edgeLabelBackground": "#eef2ff"}}}%%
graph TD
    accTitle: User login and token generation flow
    accDescr {
        A top-to-bottom chain of six boxes joined by one-way arrows. User leads to
        POST /token, labelled Sends Credentials. POST /token leads to Verify
        Credentials in DB, which leads to Determine User Roles. Determine User
        Roles leads to Generate JWT Token, which leads to Return Token to User.
    }
    A[User] -->|Sends Credentials| B(POST /token)
    B --> C[Verify Credentials in DB]
    C --> D[Determine User Roles]
    D --> E[Generate JWT Token]
    E --> F[Return Token to User]
    linkStyle default color:#111111
```

## **Token Usage**

Once a client has a JWT, it includes it in the `Authorization` header of every request to the MCP Server. The server then validates the token before processing the request.

```mermaid
sequenceDiagram
    accTitle: Token validation for an MCP Server request
    accDescr {
        A sequence between four participants: Client, MCP Server, RAG API and
        Database. Client sends Tool Call + JWT Token to MCP Server. A note over
        MCP Server lists two steps: 1. Extract Token and 2. Verify JWT Signature.
        3. Validate User in DB: MCP Server sends this to Database, and Database
        replies User Record to MCP Server. A note over MCP Server reads (If RAG
        tool is called). 4. Forward Request + Token: MCP Server sends this to RAG
        API. A note over RAG API reads 5. Verify Token Again. RAG API replies
        Processed Result to MCP Server. MCP Server replies Response to Client.
    }
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

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
