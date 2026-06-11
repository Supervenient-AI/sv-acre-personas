# ACRE Personas
### A persona framework for products that live between people

---

## Why standard personas don't work for us

Classical UX personas assume the **individual** is the unit of value: one user, one set of goals, one journey. Our product's unit of value is the **collaboration itself** — the connective tissue between people who work together but don't work *for* the same organisation. Describing our users one at a time is like describing a single neuron and hoping to capture a thought.

The teams we serve are fragmented by design: a small brand, two agencies, a couple of freelancers, all converging temporarily on a shared deliverable. The thing we need to understand — and design for — is the *configuration*, not the individuals. Individuals are substitutable; the pattern of collaboration is not.

ACRE personas model users at four layers: **Account → Constellation → Role → Edge.**

---

## The four layers

### A — Account
The organisational layer, borrowed from Account-Based Marketing. Not just firmographics (size, sector, revenue) but **collaboration posture**: how much of this organisation's work crosses its own boundary, how networked its delivery model is, how fragmented its tooling, and who pays the price when coordination fails. A four-person challenger brand that outsources all creative is a different organism from a 30-person architecture practice with rotating consultant engineers — even if both are "UK professional services SMBs."

*The Account is who buys.*

### C — Constellation
The core innovation, and the layer where most design decisions get made. A Constellation persona describes a **recurring configuration of collaboration**:

- The cast of roles involved (not named individuals — roles), **including the external immovable nodes**: the retailer's buyer, the regulator, building control, the platform's compliance process. These parties sit outside the working team but hold veto power over it, and they set the deadlines everyone else lives by. A constellation map without its gatekeepers is missing the parties most likely to sink it.
- The topology: hub-and-spoke around a founder? Agency-led chain? Peer mesh?
- **The lifecycle.** A constellation is not a snapshot; it has a shape in time. Who assembles when (the production specialist who joins in week five "by industry convention" is a temporal fact, not a personality trait); what happens at the calendar midpoint, when teams reliably revise the frame they set in meeting one (Gersick's punctuated equilibrium); how the constellation behaves in the final crunch; and how it dissolves. Trust also has a lifecycle: in temporary teams it is *presumed* from roles and reputations, peaks at the start, and erodes with every inconsistency — so the early weeks spend trust capital that cannot be re-earned later.
- The cadence and channels of communication
- The dominant **boundary objects** — the shared artefacts (mockups, dielines, copy decks, briefs) through which the parties actually coordinate, and where translation between specialisms breaks down
- Where **articulation work** concentrates — who is informally carrying the burden of "who's doing what, by when, in what order"
- **Where who-knows-what lives.** Every constellation has a transactive memory system, usually an accidental one: the founder's brain as system of record, the copywriter as uncredited keeper of tone of voice, the production director as the only person who knows the tolerances. Map it explicitly — whose knowledge is invisible to whom is one of the strongest predictors of late-stage failure.
- The characteristic failure modes — **each tagged by friction type**: *eliminate* (coordination friction — waiting, version chaos, lost context; pure loss, remove ruthlessly), *contain* (genuine conflicts of interest — these cannot be resolved away, only kept anchored to the work so task conflict never curdles into relationship conflict), or *preserve* (productive friction — critique, dissent, the constraint-holder's awkward "no"; smoothing these damages the work). An AI designed from an untyped failure list will sand down the friction that makes the work good.
- The **conflicting interests**. This is essential: the parties in a constellation do not share one goal. The agency wants scope protection; the freelancer wants prompt payment and creative credit; the founder wants speed. The tension *is* the persona. If a Constellation document reads like one big happy individual, it isn't modelling the thing our product exists to mediate.
- **The afterlife.** Constellations in professional services are repeat games: edges outlive projects, reputations carry to the next engagement (the Hollywood model), and what gets archived or lost at dissolution determines how much the next constellation must relearn. Record what survives: which edges persist, who would be rehired, where the project's memory goes.

A Constellation survives the substitution of any individual member. Swap the illustrator and it is still the same Constellation. But survival is not free — substitution carries an acute cost spike (ramp-up tax on the remaining members, new communication paths, a trust reset on every affected edge), so each Constellation should carry a **substitution stress-test**: what actually happens here when a member is swapped mid-project?

*The Constellation is what we design for.*

### R — Role
Individuals, but defined **positionally** rather than demographically. We care less about a freelancer's age, goals and favourite apps than about her position in the network: peripheral, paid per deliverable, excluded from most communication channels, conscripted into our product by someone else's purchasing decision, and rightly suspicious of anything that smells like surveillance or unpaid admin. Role personas tell us what the product must feel like *from each seat* in the constellation — especially the seats that never chose us.

Each Role maps onto one or more of the twelve collaboration archetypes (Conductor, Client Owner, Hidden Stakeholder, Creative Lead, Specialist Maker, Production Realiser, Strategist, Coordinator, Gatekeeper, Newcomer, Sponsor, Peripheral Expert). Counting archetypes per seat gives an **archetype load** — and a load of three or more in one person is a structural overload signal, not a personality assessment. A founder simultaneously holding Conductor, Client Owner, Coordinator and Sponsor *is* the founder-hub pathology, expressed as a number.

*Roles are who we must not alienate.*

### E — Edge
Properties of the **relationships**, not the people: trust level *and trajectory*, contractual basis, communication channel, shared history, information asymmetry. Trust on an edge is a vector, not a level — "strained and worsening" predicts behaviour far better than "two years, solid". For each edge, record what currently sustains the trust (role consistency, reputation, shared history) and what would erode it (role blur, inconsistency, a missed payment), because in temporary collaborations trust starts high and is spent, not accumulated. Two identical constellations behave completely differently if the brand–agency edge is "five years of trust" versus "first engagement, fixed fee, nervous." Standard persona methods have nowhere to put this information. Ours must, because our AI literally sits on the edges — and because the AI is itself a participant, the human–AI edges need modelling too. The founder may treat the AI as a chief of staff; the freelancer may initially see it as the client's monitoring tool. Both are edges, and both shape behaviour.

*Edges are what the AI must navigate — and may eventually become our permissions model.*

---

## How ACRE personas are created

The research unit is the **project**, not the company and not the individual.

1. **Select 8–12 real projects** across our wedge verticals.
2. **Map each constellation**: who is involved, employed by whom, communicating through what, around which boundary objects, and where things broke.
3. **Interview multiple members of the same constellation.** The most valuable data is the *disagreement* — where the founder's account of the project diverges from the illustrator's is exactly where the product lives.
4. **Cluster at the constellation level.** Expect a small number of recurring topologies (founder-hub, agency-led, peer mesh, relay chain) that cut across verticals. A marketing project and an interior design fit-out may be the same Constellation wearing different clothes — which tells us whether we're building for verticals or for topologies.

---

## How we use them

- **Design decisions key to Constellations.** "What does the AI surface, to whom, when?" is unanswerable at the individual level. A founder-hub constellation needs the AI to relieve the hub; a peer mesh needs it to maintain shared state.
- **Asymmetric onboarding.** One party adopts; everyone else is conscripted. Role personas define what conscription must feel like from each seat, and Edge attributes tell us how much trust capital each invitation can draw on.
- **Pricing and GTM map to layers.** We sell to the Account, design for the Constellation, and must not alienate the Roles at the periphery. The constellation *is* our buying committee.
- **AI behaviour tuning.** Edge attributes become product configuration over time: how formal the AI is across a low-trust contractual edge, what it may share across which boundaries.
- **Friction policy.** The typed failure modes tell the AI which frictions to remove (coordination), which to keep anchored to artefacts (conflicts of interest), and which to leave — or even reinforce (critique, dissent, the early "no" from a constraint-holder).

---

## A known tension to hold deliberately

Our design principle is "one shared truth". Matchmaker constellations (recruitment, talent management, lettings) break it on purpose: their business *is* standing between parties whose views of the same process must not be fully transparent to each other. For these shapes, information asymmetry is a feature the AI must protect, not a failure to fix. "One shared truth" should be read as *one truth per legitimate audience* — the edges define the audiences. This tension is named here so it gets designed for, not discovered in a sales call.

---

*One-line summary: ACRE personas describe who buys (Account), the pattern we design for (Constellation), the seats we must win over (Roles), and the relationships our AI must navigate (Edges).*