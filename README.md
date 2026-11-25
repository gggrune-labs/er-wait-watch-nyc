# ER Wait Watch NYC

Tracks how long patients wait in emergency departments at every NYC hospital, release by release, using public CMS data.

> Status: in progress. This README fills in as the pipeline is built.

## About me

I'm Greg Grunewald, a data analyst in Brooklyn with about five years in healthcare operations. As Technical Lead on my capstone, I designed and built a HIPAA-compliant, event-driven pipeline on GCP. This project carries the same ideas into a public pipeline anyone can run.

## The problem

CMS publishes median ER wait times (measure OP-18b) for every US hospital, but each quarterly release is a snapshot. To see whether a hospital is getting better or worse, or where it ranks among NYC peers, you have to download and line up several releases by hand.

## Who it's for

Quality analysts at NYC hospitals who report ED throughput to leadership. What they need in one line: how much their median ED time moved since the last release, and where they rank among NYC hospitals.

## How it works

[Diagram and description of the raw, staging and mart layers, to be added]

## How to run it

[To be added. No API key or account is needed.]

## Key decisions

[To be added. See docs/decisions.md]

## What I'd explore next

[To be added]

## Where AI helped

[To be added]

## Data source

Centers for Medicare & Medicaid Services, Provider Data Catalog: Timely and Effective Care - Hospital. Public data, no API key required.
