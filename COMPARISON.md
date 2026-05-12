# Structural comparison: LinkML-generated vs original DCAT-AP 3.0.1

This document compares the LinkML-generated artefacts under `project/`
(SHACL, OWL, JSON-Schema, …) against the original SEMICeu DCAT-AP 3.0.1
release under `original/releases/3.0.1/`.

## Run metadata

| Field | Value |
|---|---|
| Date | 2026-05-12 |
| `linkml` version | `1.11.0rc3.post8.dev0+1c5f68e4` |
| `linkml-runtime` version | `1.11.0rc3.post8.dev0+1c5f68e4` |
| LinkML pinned to | `git+https://github.com/linkml/linkml.git@main` (uv workspace) |
| Upstream commit (linkml) | `1c5f68e4` |

Capture these in the header of each future run so we can tell whether a
diff change is "LinkML changed" or "DCAT-AP changed".

## Headline numbers

| Metric                                    | Original | Generated |
|-------------------------------------------|----------|-----------|
| `sh:NodeShape` declarations               | 33       | 32        |
| Shapes with `sh:targetClass`              | 33       | 32        |
| Shapes with `sh:closed false`             | 33       | 32        |
| OWL `owl:Class` declarations              | n/a      | 32        |

Upstream has two shapes we don't emit:

- `dct:MediaTypeOrExtentShape` — a disjunction shape over MediaType and
  Extent (still blocked by gap #2 — class disjunction in range).
- `TimeInstantShape` — targets `time:Instant`, used as the range of
  `time:hasBeginning` / `time:hasEnd` on `PeriodOfTime`. Our `beginning`
  and `end` slots are still typed as plain `string` — a `TimeInstant`
  class with `class_uri: time:Instant` would close this. **New
  observation this run.**

We emit one shape upstream doesn't:

- `rdfs:ResourceShape` (`Resource` superclass we added as a generic
  abstract top). Harmless, but consider whether the `Resource` class is
  pulling its weight.

## What aligned this run

### Shape IRI scheme (gap #7 closed)

`gen-shacl` now ships `--suffix` and `--use-class-uri-names` (the latter
is the default). Adding `shacl: { suffix: Shape, closed: false }` to
`config.yaml` makes our shape IRIs follow the upstream pattern
exactly: `dcat:CatalogShape`, `spdx:ChecksumShape`,
`eli:LegalResourceShape`, etc. The local-name component now matches
`<https://semiceu.github.io/DCAT-AP/releases/3.0.1#dcat:CatalogShape>`
1:1 (the upstream namespace prefix differs, but the suffix and the
class-IRI-as-local-name now match).

### Open shapes (gap #6, properly closed now)

The prior COMPARISON.md asserted `--non-closed` was already applied, but
the config.yaml wasn't actually wired to pass it through `gen-project`.
This run adds `shacl: { closed: false }` to `config.yaml`, and every
emitted shape now carries `sh:closed false`, matching upstream's
`shacl:closed false`. Closed by configuration, no schema change needed.

### OWL class IRIs use class_uri (new gap, closed in same run)

`gen-owl --no-use-native-uris` makes OWL emit class IRIs based on
`class_uri` instead of the schema's default-prefix-derived URI. Without
the flag, our OWL was emitting `dcat_ap:Catalogue`, `dcat_ap:Checksum`,
etc.; with `owl: { use_native_uris: false }` in `config.yaml` it now
emits `dcat:Catalog`, `spdx:Checksum`, `foaf:Agent`, matching the upstream
class identifiers used across the imported ontologies (DCAT, DCT, FOAF,
SPDX, …). This was not previously called out as a gap; flagging it now
in case it regresses.

### Cardinality on `dct:rights` (Catalogue)

The prior table flagged `dct:rights` on Catalogue as a (0,∞) generated
vs (0,1) upstream mismatch. The schema's `Catalogue.slot_usage.rights:
multivalued: false` is now honoured: generated SHACL emits `sh:maxCount
1` on the property shape. Match.

## Still-open gaps (carry forward to next run)

These are the genuine LinkML expressivity gaps remaining after this
alignment run.

1. **Class disjunction in property ranges.** DCAT-AP's `DcatResource`
   (union of `Catalog | Dataset | DataService | DatasetSeries`) and
   `MediaTypeOrExtent` are emulated by introducing synthetic abstract
   superclasses; the original upstream form is `sh:or` over class
   targets. The new `MediaTypeOrExtentShape` observation in step 1
   above is the same gap, second instance.

2. **Inverse-path SHACL constraint** on `DatasetSeries` (`sh:path [
   sh:inversePath dcat:inSeries ]`) — `SlotDefinition` has an `inverse`
   field (declares the reciprocal slot) but no metaslot translates to a
   `sh:inversePath` property shape. Not closed this run.

3. **`sh:severity sh:Warning` (or anything below Violation)** — no
   slot/class metaslot found in current `linkml_runtime.linkml_model.meta`
   (grepped for `severity` / `shacl` in `SlotDefinition` fields).

4. **`sh:nodeKind sh:IRI`** — LinkML's gen-shacl emits
   `sh:BlankNodeOrIRI` for every object-valued slot; no metaslot in
   the current main lets a slot demand IRI-only.

5. **`rdf:langString` first-class type** — language-tagged literals
   (`@language`) are still mapped to plain `xsd:string`. DCAT-AP relies
   on language tags for `dct:title`, `dct:description`, etc.

6. **Per-shape property reification.** Upstream factors every constraint
   into its own property shape and references them via
   `sh:property <IRI>` (e.g.
   `<#dcat:CatalogRecordShape/06293…> sh:minCount 1 ; sh:path dct:title`).
   LinkML inlines all constraints into anonymous blank-node property
   shapes inside the parent NodeShape. Functionally equivalent;
   structurally different. Probably not worth chasing for the
   evaluation.

7. **`time:Instant` class missing.** Upstream emits `TimeInstantShape`
   targeting `time:Instant`; we model `beginning` / `end` as `string`.
   A `TimeInstant` class with `class_uri: time:Instant` would close
   this — schema-side fix, not a LinkML gap.

## Datatype disjunction (status: partial gap, no change)

Still partial. The SHACL `sh:or` over `xsd:date | xsd:dateTime |
xsd:gYear | xsd:gYearMonth` round-trips correctly via LinkML `any_of`
and the custom `gYear`/`gYearMonth` types. JSON Schema, Pydantic, and
dataclasses still flatten or collapse the disjunction (no change since
the previous run). See "Custom datatypes" below.

### Custom datatypes (`xsd:gYear`, `xsd:gYearMonth`)

To express the DCAT-AP date disjunction we added two custom types to
the schema's `types:` section (verbatim from the previous run, repeated
for completeness):

```yaml
gYear:
  uri: xsd:gYear
  base: str
gYearMonth:
  uri: xsd:gYearMonth
  base: str
```

Quirks observed (unchanged):

- `base: str` is the only practical option — LinkML doesn't ship Python
  representations for partial-date XSD types.
- The `uri:` is preserved correctly into SHACL (`sh:datatype xsd:gYear`)
  and JSON-LD context output.
- `pythongen` and `pydanticgen` reduce these custom types to `str`,
  collapsing the union to `Union[date, datetime, str]` at the Python
  level. The disjunction is preserved in `json_schema_extra` metadata
  but not in the type signature.

## What LinkML produces but the original doesn't

1. **Extra `NodeShape` declarations for range/value classes** (e.g.
   `dct:Frequency`, `vcard:Kind`, `eli:LegalResource`, `prov:Activity`),
   most of them empty. Harmless but verbose — upstream is more
   restrained about what it shapes.

2. **`sh:class` ranges on object-valued slots.** Original is largely
   silent on the *type* of related resources, relying on
   `sh:nodeKind`; the generated SHACL is more explicit, e.g.
   `sh:class dcat:Catalog` for `dct:hasPart` on Catalogue. Useful
   addition.

3. **`sh:order`** — LinkML emits ordering hints absent from the
   original.

4. **`sh:description`** taken from the slot's description — original
   shapes don't carry per-property descriptions.

## Surprising matches

1. **All 15 SHACL target classes are reproduced with the correct
   IRIs.** Prefix configuration alone was enough to make the IRIs
   round-trip.

2. **Cardinalities match almost exactly.** Where the SHACL says `(0,1)`
   or `(1,*)`, LinkML's `multivalued` / `required` / `slot_usage`
   reproduce it correctly; the previously-flagged `dct:rights` mismatch
   resolved this run.

3. **`xsd:hexBinary` and `xsd:nonNegativeInteger` round-trip.** Custom
   LinkML types map cleanly to the right XSD datatype in both SHACL
   and OWL.

4. **Datatype-vs-IRI distinction** works: `dcat:keyword` and
   `dct:identifier` come out as `sh:Literal`; object-valued slots like
   `dct:publisher` come out as `sh:BlankNodeOrIRI`.

5. **Prefix round-trip:** SPDX, ADMS, FOAF, ODRL, ELI, time, vcard
   prefixes all round-trip intact.

## Closed in this run (and how)

| Gap | Resolution |
|---|---|
| `_Shape`-suffixed shape IRIs | `gen-shacl --suffix Shape` (new flag) wired via `config.yaml` `shacl.suffix: Shape` |
| Open shapes actually applied | `gen-shacl --non-closed` wired via `config.yaml` `shacl.closed: false` (the previous run claimed this was wired, but it wasn't) |
| OWL class IRIs based on `class_uri` (e.g. `dcat:Catalog` not `dcat_ap:Catalogue`) | `gen-owl --no-use-native-uris` wired via `config.yaml` `owl.use_native_uris: false` |
| `dct:rights` cardinality on Catalogue | Already addressed in the schema via `Catalogue.slot_usage.rights.multivalued: false`; SHACL output now matches |

## Suggestions for future LinkML work (SEMIC-relevant)

- **`sh:nodeKind sh:IRI`** — add a slot-level metaslot or a `gen-shacl`
  CLI flag that lets identifier-typed slots demand IRI-only object
  values.
- **`sh:severity`** — slot/class-level severity that gen-shacl honours.
- **`rdf:langString` first-class type** with optional `@language`
  constraint.
- **Class disjunction in slot range** — first-class support for slots
  whose range is a true class union (without requiring a synthetic
  abstract superclass).
- **`sh:inversePath`** — a way to declare an inverse-path constraint
  as a SHACL property shape (separate from the `inverse:` metaslot
  which only declares the reciprocal slot).
