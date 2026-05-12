# Custom XSD datatypes collapse to `str` in Python / Pydantic output

## Context

DCAT-AP's `DateOrDateTimeDataType` allows a date-typed slot to carry
any of `xsd:date | xsd:dateTime | xsd:gYear | xsd:gYearMonth`. LinkML
ships `date` and `datetime` as built-in types but not `gYear` or
`gYearMonth`, so this repo declares them as **custom types** with
explicit `uri:` mappings. The SHACL generator round-trips the
distinction correctly (`sh:or` over four `sh:datatype` branches), but
`pythongen` and `pydanticgen` reduce both custom types to `str`,
losing the distinction at the Python type level.

## Example input

```yaml
types:
  gYear:
    uri: xsd:gYear
    base: str
  gYearMonth:
    uri: xsd:gYearMonth
    base: str

slots:
  releaseDate:
    slot_uri: dct:issued
    any_of:
      - range: date
      - range: datetime
      - range: gYear
      - range: gYearMonth
```

## Expected output

The Python type signature for `releaseDate` should preserve all four
range alternatives, e.g.

```python
releaseDate: Optional[Union[date, datetime, GYear, GYearMonth]] = ...
```

…where `GYear` / `GYearMonth` are some Python wrapper (NewType,
constrained str, dataclass) that preserves the original XSD datatype
identity for round-tripping back into RDF.

## Actual output

`gen-pydantic` deduplicates the custom types — both `gYear` and
`gYearMonth` have `base: str`, so they both collapse to `str`, and the
union becomes `Union[date, datetime, str]`:

```python
releaseDate: Optional[Union[date, datetime , str]] = Field(
    default=None,
    description="...",
    json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'date'},
                                                     {'range': 'datetime'},
                                                     {'range': 'gYear'},
                                                     {'range': 'gYearMonth'}],
                                          ...} })
```

The four-way disjunction survives only as metadata in
`json_schema_extra`. The Python type system sees a three-member union
that cannot distinguish a `gYear` string from a `gYearMonth` string
from any other string.

`gen-python` (dataclasses) is similar: the slot is typed as plain
`str` with string coercion in `__post_init__`.

## Why this matters

Round-tripping data from RDF (where the `xsd:gYear` datatype is
preserved) through Python and back is not safe: the Python layer loses
the datatype identity, so re-serialising the value to RDF either
guesses or defaults to `xsd:string`. For any LinkML-based ETL that
sits between two RDF systems, the date-disjunction round-trip is
broken at the Python boundary even though the SHACL boundary is fine.
