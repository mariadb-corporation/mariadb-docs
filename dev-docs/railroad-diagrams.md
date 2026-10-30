# Railroad diagrams

The `*-railroad.svg` files in `server/.gitbook/assets/` are syntax diagrams for SQL statement
pages. Each one mirrors the page's BNF block, so when the BNF changes, regenerate the diagram.

## Generating a diagram

The diagrams come from the [RR Railroad Diagram Generator](https://bottlecaps.de/rr/ui) by
Gunther Rademacher, version 2.6, default theme. The generator isn't committed to this repo.

1. Download the generator. It runs on any JDK from 11 on:

   ```bash
   curl -fsSL -o rr.zip https://bottlecaps.de/rr/download/rr-2.6-java11.zip
   unzip rr.zip -d rr
   ```

2. Write the grammar in W3C-style EBNF. Quoted literals (`'DELETE'`) render as keywords, and
   bare names (`tbl_name`) render as placeholders. Keep the placeholder names the page's BNF
   uses.

   ```
   UnlockTables ::= 'UNLOCK' 'TABLES'
   ```

3. Generate standalone SVGs. The output is a zip with one `diagram/<Production>.svg` for each
   production. Rename each one to `<slug>-railroad.svg`:

   ```bash
   java -jar rr/rr.war -noembedded -suppressebnf -out:out.zip grammar.ebnf
   ```

4. **Add the dark-mode background card.** This step is required:

   ```bash
   python3 .claude/hooks/railroadcheck.py --fix server/.gitbook/assets/<slug>-railroad.svg
   ```

5. Reference the diagram below the BNF block:

   ```markdown
   ![Railroad diagram of UNLOCK TABLES — equivalent to the BNF above](../../../.gitbook/assets/unlock-tables-railroad.svg)
   ```

   Captions of sub-rule diagrams drop the "— equivalent to the BNF above" part:
   `![Railroad diagram of index_option](…)`.

To check the setup, regenerate `unlock-tables-railroad.svg` from the one-line grammar above and
run `--fix`. The result is byte-for-byte identical to the committed file.

## Why the background card

The generator draws connector lines in near-black on a transparent background. On GitBook's
dark theme the lines are about 1.1–1.4:1 against the page, below the 3:1 minimum WCAG sets for
non-text contrast, so the boxes seem to float with nothing joining them. The diagrams are
`<img>` references, so page CSS can't reach inside them. Instead, each SVG carries a white card
with rounded corners and 8px of padding. The card is invisible in light mode.

The generator has no option for a background, so a regenerated diagram lacks the card until
you run `--fix`. The CI gate `railroadcheck-pr.yml` fails a pull request with a diagram that
lacks it (DOCS-6637).

If you add the card by hand, set the fill with an inline `style`, not a `fill=` attribute. The
generator's stylesheet sets `rect {fill: #332900}`, and a CSS rule overrides an attribute, so
`fill="#fff"` renders dark brown.
