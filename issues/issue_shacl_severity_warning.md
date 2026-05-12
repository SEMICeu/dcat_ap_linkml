# No way to declare SHACL `sh:severity` below `sh:Violation`

## Context

SHACL distinguishes three severity levels: `sh:Info`, `sh:Warning`,
`sh:Violation`. Application profiles use this to express "you really
should do X, but failing to do so doesn't invalidate the data" —
e.g. recommended-but-not-required cardinality. LinkML's
`SlotDefinition` / `ClassDefinition` carry `required`, `recommended`,
`minimum_cardinality`, etc. but nothing that maps to `sh:severity`.

## Example input

```yaml
classes:
  Dataset:
    class_uri: dcat:Dataset
    slots: [contactPoint]

slots:
  contactPoint:
    slot_uri: dcat:contactPoint
    recommended: true        # we'd like this to surface as sh:Warning
                             # rather than sh:Violation
    range: Kind
```

(There is no `severity:` metaslot in current
`linkml_runtime.linkml_model.meta.SlotDefinition` —
verified by grepping `dataclasses.fields(SlotDefinition)` for
`severity` and `shacl`.)

## Expected output

The generated property shape should carry `sh:severity sh:Warning`
(or `sh:Info`) when the schema author marks the constraint as
non-blocking:

```turtle
[ sh:path dcat:contactPoint ;
  sh:minCount 1 ;
  sh:severity sh:Warning ] .
```

## Actual output

No `sh:severity` is emitted by `gen-shacl`. Every constraint defaults
to `sh:Violation` (SHACL's default severity), so `required: true` and
`recommended: true` produce identical shape output if the
recommendation is wired through cardinality at all.

```turtle
[ sh:datatype xsd:string ;
  sh:minCount 1 ;
  sh:nodeKind sh:Literal ;
  sh:path dct:title ]
# ↑ no sh:severity, same shape regardless of required vs recommended
```

## Why this matters

Application profiles that distinguish "MUST" from "SHOULD" constraints
(common in DCAT-AP-style profiles and most W3C recommendations) cannot
be reproduced through LinkML. The generated SHACL is uniformly stricter
than the source: data that the source intended to flag as a *warning*
will be reported as a *violation* by any SHACL validator running the
generated shapes.
