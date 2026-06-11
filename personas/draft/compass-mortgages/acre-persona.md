# ACRE Persona 21 — The Document-Chasing Relay
### Compass Mortgages — a 6-person broker firm whose entire business is moving paperwork between parties who don't answer

*Status: hypothesis persona — generated from ACRE target universe candidate #13 (Family 3, relay chains); not yet interview-grounded.*

---

## A — Account

**Archetype:** The Professional Chaser
**Instance:** Compass Mortgages, Birmingham. Founder/senior broker, two advisers, two case managers, an administrator. ~450 completions a year — residential, self-employed specialists, increasingly complex cases the comparison sites can't place.

| Attribute | Description |
|---|---|
| Collaboration posture | Pure relay: client → broker → lender → solicitor → completion. The firm owns no step's outcome, only the chasing between steps. Its product is making other parties act in sequence. |
| Tooling | A CRM/case system, lender portals (thirty of them, each different), a sourcing system for products, open-banking document collection (half the clients manage it), WhatsApp with clients who won't email, phones that never stop. |
| Who carries coordination cost | The case managers, by job description — the rare persona where articulation work is the named role. The advisers carry the client's emotional load. |
| Buying behaviour | Proc-fee economics: revenue arrives at completion, so anything that compresses time-to-completion or saves a dying case pays for itself visibly. FCA-regulated; audit trails are non-negotiable. |
| What failure costs | A product expires while documents trickle in — the client's rate rises, the broker's reputation with them dies, and the file restarts against a worse market. A compliance gap costs the licence that is the whole business. |

---

## C — Constellation

**Definition:** A relay chain run *as a service*: the broker stands between an anxious civilian and an indifferent institution, converting the client's chaotic financial life into the lender's required format, against product deadlines that move weekly.

**Cast:**
- **Darren Fitch, 44** — founder & senior broker (Birmingham)
- **Aisha Begum, 32** — case manager; chaser-in-chief (Birmingham)
- **Gemma Slade, 35** — the client; self-employed graphic designer remortgaging, two years of accounts in a shoebox
- **Pete Naylor, 41** — BDM (business development manager) at a specialist lender; the human backchannel into an inhuman process
- **Plus:** the second adviser, the administrator, lender underwriters (faceless, decisive), valuers, the conveyancing solicitor (often a Persona 20 firm), the client's accountant

**External immovable nodes:**
- **Lender underwriting** — the black box: documents go in, silence comes out, then a request for one more thing
- **Product expiry and rate repricing** — lenders pull products with 24 hours' notice; the deadline can move *toward* you mid-case
- **The FCA** — suitability, vulnerable-customer rules, Consumer Duty: every recommendation needs an evidence trail
- **The valuation** — a third party's opinion of a building, capable of re-opening everything

**Topology:** Relay chain with a broker-shaped pump in the middle: unlike conveyancing's hubless chain, this relay *has* a motivated coordinator — the broker is paid on completion and acts like it. The pathology isn't absent ownership; it's that the pump works by manual pressure on every link, all day.

**Lifecycle (per case, 4–16 weeks):**
- *Fact-find & document gathering:* the client's financial life assembled from fragments — the single biggest source of latency, and it's the *client* who stalls: bank statements trickle, accountants take a week per letter.
- *Sourcing & recommendation:* the adviser's actual expertise, compressed into hours; the suitability evidence written for the regulator.
- *Submission & underwriting (the long dark):* the lender's queue, punctuated by single-item document requests that each restart the clock. Aisha chases; Pete gets the quiet word when a case is dying.
- *Midpoint equivalent:* the underwriter's curveball — a re-request, a valuation surprise, a criteria change — that re-opens the sourcing decision while the product clock runs.
- *Offer → completion:* the baton passes to solicitors (often into Persona 20's chain) and the broker becomes a spectator with a proc fee at stake, chasing a process they can't see.
- *Trust curve:* the client's trust is front-loaded (they handed over their financial soul at fact-find) and erodes in the underwriting silence; one saved rate or rescued case converts it into referrals — the firm's actual growth engine.

**Cadence:** Morning portal sweeps, all-day chasing in both directions (clients for documents, lenders for decisions), product-pull fire drills when lenders reprice, evening WhatsApps from anxious clients.

**Boundary objects:** The document checklist (the case's true state), the fact-find, the decision in principle, the suitability letter (regulatorily load-bearing), the mortgage offer, the product-expiry date (an invisible boundary object that everyone orbits).

**Where articulation work concentrates:** On Aisha, formally — case progression *is* the job — but the volume (60 live cases) means triage by instinct: which case is quietly dying, which lender request hasn't been forwarded, which client has gone to ground. The instinct is excellent and undocumented.

**Where who-knows-what lives:** Aisha holds the true state of 60 cases. Darren holds lender criteria folklore — which underwriter accepts what, this month — that no sourcing system captures. Pete holds the lender's internal weather. Gemma holds documents she doesn't know matter. The accountant holds the certified figures, on their own sweet time. The CRM holds an optimistic approximation of all of it.

**Characteristic failure modes** *(tagged)*:
1. Client document latency: the case stalled on its own beneficiary — **eliminate** (chase warmly, automatically, in the client's channel)
2. The single-item restart: underwriting requests arriving serially, each costing a week — **eliminate** the serial discovery (pre-empt the full list from criteria folklore)
3. Product-expiry collisions: deadline moving toward a stalled case, noticed late — **eliminate**
4. Post-offer blindness: the case inside the solicitors' chain, invisible to the broker whose fee rides on it — **eliminate** (and note: this is literally an edge into Persona 20's constellation)
5. Criteria folklore living in Darren's head — **eliminate** the concentration
6. The adviser's "I won't place you on that product just because it completes faster" — **preserve**: suitability over speed is the regulatory and moral spine
7. Lender opacity and repricing — **contain**: the lender's right to its own process is absolute; the product's job is reading its weather, not changing it

**Conflicting interests:**
- Gemma wants the best rate and minimal homework; the process demands her homework before any rate is real
- The lender protects its book with indifference to anyone's timeline
- Darren is paid on completion but regulated on suitability — a tension the FCA watches explicitly
- Aisha's triage saves the loudest cases; the quiet ones die politely

*Contain-class: the completion-fee vs. suitability tension is the named one to keep anchored — recommendation evidence and case-progression pressure must stay visibly separate.*

**Substitution stress-test:** Swap the administrator: minor. Swap *Aisha*: sixty cases' true state and the triage instinct vanish — the CRM's optimistic fiction is exposed in a fortnight of missed chases; cases die quietly in the transition. Swap Darren: the criteria folklore and lender relationships (Pete answers *his* calls) thin out; placement quality drops on exactly the complex cases that are the firm's niche. Swap Gemma's accountant mid-case: a fresh letter queue, a worse delay. The firm's resilience is inversely proportional to how much of its process lives in two people's instincts.

**Afterlife:** Cases complete and the relationship *should* hibernate, not die: the product expiry in 2/5 years is a guaranteed repeat transaction — the firm's pipeline is literally its own archive. Today, the remortgage-date follow-up runs on CRM reminders half-maintained; the folklore says a third of clients drift to whoever emails them first. Referrals (the saved-case stories) are the growth engine; lender-side trust (Pete's willingness to take the call) compounds per clean submission.

**What this constellation needs from the AI:** Run the document chase end-to-end — checklist live, client chased warmly in WhatsApp, accountant chased formally, everything timestamped for the FCA. Pre-empt underwriting: assemble the full evidence list from criteria knowledge before submission, so single-item restarts stop. Watch every product clock against every case's velocity and escalate collisions early. See into the post-offer chain (the Persona 20 join). Externalise the folklore: criteria quirks captured per case into shared, searchable knowledge. And keep the suitability record pristine and separate — the AI accelerates the process, never the advice.

---

## R — Roles

**Archetype load** (3+ = structural overload):

| Seat | Archetypes held | Load |
|---|---|---|
| Darren | Conductor · Specialist Maker (advice) · Sponsor · Strategist (criteria folklore) | **4 — the adviser-founder pathology** |
| Aisha | Coordinator (×60 cases) · Gatekeeper (triage) | 2 — articulation work as a job title, at overload volume |
| Gemma | Client Owner · Production Realiser (of her own documents, reluctantly) | 2 — the client as the chain's slowest link |
| Pete | Peripheral Expert · Gatekeeper (the backchannel) | 2 |

### Darren Fitch, 44 — Founder & Senior Broker *(The Placement Brain)*
**Birmingham.** Twenty years from bank adviser to whole-of-market specialist; the broker other brokers ring about weird cases. Criteria knowledge like a cab driver's Knowledge. **Attitude to AI:** commercially hungry for it — he's watched comparison sites eat the simple cases and knows complexity-plus-speed is the moat. Wary only of anything that muddies his suitability evidence. **Winning him looks like:** cases move a week faster, the folklore outlives his memory, and the file always shows *why* the recommendation was right.

### Aisha Begum, 32 — Case Manager *(The Sixty-Case Mind)*
**Birmingham.** Knows every case's heartbeat; phones lenders with the queue-jumping politeness of a professional. Her handover document, were she ever to write one, would be the firm's most valuable asset. **Attitude to AI:** immediate adopter — chasing is her day and she'd rather be progressing. **Winning her looks like:** the chase runs itself, the dying cases surface themselves, and her judgement gets the edge cases only.

### Gemma Slade, 35 — The Client *(The Stalled Beneficiary)*
**Kings Heath.** Self-employed, time-poor, mildly ashamed of her paperwork; wants to be told exactly what to send and then left alone. Goes quiet for nine days when overwhelmed. **Attitude to AI:** lives in WhatsApp; will respond to a friendly nudge with a photo of a document at 9pm. **Winning her looks like:** one checklist, plain words, gentle persistence, zero judgement — and a rate secured before the deadline she never knew existed.

### Pete Naylor, 41 — Lender BDM *(The Human Backchannel)*
**Field-based, M6 corridor.** The specialist lender's face to fifty broker firms; spends his days translating between underwriting's silence and brokers' panic. **Attitude to AI:** fine with anything that sends him cleaner submissions; protective of the personal-favour economy that is his entire professional value. **Winning him looks like:** Compass becomes the firm whose cases are always complete on arrival — the firm worth spending favours on.

---

## E — Edges

| Edge | Contract | Trust (level → trajectory) | Channel | Key asymmetry / note |
|---|---|---|---|---|
| Darren ↔ Gemma | Advice agreement | High at fact-find → **silence-eroded** through underwriting | WhatsApp + calls | She surrendered her financial soul; the silence afterwards reads as carelessness |
| Aisha ↔ lender portals/underwriters | Panel terms | None — procedural → **opaque by design** | Portals + hold music | The black box edge; weather-reading, not relationship |
| Darren ↔ Pete | None — repeat game | Warm, favour-based → **submission-quality-funded** | Mobile | The informal edge that rescues formal failures; strictly rationed |
| Compass ↔ solicitors | Referral/none | Thin → **the post-offer blind spot** | Email into Persona 20's chain | The broker's fee rides inside another constellation's opacity |
| Gemma ↔ her accountant | Client | Friendly → **slow as geology** | Email | The chain's most innocent stall point |
| **Aisha ↔ AI** | — | Day-one adopter | In the CRM | Chase automation + triage surfacing = the whole job's drudge layer |
| **Darren ↔ AI** | — | Hungry, evidence-careful | In-product | Advice stays his; everything around it can go |
| **Gemma ↔ AI** | — | Indifferent to the tech | WhatsApp | Warm, persistent, judgement-free nudges — tone is the feature |
| **Underwriting ↔ AI** | — | None possible | Portal scraping/structured | An edge to be read, not befriended |

**Product needs from the edge map:**
- The client edge inverts the usual problem: the principal beneficiary is the slowest link. Chase design here is emotional engineering — warmth, shame-avoidance, channel-nativeness — as much as workflow.
- The criteria-folklore externalisation is the knowledge play: every completed case should teach the firm's collective placement brain, converting Darren's head into an asset that scales past him.
- The Persona 20 join (post-offer visibility into the conveyancing chain) is the first concrete cross-persona product surface in the relay family: two constellations, one shared status object.

---

*Validation note: the relay chain with a motivated pump. Contrast with Persona 20 (no pump): if the product's chain-status layer works in both, the relay-family thesis holds across ownership models.*
