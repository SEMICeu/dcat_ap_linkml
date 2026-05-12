"""Smoke tests for `src/dcat_ap/schema/dcat_ap.yaml`.

These don't validate semantic correctness — they catch schema regressions
that would silently break the downstream generators (a missing class, a
date-disjunction slot whose `any_of` got flattened, etc.).
"""

from pathlib import Path

import pytest
from linkml_runtime.utils.schemaview import SchemaView

SCHEMA_PATH = (
    Path(__file__).resolve().parent.parent
    / "src"
    / "dcat_ap"
    / "schema"
    / "dcat_ap.yaml"
)


@pytest.fixture(scope="module")
def sv() -> SchemaView:
    return SchemaView(str(SCHEMA_PATH))


def test_schema_parses(sv: SchemaView) -> None:
    assert sv.schema.name == "dcat_ap"
    assert sv.schema.id == "https://w3id.org/semic/dcat-ap/3.0.1"


def test_target_classes_present(sv: SchemaView) -> None:
    """The 15 DCAT-AP shape target classes must all be in the schema."""
    expected = {
        "Agent",
        "Catalogue",
        "CatalogueRecord",
        "Checksum",
        "Concept",
        "ConceptScheme",
        "DataService",
        "Dataset",
        "DatasetSeries",
        "Distribution",
        "Identifier",
        "LicenceDocument",
        "Location",
        "PeriodOfTime",
        "Relationship",
    }
    missing = expected - set(sv.all_classes())
    assert not missing, f"Missing classes: {sorted(missing)}"


def test_class_uris_match_dcat_ap(sv: SchemaView) -> None:
    """A spot check that class_uri values point at the upstream IRIs."""
    expected = {
        "Catalogue": "dcat:Catalog",
        "Dataset": "dcat:Dataset",
        "DataService": "dcat:DataService",
        "DatasetSeries": "dcat:DatasetSeries",
        "Distribution": "dcat:Distribution",
        "Checksum": "spdx:Checksum",
        "LicenceDocument": "dct:LicenseDocument",
    }
    for name, uri in expected.items():
        cls = sv.get_class(name)
        assert cls.class_uri == uri, (
            f"{name}.class_uri = {cls.class_uri!r}, expected {uri!r}"
        )


@pytest.mark.parametrize(
    "slot_name",
    ["releaseDate", "modificationDate", "startDate", "endDate", "listingDate"],
)
def test_date_disjunction_slots(sv: SchemaView, slot_name: str) -> None:
    """Date slots must keep the date | datetime | gYear | gYearMonth union."""
    slot = sv.get_slot(slot_name)
    assert slot is not None, f"slot {slot_name!r} missing from schema"
    assert slot.any_of, f"slot {slot_name!r} should use any_of"
    ranges = {alt.range for alt in slot.any_of}
    assert ranges == {"date", "datetime", "gYear", "gYearMonth"}, (
        f"slot {slot_name!r} has any_of ranges {sorted(ranges)}"
    )


def test_custom_xsd_datatypes_declared(sv: SchemaView) -> None:
    """gYear / gYearMonth must be declared as custom types with xsd: URIs."""
    for type_name, uri in [("gYear", "xsd:gYear"), ("gYearMonth", "xsd:gYearMonth")]:
        t = sv.get_type(type_name)
        assert t is not None, f"type {type_name!r} missing"
        assert t.uri == uri, f"{type_name}.uri = {t.uri!r}, expected {uri!r}"
