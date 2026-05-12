# Slot range cannot be a class disjunction

## Context

DCAT-AP defines several properties whose value MUST be one of *N* named
classes — e.g. `foaf:primaryTopic` on `dcat:CatalogRecord` is "a link to
the Dataset, Data service or Catalog described in the record" (the union
`Catalog | Dataset | DataService | DatasetSeries`, named `dcat:Resource`
upstream), and `dct:format` ranges over `dct:MediaTypeOrExtent`
(the union `MediaType | Extent`). In LinkML, a slot's `range:` accepts
exactly one class name; there is no way to declare a disjunction
directly.

## Example input

```yaml
classes:
  Catalogue:        { class_uri: dcat:Catalog }
  Dataset:          { class_uri: dcat:Dataset }
  DataService:      { class_uri: dcat:DataService }
  DatasetSeries:    { class_uri: dcat:DatasetSeries }

slots:
  primaryTopic:
    slot_uri: foaf:primaryTopic
    # We would like to express: range is one of
    # {Catalogue, Dataset, DataService, DatasetSeries}
    range: ???                       # LinkML accepts only a single name
```

The workaround used in this repo is to introduce an abstract umbrella
class that the four candidate classes inherit from:

```yaml
classes:
  CataloguedResource:
    class_uri: dcat:Resource
    abstract: true
  Catalogue:     { is_a: CataloguedResource, class_uri: dcat:Catalog }
  Dataset:       { is_a: CataloguedResource, class_uri: dcat:Dataset }
  DataService:   { is_a: CataloguedResource, class_uri: dcat:DataService }
  DatasetSeries: { is_a: CataloguedResource, class_uri: dcat:DatasetSeries }

slots:
  primaryTopic:
    slot_uri: foaf:primaryTopic
    range: CataloguedResource
```

## Expected output

Something equivalent to a SHACL disjunction over class targets, e.g.

```turtle
[] sh:path foaf:primaryTopic ;
   sh:or (
       [ sh:class dcat:Catalog ]
       [ sh:class dcat:Dataset ]
       [ sh:class dcat:DataService ]
       [ sh:class dcat:DatasetSeries ]
   ) .
```

…without forcing an artificial abstract superclass that has no
counterpart in the source ontology.

## Actual output

LinkML emits a single `sh:class` pointing at the umbrella class:

```turtle
[ sh:class dcat:Resource ;
  sh:description "The resource described by this catalogue record." ;
  sh:nodeKind sh:BlankNodeOrIRI ;
  sh:path foaf:primaryTopic ]
```

For DCAT-AP 3.0.1 this happens to align with the upstream, because the
upstream itself uses `dcat:Resource` / `dct:MediaTypeOrExtent` as real
umbrella classes. But the LinkML schema is forced to declare
`CataloguedResource` (an abstract class with no counterpart in the
target ontology layout) just to satisfy LinkML's single-range
requirement, and this leaks into the OWL/Pydantic outputs as an extra
class in the inheritance hierarchy.

## Why this matters

When the target ontology genuinely models the disjunction without an
umbrella class — i.e. "this property accepts an A or a B, full stop" —
LinkML forces the schema author to invent one. That polluted class
then shows up in every downstream artefact (OWL hierarchy, Python data
model, JSON-LD context), inflating the schema and obscuring the
original semantics.
