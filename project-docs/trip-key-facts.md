# Japan Trip — key facts & canonical files (updated Aug 30, 2026)

## ⚠️ Source of truth — read this first
The plan now lives in this project, NOT in the spreadsheet:
- **`claude/plan.json`** — the full structured plan (21 days, 84 options, every stop with address/map/hours-on-date/price/booking/phone/transit/veg/verification status, act-now list, bookings with confirmation numbers and cancellation rules). Edit this when the plan changes.
- **`claude/plan-summary.md`** — compact, human-readable version of the same (read this for context in chat; it's enough for most questions).
- **Trip Desk page** — interactive artifact rendered from plan.json: `https://claude.ai/code/artifact/2be94313-bc80-415a-b895-5470f20fa001`. Gur and Rachel choose options, tick to-dos and write notes there; the page saves new versions of itself. **Before changing the plan, read the artifact (its `#state` JSON block holds current picks / done items / notes) so their choices are kept.** To republish: regenerate from plan.json with the generator (`build_page.py` pattern: plan + state embedded, `capabilities: {artifact: {}}`), and pass the URL above as `url`.
- Google Calendar holds the hard anchors only (flights, transfers, ticket pickups, luggage handover, restaurant times) — update those events if an anchor moves.

The old spreadsheet (`Japan_2026_Gur_and_Rachel_ScheduleA.xlsx` on Gur's Mac; stale copy on Google Drive) is now an ARCHIVE of the planning phase. Do not depend on it during the trip; its confirmations were folded into plan.json on Aug 30.

## Trip basics
- Travelers: **Gur & Rachel** (couple, 29). Rachel's **sister Tamar + boyfriend** join the **Hokkaido leg (Sep 7–10)**.
- Dates: **Thu Sep 3 – Wed Sep 23, 2026** (20 nights). Route: Tokyo → Hokkaido (Sapporo + Noboribetsu onsen) → Kyoto → Osaka → Takayama/Alps → Tokyo (Silver Week).
- Dietary: **Rachel = vegetarian** (may try fish); **Tamar = strict vegan** — flag at every kaiseki/ryokan.
- Style decisions (Aug 30): not big on museums/workshops (rainy-day alternates only); city days stay in the city, nature is Hokkaido + Alps (Fuji the exception); 1–2 dawn starts max; no theme parks; no go-karting; one sumo day (Sep 20 or 21) if tickets appear; Osaka night helicopter dropped Aug 31 (too pricey, not compelling); spa block Sep 22 before FARO; Sep 22 FARO is an engagement-level evening.

## Lodging (all booked via Klook)
Shibuya Stream (PBZ943404) · Sapporo Stream (KGG392117) · Takinoya Noboribetsu (JFN966234, non-refundable) · HOTEL RINGS KYOTO (HZR550734) · Hotel Royal Classic Osaka (EEV842685) · Takayama Ouan (ERB149933) · Kutsuroginoya Yuu, Shin-Hirayu/Ippōsui (GFV226893) · The Tokyo Station Hotel (YTX109746).

## Flights & rail
El Al LY91/LY92 (PNR YJ5PON) · ANA NH59 Sep 7 (FMSXWA) · ANA NH984 Sep 10 (DHYPIM) · Nozomi 84 + Hida 7 Sep 16 (Smart-EX 2001 / e5489 45760 — paper pickup at Osaka Sep 14–15) · Bus Hirayu→Matsumoto Sep 19 (185319539, mobile ticket) · Azusa 42 Sep 19 (Eki-net E37835 — paper pickup in Tokyo Sep 3–6, code 29372419579521238) · Shirakawa-gō buses Sep 17 (japanbusonline: out 07:50 res 08312001231 seats 11A/B; return 16:35 res 08312035491 seats 7A/B) · N'EX Sep 23 Tokyo 11:33 → NRT T1 (Eki-net E48412, car 3 seats 3-A/B — paper pickup at Tokyo Stn Sep 19–22, code 20292476220521218) · Udatsu Sep 4: veg course confirmed Sep 1 (2 guests, 1 veg + 1 regular, pay at restaurant).
