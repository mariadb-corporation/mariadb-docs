# Maintaining the agent skills (DX project)

How the `agent-skills/` directory is authored and kept current. This is the
human-facing companion to `agent-skills/README.md` (which covers layout and
consumption) and the per-tier `README.md` / `VENDORED.md` files. Tracked under
DOCS-6206.

The artifact is a **delta from what an LLM writes by default** — MariaDB
knowledge minus the typical LLM prior. That delta exists nowhere in the source
docs, so the high-value parts are editorial, not extractable.

> **Editorial rule (do not skip):** never name MySQL in a skill. The LLM's
> default is MySQL-shaped because its training data is MySQL-heavy, so the
> "What LLMs Often Miss" tables correct a MySQL-shaped prior — but state the
> MariaDB form directly, don't frame it as a comparison.
> - Don't: *"PERSISTENT is historical; STORED (MySQL-compat) also works."*
> - Do: *"MariaDB's keyword is PERSISTENT. STORED is also accepted as an alias."*

## The three layers, and who maintains them

| Layer | Path | Maintenance |
| --- | --- | --- |
| Tier 1 (statements) | `granular/statements/` | Hand-authored + human-verified, here |
| Tier 2 (functions) | `granular/functions/` | Extractor-generated body + hand-written scaffold, here |
| Topical | `topical/` | Vendored from `MariaDB/skills`; file bugs upstream, do not edit here |

## Where "what LLMs miss" knowledge comes from

Five sources, in roughly increasing order of reliability. The first four are
desk research; the fifth is the most reliable and removes the "must be a MariaDB
expert" gate from the author.

1. **Robert's `mysql-to-mariadb` topical skill, reverse-engineered.** Anything
   flagged "different in MariaDB" is by construction a candidate trap.
2. **`mariadb-features` "Defaults Changed" / "Behavior Changed" sections.**
   Anything listed is a trap by definition — training data predates it
   (e.g. `innodb_snapshot_isolation` default flip, `latin1`→`utf8mb4`, query
   cache off/removed).
3. **Docs `{% hint %}` blocks and inline warnings.** An inline warning is the
   docs team saying "people get this wrong" (e.g. `IF NOT EXISTS` warns rather
   than errors; FKs silently ignored on MyISAM).
4. **Version-conditional content** — GitBook `{% tabs %}` contrasting Current
   vs `< X.Y` is the team admitting behavior changed at X.Y. A trap if the LLM's
   training reflects the old behavior.
5. **Empirical testing (most reliable).** Open a fresh agent session with no
   MariaDB skill loaded, ask it to write the statement for a representative
   task, and diff its output against MariaDB-correct output. Repeat for 3–4
   prompts per statement; the same misconceptions recur. You observe traps
   rather than having to predict them.

## Tier 1 authoring workflow (per statement family)

1. **Author — Claude.** Draft the skill and a candidate "What LLMs Often Miss"
   table (8–10 rows) from sources 1–4 above. ~5–10 min.
2. **Verify — human.** Walk each row; spot-check against `mariadb-server/sql/`
   source or the canonical `server/reference/**` page. **Non-negotiable**, and
   does not require MariaDB expertise — willingness to grep is enough. ~30–45 min.
3. **Empirical confirmation — either.** Source 5: drop traps that aren't
   actually traps in current LLM output; add ones the human missed.

Realistic cost: **35–55 min per skill.**

**Why verification is non-negotiable:** at scale (100 skills × ~10 rows × a
1–2% error rate on "X works differently in MariaDB" claims) that's 10–20
factually wrong rows shipping — and they look authoritative because they sit in
a "What LLMs Often Miss" table. The query-cache slip caught during the SELECT
pilot is the cautionary tale.

### Skill conventions

- One directory per skill, containing `SKILL.md` (Claude Code skill convention).
- Frontmatter `name:` + a triage `description:` (when the skill should fire).
- Header line `*Last updated: YYYY-MM-DD*` and the **11.8 LTS** baseline note.
- Features in every current LTS branch (10.6, 10.11, 11.4, 11.8) carry no
  "since" annotation; only newer-than-10.6 features get `*(since X.Y)*`.
- Cross-link to a topical skill for feature depth rather than duplicating it
  (e.g. `mariadb-alter-table` defers column attributes to `mariadb-create-table`).
- Target ~8–12 KB. Absolute size matters, not compression ratio — it has to fit
  cheaply in agent context.

## Tier 2 maintenance (function categories)

The per-function entries are generated; the scaffold around them is not.

- Scaffold (frontmatter, intro, category-level "What LLMs Often Miss" table) is
  hand-written from `agent-skills/extractor/templates/function-category.scaffold.md`.
- The body between the `BEGIN/END GENERATED` markers is produced by
  `agent-skills/extractor/extract_function_category.py` against the canonical
  `server/reference/sql-functions/**/<category>/` pages.
- CI (`extract-function-skills.yml`, stub) re-runs the extractor when those
  pages change and opens a regeneration PR, preserving the scaffold sections.

## Per-LTS update workflow

Roughly annually, per LTS release:

1. **Structured review per Tier 1 skill** against its `server/reference/**`
   page(s) and `mariadb-server/sql/` source. For every "since X.Y" / "removed in
   X.Y" claim, verify. For every trap-table row, confirm the trap is still real.
   Flag new doc content not yet reflected. ~15–30 min per skill — cheaper than
   authoring.
2. **Targeted review** for releases with notable removals/deprecations
   (e.g. query cache removed in 13.0): review only the affected skills.
3. **Tier 2:** re-run the extractor (CI handles this on doc change).
4. **Topical:** re-vendor from upstream at the new pinned ref; update
   `topical/VENDORED.md`.
5. **Empirical-fresh-session sweep every 12–18 months.** As LLMs improve, some
   traps stop being traps; prune them so the tables don't accumulate dead weight.

## Scope discipline ("good enough" over "perfect")

- Skip differences that don't matter for application development (e.g.
  optimizer-hint deltas rarely surface in app-dev contexts).
- Cover high-use cases — DDL, DML, common SQL functions. For everything else,
  let the agent fall through to `mariadb.com/docs`.
