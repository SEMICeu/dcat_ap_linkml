# DCAT-AP 3.0.1 LinkML approximation — notes

## Scope

This is a **scoping/demo schema** built for the SEMIC × LinkML evaluation. The
goal is to produce SHACL, OWL/RDF, and JSON-LD outputs that approximate the
SEMIC DCAT-AP 3.0.1 artefacts at
<https://semiceu.github.io/DCAT-AP/releases/3.0.1/>, not to deliver a production
specification.

## Source artefacts (in `originals/`)

- `originals/dcat-ap.jsonld` — JSON-LD context (authoritative for property names
  and types in the JSON-LD serialisation)
- `originals/shapes.ttl` — SHACL shapes (authoritative for class membership and
  constraints)
- `originals/index.html` — HTML reference

The SHACL shapes were treated as the primary source of truth for class- and
property-level constraints (cardinalities, datatypes, node kinds). The JSON-LD
context provided the property naming convention used by DCAT-AP (e.g.
`releaseDate` for `dct:issued`, `licence` for `dct:license`).

## Classes captured (15 classes with shapes + 17 supporting / range classes)

Direct equivalents of the 15 SHACL `sh:targetClass` shapes:

- `Agent` (foaf:Agent)
- `Catalogue` (dcat:Catalog)
- `CatalogueRecord` (dcat:CatalogRecord)
- `Checksum` (spdx:Checksum)
- `Concept` (skos:Concept)
- `ConceptScheme` (skos:ConceptScheme)
- `DataService` (dcat:DataService)
- `Dataset` (dcat:Dataset)
- `DatasetSeries` (dcat:DatasetSeries)
- `Distribution` (dcat:Distribution)
- `Identifier` (adms:Identifier)
- `LicenceDocument` (dct:LicenseDocument)
- `Location` (dct:Location)
- `PeriodOfTime` (dct:PeriodOfTime)
- `Relationship` (dcat:Relationship)

Supporting classes (used as ranges, no constraint shape in original):
`Resource`, `CataloguedResource`, `ChecksumAlgorithm`, `Document`, `Frequency`,
`Geometry`, `Kind`, `LegalResource`, `LinguisticSystem`, `MediaType`, `Policy`,
`ProvenanceStatement`, `RightsStatement`, `Role`, `Standard`, `Activity`,
`Attribution`.

## What was deliberately not captured

- `DateOrDateTimeDataType_Shape` — original is a `sh:or` over four xsd date
  types (`xsd:date`, `xsd:dateTime`, `xsd:gYear`, `xsd:gYearMonth`). LinkML can
  declare a single primary type per slot, so date-typed slots are typed as
  plain `string` (which results in `xsd:string` in generated SHACL). See
  COMPARISON.md.
- `DcatResource_Shape` — `sh:or` over `dcat:Catalog | dcat:Dataset |
  dcat:DataService | dcat:DatasetSeries`. We model this with an abstract
  `CataloguedResource` class (range of `primaryTopic`). LinkML can't currently
  express a class union directly in a property range.
- The inverse-path warning shape on `DatasetSeries`
  (`sh:path [ sh:inversePath dcat:inSeries ]`) — not expressible as a slot in
  LinkML.
- The `sh:severity sh:Warning` distinction — LinkML has no equivalent; all
  generated shapes are violations.
- Multilingual literal handling (`@language` containers) — LinkML lacks a
  first-class language-tagged-string type; modelled as plain strings.
- `sh:nodeKind sh:IRI` vs `sh:BlankNodeOrIRI` distinction — LinkML's generator
  always emits `sh:BlankNodeOrIRI` for object-valued slots regardless of source
  intent.
- Most controlled-vocabulary value sets (Frequency, Theme, MediaType from EU
  Publications Office vocabularies) — the original DCAT-AP recommends but does
  not enforce specific code lists, and LinkML enums weren't added to keep the
  schema compact.

## Layout decisions

- Schema ID: `https://w3id.org/semic/dcat-ap/3.0.1`. Not registered. Use
  configure-w3id if/when this is to be promoted.
- Class names follow DCAT-AP English-language naming where it differs from
  the underlying URI (e.g. `Catalogue` for `dcat:Catalog`, `LicenceDocument`
  for `dct:LicenseDocument`).
- Slot URIs use the same property names as the JSON-LD context (e.g.
  `releaseDate` mapped to `dct:issued`).

## Known limitations of the approximation

- All datatype slots emit `xsd:string` even when the original SHACL specifies
  `xsd:dateTime` or member of the date-disjunction.
- LinkML's `gen-shacl` always closes shapes (`sh:closed true`); the original
  SEMIC shapes are open. This is generator behaviour, not an inherent
  limitation — could be tuned with config.
- Identifier shapes use the LinkML schema's default IRI patterns; exact IRIs
  for the SEMIC namespace `https://semiceu.github.io/DCAT-AP/...#XXX_Shape`
  are not reproduced (and would require post-processing).
