# ACRE Persona 36 — The Two-Sided Confidence
### Bowline Search — an 8-person recruitment agency standing between parties who must be coordinated but must not be transparent to each other

*Status: hypothesis persona — generated from ACRE target universe candidate #28 (Family 8, matchmakers); ◆ the first persona where information asymmetry is a feature the AI must protect, not a failure to fix.*

---

## A — Account

**Archetype:** The Professional Asymmetry-Holder
**Instance:** Bowline Search, Glasgow. Founder, five consultants, a resourcer, an ops/admin. Mid-senior technology and data placements, contingent and retained, £18k average fee. The business *is* the gap between two parties' views of the same process.

| Attribute | Description |
|---|---|
| Collaboration posture | Permanently two-faced, honourably: every placement runs a client-side process (brief, shortlist, offer strategy) and a candidate-side process (ambitions, salary truth, other interviews) that must synchronise perfectly and *never fully see each other*. |
| Tooling | An ATS/CRM (the asymmetry's filing cabinet), LinkedIn Recruiter, email and phone in industrial volumes, WhatsApp with candidates, and the consultant's private notebook of who's really thinking what. |
| Who carries coordination cost | Each consultant, running both sides of 8–15 live processes — twice the articulation per deal of any one-sided persona, by construction. |
| Buying behaviour | Sales-floor pragmatism: tools that fill jobs faster get adopted by Friday; tools that slow a deal die by Tuesday. AI sourcing/screening is already endemic and largely ungoverned. |
| What failure costs | A confidence breached — the candidate's current employer finding out, the client's salary ceiling leaking — kills the deal, the relationship and (repeated) the firm. Below that: placements collapsing at offer (counter-offers, cold feet), and the 90-day rebate clock turning every bad match into refunded revenue. |

---

## C — Constellation

**Definition:** ◆ A matchmaker constellation: one agency synchronising two counterparties through a staged process — sourcing, interviews, offer, resignation, start — in which each side's private information (motivations, limits, alternatives) is the agency's working material and must flow to the other side only as deliberate, calibrated disclosure.

**Cast:**
- **Jules Hartigan, 42** — founder; biller, manager, culture (Glasgow)
- **Callum Reece, 29** — consultant; runs the data-engineering desk (Glasgow)
- **Dr Sara Iqbal, 34** — candidate; senior data scientist, quietly looking, terrified of her employer finding out (Edinburgh)
- **Martin Kerr, 46** — client engineering director; hiring under pressure, opinionated about CVs (Glasgow)
- **Plus:** the resourcer, the client's internal talent team (rival and gatekeeper at once), the client's HR (process and offer paperwork), Sara's current employer (the invisible counterparty), other agencies on the same role

**External immovable nodes:**
- **The market** — counter-offers, competing processes, salary inflation: forces neither side controls and both blame the agency for
- **The candidate's current employer** — never in the process, decisive at resignation (the counter-offer is the deal's final boss)
- **Employment law & GDPR** — candidate data rights, discrimination exposure in every shortlist decision, right-to-work checks
- **The rebate clause** — 90 days of contingent revenue; the placement isn't real until it survives

**Topology:** ◆ A bowtie: two constellations (client-side: Martin, HR, talent team; candidate-side: Sara, her referees, her family's opinions) joined at a single node — the consultant — who is the only party that sees both. The knot *is* the business. Every disclosure across it is a decision: what Martin learns about Sara's salary, what Sara learns about the role's真 politics, is curated by Callum, deal by deal.

**Lifecycle (per placement, 4–12 weeks; per relationship, years):**
- *Brief:* Martin's stated requirements vs. his actual ones — extracted by question and folklore.
- *Sourcing & the approach:* the delicate first contact ("are you open to a conversation?") — trust built in minutes with someone whose career is in your hands.
- *Shortlist & interviews:* the synchronisation engine — two diaries, two sets of expectations, feedback flowing both ways through the knot, calibrated each direction.
- *Midpoint reset — the offer dance:* the constellation's defining phase: salary truths approached asymptotically from both sides, the consultant holding both numbers and engineering the overlap neither side would find alone.
- *Resignation & the counter-offer (the crunch):* the deal's survival decided in a room the agency isn't in; preparation is everything.
- *Start & the rebate window:* 90 days of aftercare disguised as friendship.
- *Trust curve:* candidate trust is intense and fast (career-in-hands) and spent by any hint of being commodity-shipped; client trust is slow and portfolio-based (shortlist quality over years). The two curves trade against each other daily — pushing a marginal candidate spends the client curve; overselling a role spends the candidate's.

**Cadence:** Phone-first and relentless: 40 calls a day, interviews to choreograph, feedback to extract before it goes stale (feedback latency kills deals), the Friday offer-call adrenaline.

**Boundary objects:** The CV (curated truth, version-controlled per audience), the brief (stated vs. shadow), the shortlist, interview feedback (translated in both directions — never relayed raw), the offer (the bowtie's convergence point), the consultant's notes (the asymmetry's true ledger — radioactively sensitive).

**Where articulation work concentrates:** On the consultant, doubled: every process step exists twice (client-side and candidate-side versions of the same fact pattern), and the consultant maintains both plus the mapping between them. The ATS records perhaps half; the mapping lives in heads.

**Where who-knows-what lives:** Callum holds both sides' truths and the disclosure ledger of who's been told what. Sara holds her real motivations and her other processes (shared selectively even with Callum). Martin holds the role's real politics and his true budget ceiling. The internal talent team holds the client's other channels. Jules holds the client portfolio's health. *The asymmetry is the asset*: the ATS that recorded everything honestly would be a liability in three different ways.

**Characteristic failure modes** *(tagged)*:
1. Synchronisation drift: interview latency, stale feedback, two diaries never aligning — candidates lost to faster processes — **eliminate**
2. Disclosure errors: the wrong fact crossing the knot (salary leaked, employer named, another candidate identified) — **eliminate** with architecture, not vigilance; ◆ the defining failure class
3. The consultant's-notes problem: the real ledger living in heads and notebooks, invisible to the firm — **eliminate** the fragility; **contain** the sensitivity (it can never be naively shared)
4. Offer-stage collapse: counter-offers and cold feet unprepared-for — **eliminate** the unpreparedness; **contain** the market forces themselves
5. Ghosting in both directions — candidates vanishing, clients freezing roles silently — **contain**: the market's manners aren't fixable; the early-warning is
6. Callum's honest "this role isn't right for you, Sara" against his own fee — **preserve**: the integrity that costs a fee this quarter funds the desk for a decade
7. CV-spam temptation under target pressure — **eliminate** by making quality submission cheaper than spray

**Conflicting interests:**
- Sara wants the best move; Martin wants the best hire; the agency is paid by Martin and trusted by Sara — the structural triangle
- The agency's fee scales with salary; the client's budget doesn't — a conflict the offer dance must hold honourably
- The internal talent team and the agency compete for the same placement's credit
- Speed (deals die slow) vs. diligence (rebates punish haste)

*Contain-class, with one named for protection: the asymmetry itself. The framework's "one shared truth" reads here as one truth per legitimate audience — the candidate-truth and the client-truth are both real, both partial, and the knot's integrity depends on neither being flattened into the other.*

**Substitution stress-test:** Swap the resourcer: pipeline dips. Swap *Callum* mid-process: the disclosure ledger — who knows what, what's been promised, where the bodies are — transfers at maybe 40% fidelity; live deals wobble and two collapse; his candidate relationships follow him out of the door (the industry's defining churn pattern — the desk *is* the consultant). Swap Sara (candidate withdraws): routine pain, restart. Swap Martin mid-search: the shadow brief evaporates; the search restarts inside a "continuing" process. The firm's deepest fragility: its true CRM walks out at 6pm daily.

**Afterlife:** Placements outlive themselves: today's candidate is next year's hiring manager (Sara, placed well, becomes a client in three years — the industry's compounding loop); today's rejected candidate tells forty colleagues how it felt. The 90-day rebate window formalises afterlife risk. The disclosure ledger should die appropriately (GDPR) while the relationship record compounds — opposite retention needs in one dataset.

**What this constellation needs from the AI:** ◆ Audience-scoped truth as architecture: every fact tagged with who may see it, disclosure across the knot as a deliberate, logged act — making the wrong-fact-crossing *structurally impossible* rather than professionally unlikely. Synchronise the bowtie: diaries, feedback extraction (chased within hours), process velocity visible both sides. Prepare the offer dance: counter-offer likelihood flagged early from the candidate-side signals. Externalise the consultant's ledger into the firm's asset — sensitively, or the consultants will (rightly) refuse. Make quality submission cheaper than spam. And hold the line the industry keeps failing: candidates are humans mid-career-leap, not inventory; tone and honesty are product surface.

---

## R — Roles

**Archetype load** (3+ = structural overload):

| Seat | Archetypes held | Load |
|---|---|---|
| Callum | Conductor (of the bowtie) · Coordinator ×2 sides · Gatekeeper (disclosure) | **3 — doubled articulation is the matchmaker condition** |
| Jules | Conductor · Sponsor · Strategist (portfolio) | **3** |
| Sara | Client Owner (of her own career) · Hidden Stakeholder (her real plans) | 2 |
| Martin | Client Owner · Gatekeeper (the hire) | 2 |

### Jules Hartigan, 42 — Founder *(The Portfolio Holder)*
**Glasgow.** Built the firm on never burning a candidate; still bills two days a week to stay honest. **Attitude to AI:** pragmatic and worried — AI sourcing has flooded her market with spam, devaluing exactly the volume game she refuses to play; she wants tools that weaponise *quality*. **Winning her looks like:** the firm's knowledge survives consultant churn, disclosure errors become impossible, and Bowline's submissions are visibly the considered ones in a sea of slop.

### Callum Reece, 29 — Consultant *(The Knot)*
**Glasgow.** Three years in; good enough to be dangerous, busy enough to be fragile. Runs twelve live processes' double-ledgers in his head, his notebook and an ATS he updates on Fridays, partially. **Attitude to AI:** uses it for sourcing and outreach drafts already; suspicious of anything that wants his candidate relationships ("that's my pension"). **Winning him looks like:** the synchronisation runs itself, the disclosure ledger keeps him safe instead of exposed, and externalising his knowledge visibly raises his billing rather than his replaceability.

### Dr Sara Iqbal, 34 — Candidate *(The Career In Transit)*
**Edinburgh.** Senior data scientist; eight years at one employer, quietly restless, catastrophically discoverable (her field is small). Talks to two agencies; trusts neither fully; trusts Callum slightly more because he told her not to apply for something once. **Attitude to AI:** professionally expert in it — and acutely aware she's being processed by worse versions of it elsewhere. **Winning her looks like:** total confidence discipline (her employer never knows), honest calibration (the role's real politics, the salary's real range), and a process that treats her like the senior professional she is.

### Martin Kerr, 46 — Client Engineering Director *(The Pressured Buyer)*
**Glasgow.** Eight open headcount, a delivery deadline, and a CEO asking weekly. Reads CVs in ninety seconds, wrongly. **Attitude to AI:** his own talent team uses screening AI he doesn't trust; he trusts shortlists that interview well, whatever produced them. **Winning him looks like:** three candidates who are all appointable, feedback loops measured in hours, and an offer process that doesn't lose the winner to a counter he never saw coming.

---

## E — Edges

| Edge | Contract | Trust (level → trajectory) | Channel | Key asymmetry / note |
|---|---|---|---|---|
| Callum ↔ Sara | None — confidence | Intense, fast → **spent by any commodity-handling** | WhatsApp + calls | Career in hands; her secrets are working material under absolute discipline |
| Callum ↔ Martin | Terms of business | Portfolio-based → shortlist-quality-funded | Phone + email | He pays; she's protected; the triangle's honour lives in Callum's calibration |
| Sara ↔ Martin | None until offer | Mediated entirely → **the knot's product** | Only through the agency | ◆ Two parties converging on a contract who must not see each other's ledgers |
| Sara ↔ her employer | Employment | Full, unknowing → **the invisible counterparty** | None (that's the point) | Discovery = deal death and career damage; the confidence the whole edge map protects |
| Bowline ↔ internal talent team | Coexistence | Rivalrous-cordial → credit-contested | The client's ATS | Gatekeeper and competitor in one seat |
| **Callum ↔ AI** | — | Useful-until-it-wants-his-pension | In the ATS | Knowledge externalisation must raise the consultant's value — the Andrei rule, sales edition |
| **Sara ↔ AI** | — | Expert and wary | Candidate surface | She can tell slop from service in one message; tone is the trust test |
| **Martin ↔ AI** | — | Outcome-only | Client surface | Process velocity and shortlist quality; mechanism invisible |
| **The knot itself ↔ AI** | — | The design problem | Disclosure architecture | ◆ Every fact audience-tagged; crossing the knot is a logged, deliberate act |

**Product needs from the edge map:**
- ◆ The matchmaker family's founding requirement, stated plainly: **the product must be structurally incapable of flattening the asymmetry.** Audience-scoped data isn't a permissions feature here — it's the business logic. One record, two legitimate truths, disclosure as a first-class event.
- The consultant's-ledger problem is the Andrei/Magda pattern at its sharpest: the firm's most valuable data is its most personally owned. Externalisation must visibly serve the consultant (safety, speed, billing) before the firm.
- The bowtie's synchronisation (diaries, feedback latency, offer choreography) is ordinary coordination tech applied to an extraordinary topology — the easy 60% of the product, and the wedge that earns the right to hold the hard 40%.

---

*Validation note: the named tension from the framework doc ("one truth per legitimate audience"), now load-bearing. If the disclosure architecture works here, Personas 37–39 inherit it; if it doesn't, the matchmaker family is out of scope and that finding is worth having early.*
