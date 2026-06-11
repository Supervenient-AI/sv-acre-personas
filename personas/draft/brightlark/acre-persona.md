# ACRE Persona 15 — The Sprint-Rails Studio
### Brightlark Digital — a 14-person dev agency running client product teams on tickets, repos and staging links

*Status: hypothesis persona — generated from ACRE target universe candidate #7 (Family 2, agency-led); not yet interview-grounded.*

---

## A — Account

**Archetype:** The Structured-Rails Agency
**Instance:** Brightlark Digital, Newcastle. Two co-founders (one technical, one commercial), eight developers, two designers, a delivery lead, plus 3–6 contractor developers flexing with the order book. £1.6m; builds and maintains web/mobile products for clients who can't hire their own teams.

| Attribute | Description |
|---|---|
| Collaboration posture | Pods per client: Brightlark devs + contractors + the client's product owner working as one nominal team across a commercial boundary that surfaces at every estimate, invoice and incident. |
| Tooling | The most structured in the library: GitHub, Linear/Jira (client's choice), Slack Connect channels, staging environments, CI pipelines. The boundary objects are already digital, versioned and queryable. |
| Who carries coordination cost | The delivery lead across pods; within a pod, whoever is most conscientious — currently invisible and unpriced. |
| Buying behaviour | Engineers buy tools weekly and churn them monthly; the bar is "fits the existing rails." Anything demanding its own silo dies in a sprint. Already uses AI coding assistants everywhere — the question is team-level, not individual. |
| What failure costs | A production incident at 2am with blame spanning two companies; an estimate-reality gap that converts to either margin loss or trust loss; a contractor leaving with undocumented architecture in their head. |

---

## C — Constellation

**Definition:** An agency pod and a client product owner running a continuous build-and-maintain relationship on highly structured rails — where the coordination artefacts are unusually machine-readable and the human gaps hide between them.

**Cast:**
- **Aaron Bessey, 39** — co-founder & technical director (Newcastle)
- **Holly Tran, 33** — delivery lead, runs three pods (Newcastle)
- **Viktor Hajek, 41** — contractor developer, 18 months on the same client pod (Brno, remote)
- **Megan Shore, 36** — client-side product owner at a logistics firm (Leeds)
- **Plus:** pod devs and a designer, the client's IT/security team, the client's end users (whose complaints arrive translated through Megan)

**External immovable nodes:**
- **App store review / platform deprecations** — Apple's rejection or a forced API migration re-plans a quarter, appealable to no one
- **The client's IT/security function** — gates access, deployment windows and data; the pod works inside its rules
- **The client's budget cycle** — the retainer's real shape is set yearly in a meeting nobody from Brightlark attends

**Topology:** Agency-led pods with a deeply embedded client node: Megan sits *inside* the pod's daily rituals (standups, Slack, sprint reviews) while remaining contractually outside — the inverse of Northbeam's consultants-in-foreign-territory.

**Lifecycle:**
- *Per sprint (2 weeks):* planning → build → review → retro; the most explicit micro-lifecycle in the library, and the one that hides the macro drift best.
- *Per quarter:* roadmap re-planning, where the estimate-reality ledger gets settled or buried.
- *Per contract year:* renewal; the budget meeting Brightlark doesn't attend decides the pod's existence.
- *Midpoint pattern:* projects (a rebuild, a major feature) hit the classic reset mid-way — scope discovered, estimates re-based; the rails record the *what*, never the *why we believed otherwise*.
- *Incident lifecycle:* the constellation's stress test — 2am pages, two companies' blame instincts, a postmortem whose honesty depends entirely on edge trust.
- *Trust curve:* sprint-by-sprint accrual (demos that work) punctuated by step losses (incidents, estimate shocks). Contractor trust accrues to the *person*, not the agency — a quiet liability at renewal.

**Cadence:** Standups, sprint ceremonies, Slack Connect all day, the staging link as continuous truth, deploys on the client's permitted windows.

**Boundary objects:** The ticket (the unit of negotiation), the repo and PR (the work itself, legible to half the constellation), the staging link (the demo of truth), the estimate (the contested artefact), the incident postmortem, the roadmap.

**Where articulation work concentrates:** On Holly across pods; on Megan inside hers — she translates user complaints into tickets and business politics into priorities, doing unpaid product management for both companies at once.

**Where who-knows-what lives:** Viktor holds the architecture of the system he's spent 18 months in — the deepest technical knowledge sits in the least contractually attached node. Megan holds the why of every priority. Aaron holds the cross-client technical patterns. The repo holds everything and explains little: the rails record decisions, not reasoning. Holly holds the estimate-reality history nobody writes down.

**Characteristic failure modes** *(tagged)*:
1. Reasoning evaporation: tickets record what, PRs record how, nothing records why — archaeology required within months — **eliminate**
2. Estimate-reality drift surfacing quarterly as a trust event instead of weekly as data — **eliminate**
3. Contractor knowledge concentration (Viktor risk) — **eliminate** the concentration, not the contractor
4. Incident blame ambiguity across the commercial boundary — **eliminate** the ambiguity; **contain** the genuine liability question (it's contractual, not interpersonal)
5. Megan's translation burden: user noise → tickets, unaided — **eliminate**
6. Code review rigour and the architect's "no" to expedient hacks — **preserve**: the pod's engineering culture is the quality system; pressure to smooth it is constant and must lose

**Conflicting interests:**
- The client wants velocity and a fixed budget; the agency sells time honestly measured
- Megan needs demos for her stakeholders; the pod needs uninterrupted build weeks
- Contractors optimise for engagement-extension; the agency for margin; the client for neither
- Aaron wants reusable patterns across clients; each client believes they're paying for bespoke

*Contain-class: the estimate and the incident are where commercial truth must stay anchored to artefacts — burn-down data and postmortems — or they metastasise into renewal risk.*

**Substitution stress-test:** Swap a pod dev: a sprint of slowdown — the rails genuinely help. Swap *Viktor*: the architecture's living memory leaves with a 30-day notice period; the rails hold his code, not his model of it. Swap Megan: the pod loses its priority compass and its political shield simultaneously; the next PO inherits tickets without their why. Swap Holly: three pods' estimate-history and client-tone calibration vanish. The rails make this constellation *look* substitution-proof; the test shows the load just hides better here.

**Afterlife:** Maintain contracts mean constellations rarely fully dissolve — they thin. The codebase is the permanent artefact; whoever maintains it in year five pays for every undocumented decision from year one. Contractor edges persist person-to-person (Viktor will be hired by the client one day — the classic ending). Postmortems and ADRs, where they exist, are the only memory that survives team churn — the case for making them free to produce.

**What this constellation needs from the AI:** Ride the existing rails — never add a parallel system. Attach the *why* to tickets and PRs at the moment it's spoken (standup, Slack, review) so reasoning survives churn. Keep a live estimate-reality ledger both sides can see before it becomes quarterly drama. De-concentrate Viktor's knowledge by interviewing the work, not the worker. Draft Megan's tickets from user noise. Write the postmortem timeline from the record, neutrally — the AI as the only party with no liability position.

---

## R — Roles

**Archetype load** (3+ = structural overload):

| Seat | Archetypes held | Load |
|---|---|---|
| Holly | Coordinator · Gatekeeper (scope) · Strategist (estimate history) | **3 — overload spread across three pods** |
| Megan | Client Owner · Coordinator (client-side) · Gatekeeper (priorities) | **3 — the embedded PO carries two companies' articulation work** |
| Aaron | Conductor · Specialist Maker (still codes) · Sponsor | **3 — the player-manager pattern, technical edition** |
| Viktor | Specialist Maker · Peripheral Expert | 2 — with the constellation's deepest single dependency |

Three overloaded seats — the rails distribute work, not load.

### Aaron Bessey, 39 — Co-founder & Technical Director *(The Pattern Holder)*
**Newcastle.** Ex-fintech engineer; still takes the hardest tickets, to Holly's despair. Reviews architecture across all pods. **Attitude to AI:** deeply fluent — AI-assisted coding is table stakes here; what he wants is team-level memory, not individual autocomplete. **Winning him looks like:** the why-layer exists — six months later, anyone can ask "why is the sync service built like that?" and get the real answer with sources.

### Holly Tran, 33 — Delivery Lead *(The Three-Pod Juggler)*
**Newcastle.** Ex-dev who moved to delivery and keeps her hand in. Holds the estimate-reality history of every client in spreadsheets and scar tissue. **Attitude to AI:** practical maximalist — automate the ceremony, keep the judgement. **Winning her looks like:** burn-down truth visible to clients continuously, so the quarterly conversation is a review, not a reveal.

### Viktor Hajek, 41 — Contractor Developer *(The Deep Node)*
**Brno, remote.** Eighteen months in one codebase; knows where the bodies are buried because he buried them, with comments. Day rate, three-month rolling contract, zero job security and total system criticality. **Attitude to AI:** uses everything, trusts provenance only; wary of tools that read like a prelude to his replacement. **Winning him looks like:** knowledge-sharing that credits him as the source — making him *more* valuable visible, not less valuable extracted.

### Megan Shore, 36 — Client Product Owner *(The Embedded Outsider)*
**Leeds.** Logistics-firm lifer who became "digital" by being the only one who understood the users. Inside the pod's Slack, outside its company. **Attitude to AI:** keen, overloaded — already uses ChatGPT to draft tickets from user complaint emails. **Winning her looks like:** the translation burden halves, and she walks into her own stakeholder meetings with demo links and an honest status she didn't have to compile.

---

## E — Edges

| Edge | Contract | Trust (level → trajectory) | Channel | Key asymmetry / note |
|---|---|---|---|---|
| Pod ↔ Megan | MSA + SOW | High, daily → **estimate-fragile**: accrues by demo, drops by shock | Slack Connect + ceremonies | She's in the team but not of it; candour has a contract boundary |
| Megan ↔ her stakeholders | Employment | Variable → the pod's invisible weather | Internal | Budget meeting decides the pod's life; pod never sees it |
| Brightlark ↔ Viktor | Rolling contract | Deep, personal → **structurally precarious**: trust exceeds the contract holding it | GitHub + Slack | Maximum knowledge, minimum attachment — renewal risk wears a lanyard |
| Aaron ↔ Holly | Co-leadership | High → stable, role-blurred | Everything | He dives into code she's scheduled; the player-manager tax lands on her board |
| Pod ↔ client IT/security | Access agreements | Procedural → gate-shaped | Tickets + change windows | Northbeam's sovereign-perimeter pattern, milder: deploy windows and data rules are theirs |
| Pod ↔ platforms (Apple/cloud) | ToS | None → weather | Release notes | Deprecations re-plan quarters; the AI should at least see them coming |
| **Aaron ↔ AI** | — | Fluent, demanding | In the rails | Will reject anything that doesn't cite the repo; will extend anything that does |
| **Megan ↔ AI** | — | Already self-serving with ChatGPT | Slack + tickets | Govern the existing habit by being better at it: tickets with provenance |
| **Viktor ↔ AI** | — | Capable, replacement-wary | In the rails | Frame as amplification with attribution, or meet quiet resistance |

**Product needs from the edge map:**
- This constellation is the test of *riding existing rails*: every behaviour must express itself as enrichment of tickets, PRs, and Slack — a parallel app is dead on arrival among engineers.
- The why-layer is the unique gap: rails capture decisions exhaustively and reasoning not at all. Attaching reasoning at the moment of utterance is the product's whole value here.
- The commercial boundary inside a daily-intimate team (Megan's seat, Viktor's seat) is where one-truth-per-audience applies again: full candour pod-side, honest-but-scoped client-side, and the estimate ledger deliberately shared.

---

*Validation note: tests whether the AI adds value where coordination tooling is already excellent — the bet is that structured rails record everything except the reasoning and the relationships, which is exactly the ACRE layer.*
