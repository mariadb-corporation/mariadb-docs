---
description: Quickstart guide for MysqlConnector for ADO.NET
---

# MariaDB Connector/NET Guide

### Quickstart Guide: MariaDB Connector/NET (MySqlConnector)

MariaDB Connector/NET, also known as MySqlConnector, is an ADO.NET data provider that enables .NET applications to connect and interact with MariaDB and MySQL databases. It's written entirely in C# and offers high performance and features specific to MariaDB Server.

#### 1. Overview and Features

MySqlConnector is licensed under the MIT License. It provides robust connectivity with features like:

* **Zero-configuration SSL:** For MariaDB Server 11.4+.
* **Server Redirection Logic:** Based on the latest MariaDB specification for MariaDB Server 11.3+.
* **Optimized `SET NAMES` handling:** Avoids unnecessary commands for MariaDB Server 11.5+.
* **MariaDB GSSAPI Authentication:** Support for secure authentication methods.
* **Asynchronous Operations:** Fully supports async/await patterns for non-blocking database interactions.

#### 2. Installation

The recommended way to install MySqlConnector is via NuGet.

**a. Using NuGet Package Manager Console (in Visual Studio):**

```powershell
Install-Package MySqlConnector -Version 2.4.0 # Use the latest stable version
```

**b. Using PackageReference (in your `.csproj` file):**

````xml
<PackageReference Include="MySqlConnector" Version="2.4.0" /> ```

**c. Using .NET CLI:**

```bash
dotnet add package MySqlConnector --version 2.4.0 # Use the latest stable version
````

#### 3. Basic Usage

This section provides C# examples for connecting to MariaDB and performing common database operations.

**a. Connection String:**

A connection string defines how your application connects to the database. Replace placeholder values with your actual database details.

```csharp
string connectionString = "Server=localhost;Port=3306;Database=your_database_name;Uid=your_username;Pwd=your_password;";
```

**b. Opening and Closing a Connection:**

Always ensure connections are properly opened and closed. The `using` statement is recommended as it ensures the connection is disposed of correctly, even if errors occur.

```csharp
using MySqlConnector;
using System;
using System.Data;
using System.Threading.Tasks;

public class MariaDBConnectorNetQuickstart
{
    private static string connectionString = "Server=localhost;Port=3306;Database=your_database_name;Uid=your_username;Pwd=your_password;";

    public static async Task Main(string[] args)
    {
        Console.WriteLine("Connecting to MariaDB...");

        try
        {
            await using var connection = new MySqlConnection(connectionString);
            await connection.OpenAsync();
            Console.WriteLine("Connection successful!");

            // Call your data operations here
            await SelectData(connection);
            await InsertData(connection);

            Console.WriteLine("Operations completed.");
        }
        catch (MySqlException ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }

    // ... (Data operation methods will go here)
}
```

**c. Executing a SELECT Query:**

Use `MySqlCommand` to define your SQL query and `ExecuteReaderAsync` to retrieve data.

```csharp
    private static async Task SelectData(MySqlConnection connection)
    {
        string query = "SELECT id, name FROM your_table_name;";
        await using var command = new MySqlCommand(query, connection);

        Console.WriteLine("\nRetrieving data:");
        await using var reader = await command.ExecuteReaderAsync();
        while (await reader.ReadAsync())
        {
            int id = reader.GetInt32("id");
            string name = reader.GetString("name");
            Console.WriteLine($"ID: {id}, Name: {name}");
        }
    }
```

**d. Executing INSERT/UPDATE/DELETE Queries:**

Use `ExecuteNonQueryAsync` for operations that do not return a result set (like `INSERT`, `UPDATE`, `DELETE`). Always use parameterized queries to prevent SQL injection vulnerabilities.

```csharp
    private static async Task InsertData(MySqlConnection connection)
    {
        string query = "INSERT INTO your_table_name (name, status) VALUES (@name, @status);";
        await using var command = new MySqlCommand(query, connection);

        command.Parameters.AddWithValue("@name", "New Item");
        command.Parameters.AddWithValue("@status", "active");

        int rowsAffected = await command.ExecuteNonQueryAsync();
        Console.WriteLine($"\nRows inserted: {rowsAffected}");
    }
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
