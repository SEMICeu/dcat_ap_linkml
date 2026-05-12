---
name: align-model
description: Use when asked to align, sync, refresh, or close gaps between the LinkML schema in src/dcat_ap/schema/ and the upstream SEMICeu/DCAT-AP artefacts under original/. Triggers on phrases like "align the model", "sync with linkml main", "update COMPARISON", "close LinkML gaps", or after a new upstream DCAT-AP release lands.
---

# align-model

## Mission

Re-align the LinkML schema in this repo with the upstream SEMICeu/DCAT-AP
release (currently 3.0.1, under `original/releases/3.0.1/`) using the
**latest unreleased** LinkML — the goal is to discover whether features
merged to `linkml/linkml` and `linkml/linkml-runtime` `main` since the last
PyPI release can close gaps that `COMPARISON.md` currently lists.

The skill is iterative: pin LinkML to git `main`, regenerate, diff against
upstream, look for newly-available LinkML features, try them, re-diff,
update `COMPARISON.md`. Gaps that remain after a good-faith attempt stay
documented — moving on is the right call.

## Inputs / outputs

**Read:**
- `original/releases/3.0.1/shacl/dcat-ap-SHACL.ttl` (+ `ranges.ttl`)
- `original/releases/3.0.1/context/dcat-ap.jsonld`
- `original/releases/3.0.1/index.html` (and `html/` companion assets)
- `original/releases/3.0.1/CHANGELOG.md`
- `COMPARISON.md` (existing gap inventory)
- `NOTES.md` (design rationale)
- linkml/linkml and linkml/linkml-runtime: recently merged PRs and closed issues

**Write:**
- `src/dcat_ap/schema/dcat_ap.yaml` (schema edits to try new features)
- `pyproject.toml` (pin `linkml` and `linkml-runtime` to git `main`)
- `COMPARISON.md` (refreshed gap list)
- `CLAUDE.md` (only if the pipeline workflow itself changed — new just
  recipes, new CLI flags adopted, etc.)

## Procedure

### 1. Confirm LinkML is pinned to upstream main

This project hardcodes `linkml` and `linkml-runtime` to the
`linkml/linkml*` `main` branches — that's the whole point of the
project (continuous evaluation against unreleased LinkML). `pyproject.toml`
should already look like this:

```toml
[project]
requires-python = ">=3.10,<4.0"  # linkml main is 3.10+
dependencies = [
  "linkml-runtime @ git+https://github.com/linkml/linkml.git@main#subdirectory=packages/linkml_runtime",
]

[dependency-groups]
dev = [
  "linkml @ git+https://github.com/linkml/linkml.git@main#subdirectory=packages/linkml",
  # ...other dev deps unchanged
]

# Required because project.dependencies uses a direct (git) reference.
[tool.hatch.metadata]
allow-direct-references = true
```

> `linkml` and `linkml-runtime` are now siblings in a uv workspace under
> `packages/` inside the **single** `linkml/linkml` repo. The old
> `linkml/linkml-runtime` standalone repo is no longer the source. Always
> use `#subdirectory=packages/<package_name>` against `linkml/linkml`.

If it doesn't, fix it now — do not "fall back" to PyPI versions. The git
pin stays. Then re-resolve to pull the latest commits:

```bash
uv sync --group dev --refresh
uv run linkml --version    # sanity check: should be a +g<sha> style version
uv run gen-shacl --help    # confirm currently-available CLI flags
```

Capture the resolved commit SHAs (`uv pip list | grep -i linkml`) and
record them in the COMPARISON.md header. They're the only thing that
lets the next run tell whether the upstream actually moved.

### 2. Regenerate everything

```bash
just clean        # wipes project/ and src/dcat_ap/datamodel/*
just gen-project  # SHACL, OWL, JSON Schema, ShEx, Pydantic, dataclasses, ...
just gen-doc      # mkdocs source under docs/elements/
```

If any generator fails, **stop and investigate** before continuing — a
broken generator can mask gap-closing wins or invent fake ones.

### 3. Diff against the upstream

Three comparison surfaces:

| Surface | Generated | Upstream | What to compare |
|---|---|---|---|
| **SHACL** | `project/shacl/dcat_ap.shacl.ttl` | `original/releases/3.0.1/shacl/dcat-ap-SHACL.ttl` (+ `ranges.ttl`) | NodeShape count, target classes, property paths, cardinalities, `sh:datatype`, `sh:nodeKind`, `sh:or` blocks, `sh:severity`, `sh:closed` |
| **OWL** | `project/owl/dcat_ap.owl.ttl` | TTL-serialised; see "OWL comparison" below | Class declarations, property typing (`owl:ObjectProperty` vs `owl:DatatypeProperty`), `rdfs:subClassOf`, `rdfs:domain` / `rdfs:range`, ontology metadata (`owl:Ontology`, `owl:imports`) |
| **HTML** | `docs/elements/*.md` + `docs/schema/dcat_ap.yaml` (and `mkdocs serve` if needed) | `original/releases/3.0.1/index.html` | Coverage: every class and property documented upstream appears in our mkdocs output. Labels and descriptions roughly match. |

**OWL comparison sources for 3.0.x.** DCAT-AP 3.0.1 does **not** ship a
standalone `.owl` file — it ships TTL. The OWL surface to compare against
is assembled from three places:

- `original/releases/3.0.1/html/shacl/imports.ttl` — declares
  `<http://data.europa.eu/r5r> a owl:Ontology` with `owl:imports` of DCAT,
  DCT, FOAF, LOCN, SPDX, schema.org, PROV-O, time, vcard, ADMS. Use this
  to check the **ontology metadata** of our generated OWL matches
  (ontology IRI, imports list).
- `original/releases/3.0.1/shacl/dcat-ap-SHACL.ttl` + `ranges.ttl` —
  every `sh:targetClass` should correspond to an `owl:Class` in our OWL;
  every property used in a shape should be typed correctly
  (`sh:nodeKind sh:Literal` ↔ `owl:DatatypeProperty`; otherwise
  `owl:ObjectProperty`).
- Earlier releases that *did* publish an OWL/RDF file
  (e.g. `original/releases/2.1.1/dcat-ap_2.1.1.rdf`) are useful as a
  *historical* reference for what DCAT-AP class/property axioms looked
  like when they were declared explicitly. Don't treat 2.1.1 axioms as
  authoritative for 3.0.1 — terms may have moved or been redefined — but
  do cross-check that 3.0.x hasn't quietly dropped something we still
  emit (or vice-versa).

Useful one-liners (run from repo root, paths are relative — the workspace
hook blocks absolute paths under `/Users/matentzn`):

```bash
# Count SHACL shape declarations
grep -c "a sh:NodeShape" project/shacl/dcat_ap.shacl.ttl
grep -c "a sh:NodeShape" original/releases/3.0.1/shacl/dcat-ap-SHACL.ttl

# List target classes on both sides
grep "sh:targetClass" project/shacl/dcat_ap.shacl.ttl | sort -u
grep "sh:targetClass" original/releases/3.0.1/shacl/dcat-ap-SHACL.ttl | sort -u

# OWL: classes we declare vs SHACL target classes upstream
grep "a owl:Class" project/owl/dcat_ap.owl.ttl | sort -u
grep "sh:targetClass" original/releases/3.0.1/shacl/dcat-ap-SHACL.ttl \
  | awk '{print $2}' | sort -u

# OWL: ontology IRI + imports we emit vs upstream imports.ttl
grep -E "owl:Ontology|owl:imports" project/owl/dcat_ap.owl.ttl
cat original/releases/3.0.1/html/shacl/imports.ttl
```

For deep SHACL diffing prefer ROBOT or a small Python script using
rdflib that compares (target class, property, min, max, datatype,
nodeKind) tuples — textual diffs over Turtle are noisy and unreliable.

### 4. Refresh the gap inventory

Open `COMPARISON.md`. For every gap currently listed:

- **Still a gap** → leave it, but update wording if the situation changed.
- **Closed** → move to a "Closed in this run" subsection with the
  resolving LinkML feature / CLI flag / schema construct cited.
- **New gap** → add it to "Constructs LinkML can't express well".

Always record at the top of COMPARISON.md: the date, the LinkML
generator commit SHA, and the LinkML runtime commit SHA used for the
diff. That's the only way to tell whether a future run found new
problems or just new bugs.

### 5. Survey what's new in LinkML

Goal: find features merged since the last PyPI release that might
close any of the gaps from step 4.

```bash
# Recent merged PRs (last 60 days) on the linkml generator repo
gh -R linkml/linkml pr list --state merged --limit 50 \
  --json number,title,mergedAt,labels,url \
  --search "merged:>=$(date -v-60d +%F)"  # macOS; use -d on Linux

# Recently closed issues
gh -R linkml/linkml issue list --state closed --limit 50 \
  --json number,title,closedAt,labels,url \
  --search "closed:>=$(date -v-60d +%F)"

# Same for linkml-runtime
gh -R linkml/linkml-runtime pr list --state merged --limit 30 \
  --json number,title,mergedAt,url \
  --search "merged:>=$(date -v-60d +%F)"
```

Scan titles for:

- **Generator changes** mentioning `shacl`, `owl`, `pydantic`,
  `jsonschema`, `gen-doc`, `--closed`, `--mergeimports`, severity,
  nodeKind, langString, inverse, disjunction
- **Schema-language additions**: new slot/class metaslot, new
  `any_of`/`exactly_one_of`/`none_of` handling, new built-in types
  (e.g. `langString`, `gYear`)
- **CLI flag additions**: anything that gives a generator more
  fidelity over the OWL/SHACL output

For each promising change, read the PR description and linked tests.

### 6. Experiment

For every gap in COMPARISON.md that a new feature might address,
attempt a fix:

1. Make the minimum schema or config change.
2. Regenerate (`just _test-schema` is fastest for a smoke check;
   `just gen-project` for full output).
3. Diff the affected artefact only — don't re-do the full step 3.
4. **Keep the change** if it closes the gap or makes the output
   measurably closer to upstream.
5. **Revert** if it breaks other generators or produces output that
   diverges from upstream more than before.

Common candidates to try (verify they exist in current main before
relying on them):

| Gap | Thing to try |
|---|---|
| Class-disjunction range (`DcatResource_Shape`) | `exactly_one_of` / `any_of` on slot range |
| `sh:nodeKind sh:IRI` | A slot-level annotation or new metaslot for nodeKind, or a SHACL-generator CLI flag |
| Multilingual literals | A `langString` built-in type or `multivalued` + `pattern` workaround |
| `sh:severity sh:Warning` | A slot/class annotation hooked by gen-shacl |
| Inverse path constraints | Reified relationship class + inverse declaration |
| Per-shape `_Shape` IRIs | A gen-shacl CLI flag for shape IRI templating |

Document each attempt — both the wins and the failed experiments —
in COMPARISON.md so the next run doesn't re-try the same dead ends.

### 7. Final outputs

Verify before declaring done:

- [ ] `pyproject.toml` reflects the chosen pinning strategy
- [ ] `just gen-project` and `just gen-doc` run clean
- [ ] `just test` passes (or failures are pre-existing and noted)
- [ ] `COMPARISON.md` has an updated header (date + LinkML SHAs) and
      reorganised gap list (still-open / closed-this-run / new)
- [ ] `CLAUDE.md` updated **only** if the build/test recipe surface
      actually changed (new flag, new just recipe, new generator)
- [ ] `src/dcat_ap/schema/dcat_ap.yaml` reflects every experiment
      that was kept

Do **not** commit, push, or open a PR — the human reviews first
(see global CLAUDE.md rule).

## When to stop chasing a gap

Cut your losses after one good-faith attempt per gap per run. Signs
to move on:

- The feature you'd need isn't merged yet (open PR, in-review, or
  no issue exists).
- The workaround would require restructuring the schema in a way
  that breaks other classes.
- The fix would diverge from DCAT-AP semantics rather than match
  them more closely (e.g. inventing a class hierarchy DCAT-AP
  doesn't have).
- Two consecutive runs have failed to close the gap with different
  approaches — file (or reference) a LinkML upstream issue and let
  it go for now.

## Quick reference

```bash
# 1. Pull latest LinkML main (pyproject.toml already pins to git main)
uv sync --group dev --refresh
uv pip list | grep -i linkml   # capture SHAs for COMPARISON.md header

# 2. Regenerate
just clean
just gen-project
just gen-doc

# 3. Diff generated vs original (see step 3 table for paths)

# 4-6. Iterate: refresh COMPARISON.md → survey linkml/linkml main → experiment

# 7. Verify
just test
```

## Common mistakes

| Mistake | Fix |
|---|---|
| Diffing Turtle textually and chasing whitespace/prefix-order differences | Compare structural tuples (rdflib or ROBOT), not text |
| Assuming "no `.owl` extension upstream" means there's nothing to compare | The OWL surface is TTL-serialised: `imports.ttl` (ontology metadata + imports), `dcat-ap-SHACL.ttl` (class + property declarations via `sh:targetClass`/`sh:path`), and historical `.rdf` files from DCAT-AP 2.x for cross-reference. See step 3 "OWL comparison sources for 3.0.x" |
| Re-running `gen-project` 20 times mid-experiment | Use `just _test-schema` (writes to `tmp/`) for fast iteration; full `gen-project` only once you've settled on a change |
| Editing files under `project/` or `src/dcat_ap/datamodel/` | Those are generated — your edit will vanish on next regen. Edit `src/dcat_ap/schema/dcat_ap.yaml` |
| "Falling back" to PyPI versions because git deps feel risky | Don't. The project intentionally tracks `linkml` / `linkml-runtime` `main`. Re-pin to git if someone changed it |
| Forgetting `originals/` is gone | The folder is `original/` (singular); 3.0.1 artefacts under `original/releases/3.0.1/`. See CLAUDE.md |
| Committing or opening a PR at the end | Don't. Present results and wait for human approval (global CLAUDE.md rule) |
