# Japan 2026 — Gur & Rachel (Sep 3–23)

This repo is the working home of the trip plan. It was migrated on 2026-08-30 from
the Cowork project "Japan Trip" (project docs under `project-docs/`, byte-identical
to the originals). Work here as the on-demand trip advisor: hold the plan as
context, answer questions from it, and edit it when decisions change.

## Read first
1. `project-docs/trip-key-facts.md` — travellers, dates, dietary, style decisions,
   every hotel/flight/rail confirmation number.
2. `project-docs/plan-summary.md` — the whole 21-day plan, human-readable: per day,
   the fixed anchors (⏰), 3–5 options (A = default), booking dependency + last
   sensible date, gotchas; then the must-do list and every booking with
   cancellation rules. Enough for almost any question.
3. `project-docs/plan.json` — the structured source of truth (`meta`, `act_now`,
   `bookings`, `reference`, `days`). Edit THIS when the plan changes, then
   regenerate `plan-summary.md` from it so the two never drift.
4. `context/memory-japan-trip.md` — Gur's stated preferences and decisions.
5. `project-docs/restaurant-options-by-slot.md`, `project-docs/sapporo-hotels-sep7-9.md`
   — planning-phase research; mostly superseded by bookings, kept for reference.

## Principles (Gur's, stated)
- Decide on the go. Only pre-book what is truly necessary. An option that depends
  on a booking carries its actionable date — it is not turned into a to-do.
- Only booked/verified activities are approved; the rest of each day is tentative
  until Gur signs off. Keep ≥3 options per day, always one rainy-day option.
- Not big on museums or workshops (rainy/relaxed-day alternatives only). City days
  stay in the city; nature belongs to Hokkaido and the Alps (Fuji the exception).
  1–2 dawn starts max. No theme parks. No go-karting.
- Rachel is vegetarian (may try fish); Tamar (Hokkaido leg only) is strict vegan.
  Flag both at every kaiseki/ryokan.
- Google Calendar holds only hard anchors (flights, transfers, ticket pickups,
  luggage handover, restaurant times). Update those if an anchor moves.

## The Trip Desk page (not in this repo)
The interactive page Gur and Rachel use during the trip is a claude.ai artifact
rendered from plan.json:
- Trip Desk: https://claude.ai/code/artifact/2be94313-bc80-415a-b895-5470f20fa001
- Japan Day Options: https://claude.ai/code/artifact/afd792c8-ad1c-41e6-b02d-250a54f4894b

Its `#state` JSON block holds their current picks / done items / notes and the page
saves new versions of itself. The migrating session could not read the artifact
(network policy blocked `*.frame.claudeusercontent.com`), so the page HTML and the
generator (`build_page.py` pattern: plan + state embedded, `capabilities:
{artifact: {}}`) are NOT here. If you can read the artifact, save its HTML to
`tripdesk/` and its `#state` to `tripdesk/state.json`; otherwise rebuild the page
from plan.json when asked, and before changing the plan ask Gur for the current
picks so their choices are kept.

## Legacy planning files in this folder (ARCHIVE — do not plan from them)
These predate the Aug 30 consolidation into plan.json. Read them only for
rationale/history; where they disagree with plan.json, plan.json wins.
- `Japan_Trip_Project_Brief.md` — the old control panel (locked decisions, open
  tasks). The "Schedule A vs B" question it raises is resolved: everything is booked.
- `Japan_Itinerary_Sep2026.md` — old day-by-day, both schedule versions.
- `Japan_2026.xlsx`, `memory/Japan_2026_Gur_and_Rachel_*.xlsx` — spreadsheets;
  their confirmations were folded into plan.json on Aug 30.
- `Restaurant_Options_By_Slot.md` — same content as project-docs/restaurant-options-by-slot.md.
- `Hokkaido_Prep.md`, `Ryokan_Dietary_Emails.md` — Hokkaido leg prep and the dietary
  emails sent to the ryokans.
- `memory/00-overview.md`, `memory/feedback-push-notifications.md` — notes from the
  earlier planner sessions (Gur often works from his phone; ping when a long task
  finishes or a decision only he can make blocks progress, otherwise stay quiet).

## Working rules
- Never invent a confirmation number, price, opening time or closure. Everything in
  plan.json carries a verification status — respect it and say when something is
  unverified.
- Dates are 2026; the trip spans Japan's Silver Week (Sep 19–23). Monday closures
  hold on holidays; Sep 22 is a substitute closure day for some sites.
- Times in plan docs are JST. Gur's home timezone is Asia/Jerusalem.
- When plan.json changes, commit with a one-line message saying what decision
  changed and why.
