# No way to emit a SHACL `sh:inversePath` property shape

## Context

Earlier DCAT-AP drafts (and many SHACL profiles that constrain
relationships from the "other side") use property shapes with
`sh:path [ sh:inversePath <prop> ]` to require that a resource be
referenced from elsewhere. Example pattern (here applied conceptually
to `dcat:DatasetSeries`, requiring that at least one
`dcat:Dataset` link to it via `dcat:inSeries`):

```turtle
[] sh:targetClass dcat:DatasetSeries ;
   sh:property [
       sh:path [ sh:inversePath dcat:inSeries ] ;
       sh:minCount 1 ;
   ] .
```

LinkML's `SlotDefinition` has an `inverse:` metaslot, but it declares
the *reciprocal slot*; it does not translate to a SHACL property shape
with `sh:inversePath`.

## Example input

```yaml
classes:
  Dataset:
    class_uri: dcat:Dataset
    slots: [inSeries]
  DatasetSeries:
    class_uri: dcat:DatasetSeries
    slots: [datasetInSeries]

slots:
  inSeries:
    slot_uri: dcat:inSeries
    range: DatasetSeries
  datasetInSeries:
    # "this DatasetSeries must be referenced from at least one Dataset
    #  via dcat:inSeries" — i.e. an inverse-path constraint.
    inverse: inSeries
    required: true
```

## Expected output

A SHACL property shape on `dcat:DatasetSeries` using `sh:inversePath`:

```turtle
dcat:DatasetSeriesShape sh:property [
    sh:path [ sh:inversePath dcat:inSeries ] ;
    sh:minCount 1 ;
] .
```

## Actual output

The generated `dcat:DatasetSeriesShape` contains the regular property
constraints for the slots declared on `DatasetSeries`, but no
`sh:inversePath` property shape is emitted for `datasetInSeries` (or
for any slot that uses `inverse:`):

```turtle
dcat:DatasetSeriesShape a sh:NodeShape ;
    sh:closed false ;
    sh:property [ ... regular forward-direction constraints ... ] ;
    sh:targetClass dcat:DatasetSeries .
```

There is no slot-level metaslot that drives the SHACL generator to emit
an `sh:inversePath`-based property shape.

## Why this matters

When the target SHACL profile constrains a class via inbound references
(rather than outbound properties), LinkML can only declare the
forward slot — the constraint that "instances of class X must be the
target of at least one Y" cannot be expressed. The validation
guarantee is lost: data with a `DatasetSeries` that nothing references
will validate against our generated SHACL but would (in profiles that
use `sh:inversePath`) fail upstream.
