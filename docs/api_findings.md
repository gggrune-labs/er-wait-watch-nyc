# CMS API findings

Tested on Nov 25, 2026 with `explore/explore_api.py` against the CMS Provider Data Catalog API. No API key was needed.

| # | What I tested | Result | What it means for the pipeline |
| --- | --- | --- | --- |
| 1 | Searched the catalog for "timely" | 239 datasets in the catalog. Timely and Effective Care - Hospital is `yv7e-xc69`, last modified 2026-10-19 | The ID goes in the extract. The modified date shows when a new release is out |
| 2 | Row count with and without a state filter | 161,313 rows nationwide, 5,312 for NY | The state filter works on the server, so the extract can pull NY only |
| 3 | Asked for 2,000 rows in one call | HTTP 400, zero rows | The API rejects oversized pages instead of quietly capping them, so the extract must page through results |
| 4 | Asked for 500, then 501 rows | Both returned HTTP 200 with the full count | The real cap is somewhere between 501 and 1,999 and isn't documented. I page by 500, a size I tested |
| 5 | Stacked two filters: NY and measure `OP_18b` | 153 NY hospitals, measurement window 01/01/2025 to 12/31/2025 | Combined filters work. The current release covers calendar year 2025 |
| 6 | Read a sample row | One row per hospital per measure. Dates are text (`MM/DD/YYYY`), `score` is text, county is uppercase (`ERIE`) | Staging has to parse dates, `TRY_CAST` the score, and match NYC counties in uppercase |

## Open questions

- VA hospitals are in a separate dataset (`ptds-r8im`), so the Hospital dataset leaves out NYC's VA medical centers. Include them or not?
- How many archived releases exist, and do the measure IDs stay the same across them?
- What is the exact page size limit? (Optional to pin down.)
