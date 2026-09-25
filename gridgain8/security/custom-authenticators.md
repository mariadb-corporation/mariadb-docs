---
description: >-
  Implement a custom GridGain authenticator, illustrated with a file-based ACL
  provider for PasscodeAuthenticator.
---

# Implementing Custom Authenticator

## File-based Authenticator

In this section, we implement an authenticator that loads a list of credentials from a file.
You can further enhance this implementation to work with an encrypted file or other secure sources.

We will use `PasscodeAuthenticator`, which is part of GridGain, and simply implement a custom credential provider (`AuthenticationAclProvider`).
`AuthenticationAclProvider` is an interface that has one method (`acl()`) that must return a list of credentials and the permissions associated with them. The method is called on node start-up.

The file with credentials has the following format:
Each line is either a comment or has the format "user:password:permissions", where "permissions" is a one-line [permission string](authorization-permissions.md#permission-string-format).

```text
# server permissions
server:password123:{defaultAllow:true}

# client permissions
client:123password:{defaultAllow:false, {cache:'*',permissions:['CACHE_READ']}}
```

The following code snippet is an implementation of `AuthenticationAclProvider`:

{% code title="FilebasedAclProvider.java" %}
```java
public class FilebasedAclProvider implements AuthenticationAclProvider {

    private String passwordFile;

    public FilebasedAclProvider(String passwordFile) {
        this.passwordFile = passwordFile;
        if (Files.notExists(Paths.get(passwordFile))) {
            throw new IgniteException("The password file '" + passwordFile + "' does not exist");
        }
    }

    @Override
    public Map<SecurityCredentials, SecurityPermissionSet> acl() throws IgniteException {
        return readFile();
    }

    private Map<SecurityCredentials, SecurityPermissionSet> readFile() throws IgniteException {
        Map<SecurityCredentials, SecurityPermissionSet> map = new HashMap<SecurityCredentials, SecurityPermissionSet>();

        try {
            List<String> lines = Files.readAllLines(Paths.get(passwordFile), StandardCharsets.UTF_8);

            for (int i = 0; i < lines.size(); i++) {
                String line = lines.get(i);

                // skip empty lines and comments
                if (!line.isBlank() && !line.trim().startsWith("#")) {

                    String[] parts = line.split(":");

                    if (parts.length < 3 || parts[0].isBlank() || parts[1].isBlank()) {
                        // skip incorrect password lines
                        System.out.format("Line %s of the password file has incorrect format.\n", i);
                    }

                    SecurityPermissionSet permissions;
                    try {

                        permissions = new GridSecurityPermissionSetJsonParser(parts[2]).parse();

                        map.put(new SecurityCredentials(parts[0].trim(), parts[1].trim()), permissions);

                    } catch (IgniteCheckedException e) {
                        System.out.format("Could not parse permissions from line %s", i);
                    }
                }
            }
        } catch (Exception e) {
            throw new IgniteException(e);
        }
        return map;
    }

    public static void main(String[] args) {
        IgniteConfiguration cfg = new IgniteConfiguration();

        GridGainConfiguration ggCfg = new GridGainConfiguration();

        PasscodeAuthenticator authenticator = new PasscodeAuthenticator();
        authenticator.setAclProvider(new FilebasedAclProvider("passwords"));

        ggCfg.setAuthenticator(authenticator);

        // credentials for this node
        ggCfg.setSecurityCredentialsProvider(
                new SecurityCredentialsBasicProvider(new SecurityCredentials("server", "password123")));

        cfg.setPluginConfigurations(ggCfg);

        Ignition.start(cfg);
    }
}
```
{% endcode %}

The code simply parses the provided file and returns

Run a node as follows:

```java
public static void main(String[] args) {
    IgniteConfiguration cfg = new IgniteConfiguration();

    GridGainConfiguration ggCfg = new GridGainConfiguration();

    PasscodeAuthenticator authenticator = new PasscodeAuthenticator();
    authenticator.setAclProvider(new FilebasedAclProvider("passwords"));

    ggCfg.setAuthenticator(authenticator);

    // credentials for this node
    ggCfg.setSecurityCredentialsProvider(
            new SecurityCredentialsBasicProvider(new SecurityCredentials("server", "password123")));

    cfg.setPluginConfigurations(ggCfg);

    Ignition.start(cfg);
}
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
