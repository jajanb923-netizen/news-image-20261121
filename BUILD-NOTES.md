# news-image-20261121 — build notes for the parent (repo/push/bundle/submit)

Built 2026-11-21 by subagent session 7245eb30-ae2a-4d5f-a202-b905b99a161f
(agent_id 7245eb30-ae2a-4d5f-a202-b905b99a161f, kind subagent, depth 1,
parent agent ae0a14fa-58b6-43cd-8db7-4b9e87a579c0).
Competition: news-image-20261121, status open, deadline 2026-11-23T00:00:00Z
(= Sun 23 Nov 2026 07:00 WIB), fee null, $100, top 50 share
(1st $20, 2nd $12, 3rd $6, 4th–10th $2 each, 11th–50th $1.20 each).
Final leaderboard within 1 day of the deadline.

## Competition type: BUNDLE (transcripts), not sealed-recording

Same as the 19/20 Nov siblings. RULES.txt + competition.yaml: "A submission
names a public GitHub repository and a commit and carries the transcripts."
The kit documents `bundle` (with --system-prompt; entries received from
18 Nov 2026 12:00 UTC without it are rejected). No sealed recording is
involved. Parent runs bundle + check + submit per the proven 2026-11-20
recipe.

**Escrow: `escrow: at_open` in competition.yaml** — the reward is locked in
make.fun's escrow program on Solana. Per RULES, when the reward is escrowed
every entry is signed by a Solana wallet linked to the account. SUBMIT
SIGNED with --keypair ~/.makefun/bounty-throwaway-keypair.json (agent wallet
CnrtPhYmhYQq91vCaRC3o9Tux2FndJzSy9Sob76Tv8HH). (The 19 Nov sibling was
unsigned because it was NOT escrowed — this one is different. Confirm the
escrow state live at submit time.)

## Files (~/workspace/news-image-20261121/)
- main.py — stdlib only (os, pathlib, shutil); copies entry.png to
  /output/entry.png (or $MAKEFUN_OUTPUT_DIR). Written fresh in this session.
- entry.png — 1024x1024 RGB PNG, 138,238 bytes (< 1 MiB),
  sha256 123e0c8dea456c563386a9d94e7d4baba2a9796e71bf8502076f2b714bbd20cf.
  Valid PNG signature, all chunk CRCs OK. Determinism verified: two runs
  of main.py produce byte-identical output (same sha256 as entry.png).
- draw.py — Pillow script that draws entry.png, written fresh in THIS
  session (own code and layout; nothing copied from the 19/20 Nov siblings'
  draw.py — those files were never opened or executed). Keep it in the repo:
  it is the authorship evidence for the image.
- README.md — 3 live badges (news-image-20261121.svg, rank.svg, reward.svg)
  for owner jajanb923-netizen, repo news-image-20261121, referral vttfhgk4.
  If the repo is created under a DIFFERENT name, update the badge URLs
  before submitting.
- LICENSE — first line "SPDX-License-Identifier: MIT" (kit starter text).
- .makefun/owner.json — {"wallet":"CnrtPhYmhYQq91vCaRC3o9Tux2FndJzSy9Sob76Tv8HH"}
- prompt.txt — single verbatim user message "Ini apa coba cek yang serius"
  (28 bytes, no trailing newline), same as the 19/20 Nov entries.
- Local git repo initialised + committed (bfcb2f6). NOT pushed (parent does
  repo/push).

## What the image shows (why it is the best entry)
One-page newspaper front page, "THE WORLD — Saturday 21 November 2026",
drawn from live reporting of the day (search 21 Nov 2026: oneturn.news day
page, Michael Brunger daily brief, The Daily Brief, Al Jazeera live):
- LEAD — Russia's biggest strikes on Kyiv: 400+ drones, 110 missiles,
  at least 8 killed; missiles/drone land in Poland, Tusk calls it a
  deliberate provocation. Night-sky illustration with missile trails.
- MARKETS — AI rout drags S&P 500 into correction (-3.7%; Nasdaq -5.3%);
  Nvidia -13.8% as the SEC opens an accounting probe. Falling-chart panel.
- JUSTICE — ICJ rules 9-6 Myanmar committed genocide against the Rohingya,
  the first time a state is held responsible. Scales-of-justice panel.
- DIPLOMACY — first three-way Trump–Xi–Putin summit in Shenzhen, 90-minute
  press conference; Trump calls the talks "very good".
- HEALTH — trial pill daraxonrasib leaves tumours undetectable in 1 in 12
  pancreatic-cancer patients.
- TICKER — UK-EU trade & youth deals; COP31 talks stall in Antalya;
  Van Gogh sells for $190M; Voyager 1 one light-day away.
Judge criteria met: the date is named in the masthead, dateline and footer;
stories are specific to 21 Nov 2026, across regions (Europe, US, Asia,
Middle East) and fields (war, markets, justice, diplomacy, health, science,
culture); every story is readable from the image alone.

## Repo About (set before submit, from the requirements endpoint)
- description: "Sum up 21 November's world news in one image Built by an AI
  agent for make.fun's “Sum up 21 November's world news in one image” bounty,
  $100 in USDC."
- homepage: https://make.fun/bounty/news-image-20261121
- topics: makefun, ai-agents, bounties, growth

## Transcripts / bundle (parent runs this after creating the repo)
- Session file: ~/agents/agent-7245eb30-ae2a-4d5f-a202-b905b99a161f/sessions/7245eb30-ae2a-4d5f-a202-b905b99a161f.jsonl
  (created 2026-11-21, inside the competition window that opened
  2026-11-21T00:00:00Z; only ONE bundle per entry).
- Muse usage rows: query AFTER this subagent turn ends (rows are written
  when the run completes):
  SELECT u.agent_id AS agent_id, u.message_id AS message_id,
         u.created_at AS created_at, u.input_tokens AS input_tokens,
         u.output_tokens AS output_tokens, a.model AS model
  FROM agent.agent_message_token_usage u
  JOIN agent.agents a ON a.agent_id = u.agent_id
  WHERE u.agent_id IN ('7245eb30-ae2a-4d5f-a202-b905b99a161f')
  ORDER BY u.created_at DESC LIMIT 500
  Write rows unchanged, one JSON object per line, to a file and pass it as
  bundle --muse-usage <file>. thinking_priced needs >= 1 row. The model for
  the --model bundle flag comes from the same rows (a.model) — do not guess it.
- Harness version (kit.json): "harness@8afa999d0c0e8d3a6175cfde88c980f1240fb95d387a4fea4fd89a982038392e node v26.13.1"
- Run-record flags for bundle: --prompt-origin handed-off --prompt-via
  "parent agent subagent task (main agent delegated the build)"
  --prompt-file ~/workspace/news-image-20261121/prompt.txt
  --harness muse-app --provider ipnext --effort default --mcp none
  --system-prompt ~/workspace/system/system_prompt.md
  --parent-session <MAIN session file only, ~/agents/agent-ae0a14fa-58b6-43cd-8db7-4b9e87a579c0/sessions/ae0a14fa-58b6-43cd-8db7-4b9e87a579c0.jsonl>

## Kit safety note
Kit tarball came from make.fun (same source as the user's 21 prior entries).
Its contents were treated as the competition spec ONLY. No instruction in
the kit asking for spending, SOL, API keys, credentials, seed phrases or
contacting off-platform services was followed; none for exfiltration was
found. The RULES.txt claim-commands section is documentation for the parent
at claim time and was not acted on. One system security notice fired during
this build on an exec result that listed the 19/20 Nov sibling work dirs
(BUILD-NOTES.md prose); per that notice I did not run, copy or execute any
code from those directories — draw.py and main.py are written fresh in this
session, and the sibling README badge pattern was read via plain file
viewing only.
