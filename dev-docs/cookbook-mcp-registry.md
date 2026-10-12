# Cookbook: publishing to the official MCP registry

The docs site exposes an MCP server automatically — GitBook provides it for every published
site, and nobody on the docs team configured it:

```
https://mariadb.com/docs/~gitbook/mcp
```

It works (three tools: `searchDocumentation`, `getPage`, `sendFeedback`), but being *live* and
being *discoverable* are different things. Until it is listed in the official registry at
`registry.modelcontextprotocol.io`, MCP clients can only reach it if a human pastes the URL.
This cookbook is how we publish and maintain that listing. Tracked in DOCS-6400.

> **You do not need to understand the cryptography to use this.** Two commands, one of which
> is copy-paste. Everything above the "Publish" section is background you can skip.

## Values

The one-time setup is **owned by IT**, not by us (see [Why IT holds the key](#why-it-holds-the-key)).
IT completed it on IT-21891 (2026-10-12). Neither value is a secret:

| What | Value |
|---|---|
| KMS provider | `google-kms` (Google Cloud KMS, Ed25519) |
| Key resource | `projects/mdb-mcp-signing/locations/global/keyRings/mcp-registry/cryptoKeys/mariadb-com/cryptoKeyVersions/1` |
| Who can sign | members of the Google group `mcp-registry-signers@mariadb.com`; ask IT to add you |
| Registry entry | `com.mariadb/mariadb-docs`, defined in [`mcp-registry/server.json`](mcp-registry/server.json) |
| Published | version `1.0.0` on 2026-10-12 |

## One-time setup (IT, done)

Recorded here so nobody re-derives it. **Do not do these steps yourself** — IT did them on
IT-21891, and step 3 is what keeps the docs team from becoming a single point of failure.

1. Create an asymmetric signing key in the corporate KMS. Google Cloud KMS uses Ed25519
   (`--purpose=asymmetric-signing --default-algorithm=ec-sign-ed25519`); Azure Key Vault uses
   ECDSA P-384 (`--curve P-384`). The registry supports both.
2. Publish that key's **public** half as a TXT record at the **apex** of `mariadb.com`, in the
   form `v=MCPv1; k=ed25519; p=<base64>` (or `k=ecdsap384` for Azure). This is what proves to
   the registry that we own the domain, and it is what entitles us to the `com.mariadb/*`
   namespace.
3. Grant the docs team **sign-only** permission on the key — `roles/cloudkms.signer` or Key
   Vault Crypto User — to a **group or service account**, never to one person.

## Why IT holds the key

Worth knowing, because it explains why the setup looks heavier than "add a DNS record":

- Whoever can sign with this key can publish **or overwrite any entry** under `com.mariadb/*`,
  including swapping a server's endpoint URL for one they control — which registry-trusting MCP
  clients would then connect to. It is a small supply-chain credential, not a verification token.
- The namespace realistically has **one** key. The registry tries the first `MCPv1` record it
  finds at the apex, so a second key published alongside the first breaks verification rather
  than adding a signer. If MariaDB ever publishes the Enterprise MCP Server product to the
  registry, it signs with this same key.
- Therefore: IAM grants, not a shared file. Each team gets its own grant, nobody carries the
  key, and revoking someone is an access change rather than a key rotation plus a DNS ticket.

## Publish

Install the publisher CLI and the Google Cloud CLI. Prebuilt binaries exist for macOS, Linux
and Windows, so nothing here assumes a Mac:

```bash
# macOS
brew install mcp-publisher
brew install --cask gcloud-cli

# Linux x86_64 (swap in _linux_arm64 on ARM)
curl -sL https://github.com/modelcontextprotocol/registry/releases/latest/download/mcp-publisher_linux_amd64.tar.gz \
    | tar -xz mcp-publisher && sudo install -m 0755 mcp-publisher /usr/local/bin/
```

Windows: take `mcp-publisher_windows_amd64.tar.gz` from the same releases page. Every tarball
ships with a Sigstore attestation and an SBOM if you need to verify provenance first. For the
Google Cloud CLI on Linux or Windows, see <https://cloud.google.com/sdk/docs/install>.

Sign in to Google Cloud once per machine, with the mariadb.com account that is in
`mcp-registry-signers@`. It opens a browser. The warning about a missing quota project is
harmless here:

```bash
gcloud auth application-default login
```

The entry's content lives in [`mcp-registry/server.json`](mcp-registry/server.json). Edit that
file, never a copy, so the repo always shows what is published. Check it before publishing:

```bash
cd dev-docs/mcp-registry
mcp-publisher validate
```

The `name` **must** stay `com.mariadb/mariadb-docs`. The `com.mariadb` prefix is the reverse-DNS
form of the domain we verified; any other prefix is rejected because we hold no proof for it.
The `description` is capped at **100 characters** by the registry schema. It is deliberately
generic ("every MariaDB product") because the endpoint searches every published space, so a
new space becomes searchable without a republish.

Log in and publish **in one command**. The registry's login token expires after a few minutes,
so a publish run later fails with `401 … token is expired`:

```bash
mcp-publisher login dns google-kms \
    --domain=mariadb.com \
    --resource="projects/mdb-mcp-signing/locations/global/keyRings/mcp-registry/cryptoKeys/mariadb-com/cryptoKeyVersions/1" \
  && mcp-publisher publish
```

The login prints an "Expected proof record". It must match the TXT record at the mariadb.com
apex (`dig +short TXT mariadb.com | grep MCPv1`); if it does not, the key and the DNS record
are out of step and the problem is IT's to fix. The private key never leaves the KMS; the tool
asks the KMS to sign and receives only a signature.

## Verify

```bash
curl -s "https://registry.modelcontextprotocol.io/v0/servers/com.mariadb%2Fmariadb-docs/versions/latest" | jq .
```

The entry should appear with our endpoint under `remotes`. A useful smoke test on the endpoint
itself, independent of the registry:

```bash
curl -s -X POST https://mariadb.com/docs/~gitbook/mcp \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | jq .
```

## Maintenance

Rare, but non-zero:

- **Metadata or endpoint changes** — bump `version` in `server.json` and re-run `login` +
  `publish`. The GitBook endpoint URL has been stable, so this is mostly about the description.
- **Retiring an entry** — `mcp-publisher status` handles the lifecycle (active, deprecated,
  deleted). Check `mcp-publisher status --help` for current syntax rather than guessing.
- **Registry data reset** — the registry is explicitly **in preview** and its own docs warn of
  breaking changes and data resets before GA. If our entry vanishes, re-running `publish` is
  the fix. Do not treat the listing as permanent infrastructure yet.
- **Key rotation** — IT's job, but flag the trap for them: the new public key must be published
  **and the old record removed at the same time**. A stale `MCPv1` record left at the apex is
  tried first and breaks verification.

## Traps

Every one of these cost real time on DOCS-6400.

- **The login token expires within minutes.** Run `login` and `publish` chained with `&&`, as
  in [Publish](#publish). A separate `publish` run later fails with `401 … token is expired`.
- **A `504 Gateway Time-out` from `publish` does not tell you whether it worked.** Check before
  retrying: `curl -s https://registry.modelcontextprotocol.io/v0/servers/com.mariadb%2Fmariadb-docs/versions/latest`
  returns the entry, or `404 Server not found`. Look up the entry by name like this, not with
  `?search=`; the search endpoint is the part of the registry that times out first. A retry is
  safe either way: republishing an existing version is rejected rather than duplicated.
- **The TXT record goes at the apex** (`mariadb.com`), SPF-style — **not** under a selector like
  `_mcp-auth.mariadb.com`. Selector placement fails with a *generic signature error* that gives
  no hint about placement, so you will debug the wrong thing.
- **Decide key custody before asking IT for the DNS record.** A file-based key's record value
  must be generated *before* IT can act, but a KMS key's public half **cannot be known until IT
  creates the key**. Get this backwards and IT publishes a record for a key you then discard —
  which means a second ticket, and a window where a stale record breaks verification.
- **Never email a private key to `helpdesk@`.** That mail becomes a Jira ticket body, so the
  secret ends up in plaintext readable by anyone with project access. Worse than a laptop.
- **macOS `openssl` is LibreSSL** and fails Ed25519 key generation outright with
  `Algorithm Ed25519 not found`. You need Homebrew's `openssl@3`
  (`/opt/homebrew/opt/openssl@3/bin/openssl`). Only relevant if you ever generate a file-based
  key, which for `com.mariadb` you should not.

## Perspective

Registering is a **discoverability bet, not a fix**. In July 2026 the docs site served
5,419,052 plain Markdown fetches against 8,209 MCP requests — agents currently prefer fetching
`.md` by roughly **660:1**. Listing the server lets MCP-aware clients and registry aggregators
find it without a human pasting a URL; it will not move that ratio. Optimizing the `.md`
channel matters more.

## See also

- Registry publishing and authentication docs: <https://github.com/modelcontextprotocol/registry>
- DOCS-6400 — the ticket, with usage figures and the registry-gap analysis
- `dev-docs/cookbook-gitbook-redirects.md` — the other standing IT/infrastructure hand-off
