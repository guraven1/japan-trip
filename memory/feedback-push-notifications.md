---
name: feedback-push-notifications
description: Ping Gur's phone when a long trip task finishes or a decision is needed; stay quiet otherwise.
metadata:
  type: feedback
---

Gur plans this trip partly from his phone via **Remote Control** (Claude Code runs on his Mac, phone is the window in). He wants a notification when long-running work finishes so he can lock the phone instead of watching. Set up 2026-07-01. (Mirror of the same rule in the MBA project.)

**Send a PushNotification (status: proactive) when:**
- A long task he kicked off finishes while he was likely away — booking/logistics research, restaurant or hotel shortlists, comparing Schedule A vs B, building a tracker.
- I've hit a decision only he/Rachel can make and can't proceed — A vs B choice, sister+bf participation, a budget ceiling, which specific place to book.

**Don't send for:** routine progress, or a quick answer while he's clearly still in the session.

**Message style:** under ~200 chars, one line, no markdown. Lead with the action — e.g. "Onsen ryokan options ready — 3 to compare, all bookable" or "Need A vs B from Rachel before I lock Kyoto/Takayama hotels."

**Why:** He's steering this trip and the MBA work from his phone with the Mac left on; the point of the setup is to not be tethered to the screen.

**How to apply:** Err toward silence, but reliably fire at the two triggers above. The push reaches his phone only when Remote Control is connected; otherwise it's a harmless desktop notification.
