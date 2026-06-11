# ACRE Persona 22 — The Tide-and-Tariff Relay
### Saltgate Freight — a 15-person freight forwarder moving legally loaded documents through many hands on deadlines set by ships

*Status: hypothesis persona — generated from ACRE target universe candidate #14 (Family 3, relay chains); not yet interview-grounded.*

---

## A — Account

**Archetype:** The Document Pilot
**Instance:** Saltgate Freight, Felixstowe. MD/owner, ops manager, eight operations clerks, two customs specialists, accounts. ~6,000 shipments a year — containerised imports mostly, a growing customs-brokerage line since Brexit made paperwork a product.

| Attribute | Description |
|---|---|
| Collaboration posture | A relay of institutions: shipper, origin agent, shipping line, port, customs, haulier, warehouse, client — every shipment touches eight-plus parties in four countries, none of whom share a system. |
| Tooling | A freight management system, HMRC's CDS, port community systems, shipping-line portals (each one different, all of them 2009), email at volume, phone for everything urgent, WhatsApp with hauliers. |
| Who carries coordination cost | The ops clerks, per shipment — each one shepherding 40–80 live files through eight handoffs each. The customs specialists carry the legal risk concentration. |
| Buying behaviour | Margin-per-shipment thinking; suspicious of "digital freight" platforms that promised disruption and delivered portals. Buys what reduces demurrage bills and customs penalties — costs with invoices attached. |
| What failure costs | Demurrage and detention: a container stuck at port costs £100+/day of pure loss. A customs misdeclaration is a legal event with the importer's name on it and the forwarder's fingerprints. A missed sailing is a week, minimum. |

---

## C — Constellation

**Definition:** A relay chain where the batons are documents with legal force (bills of lading, customs declarations, certificates of origin) and the clock is physical — sailings, tides, free-time windows — moving through institutions that communicate like it's still telex.

**Cast:**
- **Trevor Mott, 56** — MD/owner; forty years at the docks (Felixstowe)
- **Marta Wiśniewska, 39** — operations manager; the floor's central nervous system (Ipswich)
- **Donal Creevy, 44** — senior customs specialist; the one who signs things (Felixstowe)
- **Sanjay Mehta, 48** — client: furniture importer, 300 containers a year, margins thinner than the plywood (Leicester)
- **Plus:** ops clerks, origin agents (Shanghai, Ho Chi Minh, Gdańsk), shipping lines, hauliers, bonded warehouse, HMRC

**External immovable nodes:**
- **HMRC customs (CDS)** — declarations with legal force; queries and holds that stop physical goods dead
- **Shipping lines' schedules and free time** — sailings missed by hours cost weeks; demurrage clocks run on the line's calendar
- **The port** — gate windows, system outages, strikes, weather; physically sovereign
- **Tariff and regulation changes** — commodity-code reclassifications and new control regimes arriving by government notice, repricing everything in transit

**Topology:** Relay chain with parallel tracks: the *physical* chain (container: ship → port → haulier → warehouse) and the *documentary* chain (BoL → declaration → clearance → release) run side by side and must converge at specific moments — the container arrives whether or not its paperwork has. Saltgate pilots the documentary track and chases the physical one.

**Lifecycle (per shipment, 5–10 weeks door-to-door):**
- *Booking & origin:* the origin agent assembles cargo and documents; errors planted here (wrong weights, vague descriptions) detonate at destination weeks later.
- *On the water (the long middle):* tracking by portal and rumour; documents travel separately and slower than the ship, absurdly often.
- *Pre-arrival (the convergence crunch):* declaration lodged, duties calculated, release sought — against the vessel's actual arrival and the free-time clock. The persona's defining 72 hours.
- *Clearance or the hold:* HMRC clears, queries or inspects; a documentary query during free time is money burning by the day.
- *Delivery & dissolution:* haulier slot, warehouse booking, POD, invoice — then the file closes and its lessons evaporate.
- *Trust curve:* clients judge on the bad weeks only — nobody notices fluent clearances; one demurrage bill outweighs fifty clean files. Origin-agent trust is reciprocal and decades-deep or absent entirely.

**Cadence:** Vessel-driven: arrival reports each morning, pre-arrival pushes, panic in the free-time window, China time in the evening and the morning. Email threads per shipment that reach sixty messages without one decision in them.

**Boundary objects:** The bill of lading (the legal soul of the cargo), the customs declaration (Donal's signature, the firm's liability), the commercial invoice and packing list (where client sloppiness becomes forwarder risk), the arrival notice, the delivery order, the demurrage clock (invisible, omnipresent).

**Where articulation work concentrates:** On the ops clerks per file and Marta across the floor — sequencing documents against vessels, hauliers against releases, warehouse slots against drivers' hours. The expertise is real-time, perishable and entirely in heads and inboxes.

**Where who-knows-what lives:** Donal holds tariff classification judgement — the difference between 0% and 12% duty, defensible at audit. Marta holds the floor's live state and every haulier's reliability. Trevor holds forty years of port folklore and the relationships that un-stick stuck things. Origin agents hold the truth about what's actually in the boxes. Sanjay holds his sales commitments, made without consulting the shipping schedule. HMRC holds its own counsel.

**Characteristic failure modes** *(tagged)*:
1. Document-vessel divergence: cargo arriving before its paperwork is clearance-ready — **eliminate**; the single biggest demurrage driver
2. Origin-data sloppiness surfacing as destination crises — **eliminate** the late discovery (validate at origin, weeks earlier)
3. The sixty-message thread with no decision — **eliminate**
4. Free-time blindness: demurrage clocks tracked in heads against portal data nobody consolidates — **eliminate**
5. Classification concentration: Donal as the only safe pair of hands on commodity codes — **eliminate** the concentration; **preserve** his refusal to guess ("I'd rather query it than sign it") — that caution is the firm's licence
6. Client surprise at duties/delays they were warned about in paragraph four of message twelve — **eliminate** (a communication-format failure)
7. HMRC holds and inspections — **contain**: the state's right to inspect is absolute; the product manages around it, never around *it*

**Conflicting interests:**
- Sanjay wants landed cost certainty and delivery dates; the chain offers estimates and weather
- Shipping lines profit from demurrage; forwarders exist to prevent it — a structural opposition
- Origin agents serve the shipper's haste; Saltgate inherits the consequences
- Speed pushes against Donal's compliance caution; both are the service

*Contain-class: the speed/compliance tension is permanent and load-bearing — the AI accelerates everything around the judgement, never the judgement.*

**Substitution stress-test:** Swap an ops clerk: their 60 live files transfer via the FMS plus a fraught week — survivable because process is semi-standard. Swap *Marta*: the floor's triage instinct and haulier folklore go dark; demurrage spikes within a month. Swap *Donal*: the firm's classification risk appetite must reset to ultra-conservative (slower, costlier) until a successor earns confidence — or risk an HMRC audit finding. Swap an origin agent: a season of planted errors until the new one learns the clients' habits. Trevor's retirement (visible on the horizon) is the slow-motion version of all of these at once.

**Afterlife:** Shipments close; liabilities don't — customs declarations carry years of audit tail, and HMRC's questions arrive long after the file's clerks have moved on. The data afterlife is squandered: every shipment teaches landed-cost truth, supplier reliability and route performance, and almost none of it is harvested for the next quote. Client edges run on the absence of bad weeks; origin-agent edges are the decades-long repeat game.

**What this constellation needs from the AI:** Converge the tracks: one live view per shipment of vessel position, document status and free-time clock, with divergences flagged days early. Validate origin documents on receipt — weights, codes, descriptions — while errors are still cheap and Chinese business hours are still open. Distil the sixty-message threads into status and required actions. Watch every demurrage clock centrally. Externalise classification precedent (every code Donal signs, with reasoning) into a searchable, audit-defensible record. Tell Sanjay the truth early, in one screen, in importer's English.

---

## R — Roles

**Archetype load** (3+ = structural overload):

| Seat | Archetypes held | Load |
|---|---|---|
| Marta | Coordinator (the floor) · Gatekeeper (triage) · Strategist (haulier/route folklore) | **3 — the operational overload** |
| Trevor | Conductor · Sponsor · Peripheral Expert (port folklore) | **3 — and retiring with all of it** |
| Donal | Specialist Maker · Gatekeeper (compliance) | 2 — concentration risk, not load |
| Sanjay | Client Owner | 1 — with his cash flow inside the containers |

### Trevor Mott, 56 — MD *(The Port Whisperer)*
**Felixstowe.** Started as a clerk when manifests were paper; knows whom to ring when a container vanishes into the port's bureaucratic fog. Selling the firm to his staff in five years, he says; said it five years ago. **Attitude to AI:** breezily dismissive in the pub, quietly aware the folklore in his head is the succession problem. **Winning him looks like:** the firm's knowledge — his knowledge — visibly outliving his login.

### Marta Wiśniewska, 39 — Operations Manager *(The Floor's Nervous System)*
**Ipswich.** Ten years from clerk to ops manager; triages forty crises a day by feel. Bilingual, unflappable, permanently on two phones. **Attitude to AI:** show-me pragmatism — the third "digital freight revolution" she's been promised; this one had better answer where the container actually is. **Winning her looks like:** the divergence alarms are right, the clocks are watched, and her mornings start with exceptions instead of archaeology.

### Donal Creevy, 44 — Senior Customs Specialist *(The Signature)*
**Felixstowe.** AEO-deep expertise; treats commodity codes the way Gillian Hartwell treats searches. His signature is the firm's legal exposure. **Attitude to AI:** cautious-positive — drafting and precedent-search yes, auto-classification over his dead body. **Winning him looks like:** every past decision searchable with its reasoning, every new one his — faster, with the evidence pre-assembled.

### Sanjay Mehta, 48 — Importer Client *(The Cash-Flow Hostage)*
**Leicester.** Imports furniture for independent retailers; 300 containers of working capital perpetually afloat. Sells to his customers off a schedule the sea doesn't honour. **Attitude to AI:** whatever — he wants landed cost and arrival truth in one place instead of in paragraph four. **Winning him looks like:** he promises his retailers dates he can keep, and duty surprises stop existing.

---

## E — Edges

| Edge | Contract | Trust (level → trajectory) | Channel | Key asymmetry / note |
|---|---|---|---|---|
| Saltgate ↔ Sanjay | Trading terms, per shipment | Solid → **bad-week-fragile**: judged on demurrage bills, not clean files | Email + calls | He bears the cost of chain failures he can't see; warnings buried mid-thread don't count as warnings |
| Saltgate ↔ origin agents | Reciprocal agency, decades | Deep or nothing → reciprocity-funded | Email across timezones | They plant the errors Saltgate harvests; trust is the only QA |
| Saltgate ↔ shipping lines | Carrier terms | None — institutional → **adversarial on demurrage** | Portals | They profit from the delay the forwarder is hired to prevent |
| Donal ↔ HMRC | Legal (declarations) | Procedural → audit-shaped | CDS + formal queries | His caution is the firm's licence; the state's clock is nobody's |
| Marta ↔ hauliers | Per-job bookings | Folklore-based → reliability-scored in her head | WhatsApp + phone | Driver-hours and slot games; the physical chain's last mile |
| **Marta ↔ AI** | — | Thrice-burned pragmatist | In the FMS | Exceptions-first design or instant abandonment |
| **Donal ↔ AI** | — | Drafting yes, deciding never | Precedent archive | The classification record is the feature; autonomy is the dealbreaker |
| **Sanjay ↔ AI** | — | Indifferent to mechanism | Client status view | One screen of truth; importer's English; duty maths shown |
| **Origin agents ↔ AI** | — | Cooperative if it's less email | Structured handoff | Validation at origin is the highest-leverage intervention point in the chain |

**Product needs from the edge map:**
- The two-track convergence (physical vs. documentary) is this persona's unique demand: the AI must model *things* and *papers* as separate streams with mandatory rendezvous points — a generalisation of Sorrel & Gray's lead-time problem with legal force attached.
- Origin-side validation is the cheapest fix in the family: errors cost pennies in Shanghai and hundreds in Felixstowe; the product should move the discovery upstream across a reciprocal-agency edge.
- The precedent archive (classification decisions with reasoning) turns compliance from a bottleneck into a compounding asset — the same pattern as Compass's criteria folklore and Harewood's golden thread.

---

*Validation note: tests the relay family under physical-world clocks and institutional counterparties — the hypothesis is that demurrage gives coordination failure a daily price tag, making ROI unusually provable here.*
