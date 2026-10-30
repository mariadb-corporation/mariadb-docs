"""Landing diagrams: get-started-orientation (site landing page) and ai-tools-agent-setup (AI Tools landing page).

Usage: python3 -I landing-pages.py
Reuses the palette, styles, output folders, and svg() writer from build.py.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
src = (HERE / "build.py").read_text()
exec(src.split("# 1. AI")[0])  # palettes, STYLE, DEFS, svg(), output folders

# A. One server, wherever you run it ---------------------------------------------------------
# The four environments match the install tabs under the diagram. They are grouped by who runs
# the server, not ranked, and only MariaDB Server takes the accent color, because it is the part
# that stays the same.
svg("get-started-orientation", 790, 420,
    "Run MariaDB Server anywhere. Your code stays the same. Your application connects through a MariaDB connector, and your "
    "coding agent connects through the MariaDB MCP server. Both reach MariaDB Server, Community or Enterprise. "
    "MariaDB Server runs on any of four environments. You run it with Docker on your laptop, with Linux on your "
    "servers and VMs, or with the operator on your Kubernetes cluster, and MariaDB Enterprise Platform adds MaxScale, "
    "Galera Cluster, ColumnStore, Exa, and GridGain to any of these. Or MariaDB runs it for you in MariaDB Cloud. "
    "Moving between them changes only the connection settings: host, user, password, and TLS.",
    """
<text class="t" x="395" y="26" text-anchor="middle">Run MariaDB Server anywhere. Your code stays the same.</text>

<rect class="box" x="20" y="127" width="170" height="64" rx="6"/>
<text class="t" x="105" y="155" text-anchor="middle">Your application</text>
<text class="xs mut" x="105" y="174" text-anchor="middle">Python, Node.js, Java, PHP, .NET</text>
<rect class="box" x="20" y="231" width="170" height="64" rx="6"/>
<text class="t" x="105" y="259" text-anchor="middle">Your coding agent</text>
<text class="xs mut" x="105" y="278" text-anchor="middle">Claude Code, Codex, and more</text>
<line class="ln" x1="190" y1="159" x2="258" y2="193" marker-end="url(#a)"/>
<text class="xs mut halo" x="228" y="155" text-anchor="middle">connector</text>
<line class="ln" x1="190" y1="263" x2="258" y2="229" marker-end="url(#a)"/>
<text class="xs mut halo" x="228" y="279" text-anchor="middle">MCP server</text>

<rect class="accbox" x="260" y="159" width="190" height="104" rx="8"/>
<text class="t acct" x="355" y="189" text-anchor="middle">MariaDB Server</text>
<text class="xs" x="355" y="211" text-anchor="middle">SQL, JSON, vectors,</text>
<text class="xs" x="355" y="227" text-anchor="middle">storage engines, replication</text>
<text class="xs mut" x="355" y="249" text-anchor="middle">Community or Enterprise</text>

<path class="plain" d="M450,211 H486"/>
<path class="plain" d="M486,88 V334 M486,88 H510 M486,144 H510 M486,200 H510 M486,334 H510"/>
<text class="xs mut" transform="rotate(-90 478 140)" x="478" y="140" text-anchor="middle">runs on any of these</text>

<rect class="frame" x="500" y="40" width="270" height="242" rx="8"/>
<text class="xs mut" x="512" y="56">You run it</text>
<rect class="box" x="510" y="64" width="250" height="48" rx="6"/>
<text class="t" x="526" y="85">Docker</text>
<text class="xs mut" x="526" y="102">Your laptop, one command</text>
<rect class="box" x="510" y="120" width="250" height="48" rx="6"/>
<text class="t" x="526" y="141">Linux</text>
<text class="xs mut" x="526" y="158">Your servers and VMs</text>
<rect class="box" x="510" y="176" width="250" height="48" rx="6"/>
<text class="t" x="526" y="197">Kubernetes</text>
<text class="xs mut" x="526" y="214">Your cluster, with the operator</text>
<text class="t xs" x="512" y="242">MariaDB Enterprise Platform adds</text>
<text class="xs mut" x="512" y="257">MaxScale, Galera Cluster, ColumnStore,</text>
<text class="xs mut" x="512" y="272">Exa, and GridGain to any of these</text>

<text class="xs mut" x="512" y="302">MariaDB runs it</text>
<rect class="box" x="510" y="310" width="250" height="48" rx="6"/>
<text class="t" x="526" y="331">MariaDB Cloud</text>
<text class="xs mut" x="526" y="348">MariaDB runs it for you</text>

<text class="sm mut" x="395" y="390" text-anchor="middle">Moving between them changes only the connection settings: host, user, password, TLS.</text>
<text class="sm acct" x="395" y="410" text-anchor="middle">Pick your environment in the tabs below.</text>
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
