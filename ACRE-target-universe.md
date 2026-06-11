# ACRE Target Universe
### Candidate company types for the next wave of constellation personas

The library currently covers eight constellations across six topologies. This list expands the universe of UK SMB company types we could target, organised by **topology family** rather than sector — because the product generalises along topologies, and the persona set should stress-test all of them. Candidates marked **◆ new topology** would add a constellation shape we haven't yet modelled; the rest are high-value instances of shapes we have (useful for validating that a constellation persona really does survive a change of vertical).

Each entry: who they are → why their collaboration is fragmented → what the persona would add.

---

## Family 1 — Hub-and-spoke around a client-side hub
*The Wildfen shape: a small organisation coordinating external specialists toward a deliverable.*

1. **Interior design studios** — designer as hub for client, contractors, joiners, fabric houses, antique dealers, installers. Already in our stated wedge and conspicuously missing from the library; the supplier edges include physical-goods lead times, which our current personas lack.
2. **High-end residential builders / design-and-build firms** — client, architect, structural engineer, subbies, building control. The hub is the builder, the client is on-site weekly, and every change ripples through six trades.
3. **Bespoke furniture / architectural joinery workshops** — designer-maker hub between interior designers, architects, timber suppliers and finishers. Small, craft-proud, email-and-phone-native.
4. **Small fashion / apparel labels** — founder hub coordinating pattern cutters, sampling studios, fabric agents and an overseas factory. ◆ adds the **cross-border, cross-timezone, cross-language edge** — WhatsApp to a factory in Porto or Guangzhou is a different edge type from WhatsApp to Glasgow.
5. **Craft drinks brands (gin, beer, kombucha)** — contract production instead of owned production: the "factory" is a supplier. Near-clone of Wildfen, useful as a validation persona rather than a new one.

## Family 2 — Agency/consultancy-led accounts
*The Loop Theory shape: a small expert firm running continuous client relationships with attached freelancers.*

6. **Brand & digital design studios** — the classic 5–15 person studio; freelancer-heavy, crit-culture, client feedback loops through Figma comments and decks.
7. **Dev agencies / software studios** — sprints, client product owners, contractor developers; the boundary objects (tickets, repos, staging links) are unusually structured, which makes them a good test of whether the AI can ride existing rails.
8. **Video production companies** — per-shoot constellations (director, DOP, sound, edit, grade, client) assembled and dissolved in weeks. ◆ adds the **rapid-assembly/rapid-dissolution constellation**: the cast changes faster than any onboarding process can run.
9. **Market research agencies** — client + field recruiters + moderators + transcribers + analysts; heavy on consent, incentives and PII handling.
10. **E-learning / content studios** — instructional designers + subject-matter experts (client-side, time-poor) + animators + voiceover artists. The SME-availability bottleneck is a distinctive failure mode.
11. **Translation & localisation agencies** — a PM hub dispatching to a global freelancer network with hard deadlines and per-word economics. Possibly the purest constellation business in existence: the entire company *is* edge management.

## Family 3 — Relay chains
*◆ Largely new territory: value moves through a sequence of parties, each handoff a failure point, no single party owning the whole chain.*

12. **Conveyancing solicitors** — buyer, seller, two solicitors, two agents, lender, surveyor, and a chain of other transactions stacked behind. The UK's most famously broken relay; everyone in it hates it; nobody owns it. ◆ a pure **chain topology** where our AI could be the first thing that sees the whole sequence.
13. **Mortgage brokers** — client → broker → lender → solicitor → completion; document-chasing as the core activity (rhymes with the adviser's letters of authority, but as the *entire business*).
14. **Customs/freight forwarders & import agents** — shipper, carrier, customs, warehouse, client; documents with legal force moving through many hands on deadlines set by tides and tariffs.
15. **Probate & estate administration specialists** — executors, beneficiaries, HMRC, banks, valuers; slow institutional counterparties and emotionally loaded clients.

## Family 4 — Peer meshes with an accountable node
*The Harewood Frame shape: multi-firm professional collaboration where one party carries the liability.*

16. **Structural / civil / M&E engineering consultancies** — the other nodes of the architecture mesh; modelling one would let us see the same constellation from a different seat, which no persona method normally achieves.
17. **Planning consultancies & heritage specialists** — orbiting local authorities, with statutory consultees as immovable external nodes; deadlines set by committee calendars.
18. **Grant-funded research consortia (university + SME partnerships)** — work-package meshes across institutions with incompatible admin systems and a funder's reporting regime on top. ◆ adds the **funder-governed mesh**.
19. **Boutique law firms** — solicitor + counsel (self-employed barristers!) + expert witnesses + the other side. The counsel relationship is a genuinely strange edge: critical, prestigious, and structurally freelance.

## Family 5 — Embedded / two-environment workers
*The Northbeam shape: people working inside other organisations' perimeters.*

20. **IT MSPs (managed service providers)** — engineers living inside dozens of client environments simultaneously, with privileged access that makes our access-lifecycle story existential rather than nice-to-have.
21. **Fractional executive practices (CFO/CMO/COO portfolios)** — ◆ adds the **one-person-many-constellations topology**: a single individual who is a senior node in five unrelated organisations at once, context-switching as a way of life. The product's memory becomes their working memory.
22. **Bookkeeping & outsourced finance firms** — inside every client's Xero, inbox and payroll; a hub with deep tendrils into many small companies; deadline-driven by HMRC's calendar, not their own.

## Family 6 — Hubs of hubs
*The Bellhaven shape: a small centre coordinating autonomous organisations.*

23. **Franchise brands (small UK franchisors)** — head office coordinating dozens of owner-operated outlets: brand consistency vs. franchisee independence, with marketing assets and compliance flowing down and trading data flowing (reluctantly) up.
24. **Sustainability / ESG consultancies** — collecting standardised data not just from clients but from *clients' suppliers*: a hub-of-hubs where the outermost ring has no contractual relationship with the centre at all. ◆ adds the **no-contract outer ring**.
25. **Co-operative & federated businesses (e.g. indie retail buying groups)** — coordination with explicitly *equal* members: standardisation must be negotiated, never imposed.

## Family 7 — Consumer-as-hub
*◆ New territory: the coordinating hub is a private individual, not a business — but every spoke is one of our target SMBs.*

26. **Wedding planners** — planner + venue + caterer + florist + band + photographer + a once-in-a-lifetime, emotionally maximal client. The planner is paid precisely to be the AI-in-the-middle; the question is whether we serve the planner or threaten them.
27. **Home renovation projects (serving the architect/builder side)** — the homeowner as untrained, anxious hub of a six-figure constellation. We'd enter through the professionals, but the persona models the civilian at the centre.

## Family 8 — Matchmaker / dual-sided constellations
*◆ New territory: the business's job is to stand between two parties whose interests partially conflict.*

*Note: this family deliberately breaks the "one shared truth" design principle — here, information asymmetry is a feature the AI must protect, not a failure to fix. Read the principle as "one truth per legitimate audience", with the edges defining the audiences. Named in the framework doc as a tension to hold deliberately.*

28. **Recruitment agencies** — candidate-side and client-side processes that must be coordinated but *must not* be transparent to each other: the first persona where information asymmetry is a feature the AI must protect, not a failure to fix.
29. **Talent & influencer management agencies** — agent between talent and brands: negotiations, usage rights, content approvals, and a talent roster that is itself a set of tiny businesses.
30. **Literary & speaker agencies** — slower, contract-heavy variant of the same shape; rights and royalties as long-lived boundary objects.
31. **Lettings & property management agencies** — landlord, tenant, contractors, compliance certificates: a permanent three-sided constellation with statutory deadlines (gas safety, deposits) that never stops running. ◆ also adds the **perpetual (no-end-date) constellation** — there is no "project", only an ongoing state.

## Family 9 — Seasonal / pulse constellations
*◆ New territory: enormous temporary teams that inflate and deflate on a calendar.*

32. **Festival & live-event producers** — a core team of 4 that becomes 400 for six weeks: suppliers, crews, councils, sponsors, volunteers. Onboarding at scale, on a deadline, annually, mostly from scratch.
33. **Exhibition & trade-stand builders** — design, fabrication, logistics, venue rules, international shows; every project ends with a physical install at 2am.
34. **Sports event / mass-participation organisers (10ks, triathlons)** — councils, medics, volunteers, sponsors, timing companies; risk assessment as the central boundary object.

## Family 10 — Care & clinical coordination
*◆ New territory: multi-party coordination where the "deliverable" is a person's wellbeing and the compliance regime is unforgiving.*

35. **Multidisciplinary private clinics (physio, sports medicine, mental health)** — clinicians who are often self-employed associates renting rooms under one brand: a constellation disguised as a company. Referral pathways, treatment notes, and CQC-grade confidentiality.
36. **Domiciliary care agencies** — coordinators, rotating carers, families, GPs, councils; rota chaos and safeguarding bright lines. Heavy, but the social value and the urgency of the coordination problem are unmatched.
37. **Veterinary referral networks** — first-opinion practices + specialist centres + labs + insurers; clinical records crossing business boundaries constantly.

---

## Choosing the next five — suggested criteria

- **Topology coverage:** at least two picks from ◆-marked candidates, so the framework keeps being stress-tested rather than confirmed.
- **Wedge proximity:** at least two picks adjacent to the stated wedge (interior design and one other creative-services type are the obvious gaps in the current library).
- **Pain × ability to pay:** conveyancing and lettings have screaming pain but grim software budgets; fractional execs and MSPs pay readily.
- **Research access:** prefer types where warm intros exist through the current interviewee network (the architecture mesh, the portfolio hub and the consultancy interviews each open obvious doors).
- **One wildcard:** one pick that feels off-wedge (care coordination, festivals, consortia) — if the ACRE method produces a coherent persona there too, that's evidence the framework, and the product thesis, generalise.

A starting suggestion, for argument's sake: **interior design studio (1), conveyancing (12), fractional executive practice (21), lettings & property management (31), festival producer (32)** — two wedge-fillers, three new topologies. But the list is the deliverable; the picks are yours.
