## 1. Data source: CMS Timely and Effective Care - Hospital

**Chose:** The CMS Provider Data Catalog dataset Timely and Effective Care - Hospital (`yv7e-xc69`), focused on measure OP-18b, the median time patients spend in the emergency department.
**Considered instead:** NYC Department of Buildings complaints and violations (NYC Open Data), a pipeline on synthetic telehealth visit notes modeled on my capstone, and NYC restaurant inspection grades.
**Why:** It's free and needs no API key, so a reviewer can run the project without signing up for anything. It's healthcare, which is where my background is. And CMS publishes it every quarter and keeps past releases, so I can build real history and show change over time instead of a single snapshot. I set the restaurant idea aside because it was too close to the example project, the buildings data because it's outside healthcare, and the synthetic notes because they would need a local AI model to run, which adds setup for the reviewer.

## 2. Audience: hospital quality analysts

**Chose:** Quality analysts at NYC hospitals who report emergency department throughput to leadership.
**Considered instead:** Day-program and care-coordination staff who escort clients with disabilities to the ER and need to plan shift coverage.
**Why:** Quality analysts need two things from this data: whether their hospital's ED time is getting better or worse, and where it ranks among NYC peers. CMS releases are separate snapshots, so seeing the trend means lining up several releases by hand. That's exactly the gap a pipeline fills. I also know what OP-18b leaves out (psych and transfer patients), which is the kind of detail this audience cares about. I set the day-program audience aside because I couldn't speak to that use case from direct experience.

## 3. Extract scope: filter to New York on the server

**Chose:** Use the API's state filter to pull every NY row (all measures) into raw, then narrow to NYC counties and the ED measures in staging.
**Considered instead:** Pulling all 161,313 US rows and filtering locally, or filtering to NYC and OP-18b in the API call itself.
**Why:** I tested the state filter and it works on the server (161,313 rows down to 5,312). Keeping all of NY in raw means raw stays a faithful copy of what CMS sent, and a statewide benchmark stays possible later. Doing the NYC and measure filters in SQL keeps that logic visible and testable instead of hidden in an API call.

## 4. Page size: 500 rows per call

**Chose:** 500.
**Considered instead:** A bigger page to make fewer calls.
**Why:** A 2,000-row request returns HTTP 400. 500 and 501 both work, but the real limit isn't documented. I used a size I had tested rather than one I guessed. NY's 5,312 rows take 11 calls, which is cheap and exercises the paging logic.

## 5. VA hospitals: open

**Status:** Not decided yet.
**The question:** NYC's VA medical centers report in a separate CMS dataset (`ptds-r8im`), so the Hospital dataset leaves them out.
**Leaning:** Leave them out for the core build and say so in the README. Adding them means a second source to pull and match.
