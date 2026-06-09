# ACRE Persona 5 — The Regulated Satellite
### Calder Wealth Planning — a solo financial adviser and PA operating inside a national network's compliance perimeter

## A — Account
**Archetype:** The Franchise Satellite. A newly formed one-adviser practice (adviser + PA, second staff member arriving within months) operating under a large national wealth-management network. The network approves the software list: its own messaging app (encrypted docs, digital signatures), Salesforce, a cashflow-modelling platform, a client-portal product. Microsoft 365 sits underneath everything. The network has approved some AI (meeting transcription) and not yet others — which the practice quietly uses anyway, on the reasoning that the value is too large to wait: AI-drafted review letters take 10 minutes instead of an hour, across ~140 households. The risk calculus is personal: if it ever goes wrong, the network's reputation engine will land on the practice, hard.

## C — Constellation
**Definition:** A tiny regulated practice whose every project is a relay chain through institutions it doesn't control — the network above, product providers alongside, the client at the centre — with trust as the actual product.

**Cast:** The adviser, the PA, the network's compliance function (faceless, decisive), product providers (pension and investment companies on the other end of letters of authority), and the client households.

**Topology:** Satellite-and-relays. The practice orbits the network (which sets the rules and processes a cut of everything) while running horizontal relay chains to providers: client signs a letter of authority → adviser submits to provider → provider returns incomplete information → clarification round-trips → data lands in the practice's template → analysis → suitability letter. Weeks of latency, none of it value-adding.

**Boundary objects:** The review letter (regulatorily required, written for a reader who mostly doesn't exist — perhaps 10 of 140 households read them), the letter of authority, the suitability report, the cashflow model, the meeting transcript.

**Failure modes:**
1. AI confabulation in client-facing documents — a review letter recently invented a child ("Riley") for a family with three differently-named daughters; sent unchecked, that destroys the only asset that matters
2. The letters-of-authority relay: chase, receive partial data, chase again — drudgery that is "no good for anybody"
3. Delegation failure: a founder used to doing everything, now needing the PA to absorb whole processes
4. Tool schism: the network approves slowly; capability arrives quickly; the gap is where the practice quietly lives

**Conflicting interests:** The network wants control and auditability; the adviser wants speed and his evenings; the PA wants real responsibility without becoming the one watched by monitoring software ("I don't want my employees to feel like they're being watched"); the providers are structurally indifferent to everyone's timelines; the client wants a human who knows their children's actual names.

**What the constellation needs from the AI:** Run the relay chains — track every letter of authority, chase providers, flag what came back incomplete, assemble the data into the practice's templates. Draft review and suitability letters with a *verification layer* that surfaces every factual claim (names, figures, products) against source records before anything human-signs. Brief the PA into processes the adviser has never written down. Operate inside the approved perimeter — or be the product the network itself approves.

## R — Roles
**James Calder, 43 — Adviser & Founder (The Excel Romantic).** York. Ex-rail demand modeller; builds beautiful spreadsheets nobody asked for. The actual job is talking — making people comfortable with their financial lives — and he's clear-eyed that most clients never read the paperwork the regulator requires him to produce. Philosophy: AI makes employees more productive, it doesn't replace them. Currently teaching himself to delegate, which is going about as well as it usually does.
**Sarah Whitlow, 34 — PA (The Process Owner-To-Be).** Poached from his previous firm; knows where everything is. About to inherit the letters-of-authority misery and would pay personally to have it automated. Will resent any tool that reads like time-tracking.
**The Network (compliance function).** Not a person; a weather system. Approves tools on its own schedule; punishes incidents without appeal. Every product decision routes around or through it.
**Provider-side: "Aegon-equivalents".** Institutional counterparties who respond in weeks, in PDFs, incompletely, by design of nobody in particular.

## E — Edges
Defining edges: **practice ↔ network** (asymmetric dependency; the practice's autonomy exists at the network's pleasure — product strategy may mean selling to the network, not the satellite); **adviser ↔ client** (high-trust, fully human, and the edge AI must never visibly touch: a clanger here is unrecoverable); **practice ↔ providers** (slow, formal, automatable with zero relationship risk — the single best ROI edge in the constellation); **James ↔ Sarah** (the delegation edge: the product can be the medium through which a founder finally hands processes over).

*Grounded in: Bowcliffe Wealth / SJP interview (James St.).*
