# Object-valued slots cannot demand `sh:nodeKind sh:IRI`

## Context

SHACL distinguishes `sh:IRI` (named-resource only), `sh:BlankNode`,
and `sh:BlankNodeOrIRI`. Some application profiles forbid blank
nodes for specific properties — e.g. controlled-vocabulary references
like `dcat:theme` or `dcatap:applicableLegislation` are expected to
point at dereferenceable IRIs, not anonymous nodes. LinkML has no
slot-level metaslot for `nodeKind`: every object-valued slot becomes
`sh:nodeKind sh:BlankNodeOrIRI` in the generated SHACL.

## Example input

```yaml
classes:
  Catalogue:
    class_uri: dcat:Catalog
    slots: [applicableLegislation]

slots:
  applicableLegislation:
    slot_uri: dcatap:applicableLegislation
    range: LegalResource
    multivalued: true
    # We would like to say: value MUST be an IRI, not a blank node.
    # No metaslot exists.
```

(There is no `node_kind:` / `iri_only:` / `shacl_node_kind:` field on
`SlotDefinition` — verified by grepping
`dataclasses.fields(SlotDefinition)` for `kind` and `iri`.)

## Expected output

```turtle
[ sh:path dcatap:applicableLegislation ;
  sh:class eli:LegalResource ;
  sh:nodeKind sh:IRI ] .
```

## Actual output

Generated SHACL emits `sh:BlankNodeOrIRI` for every object-valued slot,
regardless of the underlying semantics:

```turtle
[ sh:class eli:LegalResource ;
  sh:description "The legislation applicable to the resource (DCAT-AP extension)." ;
  sh:nodeKind sh:BlankNodeOrIRI ;
  sh:path dcatap:applicableLegislation ]
```

## Why this matters

For controlled-vocabulary properties (themes, legislation references,
licences, …) the difference between "must be an IRI" and "may be a
blank node" is the difference between "URI you can resolve and reuse"
and "anonymous node that no other system can reference". Generated
shapes are looser than the source profile, so data that should fail
upstream validation passes ours.
