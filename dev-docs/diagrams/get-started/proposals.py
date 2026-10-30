"""Landing diagrams: get-started-orientation (site landing page) and ai-tools-agent-setup (AI Tools landing page).

Usage: python3 -I proposals.py
Reuses the palette, styles, output folders, and svg() writer from build.py.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
src = (HERE / "build.py").read_text()
exec(src.split("# 1. AI")[0])  # palettes, STYLE, DEFS, svg(), output folders

# A. One server, three ways to run it --------------------------------------------------------
svg("get-started-orientation", 760, 296,
    "Orientation. Your application connects through a MariaDB connector, and your coding agent connects through "
    "the MariaDB MCP server. Both reach MariaDB Server, available as MariaDB Community Server and MariaDB Enterprise "
    "Server. You run it yourself, run it with the MariaDB Enterprise Platform components around it, or let MariaDB Cloud run it.",
    """
<rect class="box" x="20" y="70" width="170" height="64" rx="6"/>
<text class="t" x="105" y="98" text-anchor="middle">Your application</text>
<text class="xs mut" x="105" y="117" text-anchor="middle">Python, Node.js, Java, PHP, .NET</text>
<rect class="box" x="20" y="176" width="170" height="64" rx="6"/>
<text class="t" x="105" y="204" text-anchor="middle">Your coding agent</text>
<text class="xs mut" x="105" y="223" text-anchor="middle">Claude Code, Codex, and more</text>
<line class="ln" x1="190" y1="102" x2="268" y2="140" marker-end="url(#a)"/>
<text class="xs mut halo" x="226" y="108" text-anchor="middle">connector</text>
<line class="ln" x1="190" y1="208" x2="268" y2="172" marker-end="url(#a)"/>
<text class="xs mut halo" x="226" y="214" text-anchor="middle">MCP server</text>

<rect class="accbox" x="270" y="104" width="190" height="104" rx="8"/>
<text class="t acct" x="365" y="134" text-anchor="middle">MariaDB Server</text>
<text class="xs" x="365" y="156" text-anchor="middle">SQL, JSON, vectors,</text>
<text class="xs" x="365" y="172" text-anchor="middle">storage engines, replication</text>
<text class="xs mut" x="365" y="194" text-anchor="middle">Community or Enterprise</text>

<text class="sm mut" x="620" y="30" text-anchor="middle">Run it the way that fits</text>
<rect class="box" x="510" y="44" width="230" height="62" rx="6"/>
<text class="t" x="530" y="70">Yourself</text>
<text class="xs mut" x="530" y="90">Docker, Linux, Windows, macOS</text>
<rect class="box" x="510" y="124" width="230" height="78" rx="6"/>
<text class="t" x="530" y="150">MariaDB Enterprise Platform</text>
<text class="xs mut" x="530" y="170">MaxScale, Galera Cluster, ColumnStore,</text>
<text class="xs mut" x="530" y="186">Exa, GridGain, Kubernetes operator</text>
<rect class="box" x="510" y="220" width="230" height="62" rx="6"/>
<text class="t" x="530" y="246">MariaDB Cloud</text>
<text class="xs mut" x="530" y="266">Serverless or Provisioned, managed</text>
<path class="ln dash" d="M460,140 H485 V75 H508" marker-end="url(#a)"/>
<path class="ln dash" d="M460,156 H508" marker-end="url(#a)"/>
<path class="ln dash" d="M460,172 H485 V251 H508" marker-end="url(#a)"/>
""")

# B. What the agent prompt sets up ------------------------------------------------------------
svg("ai-tools-agent-setup", 760, 300,
    "What the agent prompt sets up. You install the MariaDB AI plugins into Claude Code. The plugins add MariaDB skills "
    "and the mariadb-shell MCP server. The agent uses the sandbox tools to start a local MariaDB Server on port 3310 "
    "with no Docker, creates the shop database and products table with the db tools, and writes a Python script that "
    "queries it. The docs MCP server lets the agent read current MariaDB documentation.",
    """
<rect class="box" x="20" y="110" width="160" height="72" rx="6"/>
<text class="t" x="100" y="140" text-anchor="middle">You</text>
<text class="xs mut" x="100" y="160" text-anchor="middle">paste one prompt</text>
<line class="ln" x1="180" y1="146" x2="218" y2="146" marker-end="url(#a)"/>

<rect class="frame" x="220" y="20" width="250" height="262" rx="8"/>
<text class="t" x="345" y="42" text-anchor="middle">Claude Code</text>
<text class="xs mut" x="345" y="58" text-anchor="middle">with the MariaDB AI plugins</text>
<rect class="plain" x="236" y="72" width="218" height="40" rx="4"/>
<text class="sm" x="345" y="91" text-anchor="middle">MariaDB skills</text>
<text class="xs mut" x="345" y="105" text-anchor="middle">SQL and connector know-how</text>
<rect class="box" x="236" y="122" width="218" height="96" rx="6"/>
<text class="t" x="345" y="142" text-anchor="middle">mariadb-shell MCP server</text>
<text class="mono xs" x="252" y="166">sandbox.deploy</text>
<text class="xs mut" x="438" y="166" text-anchor="end">start a server</text>
<text class="mono xs" x="252" y="186">db.execute_sql</text>
<text class="xs mut" x="438" y="186" text-anchor="end">create the table</text>
<text class="mono xs" x="252" y="206">db.connect</text>
<text class="xs mut" x="438" y="206" text-anchor="end">open a session</text>
<rect class="plain" x="236" y="228" width="218" height="40" rx="4"/>
<text class="sm" x="345" y="247" text-anchor="middle">Docs MCP server</text>
<text class="xs mut" x="345" y="261" text-anchor="middle">current MariaDB syntax</text>

<rect class="accbox" x="530" y="40" width="210" height="110" rx="8"/>
<text class="t acct" x="635" y="66" text-anchor="middle">Sandbox MariaDB Server</text>
<text class="xs" x="635" y="86" text-anchor="middle">native binary, no Docker</text>
<text class="mono xs" x="635" y="106" text-anchor="middle">localhost:3310</text>
<text class="mono xs acct" x="635" y="130" text-anchor="middle">shop.products</text>
<rect class="box" x="530" y="186" width="210" height="80" rx="6"/>
<text class="t" x="635" y="212" text-anchor="middle">Your project</text>
<text class="sm" x="635" y="234" text-anchor="middle">a Python script</text>
<text class="xs mut" x="635" y="252" text-anchor="middle">MariaDB Connector/Python</text>

<line class="ln acc" x1="454" y1="166" x2="528" y2="100" marker-end="url(#ac)"/>
<text class="xs acct halo" x="492" y="122" text-anchor="middle">SQL</text>
<line class="ln" x1="470" y1="226" x2="528" y2="226" marker-end="url(#a)"/>
<text class="xs halo" x="499" y="218" text-anchor="middle">writes</text>
<path class="ln dash" d="M635,186 V152" marker-end="url(#a)"/>
<text class="xs mut" x="644" y="174">queries</text>
""", out=AI_TOOLS)
