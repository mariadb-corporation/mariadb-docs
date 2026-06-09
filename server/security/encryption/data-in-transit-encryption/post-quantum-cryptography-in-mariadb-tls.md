# Post-Quantum Cryptography in MariaDB TLS

## Overview

Quantum computers use quantum mechanics to solve mathematical problems much faster than traditional computers. Their capacity to crack the public-key cryptographic techniques that currently support TLS handshakes, such as RSA and Elliptic Curve Cryptography (ECC), is especially concerning.

This poses a threat known as **harvest now, decrypt later**: an attacker can intercept and store encrypted database communication now, then decrypt it later when sufficiently robust quantum computers are made accessible. Thus, even current threats pose a risk to long-lived sensitive data, such as financial records, intellectual property, and personally identifiable information (PII).

The **National Institute of Standards and Technology** (NIST) in the United States has standardized two post-quantum cryptography algorithms to address this:

* **ML-KEM** (Module Lattice Key Encapsulation Mechanism) (FIPS 203): A key encapsulation technique for quantum-resistant key exchange during TLS handshakes.
* **ML-DSA** (Module Lattice Digital Signature Algorithm) (FIPS 204): A digital signature scheme for quantum-resistant server authentication.
* **Hybrid mode**: Use of both classical and post-quantum algorithms together during the transition period. The session key is secure if either algorithm remains unbroken.

MariaDB automatically negotiates ML-KEM for TLS 1.3 key exchange when linked against **OpenSSL 3.5 or later**, requiring no further configuration. Because of this, MariaDB connections are inherently quantum-resistant in transit.

## Requirements

| Component      | Version Requirement |
| -------------- | ------------------- |
| MariaDB Server | -                   |
| OpenSSL        | 3.5.0 or later      |

## How It Works

MariaDB assigns the system OpenSSL library to handle TLS operations. As a TLS 1.3 key exchange group, OpenSSL 3.5 included native support for ML-KEM. A MariaDB server will automatically publish ML-KEM key exchange groups during the TLS 1.3 handshake if OpenSSL 3.5 or later is installed.

There is no need to modify any server system variables. During this time of transition, **hybrid mode** is used. This indicates that ML-KEM and a traditional method like classical Elliptic Curve (X25519) are used for key exchange. This hybrid classical and post-quantum approach is reflected in the negotiated group that can be seen in the handshake output: `X25519MLKEM768`.&#x20;

This ensures backward compatibility. Clients that do not support ML‑KEM continue to use traditional key exchange to establish connections.

### Verifying Quantum-Resistant TLS

By connecting to the OpenSSL client and examining the negotiated TLS group, you can verify that a MariaDB connection uses ML-KEM.

```sql
$ openssl s_client -starttls mysql localhost:3306
```

**Output**

Look for the Negotiated TLS1.3 group in the output:

```sql
Peer signing digest: SHA256
Peer signature type: rsa_pss_rsae_sha256
Negotiated TLS1.3 group: X25519MLKEM768
```

A value of `X25519MLKEM768` indicates that the hybrid classical and ML-KEM key exchange is operational. During transit, the connection is quantum-resistant.

### Compatibility

MariaDB automatically returns to traditional TLS 1.3 key exchange when a connecting client does not support post-quantum key exchange groups. Current clients and applications do not require any setup adjustments. Connections that are limited to classical methods remain unchanged.

### Data-in-Transit and Data-at-Rest

Post quantum cryptography secures data while it is transmitted across a network. Data at rest should also be protected with quantum‑resistant encryption to ensure comprehensive quantum resistance. For this reason, AES-256 is advised since it offers enough key length to survive known quantum attacks. See [Data-at-Rest-Encryption](../data-at-rest-encryption/) for information on how to enable encryption for table data and tablespaces in MariaDB.

### Performance Considerations

* **Handshake size**: Post‑quantum algorithms may produce slightly larger handshakes.
* **Performance impact**: Session reuse reduces overhead.
* **Workload suitability**: Appropriate for typical database workloads.

## See Also

* [TLS and Cryptography Libraries used by MariaDB](../tls-and-cryptography-libraries-used-by-mariadb.md)
* [Data-at-Rest-Encryption](../data-at-rest-encryption/)
* [Securing Connections for Client and Server](securing-connections-for-client-and-server.md)
* [NIST FIPS 203 (ML-KEM)](https://csrc.nist.gov/pubs/fips/203/final)&#x20;
* [NIST FIPS 204 (ML-DSA)](https://csrc.nist.gov/pubs/fips/204/final)
