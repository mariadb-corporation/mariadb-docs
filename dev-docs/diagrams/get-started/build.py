"""Build the Get Started page diagrams as light and dark SVG pairs.

Usage: python3 -I build.py
Each diagram is written once with CSS classes; the script bakes the light and dark palettes
into two files, <name>-light.svg and <name>-dark.svg, for a GitBook <picture> block.
Palettes follow the 2026-11-03 site theme (rehearsal site site_bFEbB): primary #8328ED (light)
and #BEA4FD (dark), with neutral grays to match its neutral tint.
"""
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
GET_STARTED = REPO / "get-started/.gitbook/assets"
AI_TOOLS = REPO / "ai-tools/.gitbook/assets"

PALETTES = {
    "light": dict(fg="#18181b", muted="#5f5f69", panel="#f4f4f5", line="#c4c4cc", accent="#8328ED",
                  accentsoft="#f1e8fe", accenttext="#8328ED", halo="#ffffff", on="#ffffff"),
    "dark": dict(fg="#ececef", muted="#a1a1aa", panel="#1e1e22", line="#45454d", accent="#BEA4FD",
                 accentsoft="#2b2242", accenttext="#BEA4FD", halo="#111113", on="#18181b"),
}

STYLE = """<style>
  text {{ fill: {fg}; font: 13px Lato, "Helvetica Neue", Arial, sans-serif; }}
  .mono {{ font-family: "JetBrains Mono", Menlo, Consolas, monospace; font-size: 12px; font-variant-ligatures: none; }}
  .t {{ font-weight: 700; font-size: 14px; }} .sm {{ font-size: 12px; }} .xs {{ font-size: 11px; }}
  .mut {{ fill: {muted}; }} .acct {{ fill: {accenttext}; }}
  .box {{ fill: {panel}; stroke: {line}; }} .plain {{ fill: none; stroke: {line}; }}
  .accbox {{ fill: {accentsoft}; stroke: {accent}; }} .frame {{ fill: none; stroke: {muted}; stroke-dasharray: 5 4; }}
  .ln {{ fill: none; stroke: {fg}; stroke-width: 1.4; }} .dash {{ stroke-dasharray: 5 4; }}
  .acc {{ stroke: {accent}; stroke-width: 2; }} .mut-ln {{ stroke: {muted}; }}
  .fillacc {{ fill: {accent}; }} .fillsoft {{ fill: {accentsoft}; }} .fillpanel {{ fill: {panel}; }}
  .halo {{ paint-order: stroke; stroke: {halo}; stroke-width: 4px; stroke-linejoin: round; }}
  .on {{ fill: {on}; }} .cmd {{ font-size: 10.5px; font-variant-ligatures: none; }}
  .mk {{ fill: {fg}; }} .mkacc {{ fill: {accent}; }}
</style>"""

DEFS = """<defs>
  <marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="mk" d="M0,0 L10,5 L0,10 z"/></marker>
  <marker id="ac" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="mkacc" d="M0,0 L10,5 L0,10 z"/></marker>
</defs>"""


def svg(name, w, h, label, body, out=GET_STARTED):
    for mode, pal in PALETTES.items():
        doc = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
               f'role="img" aria-label="{label}">\n{DEFS}\n{STYLE.format(**pal)}\n{body}\n</svg>\n')
        (out / f"{name}-{mode}.svg").write_text(doc)
        print("built", (out / f"{name}-{mode}.svg").relative_to(REPO))


# 1. AI: semantic search in one query ---------------------------------------------------------
svg("ai-semantic-search", 760, 300,
    "Semantic search: your application calls an embedding model, from a provider or running locally, to turn "
    "the search phrase into a vector, then sends one SQL query to MariaDB Server. The query walks the vector index on the product_embeddings "
    "table, joins the products table for names, and returns the two nearest products with their distances.",
    """
<rect class="box" x="20" y="36" width="230" height="58" rx="6"/>
<text class="t" x="135" y="60" text-anchor="middle">Search phrase</text>
<text class="mono sm mut" x="135" y="80" text-anchor="middle">"something to light my desk"</text>
<line class="ln" x1="135" y1="94" x2="135" y2="124" marker-end="url(#a)"/>
<rect class="box" x="20" y="126" width="230" height="58" rx="6"/>
<text class="t" x="135" y="150" text-anchor="middle">Embedding model</text>
<text class="sm mut" x="135" y="170" text-anchor="middle">from a provider or running locally</text>
<rect class="accbox" x="20" y="222" width="230" height="62" rx="6"/>
<text class="t acct" x="135" y="244" text-anchor="middle">Nearest products</text>
<text class="mono sm" x="40" y="264">Desk lamp</text><text class="mono sm" x="230" y="264" text-anchor="end">0.007</text>
<text class="mono sm" x="40" y="278">Standing desk</text><text class="mono sm" x="230" y="278" text-anchor="end">0.501</text>

<rect class="frame" x="300" y="16" width="440" height="276" rx="8"/>
<text class="t" x="520" y="38" text-anchor="middle">MariaDB Server</text>
<rect class="plain" x="320" y="60" width="180" height="112" rx="6"/>
<text class="sm mut" x="334" y="80">one SQL query</text>
<text class="mono sm" x="334" y="102">ORDER BY</text>
<text class="mono sm acct" x="334" y="120">VEC_DISTANCE_COSINE(</text>
<text class="mono sm acct" x="350" y="138">embedding, ?)</text>
<text class="mono sm" x="334" y="158">LIMIT 2</text>
<rect class="accbox" x="550" y="60" width="170" height="54" rx="6"/>
<text class="mono t acct" x="635" y="84" text-anchor="middle">VECTOR INDEX</text>
<text class="xs" x="635" y="102" text-anchor="middle">neighbor graph, cosine</text>
<rect class="box" x="550" y="142" width="170" height="54" rx="6"/>
<text class="mono t" x="635" y="164" text-anchor="middle">product_embeddings</text>
<text class="mono xs acct" x="635" y="184" text-anchor="middle">embedding VECTOR(4)</text>
<rect class="box" x="550" y="226" width="170" height="50" rx="6"/>
<text class="mono t" x="635" y="248" text-anchor="middle">products</text>
<text class="mono xs mut" x="635" y="266" text-anchor="middle">id, name, price</text>
<line class="ln acc" x1="500" y1="88" x2="548" y2="88" marker-end="url(#ac)"/>
<text class="xs acct" x="524" y="80" text-anchor="middle">walks</text>
<line class="ln" x1="635" y1="114" x2="635" y2="140" marker-end="url(#a)"/>
<text class="xs mut" x="644" y="132">indexes</text>
<line class="ln" x1="635" y1="196" x2="635" y2="224" marker-end="url(#a)"/>
<text class="xs mut" x="644" y="214">JOIN on id</text>

<path class="ln" d="M250,155 H285 V116 H318" marker-end="url(#a)"/>
<text class="xs halo" x="285" y="108" text-anchor="middle">vector</text>
<path class="ln dash" d="M320,150 H290 V253 H252" marker-end="url(#a)"/>
<text class="xs halo" x="270" y="246" text-anchor="middle">rows</text>
""")

# 2. Analytics: one database, two storage engines ----------------------------------------------
# The sales table names no engine on purpose: ColumnStore is one columnar engine, and the diagram
# shows the idea (rows versus columns, one join), not a product choice. What the report reads is
# marked with an accent outline as well as a fill, so it does not rest on a faint fill alone.
ROW_Y, ROW_H = 130, 24
cells = []
# InnoDB: 5 rows x 5 cols, one row read (a checkout reads one product)
for r in range(5):
    for c in range(5):
        cls = "fillsoft" if r == 2 else "fillpanel"
        cells.append(f'<rect class="{cls}" x="{36 + c * 58}" y="{ROW_Y + r * ROW_H}" width="54" height="20" rx="2"/>')
cells.append(f'<rect class="plain acc" x="32" y="{ROW_Y + 2 * ROW_H - 4}" width="294" height="28" rx="4"/>')
# Columnar: 5 rows x 5 cols, columns 1, 3, 4 read (product_id, quantity, price)
for r in range(5):
    for c in range(5):
        cls = "fillsoft" if c in (1, 3, 4) else "fillpanel"
        cells.append(f'<rect class="{cls}" x="{384 + c * 70}" y="{ROW_Y + r * ROW_H}" width="66" height="20" rx="2"/>')
for x, w in ((450, 74), (590, 144)):  # product_id; quantity and price together
    cells.append(f'<rect class="plain acc" x="{x}" y="108" width="{w}" height="142" rx="4"/>')
heads_l = ["id", "name", "price", "stock", "..."]
heads_r = ["sale_id", "product_id", "sale_date", "quantity", "price"]
hl = "".join(f'<text class="mono xs mut" x="{63 + i * 58}" y="122" text-anchor="middle">{h}</text>' for i, h in enumerate(heads_l))
hr = "".join(f'<text class="mono xs {"acct" if i in (1, 3, 4) else "mut"}" x="{417 + i * 70}" y="122" text-anchor="middle"'
             f'{" font-weight=\"700\"" if i in (1, 3, 4) else ""}>{h}</text>' for i, h in enumerate(heads_r))
svg("analytics-two-engines", 760, 354,
    "One database, two storage engines. The products table uses InnoDB, which stores whole rows together, "
    "so a checkout reads one complete row. The sales table uses a columnar engine, which stores each column apart, "
    "so a revenue report reads only the product_id, quantity, and price columns. One SELECT joins both tables.",
    f"""
<rect class="frame" x="16" y="12" width="728" height="330" rx="8"/>
<text class="t" x="380" y="36" text-anchor="middle">One database: shop</text>
<text class="t" x="179" y="62" text-anchor="middle">products  ·  InnoDB</text>
<text class="sm" x="179" y="82" text-anchor="middle">Rows stored together.</text>
<text class="xs mut" x="179" y="98" text-anchor="middle">A checkout reads one whole row.</text>
<text class="t" x="557" y="62" text-anchor="middle">sales  ·  a columnar engine</text>
<text class="sm" x="557" y="82" text-anchor="middle">Columns stored apart.</text>
<text class="xs mut" x="557" y="98" text-anchor="middle">A report reads three columns of every row.</text>
{hl}{hr}
{''.join(cells)}
<path class="ln acc" d="M179,290 V258" marker-end="url(#ac)"/>
<path class="ln acc" d="M557,290 V258" marker-end="url(#ac)"/>
<rect class="accbox" x="150" y="290" width="460" height="38" rx="6"/>
<text class="mono sm" x="380" y="314" text-anchor="middle">SELECT p.name, SUM(s.quantity * s.price) ... JOIN</text>
""")

# 3. Operations: back up, prepare, restore, verify ----------------------------------------------
stages = [("1  Back up", "mariadb-backup --backup", "copies data files while", "the server keeps running"),
          ("2  Prepare", "mariadb-backup --prepare", "makes the copied files", "consistent"),
          ("3  Restore", "mariadb-backup --copy-back", "into an empty data directory,", "then chown mysql:mysql"),
          ("4  Verify", "SELECT COUNT(*) ...", "start the server and compare", "row counts")]
ob = []
for i, (title, cmd, l1, l2) in enumerate(stages):
    x = 20 + i * 182
    cls = "accbox" if i == 3 else "box"
    ob.append(f'<rect class="{cls}" x="{x}" y="30" width="172" height="112" rx="6"/>')
    ob.append(f'<text class="t{" acct" if i == 3 else ""}" x="{x + 10}" y="54">{title}</text>')
    ob.append(f'<text class="mono cmd" x="{x + 10}" y="78">{cmd}</text>')
    ob.append(f'<text class="xs mut" x="{x + 10}" y="102">{l1}</text>')
    ob.append(f'<text class="xs mut" x="{x + 10}" y="118">{l2}</text>')
    if i < 3:
        ob.append(f'<line class="ln" x1="{x + 172}" y1="86" x2="{x + 181}" y2="86" marker-end="url(#a)"/>')
# server state band
ob.append('<text class="sm mut" x="20" y="178">Server</text>')
ob.append('<rect class="fillacc" x="80" y="166" width="300" height="16" rx="3"/>')
ob.append('<rect class="plain" x="384" y="166" width="196" height="16" rx="3"/>')
ob.append('<rect class="fillacc" x="584" y="166" width="154" height="16" rx="3"/>')
ob.append('<text class="xs" x="230" y="200" text-anchor="middle">running</text>')
ob.append('<text class="xs" x="482" y="200" text-anchor="middle">stopped for the restore</text>')
ob.append('<text class="xs" x="662" y="200" text-anchor="middle">running</text>')
svg("operations-backup-restore", 760, 220,
    "Back up and restore with mariadb-backup in four stages. First, back up while the server keeps running. "
    "Second, prepare the copied files so they are consistent. Third, stop the server and copy the backup into an "
    "empty data directory. Fourth, start the server and verify row counts. The server is stopped only during the restore.",
    "\n".join(ob))

# 4. Platform: the request path through MaxScale ------------------------------------------------
svg("platform-request-path", 770, 330,
    "Request path in MariaDB Enterprise Platform. Your application connects through a MariaDB connector to MaxScale "
    "on port 4006. MaxScale's read/write split service sends writes to the primary server and reads to the replicas, "
    "and its monitor tracks which server is primary. The primary replicates to two replicas. MariaDB Enterprise Manager "
    "watches every component from outside the query path.",
    """
<rect class="box" x="20" y="110" width="170" height="70" rx="6"/>
<text class="t" x="105" y="138" text-anchor="middle">Your application</text>
<text class="sm mut" x="105" y="158" text-anchor="middle">MariaDB connector</text>
<line class="ln" x1="190" y1="145" x2="248" y2="145" marker-end="url(#a)"/>
<text class="xs mut halo" x="219" y="137" text-anchor="middle">port 4006</text>

<rect class="accbox" x="250" y="70" width="200" height="150" rx="6"/>
<text class="t acct" x="350" y="96" text-anchor="middle">MaxScale</text>
<rect class="plain" x="266" y="110" width="168" height="40" rx="4"/>
<text class="mono xs" x="350" y="127" text-anchor="middle">readwritesplit</text>
<text class="xs mut" x="350" y="142" text-anchor="middle">routes each statement</text>
<rect class="plain" x="266" y="160" width="168" height="40" rx="4"/>
<text class="mono xs" x="350" y="177" text-anchor="middle">mariadbmon</text>
<text class="xs mut" x="350" y="192" text-anchor="middle">tracks the primary</text>

<rect class="box" x="560" y="40" width="180" height="56" rx="6"/>
<text class="t" x="650" y="64" text-anchor="middle">Primary</text>
<text class="xs mut" x="650" y="82" text-anchor="middle">MariaDB Enterprise Server</text>
<rect class="box" x="560" y="140" width="180" height="56" rx="6"/>
<text class="t" x="650" y="164" text-anchor="middle">Replica</text>
<text class="xs mut" x="650" y="182" text-anchor="middle">MariaDB Enterprise Server</text>
<rect class="box" x="560" y="216" width="180" height="56" rx="6"/>
<text class="t" x="650" y="240" text-anchor="middle">Replica</text>
<text class="xs mut" x="650" y="258" text-anchor="middle">MariaDB Enterprise Server</text>

<path class="ln acc" d="M450,100 H505 V68 H558" marker-end="url(#ac)"/>
<text class="xs acct halo" x="505" y="60" text-anchor="middle">writes</text>
<path class="ln" d="M450,170 H558" marker-end="url(#a)"/>
<path class="ln" d="M505,170 V244 H558" marker-end="url(#a)"/>
<text class="xs halo" x="505" y="162" text-anchor="middle">reads</text>
<path class="ln dash" d="M740,68 H752 V244 H742" marker-end="url(#a)"/>
<path class="ln dash" d="M752,168 H742" marker-end="url(#a)"/>
<text class="xs mut" x="650" y="122" text-anchor="middle">replicates to both replicas</text>

<rect class="frame" x="250" y="276" width="490" height="40" rx="6"/>
<text class="t" x="270" y="301">MariaDB Enterprise Manager</text>
<text class="xs mut" x="720" y="301" text-anchor="end">monitors every component, outside the query path</text>
<line class="ln dash mut-ln" x1="350" y1="276" x2="350" y2="222"/>
""")
