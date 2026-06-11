# ACRE Persona 28 — The Privileged Guest at Scale
### Cobalt Ridge IT — a 20-person MSP living inside sixty client environments with the keys to all of them

*Status: hypothesis persona — generated from ACRE target universe candidate #20 (Family 5, embedded workers); not yet interview-grounded.*

---

## A — Account

**Archetype:** The Many-Perimeter Custodian
**Instance:** Cobalt Ridge IT, Warrington. MD/owner, service desk lead, eight desk engineers, four field/project engineers, an ops manager, sales and admin. ~60 managed clients (5–100 seats each): accountants, law firms, manufacturers, charities.

| Attribute | Description |
|---|---|
| Collaboration posture | The Northbeam condition, industrialised: engineers operate inside *dozens* of client environments daily — admin credentials, remote access, email tenancies — without ever belonging to any of them. The firm is a guest with root, sixty times over. |
| Tooling | PSA (tickets/contracts), RMM (the remote-control layer), a password vault the auditors ask about, M365 partner portals, documentation platform (IT Glue-shaped) at 60% accuracy and decaying. |
| Who carries coordination cost | The service desk lead in real time; the documentation platform absorbs what engineers remember to feed it, which is the gap the whole model leaks through. |
| Buying behaviour | Tool-dense by trade (MSPs run on software stacks) and commercially per-seat-sensitive. Security posture is now sales material: cyber insurance and client audits ask hard questions. |
| What failure costs | The catastrophic tail: an engineer's credentials breached = sixty clients breached — the MSP is the supply-chain attack surface, and knows it. The daily grind: tickets bouncing between engineers who each lack the context the last one had; the client who rings "their" engineer directly and bypasses every system. |

---

## C — Constellation

**Definition:** A hub of engineers embedded by remote access into many small organisations simultaneously — holding privileged access, undocumented tribal knowledge and de facto responsibility for systems the clients themselves don't understand — where the access lifecycle isn't a compliance afterthought but the entire risk model.

**Cast:**
- **Steve Garrott, 47** — MD/owner; ex-engineer, reluctant executive (Warrington)
- **Chloe Bevan, 29** — service desk lead; queue commander (Warrington)
- **Andrei Stoica, 36** — senior engineer; the one who knows every client's weirdness (Manchester)
- **Pam Hesketh, 52** — client-side practice manager at a 30-seat accountancy firm; "the IT person" by default, not desire
- **Plus:** desk and field engineers, the ops manager, sixty clients' staff, vendors (Microsoft above all), the cyber insurer

**External immovable nodes:**
- **Microsoft** — licensing changes, forced migrations, partner-programme reshuffles: unilateral weather for the whole client base at once
- **The cyber insurers and client auditors** — questionnaires with teeth: access lists, MFA coverage, offboarding evidence
- **Threat actors** — the only adversarial node in the library that attacks rather than negotiates; they set real deadlines (patch windows) and real stakes
- **Compliance frameworks (Cyber Essentials, client-side regulators)** — the accountancy and law clients import their regulators' demands into the MSP's scope

**Topology:** Hub with sixty embedded tendrils. Each client believes they have "an IT department"; actually they have a slice of a queue plus whatever Andrei remembers. Inverted knowledge gravity: the MSP knows the clients' systems better than the clients do — the opposite asymmetry to every other persona's client edge.

**Lifecycle:** Perpetual, pulsing on three clocks:
- *Per ticket (minutes–days):* the atomic unit; context assembles, resolves, evaporates.
- *Per client (years):* onboarding (discover the horrors, document the estate — the only time documentation is ever complete), steady state (decay), quarterly reviews (sales theatre plus genuine roadmap), and offboarding — the family's signature event: *proving you've given the keys back*, to a leaver or a whole departing client.
- *Per incident (the crunch):* outage or breach — all clocks converge; the constellation's true quality is revealed in an afternoon.
- *Staff-leaver lifecycle (internal but radioactive):* an engineer leaving holds credentials and tribal knowledge across sixty environments; offboarding *them* properly is the audit question that decides the insurance premium.
- *Trust curve:* clients judge on incidents and ring-back speed; trust accrues invisibly during quiet years and is spent in one bad outage. Engineers' personal edges with client staff accrete dangerously — loyalty to "their engineer" over the firm.

**Cadence:** The queue, always; alerts from the RMM around the clock; the monthly patch cycle; quarterly reviews; renewal seasons.

**Boundary objects:** The ticket (context's container and coffin), the documentation page (truth at onboarding, folklore thereafter), the access/credential vault (the crown jewels), the client's "IT roadmap" (the strategic veneer on the operational truth), the offboarding checklist (existential, often improvised).

**Where articulation work concentrates:** On Chloe across the queue (which engineer, which client, which context); on Andrei implicitly — he is the documentation platform's missing 40%, paged by colleagues all day for what only he knows.

**Where who-knows-what lives:** Andrei holds the undocumented 40% of sixty estates. The documentation holds onboarding-era truth plus decay. Pam holds her firm's business context ("payroll runs Thursday — never touch the server Wednesday night") that no ticket captures. Steve holds the commercial map. The vault holds the credentials; the engineers' muscle memory holds the *other* credentials, which is the audit finding waiting to happen.

**Characteristic failure modes** *(tagged)*:
1. Context evaporation between tickets: every engineer re-derives what the last one knew — **eliminate**
2. Documentation decay: truth at onboarding, fiction by year two — **eliminate** (capture from the work, not from engineer discipline)
3. Access-lifecycle sprawl: client staff leave, nobody tells the MSP; MSP engineers leave, the offboarding race begins — **eliminate**; this is Northbeam's audit finding with breach-grade stakes
4. The personal-engineer bypass: clients ringing Andrei directly, queue and record skipped — **contain**: the relationship is real value; the bypass of the record is what must go
5. Alert fatigue: the RMM crying wolf until the real one arrives — **eliminate**
6. Andrei's "don't patch that tonight, payroll runs Thursday" — **preserve**: client-context caution is the quality system; it just shouldn't live in one head
7. Vendor weather (Microsoft repricing/migrations) — **contain**: unchangeable; the product's job is blast-radius assessment across sixty clients in hours, not weeks

**Conflicting interests:**
- Clients want unlimited support on fixed contracts; the MSP's margin is the gap
- Engineers optimise for ticket closure; clients for actual resolution; the metrics diverge quietly
- Steve sells "proactive strategic IT"; the queue delivers reactive firefighting; both are true
- Security demands friction (MFA, change control) the clients resent until the day it saves them

*Contain-class: the fixed-fee/unlimited-demand tension and the security-friction tension are permanent; the product makes both visible (effort per client, risk accepted per decision) so they're priced rather than absorbed.*

**Substitution stress-test:** Swap a desk engineer: days, the queue absorbs it. Swap *Andrei*: sixty environments' undocumented 40% leaves; ticket times balloon, two clients churn within a quarter "because the service got worse" — the firm's deepest hidden dependency. Swap *Chloe*: queue triage instinct and engineer-skill mapping vanish; SLA breaches within weeks. Swap Pam (client-side): the MSP loses its business-context informant at that client, and "never touch the server Wednesday night" gets re-learned the hard way. Client staff churn constantly and *silently* — every unreported leaver is a live credential — the family's defining substitution risk runs in the customer's HR system, invisible.

**Afterlife:** Client offboarding is the model's integrity test: credentials returned, access revoked, documentation handed over — done well it seeds referrals; done badly it's the horror story at the next chamber-of-commerce lunch. Engineer alumni carry tribal knowledge to competitors. The documentation estate is the saleable asset when Steve eventually exits — MSP valuations literally price documentation quality. The insurer's renewal questionnaire is an annual afterlife audit of every access decision ever made.

**What this constellation needs from the AI:** Context that travels with the ticket: every client's history, quirks and Pam-facts assembled per ticket automatically. Documentation that self-maintains from the work itself (sessions, changes, resolutions harvested into the record). The access lifecycle as a first-class object — every credential, who holds it, granted-when, last-used, revoke-by — reconciled continuously against client HR reality and engineer rosters, audit-exportable on demand. Vendor blast-radius analysis across all sixty estates. De-concentrate Andrei without demoting him. And the bar above all: the product itself holds MSP-grade access to everything — its own security posture must exceed the standard it enables.

---

## R — Roles

**Archetype load** (3+ = structural overload):

| Seat | Archetypes held | Load |
|---|---|---|
| Steve | Conductor · Sponsor · Strategist · Client Owner (top accounts) | **4 — the engineer-turned-MD pathology** |
| Chloe | Coordinator (the queue) · Gatekeeper (SLA triage) | 2 — at alert-storm volume |
| Andrei | Specialist Maker · Peripheral Expert (×60) · Gatekeeper (change caution) | **3 — the tribal-knowledge overload** |
| Pam | Client Owner · Coordinator (client-side, conscripted) | 2 — "the IT person" who never applied for it |

### Steve Garrott, 47 — MD *(The Reluctant Executive)*
**Warrington.** Built the firm from his spare room and a van; still happiest fixing things, now sells and worries instead. The insurance questionnaire keeps him up more than the threat actors do. **Attitude to AI:** commercially keen (every MSP podcast says adopt or die), operationally cautious (root access plus generative AI is a sentence that frightens insurers). **Winning him looks like:** documentation stops decaying, the audit answers assemble themselves, and the firm's valuation-grade asset builds itself from daily work.

### Chloe Bevan, 29 — Service Desk Lead *(The Queue Commander)*
**Warrington.** Runs the board like air-traffic control; knows every engineer's strengths and every client's patience threshold. **Attitude to AI:** immediate — triage, context-assembly and alert-noise reduction are her entire pain surface. **Winning her looks like:** tickets arrive pre-contexted, alerts arrive pre-filtered, and the SLA clock stops being beaten by archaeology.

### Andrei Stoica, 36 — Senior Engineer *(The Walking Documentation)*
**Manchester.** Eight years in; can navigate any of the sixty estates blindfolded. Paged constantly by colleagues; flattered and exhausted by being irreplaceable. **Attitude to AI:** highly capable, quietly ambivalent — externalising his knowledge feels like dismantling his standing. **Winning him looks like:** the harvest credits him (his name on the knowledge, his interrupts dropping by half) and frees him for the project work he's been promised for three years.

### Pam Hesketh, 52 — Client Practice Manager *(The Conscripted IT Person)*
**Client-side, accountancy firm.** Office manager who became "the IT contact" because she sat nearest the server. Translates between her partners' fury and the MSP's ticket language. **Attitude to AI:** none for herself; gratitude for anything that means she explains a problem once. **Winning her looks like:** she reports things in plain English, never repeats herself, and the Thursday-payroll rule is finally known by the *firm*, not just by Andrei.

---

## E — Edges

| Edge | Contract | Trust (level → trajectory) | Channel | Key asymmetry / note |
|---|---|---|---|---|
| Cobalt Ridge ↔ each client | Managed service contract | Quiet-years-accrued → **incident-spent**: one bad outage erases three good years | Tickets + Pam-equivalents | Inverted knowledge gravity: the supplier knows the client's estate better than the client |
| Engineers ↔ client environments | Privileged credentials | Technical, total → **the supply-chain risk edge** | RMM + vault | Sixty root-level edges; the firm *is* the attack surface |
| Pam ↔ Andrei | None — habit | Warm, personal → **the bypass edge** | Direct mobile | Real value, off the record; the record must capture it without killing it |
| Chloe ↔ engineers | Internal | High → queue-mediated | PSA board | Skill-and-context matching lives in her head |
| Firm ↔ Microsoft/vendors | Partner agreements | None — weather | Portals + announcements | Unilateral changes ×60 client estates = the blast-radius problem |
| Firm ↔ insurer/auditors | Policy + questionnaires | Evidence-based → premium-priced | Annual forms | The access-lifecycle record is literally money here |
| **Chloe ↔ AI** | — | Day-one | In PSA/RMM | Triage + context assembly is the wedge |
| **Andrei ↔ AI** | — | Capable, status-wary | In the tools | Credit-preserving harvest or quiet sabotage |
| **Steve ↔ AI** | — | Keen but insurer-haunted | Governance view | The product's own security posture is the first sales conversation |
| **Clients ↔ AI** | — | Mostly unaware | Via better service | They experience it as "the IT company got good"; that's the correct UX |

**Product needs from the edge map:**
- The access lifecycle is existential here, not hygienic: every credential as a managed object with grant/use/revoke states, reconciled against *two* HR realities (the firm's and each client's). This is Northbeam's wedge with breach-grade stakes and an insurer willing to price the improvement.
- The Andrei problem names a general law: tribal-knowledge externalisation must *raise* the expert's status (attribution, interrupt-reduction, promotion to interesting work) or it will be resisted into failure.
- The product holds the keys to the keys: its own security architecture is the adoption gate, the insurance conversation and the moat, all at once.

---

*Validation note: tests the embedded family at maximum privilege and maximum multiplicity — the access-lifecycle thesis either proves existential here or it isn't a thesis.*
