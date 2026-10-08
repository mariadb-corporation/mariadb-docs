---
description: Quickstart guide for Connector/Ruby
---

# Connector/Ruby Guide

### Quickstart Guide: MariaDB Connector/Ruby (using `mysql2` gem)

While there isn't a separate "MariaDB Connector/Ruby" gem, the widely used `mysql2` gem serves as the primary and highly compatible Ruby client for connecting to both MariaDB and MySQL databases. It provides a robust API for database interactions in Ruby applications.

#### 1. Overview

The `mysql2` gem provides a Ruby interface to the MariaDB/MySQL C client library (either `libmysqlclient` or MariaDB Connector/C). It allows Ruby applications to execute SQL queries, fetch results, and manage database connections efficiently. It's available on [rubygems.org/gems/mysql2](https://rubygems.org/gems/mysql2).

#### 2. Installation

Before installing the `mysql2` gem, you might need to install development libraries for MariaDB Connector/C or MySQL Client on your system.

**a. Install System Dependencies (e.g., on Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libmariadb-dev # Or libmysqlclient-dev
```

On other systems (Fedora, CentOS, macOS), the package names might differ (e.g., `mariadb-devel`, `mysql-devel`).

**b. Install the `mysql2` gem:**

Once the system dependencies are in place, install the gem using Bundler (recommended for Rails/Gemfile projects) or directly via `gem install`:

```bash
# If using Bundler (e.g., in a Rails project's Gemfile)
# Gemfile
# gem 'mysql2'
bundle install

# Or directly
gem install mysql2
```

#### 3. Basic Usage

Here's how to connect to MariaDB and perform common database operations using the `mysql2` gem:

**a. Connect to the Database:**

```ruby
require 'mysql2'

begin
  client = Mysql2::Client.new(
    host: 'localhost',
    port: 3306,
    username: 'your_username',
    password: 'your_password',
    database: 'your_database_name'
  )
  puts "Successfully connected to MariaDB!"

  # ... database operations ...

rescue Mysql2::Error => e
  puts "Error connecting to database: #{e.message}"
ensure
  client&.close # Ensure the connection is closed
end
```

Replace `localhost`, `3306`, `your_username`, `your_password`, and `your_database_name` with your actual database details.

**b. Execute a SELECT Query:**

```ruby
# Assuming 'client' is an open connection
results = client.query("SELECT id, name FROM your_table_name WHERE status = 'active'")

puts "\nSelected Rows:"
results.each do |row|
  puts "ID: #{row['id']}, Name: #{row['name']}"
end
```

The `results` object behaves like an enumerable, allowing you to iterate over rows. Column names are accessible as hash keys.

**c. Execute INSERT/UPDATE/DELETE Queries:**

For data manipulation, use `query`. For safety, **always use prepared statements or proper escaping** for user-provided input.

```ruby
# INSERT Example (using prepared statement)
statement = client.prepare("INSERT INTO your_table_name (name, status) VALUES (?, ?)")
insert_result = statement.execute("New Item", "pending")
puts "\nRows inserted: #{insert_result.affected_rows}, Last ID: #{insert_result.last_id}"

# UPDATE Example
update_result = client.query("UPDATE your_table_name SET status = 'completed' WHERE name = 'New Item'")
puts "Rows updated: #{update_result.affected_rows}"

# DELETE Example
delete_result = client.query("DELETE FROM your_table_name WHERE name = 'New Item'")
puts "Rows deleted: #{delete_result.affected_rows}"
```

**d. Prepared Statements (Recommended for security and performance):**

Prepared statements allow you to separate the SQL query structure from the data, preventing SQL injection and improving performance for repeated queries.

```ruby
# Assuming 'client' is an open connection
statement = client.prepare("SELECT * FROM users WHERE login_count = ?")

# Execute with different parameters
result1 = statement.execute(1)
puts "\nUsers with login_count = 1:"
result1.each { |row| puts row.inspect }

result2 = statement.execute(5)
puts "\nUsers with login_count = 5:"
result2.each { |row| puts row.inspect }
```

**Before Running:**

1. Ensure you have a MariaDB server running and a database/table set up.
2. Replace placeholder values with your actual database credentials and table/column names.

#### Important Notes:

* **Error Handling:** Always wrap your database operations in `begin...rescue...end` blocks to catch `Mysql2::Error` exceptions.
* **Connection Closing:** Ensure your `Mysql2::Client` connection is closed using `client.close` in a `ensure` block to release database resources.
* **Prepared Statements/Escaping:** Never concatenate user-provided strings directly into SQL queries. Use prepared statements with placeholders (`?`) or `client.escape()` for string literals.

#### Further Resources:

* [mysql2 gem on RubyGems.org](https://rubygems.org/gems/mysql2)
* [mysql2 gem Documentation (Rubydoc.info)](https://www.rubydoc.info/gems/mysql2/)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
