# Language-tagged literals (`rdf:langString`) are not a first-class type

## Context

DCAT-AP titles, descriptions, and similar human-readable strings are
expected to be language-tagged literals (`rdf:langString`) so that
catalogues can carry multilingual metadata. The upstream SHACL
expresses this permissively — properties like `dct:title` and
`dct:description` are constrained to `sh:nodeKind sh:Literal` with
**no `sh:datatype`** at all, allowing both plain `xsd:string` and
`rdf:langString`. LinkML's `string` primitive maps strictly to
`xsd:string`, and the SHACL generator emits `sh:datatype xsd:string`,
which is stricter than the source.

## Example input

```yaml
classes:
  Catalogue:
    class_uri: dcat:Catalog
    slots: [title]
    slot_usage:
      title: { required: true, multivalued: true }

slots:
  title:
    slot_uri: dct:title
    range: string         # only LinkML primitive for textual content
    multivalued: true
```

There is no built-in `langString` type and no slot/type-level metaslot
to declare a slot as "any literal, language tag optional".

## Expected output

A SHACL property shape matching the upstream constraint — no
`sh:datatype`, language-tagged literals accepted:

```turtle
[ sh:path dct:title ;
  sh:nodeKind sh:Literal ;
  sh:minCount 1 ] .
```

(Equivalent upstream form, from
`original/releases/3.0.1/shacl/dcat-ap-SHACL.ttl`:
`shacl:nodeKind shacl:Literal ; shacl:path dc:title .`)

## Actual output

```turtle
[ sh:datatype xsd:string ;
  sh:description "A name given to the resource." ;
  sh:minCount 1 ;
  sh:nodeKind sh:Literal ;
  sh:order 0 ;
  sh:path dct:title ]
```

The `sh:datatype xsd:string` clause forbids language-tagged literals:
under SHACL semantics, a value `"Open Data Catalogue"@en` (an
`rdf:langString`) is rejected by `sh:datatype xsd:string`.

## Why this matters

Multilingual metadata is a core requirement for European data
catalogues, and DCAT-AP relies on language-tagged literals throughout.
Our generated shapes will reject perfectly valid multilingual data, so
SHACL validation against the LinkML-derived shapes is not a faithful
substitute for validation against the SEMIC originals. There is also
no way for downstream code (Pydantic models, JSON-Schema validators)
to express "language-tagged string" as a type.
