# Cookbook: the Community Tools sync

The docs for **MariaDB AI Plugins** and **MariaDB Shell** are written in their product repos, not
here. A workflow copies them into the Tools space, one way (DOCS-6926):

| Product | Source repo | Source folder | Published from |
|---------|-------------|---------------|----------------|
| MariaDB AI Plugins | [`mariadb-corporation/ai-plugins`](https://github.com/mariadb-corporation/ai-plugins) | `docs-ref/content/community/mariadb-ai-plugins/` | `tools/community/mariadb-ai-plugins/` |
| MariaDB Shell | [`mariadb-corporation/mariadb-shell`](https://github.com/mariadb-corporation/mariadb-shell) | `docs-ref/content/community/mariadb-shell/` | `tools/community/mariadb-shell/` |

Each repo's `docs-ref/content/` is laid out like our `tools/` space, so the paths match one to one.
The rest of `docs-ref/` is a Docusaurus preview of the pages and isn't copied. The repos' `docs/`
folders are a different site (ai-plugins.mariadb.org) and aren't copied either.

## The rule: edit upstream only

**Never edit a synced page here, in a PR or in the GitBook editor.** The next sync overwrites it.
Make the change in the product repo instead:

1. Open a PR in the product repo that changes the page under `docs-ref/content/`. The docs team
   has write access through the `documentation-team` GitHub team. `main` is protected there, and
   Mike Zinner reviews. Title a docs-only PR `[bypass-ci] docs-ref: …`.
2. Before opening it, run our gates on the changed pages, because the product repo's preview
   doesn't model everything GitBook does (desccheck, fragcheck and codespell, as in the pre-PR
   cookbook).
3. Once it's merged, the next sync brings the change here.

Two checks enforce this:

- **`community-tools-guard.yml`** fails any PR here that changes a synced page, except the sync's
  own PR. It comments with a link to each page's source file.
- **The GitBook-edit digest** ([cookbook](cookbook-gitbook-edit-review.md)) lists every GitBook-UI
  commit, so a UI edit to a synced page shows up there. Redo it upstream, and let the next sync
  revert it here.

## What the sync does

`.github/workflows/sync-community-tools-docs.yml` runs on weekdays at 05:47 UTC, and on demand
from the Actions tab (input `products`: a space-separated list of product keys, or `all`). It
calls `.github/scripts/sync_community_tools.py`, which, for each product:

- replaces `tools/community/<product>/` with the source folder, **byte for byte**;
- replaces the product's subtree in `tools/SUMMARY.md`, under Community Tools;
- replaces the product's `## <title>` section in `tools/community/README.md` and its
  `### <title>` section in `tools/README.md` with the sections from the source repo's stand-in
  landing pages (`content/community/README.md` and `content/README.md`). The rest of those
  stand-ins is never copied. A new product's sections go last, before the licence footer;
- copies the images its pages use into `tools/.gitbook/assets/`, and removes images it no
  longer uses.

If anything changed, the workflow opens or updates a PR from `automated/sync-community-tools-docs`,
and runs the content gates on it (`doc-gates.yml`; the verdict appears as the `doc-gates`
status). Review the diff and merge it like any other PR. A gate failure is fixed upstream, never
on the PR branch.

The sync stops without a PR if the source needs fixing first:

- **A link alias** (`{server}/…`) in a synced page. Our alias bot would rewrite it, and the
  page would no longer match its source. Synced pages link to other spaces with absolute
  `https://mariadb.com/docs/…` URLs, the one exception to the [alias rule](link-aliases.md).
  Within the Tools space, a page links to another product's pages by absolute URL too: the
  product repo doesn't have them, so a relative link would break its preview build.
- **A missing image**, or an image whose name collides with a different file already in
  `tools/.gitbook/assets/`.

## The config: `.github/community-tools.json`

```json
"products": {
  "mariadb-shell": {
    "title": "MariaDB Shell",
    "repo": "mariadb-corporation/mariadb-shell",
    "ref": "main",
    "exclude": ["mcp-server/rest-daemon-tools.md"]
  }
}
```

- **The key** is the product's folder name, in the source and here.
- **`title`** must match the nav entry and the landing-page section headings.
- **`ref`** is the branch or tag to copy from.
- **`exclude`** holds back pages that aren't ready to publish, for example docs for an
  unreleased feature. Each entry is a path relative to the product folder; a glob (`*`) or a
  folder name excludes several pages. The sync drops their files and their nav entries. A
  link to an excluded page from a synced page is dead, and the gates report it: remove the
  link upstream, or exclude the linking page as well.

`synced` is written by the script: for each product, the source commit it copied last and the
images it copied. Don't edit it by hand.

**Adding a product** (for example the MariaDB REST Service, from `mariadb-shell`'s
`docs-ref/content/community/mariadb-rest-service/`): add an entry to `products`, then add its
folder to the exclusions in `expand-gitbook-aliases.yml` and to this page's table. The guard reads
the config, so it needs no change.

## Running it locally

From the repo root, with a checkout of each product repo in a folder named after its key:

```bash
git clone --depth 1 https://github.com/mariadb-corporation/ai-plugins /tmp/src/mariadb-ai-plugins
git clone --depth 1 https://github.com/mariadb-corporation/mariadb-shell /tmp/src/mariadb-shell
python3 .github/scripts/sync_community_tools.py --src /tmp/src
```

`--product <key>` syncs only that product. Then run the gates on `tools/` as usual. Use this to
preview a sync; let the workflow open the actual PR.
