# Structural comparison: LinkML-generated vs original DCAT-AP 3.0.1

This document compares the LinkML-generated SHACL shapes
(`project/shacl/dcat_ap.shacl.ttl`) against the original SEMIC DCAT-AP 3.0.1
SHACL shapes (`original/releases/3.0.1/shacl/dcat-ap-SHACL.ttl`).

> **Note on the snapshot.** The figures below were produced against an earlier
> local snapshot of the SEMIC SHACL file that carried the
> `releases/3.0.0/.../shapes.ttl` namespace (essentially the 3.0.0 shapes
> labelled as 3.0.1). Now that the full upstream repository is available under
> `original/`, the 3.0.1 SHACL is materially larger (~2200 lines vs ~750) and
> the headline shape/property counts in this table should be re-derived. The
> *qualitative* observations (matching target classes, the date-disjunction
> gap, etc.) still hold; the numeric ones need a refresh.

## Headline numbers

| Metric                                    | Original | Generated |
|-------------------------------------------|----------|-----------|
| `sh:NodeShape` declarations               | 17       | 32        |
| Shapes with `sh:targetClass`              | 15       | 32        |
| Auxiliary disjunction shapes (`sh:or`)    | 2        | 0         |
| Distinct property paths used              | ~62      | ~63       |

The generated SHACL has more shapes because LinkML emits a `NodeShape` for
every class in the schema (including ones used purely as ranges in DCAT-AP,
e.g. `dct:Frequency`, `vcard:Kind`, `prov:Activity`). The original only
declares shapes for the 15 main DCAT-AP classes plus two helper shapes.

## What matched

All **15 shape target classes** in the original have corresponding generated
shapes with identical IRIs (modulo the `_Shape` suffix on the shape IRI itself):

```
adms:Identifier      ✓
dcat:Catalog         ✓
dcat:CatalogRecord   ✓
dcat:DataService     ✓
dcat:Dataset         ✓
dcat:DatasetSeries   ✓
dcat:Distribution    ✓
dcat:Relationship    ✓
dct:LicenseDocument  ✓
dct:Location         ✓
dct:PeriodOfTime     ✓
foaf:Agent           ✓
skos:Concept         ✓
skos:ConceptScheme   ✓
spdx:Checksum        ✓
```

### Sampled shape diff: `dcat:Catalog`

| Property path                | Original (min, max)        | Generated (min, max) | Note |
|------------------------------|----------------------------|----------------------|------|
| `dct:title`                  | (1, ∞)                     | (1, ∞)               | match |
| `dct:description`            | (1, ∞)                     | (1, ∞)               | match |
| `dct:publisher`              | (1, 1)                     | (1, 1)               | match |
| `dct:creator`                | (0, 1)                     | (0, 1)               | match |
| `dct:license`                | (0, 1)                     | (0, 1)               | match |
| `foaf:homepage`              | (0, 1)                     | (0, 1)               | match |
| `dct:issued`                 | (0, 1)                     | (0, 1)               | match |
| `dct:modified`               | (0, 1)                     | (0, 1)               | match |
| `dct:rights`                 | (0, 1)                     | (0, ∞)               | **mismatch** — original maxCount 1 |
| `dcat:catalog`               | (0, ∞)                     | (0, ∞)               | match |
| `dcat:dataset`               | (0, ∞)                     | (0, ∞)               | match |
| `dcat:service`               | (0, ∞)                     | (0, ∞)               | match |
| `dcat:record`                | (0, ∞)                     | (0, ∞)               | match |
| `dcat:themeTaxonomy`         | (0, ∞)                     | (0, ∞)               | match |
| `dcatap:applicableLegislation` | (0, ∞), nodeKind IRI    | (0, ∞), nodeKind BlankNodeOrIRI | nodeKind looser |
| `dct:language`               | (0, ∞)                     | (0, ∞)               | match |
| `dct:spatial`                | (0, ∞)                     | (0, ∞)               | match |
| `dct:hasPart`                | (0, ∞)                     | (0, ∞)               | match |

### Sampled shape diff: `spdx:Checksum`

| Property              | Original                  | Generated                 |
|-----------------------|---------------------------|---------------------------|
| `spdx:algorithm`      | (1, 1)                    | (1, 1) + class range      |
| `spdx:checksumValue`  | (1, 1) datatype hexBinary | (1, 1) datatype hexBinary |

Match plus an extra `sh:class` constraint in generated (LinkML knows the range
class and emits it).

### Sampled shape diff: `adms:Identifier`

| Property         | Original | Generated |
|------------------|----------|-----------|
| `skos:notation`  | (0, 1)   | (0, 1)    |

Exact match.

## What's missing in the LinkML version

1. ~~**`DateOrDateTimeDataType_Shape`**~~ — *resolved.* Originally noted as a
   gap; the latest revision uses LinkML `any_of` plus custom `gYear` /
   `gYearMonth` types, and the SHACL generator emits an inlined `sh:or` with
   all four datatype branches for `dct:issued`, `dct:modified`,
   `dcat:startDate`, `dcat:endDate`. See "Datatype disjunction" below for the
   detailed experimental result.

2. **`DcatResource_Shape`** — the original `sh:or` over `dcat:Catalog |
   dcat:Dataset | dcat:DataService | dcat:DatasetSeries` becomes an abstract
   `CataloguedResource` superclass in LinkML. The SHACL output therefore uses
   `sh:class dcat:Resource` instead of the original disjunction.

3. **Inverse-path constraint** on `DatasetSeries`
   (`sh:path [ sh:inversePath dcat:inSeries ]`) — not emitted, no LinkML
   construct exists for this.

4. **`sh:severity sh:Warning`** — the warning-level severity used on the
   inverse-path shape isn't supported. All generated shapes are
   `sh:Violation`.

5. **`sh:nodeKind sh:IRI` distinction** — the original uses `sh:IRI` (no blank
   nodes allowed) for some properties (e.g.
   `dcatap:applicableLegislation`, `dcat:theme`). LinkML's generator emits
   `sh:BlankNodeOrIRI` for all object-valued slots.

6. **Open-world shapes** — *not a gap; CLI flag handles it.* Original
   SEMIC shapes are *open* (no `sh:closed`). Default `gen-shacl`
   output is closed. The bundled SHACL in `project/shacl/` is now
   generated with `--non-closed`, so every shape carries
   `sh:closed false` — matching the SEMIC semantics. Mixin and
   abstract classes already get `sh:closed false` even in default
   mode (see `shaclgen.py:488-493`). The only residual question is
   per-class override, which is tracked upstream as
   [linkml/linkml#1249](https://github.com/linkml/linkml/issues/1249).
   Don't file a duplicate.

7. **Specific SHACL `rdfs:label` and `_Shape`-suffixed IRIs** —
   the original has e.g. `:Catalog_Shape rdfs:label "Catalog"@en`. LinkML
   generates a shape whose IRI *is* the target class IRI, with a
   `rdfs:comment` taken from the slot description. The labels and shape IRIs
   are not reproduced.

8. **Multilingual literals (`@language`)** — DCAT-AP expects
   language-tagged literals for `dct:title`, `dct:description`, etc. The
   JSON-LD context uses `@container: "@set"` with no `@type` constraint,
   implying language-tagged strings are valid. LinkML's generator types these
   as plain `xsd:string`.

## What LinkML produces but the original doesn't

1. **17 extra `NodeShape` declarations** for range/value classes
   (e.g. `dct:Frequency`, `vcard:Kind`, `eli:LegalResource`, `prov:Activity`),
   most of them empty (no constraints). Harmless but verbose.

2. ~~**`sh:closed true` + `sh:ignoredProperties (rdf:type)`** on every shape — makes the shapes much stricter than the original.~~
   *Resolved.* The SHACL in `project/shacl/` is now generated with
   `--non-closed`, so every shape is `sh:closed false`. (Default
   `gen-shacl` is closed; the flag toggles it.)

3. **`sh:class` ranges on object-valued slots** — the original is largely
   silent on the *type* of related resources (relying on `sh:nodeKind`); the
   generated SHACL is more explicit, e.g. `sh:class dcat:Catalog` for
   `dct:hasPart` on Catalogue. Often a useful addition.

4. **`sh:order`** — LinkML emits ordering hints absent from the original.

5. **`sh:description`** taken from the slot's description — original shapes
   don't carry per-property descriptions.

## Constructs LinkML can't express well (key for SEMIC discussion)

These are the most important gaps for the SEMIC × LinkML evaluation:

1. **Datatype disjunction (`sh:or` over multiple datatypes)** — *partial gap.*
   LinkML supports type disjunctions via `any_of`:

   ```yaml
   slots:
     event_date:
       any_of:
         - range: date
         - range: datetime
   ```

   The SHACL generator translates `any_of` → `sh:or`, so the round-trip works
   for date/datetime. However:
   - `xsd:gYear` and `xsd:gYearMonth` are **not built-in** LinkML types
     (only `date`, `datetime`, `date_or_datetime`, `time` are). Custom types
     with explicit `uri: xsd:gYear` are required, and downstream generators
     (JSON Schema, Pydantic, Python dataclasses) may not handle them cleanly.
   - **Generator coverage is uneven**: SHACL handles `any_of` well, but
     pythongen, JSON Schema, and others tend to pick a single range or
     flatten the union.

   Net: expressible syntactically; the gap is narrower than "can't express it"
   but real — the issue is custom XSD datatype support and inconsistent
   generator handling, not the meta-modelling primitive.

   **Experimental result (this project).** We replaced
   `range: datetime` on `releaseDate` (`dct:issued`),
   `modificationDate` (`dct:modified`), `listingDate` (`dct:issued` on
   `dcat:CatalogRecord`), `startDate` and `endDate` with an `any_of` over
   `date | datetime | gYear | gYearMonth` (the latter two declared as
   custom types — see "Custom datatypes" below) and re-ran `gen-project`.
   Observed behaviour:
   - **SHACL** (`project/shacl/dcat_ap.shacl.ttl`): `sh:or` is emitted with
     all four `sh:datatype` branches plus `sh:nodeKind sh:Literal` on each.
     Structurally this is **equivalent** to the original
     `:DateOrDateTimeDataType_Shape` `sh:or` block, just inlined into each
     property shape rather than referenced via `sh:node` / `sh:shape`. Net
     semantic content matches the original.
   - **JSON Schema** (`project/jsonschema/dcat_ap.schema.json`): the slot
     becomes a JSON Schema `anyOf` with four branches — `format: "date"`,
     `format: "date-time"`, and two plain `type: "string"` (for `gYear` and
     `gYearMonth`, since JSON Schema has no `format` for those). Validation
     is therefore weaker for `gYear`/`gYearMonth` than for date/dateTime.
   - **Pydantic** (`src/dcat_ap/datamodel/dcat_ap_pydantic.py`): the slot is
     typed as `Union[date, datetime, str]` (deduplicated — both custom
     `gYear` and `gYearMonth` collapse to `str`). The original `any_of`
     metadata is preserved in `json_schema_extra`.
   - **Python dataclasses** (`src/dcat_ap/datamodel/dcat_ap.py`):
     pythongen flattens to plain `str` and adds string-coercion in
     `__post_init__`. The disjunction is lost at the type level.

   So the SHACL round-trip *is* faithful for this DCAT-AP construct; the
   degradation lives in the JSON-and-Python-shaped end of the toolchain,
   not in the SHACL output.

### Custom datatypes (`xsd:gYear`, `xsd:gYearMonth`)

To express the DCAT-AP date disjunction we added two custom types to the
schema's `types:` section:

```yaml
gYear:
  uri: xsd:gYear
  base: str
  description: An XSD gYear literal …

gYearMonth:
  uri: xsd:gYearMonth
  base: str
  description: An XSD gYearMonth literal …
```

Quirks observed:
- `base: str` is the only practical option — LinkML doesn't ship Python
  representations for partial-date XSD types, so values flow through as
  strings.
- The `uri:` is preserved correctly into SHACL (`sh:datatype xsd:gYear`)
  and JSON-LD context output.
- pythongen and pydanticgen both reduce these custom types to `str` (they
  don't introspect the `uri:` to pick a richer type), so two distinct
  custom types collapse into a single `str` member of the union — losing
  the distinction between `gYear` and `gYearMonth` at the Python level.
- gen-typescript prints a `WARNING: Unknown type.base: decimal` (unrelated
  to our changes — pre-existing on `decimal`) but otherwise emits
  `string` for the new types, as expected.

2. **Class disjunction in property ranges** — LinkML requires a single named
   range. DCAT-AP's `DcatResource` (union of four classes) has to be
   emulated by introducing a synthetic abstract superclass, which then
   ripples into the OWL/RDF semantics in ways the original doesn't have.

3. **Inverse path constraints** — SHACL property paths with `sh:inversePath`
   aren't representable as LinkML slots.

4. **`sh:severity sh:Warning` (or any severity below Violation)** — LinkML's
   generator can't distinguish constraint levels.

5. **`sh:nodeKind sh:IRI` (no blank nodes)** — LinkML's gen-shacl always
   emits `BlankNodeOrIRI` for object-valued slots; the stricter "must be an
   IRI" constraint isn't expressible.

6. **Open-shape vs closed-shape control** — *already supported.*
   `gen-shacl` has a `--closed/--non-closed` CLI flag (or
   `shacl: { closed: false }` in the gen-project config). The bundled
   SHACL is now built with `--non-closed`. Mixin/abstract classes
   already get `sh:closed false` automatically. Per-class
   override is the only remaining open question, tracked upstream as
   [linkml/linkml#1249](https://github.com/linkml/linkml/issues/1249).

7. **Language-tagged-string as a first-class type** — DCAT-AP relies on
   `rdf:langString`. LinkML maps everything to `xsd:string`.

## Surprising matches

1. **All 15 SHACL target classes are reproduced with the correct IRIs.** The
   prefix configuration alone was enough to make the IRIs round-trip.

2. **Cardinalities match exactly** for the vast majority of properties. Where
   the SHACL says `(0,1)` or `(1,*)`, LinkML's `multivalued` and `required`
   reproduce it correctly.

3. **`xsd:hexBinary` and `xsd:nonNegativeInteger` round-trip.** Custom LinkML
   types map cleanly to the right XSD datatype in both SHACL and OWL.

4. **Datatype-vs-IRI distinction** mostly works: `dcat:keyword` and
   `dct:identifier` correctly come out as `sh:Literal`, while object-valued
   slots like `dct:publisher` correctly come out as `sh:BlankNodeOrIRI`.

5. **SPDX, ADMS, FOAF, ODRL, ELI, time, vcard prefixes** all round-trip
   intact — the generated SHACL uses the same prefix declarations the
   original does.

## Suggestions for future LinkML work (SEMIC-relevant)

- Add `sh_or_datatypes` (or similar) annotation that lets a slot declare a
  union of acceptable XSD datatypes, generating `sh:or`.
- Make the gen-shacl generator honour `class_uri` for the *shape IRI* (or at
  least add a `_Shape` suffix to a configurable IRI base) so DCAT-AP shape
  IRIs can be reproduced exactly.
- Support for `sh:severity` levels.
- First-class language-tagged-string type with optional `@language`
  constraint.
