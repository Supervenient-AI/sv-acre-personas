# ACRE Persona 6 — The Embedded Consultancy
### Northbeam Advisory — consultants living inside their enterprise clients' environments

## A — Account
**Archetype:** The Two-Laptop Consultancy. Northbeam, ~45-person transformation consultancy, organised in client-aligned pillars so siloed that the team serving one enterprise never needs to speak to the team serving another. Consultants spend 1–2 days a week physically at client sites, carrying two laptops: their own and the client-issued one, each opening onto a different world (the client's Teams/stack vs Northbeam's own M365). Fully distributed otherwise — client offices, WeWorks, full-remote, Paris; one team day a month at a WeWork to remember each other's faces. Currently going through ISO accreditation including the new AI management standard, which has forced an audit of tool sprawl — and the audit was ugly: 100+ licences on one whiteboard platform from workshop guests added and never removed, redundant accounts everywhere, and at least one case of clients being able to see the firm's *entire* whiteboard estate.

## C — Constellation
**Definition:** A consultant pod embedded inside an enterprise client's environment — working in the client's tools, on the client's laptop, under the client's governance — while the consultancy tries to retain its own institutional knowledge and methods.

**Cast:** Engagement lead, 2–4 consultants (embedded 1–2 days/week), the client's programme owner, the client's IT/security function (controls the environment the consultants work in), Northbeam's own ops/governance lead (fighting the licence hydra), and workshop participants who flow through shared tools in dozens.

**Topology:** Pods embedded in foreign territory. Each pod lives mostly inside its client's perimeter; the consultancy's own knowledge layer is wherever fragments escape back to — which is the problem.

**Boundary objects:** The workshop board (the single biggest leak surface), the deliverable deck, the client's own systems of record, and the consultancy's methods/IP — which exists to be reused across clients but keeps getting trapped inside individual client environments.

**Failure modes:**
1. Access sprawl: every workshop adds guests to shared tools; nobody removes them; governance discovers it years later at audit
2. Cross-client leakage — the nightmare scenario in a firm whose clients are competitors-adjacent
3. Knowledge fragmentation: what a consultant learns inside Client A's Teams never reaches the firm's collective memory
4. Workslop and brain-fry: "there's nothing worse than being presented the obviously-AI set of slides" — quality erosion at exactly the layer clients are paying premium rates for
5. Tool divergence: the firm's preferred AI tooling isn't accessible inside every client environment, so workflows can't standardise

**Conflicting interests:** Client IT wants the consultants fully inside its perimeter; the consultancy needs knowledge to compound *across* clients; individual consultants optimise for whichever laptop is in front of them; governance wants a single source of truth that the embedded reality keeps shredding.

**What the constellation needs from the AI:** Be the consultancy's own continuous layer that travels with the consultant across environments — a single source of truth on the firm's side, *piped into* each client environment (their Teams, their Salesforce) rather than replacing it. Manage the access lifecycle: who was added to what, for which workshop, and when they should be removed. Hold the firm's methods as reusable workflows. Keep an auditable line between client-confidential context and firm knowledge — which is also exactly what the ISO auditors want to see.

## R — Roles
**Katie Marsh, 42 — Engagement & Ops Lead (The Governance Conscience).** London, ex-startup operator; the person who discovered the 100 licences and now owns the cleanup. Has used vibe-coding tools for landing pages; fluent enough to be dangerous, senior enough to think commercially. Asks of any product: how does this fit the tools we already have, and what does it cost at scale — token anxiety is real.
**Raj Patel, 35 — Senior Consultant (The Two-Laptop Life).** Reading; Tuesdays and Wednesdays at a banking client's office on their hardware, rest of the week everywhere. His best thinking is trapped in a client tenant he'll lose access to when the engagement ends.
**Client-side: enterprise IT/security.** Not hostile, simply sovereign. The product enters this constellation on their terms or not at all.
**Fiona Drummond, 51 — Northbeam Partner (The Pillar Owner).** Cares about utilisation, quality, and never appearing in a leakage incident report. Will sponsor anything that demonstrably reduces the third.

## E — Edges
Defining edges: **consultant ↔ client environment** (the consultant is a guest with two identities; the AI must follow the person across the boundary without smuggling data across it); **pod ↔ firm knowledge base** (the broken edge the product exists to repair); **firm ↔ workshop guests** (high-volume, short-lived access relationships that currently have no lifecycle — an edge type most tools don't even model); **Katie ↔ auditors** (governance as a feature: the edge map *is* the compliance evidence).

*Grounded in: Katie Lewis interview, with workslop/brain-fry validation from the same conversation.*
