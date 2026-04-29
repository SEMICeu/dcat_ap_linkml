# Structural comparison: LinkML-generated vs original DCAT-AP 3.0.1

This document compares the LinkML-generated SHACL shapes
(`project/shacl/dcat_ap.shacl.ttl`) against the original SEMIC DCAT-AP 3.0.1
SHACL shapes (`originals/shapes.ttl`).

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

1. **`DateOrDateTimeDataType_Shape`** — the original uses a `sh:or` disjunction
   over `xsd:date`, `xsd:dateTime`, `xsd:gYear`, `xsd:gYearMonth` for date-typed
   slots. LinkML can declare only one type per slot, so generated SHACL emits
   `xsd:string` for `dct:issued`, `dct:modified`, `dcat:startDate`,
   `dcat:endDate`. **Significant semantic loss for date validation.**

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

6. **Open-world shapes** — original SEMIC shapes are *open* (no
   `sh:closed`). LinkML's generator emits `sh:closed true` plus
   `sh:ignoredProperties (rdf:type)`. This will reject any property not
   explicitly in the schema, which is stricter than DCAT-AP intends.

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

2. **`sh:closed true` + `sh:ignoredProperties (rdf:type)`** on every shape —
   makes the shapes much stricter than the original.

3. **`sh:class` ranges on object-valued slots** — the original is largely
   silent on the *type* of related resources (relying on `sh:nodeKind`); the
   generated SHACL is more explicit, e.g. `sh:class dcat:Catalog` for
   `dct:hasPart` on Catalogue. Often a useful addition.

4. **`sh:order`** — LinkML emits ordering hints absent from the original.

5. **`sh:description`** taken from the slot's description — original shapes
   don't carry per-property descriptions.

## Constructs LinkML can't express well (key for SEMIC discussion)

These are the most important gaps for the SEMIC × LinkML evaluation:

1. **Datatype disjunction (`sh:or` over multiple datatypes)** — there is no
   way in LinkML to say "this slot is one of `xsd:date`, `xsd:dateTime`,
   `xsd:gYear`, or `xsd:gYearMonth`". This is the single most impactful gap
   because DCAT-AP uses it pervasively for date-valued properties.

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

6. **Open-shape vs closed-shape control** — at minimum `gen-shacl` should
   support a per-class or schema-wide open/closed flag.

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
- Add `closed_shapes: false` config option (or per-class `closed: false`).
- Make the gen-shacl generator honour `class_uri` for the *shape IRI* (or at
  least add a `_Shape` suffix to a configurable IRI base) so DCAT-AP shape
  IRIs can be reproduced exactly.
- Support for `sh:severity` levels.
- First-class language-tagged-string type with optional `@language`
  constraint.
