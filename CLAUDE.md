# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Mission

Translate **SEMICeu/DCAT-AP** (currently 3.0.1) into a complete LinkML-driven
pipeline. This is a **scoping/demo schema** built for the SEMIC × LinkML
evaluation — the deliverable is the *evaluation*, not a production DCAT-AP
profile. The point is to surface gaps in LinkML by trying to reproduce the
SEMIC SHACL / JSON-LD / HTML artefacts at
<https://semiceu.github.io/DCAT-AP/releases/3.0.1/> and to track those gaps
as LinkML's `main` branch evolves.

Iterative workflow: every time we discover something in DCAT-AP that LinkML
cannot represent cleanly,

1. document the gap in `COMPARISON.md`,
2. file it as an issue under `issues/` (see the `track-issues` skill),
3. work around it in the LinkML schema if a reasonable approximation exists,
4. retrofit once LinkML gains the capability (re-run the `align-model` skill
   against the latest `linkml/linkml` `main`).

`COMPARISON.md` is the running ledger of "what matches / what's missing / what
LinkML can't yet express". **Keep it current whenever the schema or the
upstream artefacts change.** Treat it as a deliverable, not a scratch file.

## LinkML version pinning

`pyproject.toml` pins both `linkml` and `linkml-runtime` to git
`linkml/linkml@main` (the linkml repo is now a uv workspace; both packages
live under `packages/` and are pulled via `#subdirectory=...` URLs). This is
**intentional and permanent**: the project's purpose is continuous evaluation
against unreleased LinkML. Do not "fall back" to PyPI versions. To pull newer
commits run `uv sync --group dev --refresh`.

## Repository layout

- `src/dcat_ap/schema/dcat_ap.yaml` — **the only hand-edited schema file.**
  Everything else is generated.
- `src/dcat_ap/datamodel/` — generated Python (dataclasses + Pydantic). Do not
  edit by hand; regenerate via `just gen-python`.
- `project/` — generated artefacts (SHACL, OWL, JSON Schema, ShEx, GraphQL,
  Java, TypeScript, Excel, Protobuf, SQL DDL, JSON-LD context, prefix map).
  Gitignored except `project/README.md`.
- `docs/elements/` — generated per-class/per-slot Markdown. Gitignored.
- `original/` — **read-only clone of <https://github.com/SEMICeu/DCAT-AP>**
  (gitignored). The full upstream repo, including every released version under
  `original/releases/`. Primary 3.0.1 sources of truth:
  - `original/releases/3.0.1/shacl/dcat-ap-SHACL.ttl` — SHACL shapes
    (authoritative for cardinalities/datatypes/nodeKind)
  - `original/releases/3.0.1/shacl/ranges.ttl` — class-range SHACL
  - `original/releases/3.0.1/context/dcat-ap.jsonld` — JSON-LD context
    (authoritative for property names like `releaseDate` ↔ `dct:issued`)
  - `original/releases/3.0.1/html/shacl/imports.ttl` — declares the
    DCAT-AP `owl:Ontology` (`<http://data.europa.eu/r5r>`) and its
    `owl:imports`. 3.0.1 has no standalone `.owl` file — this TTL is
    the OWL "footprint" to diff our generated OWL against.
  - `original/releases/3.0.1/index.html` — HTML spec
  - `original/releases/3.0.1/CHANGELOG.md` — release notes
  - Historical OWL/RDF axioms for cross-reference live in
    `original/releases/<2.x>/dcat-ap_<2.x>.rdf` — useful when checking
    that 3.0.x hasn't silently dropped class/property declarations.

  To refresh: `rm -rf original && git clone --depth=1
  https://github.com/SEMICeu/DCAT-AP original && rm -rf original/.git`.
- `tests/data/{valid,invalid}/` — example data tested by
  `linkml-run-examples`. Both directories are currently empty (`.gitkeep`
  only). Populating these is part of the gap-closing work.

## Build / generate / test

All recipes go through [`just`](https://github.com/casey/just/). Run `just`
(no args) for the list. Environment variables come from `config.public.mk`
(loaded automatically via `set dotenv-load`); generator-level config lives in
`config.yaml`.

| Recipe | What it does |
|---|---|
| `just install` | `uv sync --group dev` |
| `just gen-project` | Run all configured LinkML generators → `project/`; also writes the Python dataclasses + Pydantic into `src/dcat_ap/datamodel/` |
| `just gen-python` | Just the Python data models |
| `just gen-doc` | Schema markdown + bundled YAML under `docs/` |
| `just site` | `gen-project` + `gen-doc` |
| `just test` | Schema regen smoke test + pytest + `linkml-run-examples` |
| `just lint` | `linkml-lint` over the schema source dir |
| `just clean` | Remove `project/`, `tmp/`, generated docs, and `src/dcat_ap/datamodel/*` (except `__init__.py`) |

Subset recipes used during iteration:

- `just _test-schema` — `gen-project` into `tmp/` only (fast sanity check)
- `just _test-python` — regen Python then `pytest`
- `just _test-examples` — run `linkml-run-examples` against `tests/data/valid`
  and `tests/data/invalid`

Run a single pytest: `uv run pytest tests/path/to/test.py::test_name`.

The SHACL output is generated with `--non-closed` (see `config.yaml`/justfile)
to match SEMIC's open-shape semantics — don't switch to closed shapes without
updating COMPARISON.md.

## Schema architecture

The schema is a single file (`src/dcat_ap/schema/dcat_ap.yaml`) with three
sections worth understanding before editing:

1. **Top-level prefixes** map DCAT-AP's namespaces (`dcat`, `dcatap`, `dct`,
   `foaf`, `skos`, `adms`, `spdx`, `prov`, `odrl`, `locn`, `time`, `vcard`,
   `eli`). These flow into both SHACL output and the JSON-LD context, so they
   round-trip — do not rename casually.
2. **Classes** mirror the 15 SHACL `sh:targetClass` shapes plus ~17 supporting
   range classes. LinkML class names use the DCAT-AP English label
   (e.g. `Catalogue`, `LicenceDocument`) while the underlying `class_uri`
   points at the URI form (e.g. `dcat:Catalog`, `dct:LicenseDocument`). The
   synthetic abstract `CataloguedResource` superclass emulates the original
   `sh:or` over Catalog/Dataset/DataService/DatasetSeries — LinkML can't
   express a class disjunction as a slot range.
3. **Slot URIs** follow the JSON-LD context (e.g. `releaseDate` mapped to
   `dct:issued`), not the SHACL property names. Keep that convention.

Schema ID: `https://w3id.org/semic/dcat-ap/3.0.1`. **Not registered** — use
`configure-w3id` if/when this is promoted beyond the demo.

### Class inventory

The 15 classes with direct SHACL `sh:targetClass` shapes upstream
(LinkML name → URI):

| LinkML | URI |
|---|---|
| `Agent` | `foaf:Agent` |
| `Catalogue` | `dcat:Catalog` |
| `CatalogueRecord` | `dcat:CatalogRecord` |
| `Checksum` | `spdx:Checksum` |
| `Concept` | `skos:Concept` |
| `ConceptScheme` | `skos:ConceptScheme` |
| `DataService` | `dcat:DataService` |
| `Dataset` | `dcat:Dataset` |
| `DatasetSeries` | `dcat:DatasetSeries` |
| `Distribution` | `dcat:Distribution` |
| `Identifier` | `adms:Identifier` |
| `LicenceDocument` | `dct:LicenseDocument` |
| `Location` | `dct:Location` |
| `PeriodOfTime` | `dct:PeriodOfTime` |
| `Relationship` | `dcat:Relationship` |

Supporting classes (used as ranges, no `sh:targetClass` upstream):
`Resource`, `CataloguedResource`, `ChecksumAlgorithm`, `Document`,
`Frequency`, `Geometry`, `Kind`, `LegalResource`, `LinguisticSystem`,
`MediaType`, `Policy`, `ProvenanceStatement`, `RightsStatement`, `Role`,
`Standard`, `Activity`, `Attribution`.

### Date-disjunction handling

Date-typed slots (`releaseDate`, `modificationDate`, `listingDate`,
`startDate`, `endDate`) use `any_of` over `date | datetime | gYear |
gYearMonth`. The two `g*` types are declared as custom types with explicit
`uri: xsd:gYear` / `xsd:gYearMonth` because LinkML doesn't ship them. This is
the only practical way to round-trip the DCAT-AP date disjunction through
SHACL; the cost is that Python/Pydantic collapse them to `str`. See
COMPARISON.md "Custom datatypes" for the full picture.

## Known gaps (do not "fix" silently)

These are deliberate approximations driven by LinkML limitations. Document any
change to them in COMPARISON.md:

- `DcatResource_Shape` (class disjunction in range) → modelled as abstract
  `CataloguedResource`.
- Inverse-path SHACL constraint on `DatasetSeries` → not expressible.
- `sh:severity sh:Warning` → all generated shapes are violations.
- `sh:nodeKind sh:IRI` (no blank nodes) → LinkML emits `BlankNodeOrIRI`.
- Per-shape `rdfs:label` and `_Shape`-suffixed IRIs → not reproduced.
- Multilingual literals (`rdf:langString`) → emitted as plain `xsd:string`.

### Deliberate scoping omissions (not LinkML gaps)

Things upstream DCAT-AP has that we intentionally don't model — these are
scoping choices for the demo, not LinkML limitations:

- **EU Publications Office controlled vocabularies** (Frequency, Theme,
  MediaType, etc.). The original DCAT-AP *recommends* but doesn't *enforce*
  these code lists. Adding them as LinkML enums would bloat the schema
  without changing what the gap-finding evaluation tests.

## Working with this repo

- **Edit `src/dcat_ap/schema/dcat_ap.yaml` only.** Anything under `project/`,
  `src/dcat_ap/datamodel/`, or `docs/elements/` is generated and will be
  overwritten by `just gen-project` / `just gen-doc`.
- After a schema change, the standard cycle is `just gen-project` → eyeball
  the SHACL/JSON-Schema/OWL diff under `project/` → update COMPARISON.md if a
  gap closed or opened → `just test`.
- The `original/` checkout is the upstream artefact for diffing. Compare
  generated SHACL against `original/releases/3.0.1/shacl/dcat-ap-SHACL.ttl`
  (and `ranges.ttl`), not against an older local snapshot.
- This repo is bootstrapped from the [linkml-project-copier
  template](https://github.com/dalito/linkml-project-copier). `copier update`
  refreshes scaffolding via `just update`.

## Conventions inherited from `~/.claude/CLAUDE.md`

- Never `git commit`, push, or open PRs unless the user explicitly says so.
- Prefer `git mv` over `mv` for tracked files.
- `gh issue view` / `gh pr view` must use `--json` (the plain forms hit
  deprecated GraphQL fields).
