import requests

CATALOG_URL = "https://data.cms.gov/provider-data/api/1/metastore/schemas/dataset/items"

response = requests.get(CATALOG_URL, timeout=60)
response.raise_for_status()
datasets = response.json()

print(f"Datasets in the catalog: {len(datasets)}")

for ds in datasets:
    title = ds.get("title", "")
    if "timely" in title.lower():
        print(ds.get("identifier"), "|", title, "|", ds.get("modified"))
DATASET_ID = "yv7e-xc69"
QUERY_URL = f"https://data.cms.gov/provider-data/api/1/datastore/query/{DATASET_ID}/0"

# Test 1: no filter. How many rows in the whole dataset?
r = requests.get(QUERY_URL, params={"limit": 1, "count": "true"}, timeout=60)
print("All rows:", r.json().get("count"))

# Test 2: filter to New York. Does the count actually drop?
ny_params = {
    "limit": 1,
    "count": "true",
    "conditions[0][property]": "state",
    "conditions[0][value]": "NY",
    "conditions[0][operator]": "=",
}
r = requests.get(QUERY_URL, params=ny_params, timeout=60)
print("NY rows:", r.json().get("count"))
print("Sample row:", r.json()["results"][0])

# Test 3: ask for more rows than the API probably allows. What comes back?
r = requests.get(QUERY_URL, params={"limit": 2000}, timeout=60)
print("Asked for 2000, got:", len(r.json().get("results", [])), "| status:", r.status_code)


# Test 4: find the real page size limit, and read the error message
for size in [500, 501]:
    r = requests.get(QUERY_URL, params={"limit": size}, timeout=60)
    print(f"limit={size} -> status {r.status_code}, rows: {len(r.json().get('results', []))}")
    if r.status_code != 200:
        print("  Error says:", r.text[:300])

# Test 5: NY + OP-18b only. How many NY hospitals report ER wait time?
op18_params = {
    "limit": 500,
    "count": "true",
    "conditions[0][property]": "state",
    "conditions[0][value]": "NY",
    "conditions[0][operator]": "=",
    "conditions[1][property]": "measure_id",
    "conditions[1][value]": "OP_18b",
    "conditions[1][operator]": "=",
}
r = requests.get(QUERY_URL, params=op18_params, timeout=60)
data = r.json()
print("NY hospitals with OP_18b:", data.get("count"))
if data.get("results"):
    row = data["results"][0]
    print("Example:", row["facility_name"], "|", row["countyparish"], "|", row["score"], "min |", row["start_date"], "to", row["end_date"])

