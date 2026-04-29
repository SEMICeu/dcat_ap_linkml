# Auto generated from dcat_ap.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-04-29T14:49:42
# Schema: dcat_ap
#
# id: https://w3id.org/semic/dcat-ap/3.0.1
# description: A LinkML approximation of the SEMIC DCAT-AP 3.0.1 specification. This schema captures the core classes and properties of DCAT-AP 3.0.1 as defined by the SHACL shapes at https://semiceu.github.io/DCAT-AP/releases/3.0.1/html/shacl/shapes.ttl and the JSON-LD context at https://semiceu.github.io/DCAT-AP/releases/3.0.1/context/dcat-ap.jsonld This is a SCOPING/DEMO schema, not a production specification. Some constructs (e.g. property-level disjunction shapes, sh:or with multiple datatypes, inverse paths) are not directly expressible in LinkML and are approximated or omitted.
# license: CC-BY-4.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Decimal, Integer, String
from linkml_runtime.utils.metamodelcore import Decimal

metamodel_version = "1.7.0"
version = None

# Namespaces
ADMS = CurieNamespace('adms', 'http://www.w3.org/ns/adms#')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCAT_AP = CurieNamespace('dcat_ap', 'https://w3id.org/semic/dcat-ap/')
DCATAP = CurieNamespace('dcatap', 'http://data.europa.eu/r5r/')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
ELI = CurieNamespace('eli', 'http://data.europa.eu/eli/ontology#')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LOCN = CurieNamespace('locn', 'http://www.w3.org/ns/locn#')
ODRL = CurieNamespace('odrl', 'http://www.w3.org/ns/odrl/2/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SPDX = CurieNamespace('spdx', 'http://spdx.org/rdf/terms#')
TIME = CurieNamespace('time', 'http://www.w3.org/2006/time#')
VCARD = CurieNamespace('vcard', 'http://www.w3.org/2006/vcard/ns#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = DCAT_AP


# Types
class HexBinary(str):
    """ A hex-binary encoded value. """
    type_class_uri = XSD["hexBinary"]
    type_class_curie = "xsd:hexBinary"
    type_name = "hexBinary"
    type_model_uri = DCAT_AP.HexBinary


class Duration(str):
    """ An XSD duration literal. """
    type_class_uri = XSD["duration"]
    type_class_curie = "xsd:duration"
    type_name = "duration"
    type_model_uri = DCAT_AP.Duration


class NonNegativeInteger(int):
    """ An XSD non-negative integer. """
    type_class_uri = XSD["nonNegativeInteger"]
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "nonNegativeInteger"
    type_model_uri = DCAT_AP.NonNegativeInteger


class GYear(str):
    """ An XSD gYear literal (a Gregorian calendar year, e.g. "2024"). Used in DCAT-AP's DateOrDateTimeDataType disjunction. """
    type_class_uri = XSD["gYear"]
    type_class_curie = "xsd:gYear"
    type_name = "gYear"
    type_model_uri = DCAT_AP.GYear


class GYearMonth(str):
    """ An XSD gYearMonth literal (a Gregorian calendar year and month, e.g. "2024-04"). Used in DCAT-AP's DateOrDateTimeDataType disjunction. """
    type_class_uri = XSD["gYearMonth"]
    type_class_curie = "xsd:gYearMonth"
    type_name = "gYearMonth"
    type_model_uri = DCAT_AP.GYearMonth


# Class references



class Resource(YAMLRoot):
    """
    Top-level abstract resource. Used as a generic node range when the DCAT-AP shape only constrains nodeKind to
    BlankNodeOrIRI/IRI without a specific class.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RDFS["Resource"]
    class_class_curie: ClassVar[str] = "rdfs:Resource"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.Resource


class CataloguedResource(Resource):
    """
    Union of Catalogue, Dataset, DataService, DatasetSeries (a.k.a. dcat:Resource).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Resource"]
    class_class_curie: ClassVar[str] = "dcat:Resource"
    class_name: ClassVar[str] = "CataloguedResource"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.CataloguedResource


@dataclass(repr=False)
class Agent(YAMLRoot):
    """
    An agent (e.g. a person, organisation) responsible for a resource.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF["Agent"]
    class_class_curie: ClassVar[str] = "foaf:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.Agent

    name: Union[str, list[str]] = None
    type: Optional[Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, list):
            self.name = [self.name] if self.name is not None else []
        self.name = [v if isinstance(v, str) else str(v) for v in self.name]

        self._normalize_inlined_as_list(slot_name="type", slot_type=Concept, key_name="preferredLabel", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Catalogue(CataloguedResource):
    """
    A curated collection of metadata about resources (e.g. datasets and data services in the context of a data
    catalogue).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Catalog"]
    class_class_curie: ClassVar[str] = "dcat:Catalog"
    class_name: ClassVar[str] = "Catalogue"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.Catalogue

    title: Union[str, list[str]] = None
    description: Union[str, list[str]] = None
    publisher: Union[dict, Agent] = None
    applicableLegislation: Optional[Union[Union[dict, "LegalResource"], list[Union[dict, "LegalResource"]]]] = empty_list()
    catalogue: Optional[Union[Union[dict, "Catalogue"], list[Union[dict, "Catalogue"]]]] = empty_list()
    creator: Optional[Union[Union[dict, Agent], list[Union[dict, Agent]]]] = empty_list()
    dataset: Optional[Union[Union[dict, "Dataset"], list[Union[dict, "Dataset"]]]] = empty_list()
    geographicalCoverage: Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]] = empty_list()
    hasPart: Optional[Union[Union[dict, "Catalogue"], list[Union[dict, "Catalogue"]]]] = empty_list()
    homepage: Optional[Union[dict, "Document"]] = None
    language: Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]] = empty_list()
    licence: Optional[Union[dict, "LicenceDocument"]] = None
    modificationDate: Optional[str] = None
    record: Optional[Union[Union[dict, "CatalogueRecord"], list[Union[dict, "CatalogueRecord"]]]] = empty_list()
    releaseDate: Optional[str] = None
    rights: Optional[Union[Union[dict, "RightsStatement"], list[Union[dict, "RightsStatement"]]]] = empty_list()
    service: Optional[Union[Union[dict, "DataService"], list[Union[dict, "DataService"]]]] = empty_list()
    temporalCoverage: Optional[Union[Union[dict, "PeriodOfTime"], list[Union[dict, "PeriodOfTime"]]]] = empty_list()
    themes: Optional[Union[Union[dict, "ConceptScheme"], list[Union[dict, "ConceptScheme"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if self._is_empty(self.publisher):
            self.MissingRequiredField("publisher")
        if not isinstance(self.publisher, Agent):
            self.publisher = Agent(**as_dict(self.publisher))

        if not isinstance(self.applicableLegislation, list):
            self.applicableLegislation = [self.applicableLegislation] if self.applicableLegislation is not None else []
        self.applicableLegislation = [v if isinstance(v, LegalResource) else LegalResource(**as_dict(v)) for v in self.applicableLegislation]

        self._normalize_inlined_as_list(slot_name="catalogue", slot_type=Catalogue, key_name="title", keyed=False)

        self._normalize_inlined_as_list(slot_name="creator", slot_type=Agent, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="dataset", slot_type=Dataset, key_name="title", keyed=False)

        if not isinstance(self.geographicalCoverage, list):
            self.geographicalCoverage = [self.geographicalCoverage] if self.geographicalCoverage is not None else []
        self.geographicalCoverage = [v if isinstance(v, Location) else Location(**as_dict(v)) for v in self.geographicalCoverage]

        self._normalize_inlined_as_list(slot_name="hasPart", slot_type=Catalogue, key_name="title", keyed=False)

        if self.homepage is not None and not isinstance(self.homepage, Document):
            self.homepage = Document()

        if not isinstance(self.language, list):
            self.language = [self.language] if self.language is not None else []
        self.language = [v if isinstance(v, LinguisticSystem) else LinguisticSystem(**as_dict(v)) for v in self.language]

        if self.licence is not None and not isinstance(self.licence, LicenceDocument):
            self.licence = LicenceDocument(**as_dict(self.licence))

        if self.modificationDate is not None and not isinstance(self.modificationDate, str):
            self.modificationDate = str(self.modificationDate)

        self._normalize_inlined_as_list(slot_name="record", slot_type=CatalogueRecord, key_name="modificationDate", keyed=False)

        if self.releaseDate is not None and not isinstance(self.releaseDate, str):
            self.releaseDate = str(self.releaseDate)

        if not isinstance(self.rights, list):
            self.rights = [self.rights] if self.rights is not None else []
        self.rights = [v if isinstance(v, RightsStatement) else RightsStatement(**as_dict(v)) for v in self.rights]

        self._normalize_inlined_as_list(slot_name="service", slot_type=DataService, key_name="title", keyed=False)

        if not isinstance(self.temporalCoverage, list):
            self.temporalCoverage = [self.temporalCoverage] if self.temporalCoverage is not None else []
        self.temporalCoverage = [v if isinstance(v, PeriodOfTime) else PeriodOfTime(**as_dict(v)) for v in self.temporalCoverage]

        self._normalize_inlined_as_list(slot_name="themes", slot_type=ConceptScheme, key_name="title", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CatalogueRecord(YAMLRoot):
    """
    A description of a single entry in a data catalogue.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["CatalogRecord"]
    class_class_curie: ClassVar[str] = "dcat:CatalogRecord"
    class_name: ClassVar[str] = "CatalogueRecord"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.CatalogueRecord

    modificationDate: str = None
    primaryTopic: Union[dict, CataloguedResource] = None
    applicationProfile: Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]] = empty_list()
    changeType: Optional[Union[dict, "Concept"]] = None
    description: Optional[Union[str, list[str]]] = empty_list()
    language: Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]] = empty_list()
    listingDate: Optional[str] = None
    sourceMetadata: Optional[Union[dict, "CatalogueRecord"]] = None
    title: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.modificationDate):
            self.MissingRequiredField("modificationDate")
        if not isinstance(self.modificationDate, str):
            self.modificationDate = str(self.modificationDate)

        if self._is_empty(self.primaryTopic):
            self.MissingRequiredField("primaryTopic")
        if not isinstance(self.primaryTopic, CataloguedResource):
            self.primaryTopic = CataloguedResource()

        if not isinstance(self.applicationProfile, list):
            self.applicationProfile = [self.applicationProfile] if self.applicationProfile is not None else []
        self.applicationProfile = [v if isinstance(v, Standard) else Standard(**as_dict(v)) for v in self.applicationProfile]

        if self.changeType is not None and not isinstance(self.changeType, Concept):
            self.changeType = Concept(**as_dict(self.changeType))

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.language, list):
            self.language = [self.language] if self.language is not None else []
        self.language = [v if isinstance(v, LinguisticSystem) else LinguisticSystem(**as_dict(v)) for v in self.language]

        if self.listingDate is not None and not isinstance(self.listingDate, str):
            self.listingDate = str(self.listingDate)

        if self.sourceMetadata is not None and not isinstance(self.sourceMetadata, CatalogueRecord):
            self.sourceMetadata = CatalogueRecord(**as_dict(self.sourceMetadata))

        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Checksum(YAMLRoot):
    """
    A value that allows the contents of a file to be authenticated.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX["Checksum"]
    class_class_curie: ClassVar[str] = "spdx:Checksum"
    class_name: ClassVar[str] = "Checksum"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.Checksum

    algorithm: Union[dict, "ChecksumAlgorithm"] = None
    checksumValue: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.algorithm):
            self.MissingRequiredField("algorithm")
        if not isinstance(self.algorithm, ChecksumAlgorithm):
            self.algorithm = ChecksumAlgorithm()

        if self._is_empty(self.checksumValue):
            self.MissingRequiredField("checksumValue")
        if not isinstance(self.checksumValue, str):
            self.checksumValue = str(self.checksumValue)

        super().__post_init__(**kwargs)


class ChecksumAlgorithm(Resource):
    """
    An algorithm used to produce a checksum.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX["ChecksumAlgorithm"]
    class_class_curie: ClassVar[str] = "spdx:ChecksumAlgorithm"
    class_name: ClassVar[str] = "ChecksumAlgorithm"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.ChecksumAlgorithm


@dataclass(repr=False)
class Concept(YAMLRoot):
    """
    A concept (e.g. a category, theme, keyword).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS["Concept"]
    class_class_curie: ClassVar[str] = "skos:Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.Concept

    preferredLabel: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferredLabel):
            self.MissingRequiredField("preferredLabel")
        if not isinstance(self.preferredLabel, list):
            self.preferredLabel = [self.preferredLabel] if self.preferredLabel is not None else []
        self.preferredLabel = [v if isinstance(v, str) else str(v) for v in self.preferredLabel]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConceptScheme(YAMLRoot):
    """
    A controlled vocabulary or category scheme.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS["ConceptScheme"]
    class_class_curie: ClassVar[str] = "skos:ConceptScheme"
    class_name: ClassVar[str] = "ConceptScheme"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.ConceptScheme

    title: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataService(CataloguedResource):
    """
    A collection of operations that provides access to one or more datasets or data processing functions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["DataService"]
    class_class_curie: ClassVar[str] = "dcat:DataService"
    class_name: ClassVar[str] = "DataService"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.DataService

    title: Union[str, list[str]] = None
    endpointUrl: Union[Union[dict, Resource], list[Union[dict, Resource]]] = None
    description: Optional[Union[str, list[str]]] = empty_list()
    accessRights: Optional[Union[dict, "RightsStatement"]] = None
    applicableLegislation: Optional[Union[Union[dict, "LegalResource"], list[Union[dict, "LegalResource"]]]] = empty_list()
    conformsTo: Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]] = empty_list()
    contactPoint: Optional[Union[Union[dict, "Kind"], list[Union[dict, "Kind"]]]] = empty_list()
    documentation: Optional[Union[Union[dict, "Document"], list[Union[dict, "Document"]]]] = empty_list()
    endpointDescription: Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]] = empty_list()
    format: Optional[Union[Union[dict, "MediaType"], list[Union[dict, "MediaType"]]]] = empty_list()
    keyword: Optional[Union[str, list[str]]] = empty_list()
    landingPage: Optional[Union[Union[dict, "Document"], list[Union[dict, "Document"]]]] = empty_list()
    licence: Optional[Union[dict, "LicenceDocument"]] = None
    publisher: Optional[Union[dict, Agent]] = None
    servesDataset: Optional[Union[Union[dict, "Dataset"], list[Union[dict, "Dataset"]]]] = empty_list()
    theme: Optional[Union[Union[dict, Concept], list[Union[dict, Concept]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        if self._is_empty(self.endpointUrl):
            self.MissingRequiredField("endpointUrl")
        if not isinstance(self.endpointUrl, list):
            self.endpointUrl = [self.endpointUrl] if self.endpointUrl is not None else []
        self.endpointUrl = [v if isinstance(v, Resource) else Resource(**as_dict(v)) for v in self.endpointUrl]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if self.accessRights is not None and not isinstance(self.accessRights, RightsStatement):
            self.accessRights = RightsStatement()

        if not isinstance(self.applicableLegislation, list):
            self.applicableLegislation = [self.applicableLegislation] if self.applicableLegislation is not None else []
        self.applicableLegislation = [v if isinstance(v, LegalResource) else LegalResource(**as_dict(v)) for v in self.applicableLegislation]

        if not isinstance(self.conformsTo, list):
            self.conformsTo = [self.conformsTo] if self.conformsTo is not None else []
        self.conformsTo = [v if isinstance(v, Standard) else Standard(**as_dict(v)) for v in self.conformsTo]

        if not isinstance(self.contactPoint, list):
            self.contactPoint = [self.contactPoint] if self.contactPoint is not None else []
        self.contactPoint = [v if isinstance(v, Kind) else Kind(**as_dict(v)) for v in self.contactPoint]

        if not isinstance(self.documentation, list):
            self.documentation = [self.documentation] if self.documentation is not None else []
        self.documentation = [v if isinstance(v, Document) else Document(**as_dict(v)) for v in self.documentation]

        if not isinstance(self.endpointDescription, list):
            self.endpointDescription = [self.endpointDescription] if self.endpointDescription is not None else []
        self.endpointDescription = [v if isinstance(v, Resource) else Resource(**as_dict(v)) for v in self.endpointDescription]

        if not isinstance(self.format, list):
            self.format = [self.format] if self.format is not None else []
        self.format = [v if isinstance(v, MediaType) else MediaType(**as_dict(v)) for v in self.format]

        if not isinstance(self.keyword, list):
            self.keyword = [self.keyword] if self.keyword is not None else []
        self.keyword = [v if isinstance(v, str) else str(v) for v in self.keyword]

        if not isinstance(self.landingPage, list):
            self.landingPage = [self.landingPage] if self.landingPage is not None else []
        self.landingPage = [v if isinstance(v, Document) else Document(**as_dict(v)) for v in self.landingPage]

        if self.licence is not None and not isinstance(self.licence, LicenceDocument):
            self.licence = LicenceDocument(**as_dict(self.licence))

        if self.publisher is not None and not isinstance(self.publisher, Agent):
            self.publisher = Agent(**as_dict(self.publisher))

        self._normalize_inlined_as_list(slot_name="servesDataset", slot_type=Dataset, key_name="title", keyed=False)

        self._normalize_inlined_as_list(slot_name="theme", slot_type=Concept, key_name="preferredLabel", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(CataloguedResource):
    """
    A collection of data, published or curated by a single agent, and available for access or download in one or more
    representations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Dataset"]
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.Dataset

    title: Union[str, list[str]] = None
    description: Union[str, list[str]] = None
    accessRights: Optional[Union[dict, "RightsStatement"]] = None
    applicableLegislation: Optional[Union[Union[dict, "LegalResource"], list[Union[dict, "LegalResource"]]]] = empty_list()
    conformsTo: Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]] = empty_list()
    contactPoint: Optional[Union[Union[dict, "Kind"], list[Union[dict, "Kind"]]]] = empty_list()
    creator: Optional[Union[Union[dict, Agent], list[Union[dict, Agent]]]] = empty_list()
    datasetDistribution: Optional[Union[Union[dict, "Distribution"], list[Union[dict, "Distribution"]]]] = empty_list()
    documentation: Optional[Union[Union[dict, "Document"], list[Union[dict, "Document"]]]] = empty_list()
    frequency: Optional[Union[dict, "Frequency"]] = None
    geographicalCoverage: Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]] = empty_list()
    hasVersion: Optional[Union[Union[dict, "Dataset"], list[Union[dict, "Dataset"]]]] = empty_list()
    identifier: Optional[Union[str, list[str]]] = empty_list()
    inSeries: Optional[Union[Union[dict, "DatasetSeries"], list[Union[dict, "DatasetSeries"]]]] = empty_list()
    isReferencedBy: Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]] = empty_list()
    keyword: Optional[Union[str, list[str]]] = empty_list()
    landingPage: Optional[Union[Union[dict, "Document"], list[Union[dict, "Document"]]]] = empty_list()
    language: Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]] = empty_list()
    modificationDate: Optional[str] = None
    otherIdentifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()
    provenance: Optional[Union[Union[dict, "ProvenanceStatement"], list[Union[dict, "ProvenanceStatement"]]]] = empty_list()
    publisher: Optional[Union[dict, Agent]] = None
    qualifiedAttribution: Optional[Union[Union[dict, "Attribution"], list[Union[dict, "Attribution"]]]] = empty_list()
    qualifiedRelation: Optional[Union[Union[dict, "Relationship"], list[Union[dict, "Relationship"]]]] = empty_list()
    relatedResource: Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]] = empty_list()
    releaseDate: Optional[str] = None
    sample: Optional[Union[Union[dict, "Distribution"], list[Union[dict, "Distribution"]]]] = empty_list()
    source: Optional[Union[Union[dict, "Dataset"], list[Union[dict, "Dataset"]]]] = empty_list()
    spatialResolution: Optional[Union[Decimal, list[Decimal]]] = empty_list()
    temporalCoverage: Optional[Union[Union[dict, "PeriodOfTime"], list[Union[dict, "PeriodOfTime"]]]] = empty_list()
    temporalResolution: Optional[str] = None
    theme: Optional[Union[Union[dict, Concept], list[Union[dict, Concept]]]] = empty_list()
    type: Optional[Union[Union[dict, Concept], list[Union[dict, Concept]]]] = empty_list()
    version: Optional[str] = None
    versionNotes: Optional[Union[str, list[str]]] = empty_list()
    wasGeneratedBy: Optional[Union[Union[dict, "Activity"], list[Union[dict, "Activity"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if self.accessRights is not None and not isinstance(self.accessRights, RightsStatement):
            self.accessRights = RightsStatement()

        if not isinstance(self.applicableLegislation, list):
            self.applicableLegislation = [self.applicableLegislation] if self.applicableLegislation is not None else []
        self.applicableLegislation = [v if isinstance(v, LegalResource) else LegalResource(**as_dict(v)) for v in self.applicableLegislation]

        if not isinstance(self.conformsTo, list):
            self.conformsTo = [self.conformsTo] if self.conformsTo is not None else []
        self.conformsTo = [v if isinstance(v, Standard) else Standard(**as_dict(v)) for v in self.conformsTo]

        if not isinstance(self.contactPoint, list):
            self.contactPoint = [self.contactPoint] if self.contactPoint is not None else []
        self.contactPoint = [v if isinstance(v, Kind) else Kind(**as_dict(v)) for v in self.contactPoint]

        self._normalize_inlined_as_list(slot_name="creator", slot_type=Agent, key_name="name", keyed=False)

        if not isinstance(self.datasetDistribution, list):
            self.datasetDistribution = [self.datasetDistribution] if self.datasetDistribution is not None else []
        self.datasetDistribution = [v if isinstance(v, Distribution) else Distribution(**as_dict(v)) for v in self.datasetDistribution]

        if not isinstance(self.documentation, list):
            self.documentation = [self.documentation] if self.documentation is not None else []
        self.documentation = [v if isinstance(v, Document) else Document(**as_dict(v)) for v in self.documentation]

        if self.frequency is not None and not isinstance(self.frequency, Frequency):
            self.frequency = Frequency()

        if not isinstance(self.geographicalCoverage, list):
            self.geographicalCoverage = [self.geographicalCoverage] if self.geographicalCoverage is not None else []
        self.geographicalCoverage = [v if isinstance(v, Location) else Location(**as_dict(v)) for v in self.geographicalCoverage]

        self._normalize_inlined_as_list(slot_name="hasVersion", slot_type=Dataset, key_name="title", keyed=False)

        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier] if self.identifier is not None else []
        self.identifier = [v if isinstance(v, str) else str(v) for v in self.identifier]

        self._normalize_inlined_as_list(slot_name="inSeries", slot_type=DatasetSeries, key_name="title", keyed=False)

        if not isinstance(self.isReferencedBy, list):
            self.isReferencedBy = [self.isReferencedBy] if self.isReferencedBy is not None else []
        self.isReferencedBy = [v if isinstance(v, Resource) else Resource(**as_dict(v)) for v in self.isReferencedBy]

        if not isinstance(self.keyword, list):
            self.keyword = [self.keyword] if self.keyword is not None else []
        self.keyword = [v if isinstance(v, str) else str(v) for v in self.keyword]

        if not isinstance(self.landingPage, list):
            self.landingPage = [self.landingPage] if self.landingPage is not None else []
        self.landingPage = [v if isinstance(v, Document) else Document(**as_dict(v)) for v in self.landingPage]

        if not isinstance(self.language, list):
            self.language = [self.language] if self.language is not None else []
        self.language = [v if isinstance(v, LinguisticSystem) else LinguisticSystem(**as_dict(v)) for v in self.language]

        if self.modificationDate is not None and not isinstance(self.modificationDate, str):
            self.modificationDate = str(self.modificationDate)

        if not isinstance(self.otherIdentifier, list):
            self.otherIdentifier = [self.otherIdentifier] if self.otherIdentifier is not None else []
        self.otherIdentifier = [v if isinstance(v, Identifier) else Identifier(**as_dict(v)) for v in self.otherIdentifier]

        if not isinstance(self.provenance, list):
            self.provenance = [self.provenance] if self.provenance is not None else []
        self.provenance = [v if isinstance(v, ProvenanceStatement) else ProvenanceStatement(**as_dict(v)) for v in self.provenance]

        if self.publisher is not None and not isinstance(self.publisher, Agent):
            self.publisher = Agent(**as_dict(self.publisher))

        if not isinstance(self.qualifiedAttribution, list):
            self.qualifiedAttribution = [self.qualifiedAttribution] if self.qualifiedAttribution is not None else []
        self.qualifiedAttribution = [v if isinstance(v, Attribution) else Attribution(**as_dict(v)) for v in self.qualifiedAttribution]

        if not isinstance(self.qualifiedRelation, list):
            self.qualifiedRelation = [self.qualifiedRelation] if self.qualifiedRelation is not None else []
        self.qualifiedRelation = [v if isinstance(v, Relationship) else Relationship(**as_dict(v)) for v in self.qualifiedRelation]

        if not isinstance(self.relatedResource, list):
            self.relatedResource = [self.relatedResource] if self.relatedResource is not None else []
        self.relatedResource = [v if isinstance(v, Resource) else Resource(**as_dict(v)) for v in self.relatedResource]

        if self.releaseDate is not None and not isinstance(self.releaseDate, str):
            self.releaseDate = str(self.releaseDate)

        if not isinstance(self.sample, list):
            self.sample = [self.sample] if self.sample is not None else []
        self.sample = [v if isinstance(v, Distribution) else Distribution(**as_dict(v)) for v in self.sample]

        self._normalize_inlined_as_list(slot_name="source", slot_type=Dataset, key_name="title", keyed=False)

        if not isinstance(self.spatialResolution, list):
            self.spatialResolution = [self.spatialResolution] if self.spatialResolution is not None else []
        self.spatialResolution = [v if isinstance(v, Decimal) else Decimal(v) for v in self.spatialResolution]

        if not isinstance(self.temporalCoverage, list):
            self.temporalCoverage = [self.temporalCoverage] if self.temporalCoverage is not None else []
        self.temporalCoverage = [v if isinstance(v, PeriodOfTime) else PeriodOfTime(**as_dict(v)) for v in self.temporalCoverage]

        if self.temporalResolution is not None and not isinstance(self.temporalResolution, str):
            self.temporalResolution = str(self.temporalResolution)

        self._normalize_inlined_as_list(slot_name="theme", slot_type=Concept, key_name="preferredLabel", keyed=False)

        self._normalize_inlined_as_list(slot_name="type", slot_type=Concept, key_name="preferredLabel", keyed=False)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if not isinstance(self.versionNotes, list):
            self.versionNotes = [self.versionNotes] if self.versionNotes is not None else []
        self.versionNotes = [v if isinstance(v, str) else str(v) for v in self.versionNotes]

        if not isinstance(self.wasGeneratedBy, list):
            self.wasGeneratedBy = [self.wasGeneratedBy] if self.wasGeneratedBy is not None else []
        self.wasGeneratedBy = [v if isinstance(v, Activity) else Activity(**as_dict(v)) for v in self.wasGeneratedBy]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DatasetSeries(CataloguedResource):
    """
    A collection of datasets that share a common schema and represent a change over time.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["DatasetSeries"]
    class_class_curie: ClassVar[str] = "dcat:DatasetSeries"
    class_name: ClassVar[str] = "DatasetSeries"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.DatasetSeries

    title: Union[str, list[str]] = None
    description: Union[str, list[str]] = None
    publisher: Optional[Union[dict, Agent]] = None
    applicableLegislation: Optional[Union[Union[dict, "LegalResource"], list[Union[dict, "LegalResource"]]]] = empty_list()
    contactPoint: Optional[Union[Union[dict, "Kind"], list[Union[dict, "Kind"]]]] = empty_list()
    frequency: Optional[Union[dict, "Frequency"]] = None
    geographicalCoverage: Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]] = empty_list()
    modificationDate: Optional[str] = None
    releaseDate: Optional[str] = None
    temporalCoverage: Optional[Union[Union[dict, "PeriodOfTime"], list[Union[dict, "PeriodOfTime"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if self.publisher is not None and not isinstance(self.publisher, Agent):
            self.publisher = Agent(**as_dict(self.publisher))

        if not isinstance(self.applicableLegislation, list):
            self.applicableLegislation = [self.applicableLegislation] if self.applicableLegislation is not None else []
        self.applicableLegislation = [v if isinstance(v, LegalResource) else LegalResource(**as_dict(v)) for v in self.applicableLegislation]

        if not isinstance(self.contactPoint, list):
            self.contactPoint = [self.contactPoint] if self.contactPoint is not None else []
        self.contactPoint = [v if isinstance(v, Kind) else Kind(**as_dict(v)) for v in self.contactPoint]

        if self.frequency is not None and not isinstance(self.frequency, Frequency):
            self.frequency = Frequency()

        if not isinstance(self.geographicalCoverage, list):
            self.geographicalCoverage = [self.geographicalCoverage] if self.geographicalCoverage is not None else []
        self.geographicalCoverage = [v if isinstance(v, Location) else Location(**as_dict(v)) for v in self.geographicalCoverage]

        if self.modificationDate is not None and not isinstance(self.modificationDate, str):
            self.modificationDate = str(self.modificationDate)

        if self.releaseDate is not None and not isinstance(self.releaseDate, str):
            self.releaseDate = str(self.releaseDate)

        if not isinstance(self.temporalCoverage, list):
            self.temporalCoverage = [self.temporalCoverage] if self.temporalCoverage is not None else []
        self.temporalCoverage = [v if isinstance(v, PeriodOfTime) else PeriodOfTime(**as_dict(v)) for v in self.temporalCoverage]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Distribution(YAMLRoot):
    """
    A specific representation of a dataset (e.g. a downloadable file or an API access).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Distribution"]
    class_class_curie: ClassVar[str] = "dcat:Distribution"
    class_name: ClassVar[str] = "Distribution"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.Distribution

    accessUrl: Union[Union[dict, Resource], list[Union[dict, Resource]]] = None
    accessService: Optional[Union[Union[dict, DataService], list[Union[dict, DataService]]]] = empty_list()
    applicableLegislation: Optional[Union[Union[dict, "LegalResource"], list[Union[dict, "LegalResource"]]]] = empty_list()
    availability: Optional[Union[dict, Concept]] = None
    byteSize: Optional[int] = None
    checksum: Optional[Union[dict, Checksum]] = None
    compressionFormat: Optional[Union[dict, "MediaType"]] = None
    description: Optional[Union[str, list[str]]] = empty_list()
    documentation: Optional[Union[Union[dict, "Document"], list[Union[dict, "Document"]]]] = empty_list()
    downloadUrl: Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]] = empty_list()
    format: Optional[Union[Union[dict, "MediaType"], list[Union[dict, "MediaType"]]]] = empty_list()
    hasPolicy: Optional[Union[dict, "Policy"]] = None
    language: Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]] = empty_list()
    licence: Optional[Union[dict, "LicenceDocument"]] = None
    linkedSchemas: Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]] = empty_list()
    mediaType: Optional[Union[dict, "MediaType"]] = None
    modificationDate: Optional[str] = None
    packagingFormat: Optional[Union[dict, "MediaType"]] = None
    releaseDate: Optional[str] = None
    rights: Optional[Union[Union[dict, "RightsStatement"], list[Union[dict, "RightsStatement"]]]] = empty_list()
    spatialResolution: Optional[Union[Decimal, list[Decimal]]] = empty_list()
    status: Optional[Union[dict, Concept]] = None
    temporalResolution: Optional[str] = None
    title: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.accessUrl):
            self.MissingRequiredField("accessUrl")
        if not isinstance(self.accessUrl, list):
            self.accessUrl = [self.accessUrl] if self.accessUrl is not None else []
        self.accessUrl = [v if isinstance(v, Resource) else Resource(**as_dict(v)) for v in self.accessUrl]

        self._normalize_inlined_as_list(slot_name="accessService", slot_type=DataService, key_name="title", keyed=False)

        if not isinstance(self.applicableLegislation, list):
            self.applicableLegislation = [self.applicableLegislation] if self.applicableLegislation is not None else []
        self.applicableLegislation = [v if isinstance(v, LegalResource) else LegalResource(**as_dict(v)) for v in self.applicableLegislation]

        if self.availability is not None and not isinstance(self.availability, Concept):
            self.availability = Concept(**as_dict(self.availability))

        if self.byteSize is not None and not isinstance(self.byteSize, int):
            self.byteSize = int(self.byteSize)

        if self.checksum is not None and not isinstance(self.checksum, Checksum):
            self.checksum = Checksum(**as_dict(self.checksum))

        if self.compressionFormat is not None and not isinstance(self.compressionFormat, MediaType):
            self.compressionFormat = MediaType()

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.documentation, list):
            self.documentation = [self.documentation] if self.documentation is not None else []
        self.documentation = [v if isinstance(v, Document) else Document(**as_dict(v)) for v in self.documentation]

        if not isinstance(self.downloadUrl, list):
            self.downloadUrl = [self.downloadUrl] if self.downloadUrl is not None else []
        self.downloadUrl = [v if isinstance(v, Resource) else Resource(**as_dict(v)) for v in self.downloadUrl]

        if not isinstance(self.format, list):
            self.format = [self.format] if self.format is not None else []
        self.format = [v if isinstance(v, MediaType) else MediaType(**as_dict(v)) for v in self.format]

        if self.hasPolicy is not None and not isinstance(self.hasPolicy, Policy):
            self.hasPolicy = Policy()

        if not isinstance(self.language, list):
            self.language = [self.language] if self.language is not None else []
        self.language = [v if isinstance(v, LinguisticSystem) else LinguisticSystem(**as_dict(v)) for v in self.language]

        if self.licence is not None and not isinstance(self.licence, LicenceDocument):
            self.licence = LicenceDocument(**as_dict(self.licence))

        if not isinstance(self.linkedSchemas, list):
            self.linkedSchemas = [self.linkedSchemas] if self.linkedSchemas is not None else []
        self.linkedSchemas = [v if isinstance(v, Standard) else Standard(**as_dict(v)) for v in self.linkedSchemas]

        if self.mediaType is not None and not isinstance(self.mediaType, MediaType):
            self.mediaType = MediaType()

        if self.modificationDate is not None and not isinstance(self.modificationDate, str):
            self.modificationDate = str(self.modificationDate)

        if self.packagingFormat is not None and not isinstance(self.packagingFormat, MediaType):
            self.packagingFormat = MediaType()

        if self.releaseDate is not None and not isinstance(self.releaseDate, str):
            self.releaseDate = str(self.releaseDate)

        if not isinstance(self.rights, list):
            self.rights = [self.rights] if self.rights is not None else []
        self.rights = [v if isinstance(v, RightsStatement) else RightsStatement(**as_dict(v)) for v in self.rights]

        if not isinstance(self.spatialResolution, list):
            self.spatialResolution = [self.spatialResolution] if self.spatialResolution is not None else []
        self.spatialResolution = [v if isinstance(v, Decimal) else Decimal(v) for v in self.spatialResolution]

        if self.status is not None and not isinstance(self.status, Concept):
            self.status = Concept(**as_dict(self.status))

        if self.temporalResolution is not None and not isinstance(self.temporalResolution, str):
            self.temporalResolution = str(self.temporalResolution)

        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        super().__post_init__(**kwargs)


class Document(Resource):
    """
    A foaf:Document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF["Document"]
    class_class_curie: ClassVar[str] = "foaf:Document"
    class_name: ClassVar[str] = "Document"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.Document


class Frequency(Resource):
    """
    A rate at which something recurs (DC Terms Frequency).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["Frequency"]
    class_class_curie: ClassVar[str] = "dct:Frequency"
    class_name: ClassVar[str] = "Frequency"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.Frequency


class Geometry(Resource):
    """
    A spatial geometry (locn:Geometry).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LOCN["Geometry"]
    class_class_curie: ClassVar[str] = "locn:Geometry"
    class_name: ClassVar[str] = "Geometry"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.Geometry


@dataclass(repr=False)
class Identifier(YAMLRoot):
    """
    An identifier in a particular context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADMS["Identifier"]
    class_class_curie: ClassVar[str] = "adms:Identifier"
    class_name: ClassVar[str] = "Identifier"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.Identifier

    notation: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.notation is not None and not isinstance(self.notation, str):
            self.notation = str(self.notation)

        super().__post_init__(**kwargs)


class Kind(Resource):
    """
    A vCard Kind.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VCARD["Kind"]
    class_class_curie: ClassVar[str] = "vcard:Kind"
    class_name: ClassVar[str] = "Kind"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.Kind


class LegalResource(Resource):
    """
    A legal resource (ELI).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ELI["LegalResource"]
    class_class_curie: ClassVar[str] = "eli:LegalResource"
    class_name: ClassVar[str] = "LegalResource"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.LegalResource


@dataclass(repr=False)
class LicenceDocument(YAMLRoot):
    """
    A legal document giving official permission to do something with a resource.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["LicenseDocument"]
    class_class_curie: ClassVar[str] = "dct:LicenseDocument"
    class_name: ClassVar[str] = "LicenceDocument"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.LicenceDocument

    type: Optional[Union[Union[dict, Concept], list[Union[dict, Concept]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="type", slot_type=Concept, key_name="preferredLabel", keyed=False)

        super().__post_init__(**kwargs)


class LinguisticSystem(Resource):
    """
    A linguistic system (DC Terms LinguisticSystem).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["LinguisticSystem"]
    class_class_curie: ClassVar[str] = "dct:LinguisticSystem"
    class_name: ClassVar[str] = "LinguisticSystem"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.LinguisticSystem


@dataclass(repr=False)
class Location(YAMLRoot):
    """
    A spatial region or named place.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["Location"]
    class_class_curie: ClassVar[str] = "dct:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.Location

    bbox: Optional[str] = None
    centroid: Optional[str] = None
    geometry: Optional[Union[dict, Geometry]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.bbox is not None and not isinstance(self.bbox, str):
            self.bbox = str(self.bbox)

        if self.centroid is not None and not isinstance(self.centroid, str):
            self.centroid = str(self.centroid)

        if self.geometry is not None and not isinstance(self.geometry, Geometry):
            self.geometry = Geometry()

        super().__post_init__(**kwargs)


class MediaType(Resource):
    """
    An IANA media type (DC Terms MediaType).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["MediaType"]
    class_class_curie: ClassVar[str] = "dct:MediaType"
    class_name: ClassVar[str] = "MediaType"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.MediaType


@dataclass(repr=False)
class PeriodOfTime(YAMLRoot):
    """
    An interval of time named or defined by its start and end.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["PeriodOfTime"]
    class_class_curie: ClassVar[str] = "dct:PeriodOfTime"
    class_name: ClassVar[str] = "PeriodOfTime"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.PeriodOfTime

    beginning: Optional[str] = None
    end: Optional[str] = None
    endDate: Optional[str] = None
    startDate: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.beginning is not None and not isinstance(self.beginning, str):
            self.beginning = str(self.beginning)

        if self.end is not None and not isinstance(self.end, str):
            self.end = str(self.end)

        if self.endDate is not None and not isinstance(self.endDate, str):
            self.endDate = str(self.endDate)

        if self.startDate is not None and not isinstance(self.startDate, str):
            self.startDate = str(self.startDate)

        super().__post_init__(**kwargs)


class Policy(Resource):
    """
    An ODRL policy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ODRL["Policy"]
    class_class_curie: ClassVar[str] = "odrl:Policy"
    class_name: ClassVar[str] = "Policy"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.Policy


class ProvenanceStatement(Resource):
    """
    A statement of provenance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["ProvenanceStatement"]
    class_class_curie: ClassVar[str] = "dct:ProvenanceStatement"
    class_name: ClassVar[str] = "ProvenanceStatement"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.ProvenanceStatement


@dataclass(repr=False)
class Relationship(YAMLRoot):
    """
    An association between resources where one has a particular role.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Relationship"]
    class_class_curie: ClassVar[str] = "dcat:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.Relationship

    hadRole: Union[Union[dict, "Role"], list[Union[dict, "Role"]]] = None
    relation: Union[Union[dict, Resource], list[Union[dict, Resource]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.hadRole):
            self.MissingRequiredField("hadRole")
        if not isinstance(self.hadRole, list):
            self.hadRole = [self.hadRole] if self.hadRole is not None else []
        self.hadRole = [v if isinstance(v, Role) else Role(**as_dict(v)) for v in self.hadRole]

        if self._is_empty(self.relation):
            self.MissingRequiredField("relation")
        if not isinstance(self.relation, list):
            self.relation = [self.relation] if self.relation is not None else []
        self.relation = [v if isinstance(v, Resource) else Resource(**as_dict(v)) for v in self.relation]

        super().__post_init__(**kwargs)


class RightsStatement(Resource):
    """
    A statement about rights associated with a resource.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["RightsStatement"]
    class_class_curie: ClassVar[str] = "dct:RightsStatement"
    class_name: ClassVar[str] = "RightsStatement"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.RightsStatement


class Role(Resource):
    """
    A role (dcat:Role).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Role"]
    class_class_curie: ClassVar[str] = "dcat:Role"
    class_name: ClassVar[str] = "Role"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.Role


class Standard(Resource):
    """
    A standard (DC Terms Standard).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["Standard"]
    class_class_curie: ClassVar[str] = "dct:Standard"
    class_name: ClassVar[str] = "Standard"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.Standard


class Activity(Resource):
    """
    A PROV activity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Activity"]
    class_class_curie: ClassVar[str] = "prov:Activity"
    class_name: ClassVar[str] = "Activity"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.Activity


class Attribution(Resource):
    """
    A PROV attribution.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Attribution"]
    class_class_curie: ClassVar[str] = "prov:Attribution"
    class_name: ClassVar[str] = "Attribution"
    class_model_uri: ClassVar[URIRef] = DCAT_AP.Attribution


# Enumerations


# Slots
class slots:
    pass

slots.title = Slot(uri=DCT.title, name="title", curie=DCT.curie('title'),
                   model_uri=DCAT_AP.title, domain=None, range=Optional[Union[str, list[str]]])

slots.description = Slot(uri=DCT.description, name="description", curie=DCT.curie('description'),
                   model_uri=DCAT_AP.description, domain=None, range=Optional[Union[str, list[str]]])

slots.identifier = Slot(uri=DCT.identifier, name="identifier", curie=DCT.curie('identifier'),
                   model_uri=DCAT_AP.identifier, domain=None, range=Optional[Union[str, list[str]]])

slots.keyword = Slot(uri=DCAT.keyword, name="keyword", curie=DCAT.curie('keyword'),
                   model_uri=DCAT_AP.keyword, domain=None, range=Optional[Union[str, list[str]]])

slots.notation = Slot(uri=SKOS.notation, name="notation", curie=SKOS.curie('notation'),
                   model_uri=DCAT_AP.notation, domain=None, range=Optional[str])

slots.preferredLabel = Slot(uri=SKOS.prefLabel, name="preferredLabel", curie=SKOS.curie('prefLabel'),
                   model_uri=DCAT_AP.preferredLabel, domain=None, range=Optional[Union[str, list[str]]])

slots.name = Slot(uri=FOAF.name, name="name", curie=FOAF.curie('name'),
                   model_uri=DCAT_AP.name, domain=None, range=Optional[Union[str, list[str]]])

slots.version = Slot(uri=DCAT.version, name="version", curie=DCAT.curie('version'),
                   model_uri=DCAT_AP.version, domain=None, range=Optional[str])

slots.versionNotes = Slot(uri=ADMS.versionNotes, name="versionNotes", curie=ADMS.curie('versionNotes'),
                   model_uri=DCAT_AP.versionNotes, domain=None, range=Optional[Union[str, list[str]]])

slots.bbox = Slot(uri=DCAT.bbox, name="bbox", curie=DCAT.curie('bbox'),
                   model_uri=DCAT_AP.bbox, domain=None, range=Optional[str])

slots.centroid = Slot(uri=DCAT.centroid, name="centroid", curie=DCAT.curie('centroid'),
                   model_uri=DCAT_AP.centroid, domain=None, range=Optional[str])

slots.startDate = Slot(uri=DCAT.startDate, name="startDate", curie=DCAT.curie('startDate'),
                   model_uri=DCAT_AP.startDate, domain=None, range=Optional[str])

slots.endDate = Slot(uri=DCAT.endDate, name="endDate", curie=DCAT.curie('endDate'),
                   model_uri=DCAT_AP.endDate, domain=None, range=Optional[str])

slots.releaseDate = Slot(uri=DCT.issued, name="releaseDate", curie=DCT.curie('issued'),
                   model_uri=DCAT_AP.releaseDate, domain=None, range=Optional[str])

slots.modificationDate = Slot(uri=DCT.modified, name="modificationDate", curie=DCT.curie('modified'),
                   model_uri=DCAT_AP.modificationDate, domain=None, range=Optional[str])

slots.listingDate = Slot(uri=DCT.issued, name="listingDate", curie=DCT.curie('issued'),
                   model_uri=DCAT_AP.listingDate, domain=None, range=Optional[str])

slots.byteSize = Slot(uri=DCAT.byteSize, name="byteSize", curie=DCAT.curie('byteSize'),
                   model_uri=DCAT_AP.byteSize, domain=None, range=Optional[int])

slots.spatialResolution = Slot(uri=DCAT.spatialResolutionInMeters, name="spatialResolution", curie=DCAT.curie('spatialResolutionInMeters'),
                   model_uri=DCAT_AP.spatialResolution, domain=None, range=Optional[Union[Decimal, list[Decimal]]])

slots.temporalResolution = Slot(uri=DCAT.temporalResolution, name="temporalResolution", curie=DCAT.curie('temporalResolution'),
                   model_uri=DCAT_AP.temporalResolution, domain=None, range=Optional[str])

slots.checksumValue = Slot(uri=SPDX.checksumValue, name="checksumValue", curie=SPDX.curie('checksumValue'),
                   model_uri=DCAT_AP.checksumValue, domain=None, range=Optional[str])

slots.publisher = Slot(uri=DCT.publisher, name="publisher", curie=DCT.curie('publisher'),
                   model_uri=DCAT_AP.publisher, domain=None, range=Optional[Union[dict, Agent]])

slots.creator = Slot(uri=DCT.creator, name="creator", curie=DCT.curie('creator'),
                   model_uri=DCAT_AP.creator, domain=None, range=Optional[Union[Union[dict, Agent], list[Union[dict, Agent]]]])

slots.contactPoint = Slot(uri=DCAT.contactPoint, name="contactPoint", curie=DCAT.curie('contactPoint'),
                   model_uri=DCAT_AP.contactPoint, domain=None, range=Optional[Union[Union[dict, Kind], list[Union[dict, Kind]]]])

slots.language = Slot(uri=DCT.language, name="language", curie=DCT.curie('language'),
                   model_uri=DCAT_AP.language, domain=None, range=Optional[Union[Union[dict, LinguisticSystem], list[Union[dict, LinguisticSystem]]]])

slots.licence = Slot(uri=DCT.license, name="licence", curie=DCT.curie('license'),
                   model_uri=DCAT_AP.licence, domain=None, range=Optional[Union[dict, LicenceDocument]])

slots.rights = Slot(uri=DCT.rights, name="rights", curie=DCT.curie('rights'),
                   model_uri=DCAT_AP.rights, domain=None, range=Optional[Union[Union[dict, RightsStatement], list[Union[dict, RightsStatement]]]])

slots.hasPart = Slot(uri=DCT.hasPart, name="hasPart", curie=DCT.curie('hasPart'),
                   model_uri=DCAT_AP.hasPart, domain=None, range=Optional[Union[Union[dict, Catalogue], list[Union[dict, Catalogue]]]])

slots.geographicalCoverage = Slot(uri=DCT.spatial, name="geographicalCoverage", curie=DCT.curie('spatial'),
                   model_uri=DCAT_AP.geographicalCoverage, domain=None, range=Optional[Union[Union[dict, Location], list[Union[dict, Location]]]])

slots.temporalCoverage = Slot(uri=DCT.temporal, name="temporalCoverage", curie=DCT.curie('temporal'),
                   model_uri=DCAT_AP.temporalCoverage, domain=None, range=Optional[Union[Union[dict, PeriodOfTime], list[Union[dict, PeriodOfTime]]]])

slots.themes = Slot(uri=DCAT.themeTaxonomy, name="themes", curie=DCAT.curie('themeTaxonomy'),
                   model_uri=DCAT_AP.themes, domain=None, range=Optional[Union[Union[dict, ConceptScheme], list[Union[dict, ConceptScheme]]]])

slots.theme = Slot(uri=DCAT.theme, name="theme", curie=DCAT.curie('theme'),
                   model_uri=DCAT_AP.theme, domain=None, range=Optional[Union[Union[dict, Concept], list[Union[dict, Concept]]]])

slots.homepage = Slot(uri=FOAF.homepage, name="homepage", curie=FOAF.curie('homepage'),
                   model_uri=DCAT_AP.homepage, domain=None, range=Optional[Union[dict, Document]])

slots.catalogue = Slot(uri=DCAT.catalog, name="catalogue", curie=DCAT.curie('catalog'),
                   model_uri=DCAT_AP.catalogue, domain=None, range=Optional[Union[Union[dict, Catalogue], list[Union[dict, Catalogue]]]])

slots.dataset = Slot(uri=DCAT.dataset, name="dataset", curie=DCAT.curie('dataset'),
                   model_uri=DCAT_AP.dataset, domain=None, range=Optional[Union[Union[dict, Dataset], list[Union[dict, Dataset]]]])

slots.service = Slot(uri=DCAT.service, name="service", curie=DCAT.curie('service'),
                   model_uri=DCAT_AP.service, domain=None, range=Optional[Union[Union[dict, DataService], list[Union[dict, DataService]]]])

slots.record = Slot(uri=DCAT.record, name="record", curie=DCAT.curie('record'),
                   model_uri=DCAT_AP.record, domain=None, range=Optional[Union[Union[dict, CatalogueRecord], list[Union[dict, CatalogueRecord]]]])

slots.applicationProfile = Slot(uri=DCT.conformsTo, name="applicationProfile", curie=DCT.curie('conformsTo'),
                   model_uri=DCAT_AP.applicationProfile, domain=None, range=Optional[Union[Union[dict, Standard], list[Union[dict, Standard]]]])

slots.changeType = Slot(uri=ADMS.status, name="changeType", curie=ADMS.curie('status'),
                   model_uri=DCAT_AP.changeType, domain=None, range=Optional[Union[dict, Concept]])

slots.primaryTopic = Slot(uri=FOAF.primaryTopic, name="primaryTopic", curie=FOAF.curie('primaryTopic'),
                   model_uri=DCAT_AP.primaryTopic, domain=None, range=Optional[Union[dict, CataloguedResource]])

slots.sourceMetadata = Slot(uri=DCT.source, name="sourceMetadata", curie=DCT.curie('source'),
                   model_uri=DCAT_AP.sourceMetadata, domain=None, range=Optional[Union[dict, CatalogueRecord]])

slots.applicableLegislation = Slot(uri=DCATAP.applicableLegislation, name="applicableLegislation", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=DCAT_AP.applicableLegislation, domain=None, range=Optional[Union[Union[dict, LegalResource], list[Union[dict, LegalResource]]]])

slots.algorithm = Slot(uri=SPDX.algorithm, name="algorithm", curie=SPDX.curie('algorithm'),
                   model_uri=DCAT_AP.algorithm, domain=None, range=Optional[Union[dict, ChecksumAlgorithm]])

slots.type = Slot(uri=DCT.type, name="type", curie=DCT.curie('type'),
                   model_uri=DCAT_AP.type, domain=None, range=Optional[Union[Union[dict, Concept], list[Union[dict, Concept]]]])

slots.accessRights = Slot(uri=DCT.accessRights, name="accessRights", curie=DCT.curie('accessRights'),
                   model_uri=DCAT_AP.accessRights, domain=None, range=Optional[Union[dict, RightsStatement]])

slots.conformsTo = Slot(uri=DCT.conformsTo, name="conformsTo", curie=DCT.curie('conformsTo'),
                   model_uri=DCAT_AP.conformsTo, domain=None, range=Optional[Union[Union[dict, Standard], list[Union[dict, Standard]]]])

slots.documentation = Slot(uri=FOAF.page, name="documentation", curie=FOAF.curie('page'),
                   model_uri=DCAT_AP.documentation, domain=None, range=Optional[Union[Union[dict, Document], list[Union[dict, Document]]]])

slots.endpointUrl = Slot(uri=DCAT.endpointURL, name="endpointUrl", curie=DCAT.curie('endpointURL'),
                   model_uri=DCAT_AP.endpointUrl, domain=None, range=Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]])

slots.endpointDescription = Slot(uri=DCAT.endpointDescription, name="endpointDescription", curie=DCAT.curie('endpointDescription'),
                   model_uri=DCAT_AP.endpointDescription, domain=None, range=Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]])

slots.format = Slot(uri=DCT.format, name="format", curie=DCT.curie('format'),
                   model_uri=DCAT_AP.format, domain=None, range=Optional[Union[Union[dict, MediaType], list[Union[dict, MediaType]]]])

slots.landingPage = Slot(uri=DCAT.landingPage, name="landingPage", curie=DCAT.curie('landingPage'),
                   model_uri=DCAT_AP.landingPage, domain=None, range=Optional[Union[Union[dict, Document], list[Union[dict, Document]]]])

slots.servesDataset = Slot(uri=DCAT.servesDataset, name="servesDataset", curie=DCAT.curie('servesDataset'),
                   model_uri=DCAT_AP.servesDataset, domain=None, range=Optional[Union[Union[dict, Dataset], list[Union[dict, Dataset]]]])

slots.datasetDistribution = Slot(uri=DCAT.distribution, name="datasetDistribution", curie=DCAT.curie('distribution'),
                   model_uri=DCAT_AP.datasetDistribution, domain=None, range=Optional[Union[Union[dict, Distribution], list[Union[dict, Distribution]]]])

slots.frequency = Slot(uri=DCT.accrualPeriodicity, name="frequency", curie=DCT.curie('accrualPeriodicity'),
                   model_uri=DCAT_AP.frequency, domain=None, range=Optional[Union[dict, Frequency]])

slots.hasVersion = Slot(uri=DCAT.hasVersion, name="hasVersion", curie=DCAT.curie('hasVersion'),
                   model_uri=DCAT_AP.hasVersion, domain=None, range=Optional[Union[Union[dict, Dataset], list[Union[dict, Dataset]]]])

slots.inSeries = Slot(uri=DCAT.inSeries, name="inSeries", curie=DCAT.curie('inSeries'),
                   model_uri=DCAT_AP.inSeries, domain=None, range=Optional[Union[Union[dict, DatasetSeries], list[Union[dict, DatasetSeries]]]])

slots.isReferencedBy = Slot(uri=DCT.isReferencedBy, name="isReferencedBy", curie=DCT.curie('isReferencedBy'),
                   model_uri=DCAT_AP.isReferencedBy, domain=None, range=Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]])

slots.otherIdentifier = Slot(uri=ADMS.identifier, name="otherIdentifier", curie=ADMS.curie('identifier'),
                   model_uri=DCAT_AP.otherIdentifier, domain=None, range=Optional[Union[Union[dict, Identifier], list[Union[dict, Identifier]]]])

slots.provenance = Slot(uri=DCT.provenance, name="provenance", curie=DCT.curie('provenance'),
                   model_uri=DCAT_AP.provenance, domain=None, range=Optional[Union[Union[dict, ProvenanceStatement], list[Union[dict, ProvenanceStatement]]]])

slots.qualifiedAttribution = Slot(uri=PROV.qualifiedAttribution, name="qualifiedAttribution", curie=PROV.curie('qualifiedAttribution'),
                   model_uri=DCAT_AP.qualifiedAttribution, domain=None, range=Optional[Union[Union[dict, Attribution], list[Union[dict, Attribution]]]])

slots.qualifiedRelation = Slot(uri=DCAT.qualifiedRelation, name="qualifiedRelation", curie=DCAT.curie('qualifiedRelation'),
                   model_uri=DCAT_AP.qualifiedRelation, domain=None, range=Optional[Union[Union[dict, Relationship], list[Union[dict, Relationship]]]])

slots.relatedResource = Slot(uri=DCT.relation, name="relatedResource", curie=DCT.curie('relation'),
                   model_uri=DCAT_AP.relatedResource, domain=None, range=Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]])

slots.sample = Slot(uri=ADMS.sample, name="sample", curie=ADMS.curie('sample'),
                   model_uri=DCAT_AP.sample, domain=None, range=Optional[Union[Union[dict, Distribution], list[Union[dict, Distribution]]]])

slots.source = Slot(uri=DCT.source, name="source", curie=DCT.curie('source'),
                   model_uri=DCAT_AP.source, domain=None, range=Optional[Union[Union[dict, Dataset], list[Union[dict, Dataset]]]])

slots.wasGeneratedBy = Slot(uri=PROV.wasGeneratedBy, name="wasGeneratedBy", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=DCAT_AP.wasGeneratedBy, domain=None, range=Optional[Union[Union[dict, Activity], list[Union[dict, Activity]]]])

slots.accessUrl = Slot(uri=DCAT.accessURL, name="accessUrl", curie=DCAT.curie('accessURL'),
                   model_uri=DCAT_AP.accessUrl, domain=None, range=Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]])

slots.accessService = Slot(uri=DCAT.accessService, name="accessService", curie=DCAT.curie('accessService'),
                   model_uri=DCAT_AP.accessService, domain=None, range=Optional[Union[Union[dict, DataService], list[Union[dict, DataService]]]])

slots.availability = Slot(uri=DCATAP.availability, name="availability", curie=DCATAP.curie('availability'),
                   model_uri=DCAT_AP.availability, domain=None, range=Optional[Union[dict, Concept]])

slots.checksum = Slot(uri=SPDX.checksum, name="checksum", curie=SPDX.curie('checksum'),
                   model_uri=DCAT_AP.checksum, domain=None, range=Optional[Union[dict, Checksum]])

slots.compressionFormat = Slot(uri=DCAT.compressFormat, name="compressionFormat", curie=DCAT.curie('compressFormat'),
                   model_uri=DCAT_AP.compressionFormat, domain=None, range=Optional[Union[dict, MediaType]])

slots.downloadUrl = Slot(uri=DCAT.downloadURL, name="downloadUrl", curie=DCAT.curie('downloadURL'),
                   model_uri=DCAT_AP.downloadUrl, domain=None, range=Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]])

slots.hasPolicy = Slot(uri=ODRL.hasPolicy, name="hasPolicy", curie=ODRL.curie('hasPolicy'),
                   model_uri=DCAT_AP.hasPolicy, domain=None, range=Optional[Union[dict, Policy]])

slots.linkedSchemas = Slot(uri=DCT.conformsTo, name="linkedSchemas", curie=DCT.curie('conformsTo'),
                   model_uri=DCAT_AP.linkedSchemas, domain=None, range=Optional[Union[Union[dict, Standard], list[Union[dict, Standard]]]])

slots.mediaType = Slot(uri=DCAT.mediaType, name="mediaType", curie=DCAT.curie('mediaType'),
                   model_uri=DCAT_AP.mediaType, domain=None, range=Optional[Union[dict, MediaType]])

slots.packagingFormat = Slot(uri=DCAT.packageFormat, name="packagingFormat", curie=DCAT.curie('packageFormat'),
                   model_uri=DCAT_AP.packagingFormat, domain=None, range=Optional[Union[dict, MediaType]])

slots.status = Slot(uri=ADMS.status, name="status", curie=ADMS.curie('status'),
                   model_uri=DCAT_AP.status, domain=None, range=Optional[Union[dict, Concept]])

slots.hadRole = Slot(uri=DCAT.hadRole, name="hadRole", curie=DCAT.curie('hadRole'),
                   model_uri=DCAT_AP.hadRole, domain=None, range=Optional[Union[Union[dict, Role], list[Union[dict, Role]]]])

slots.relation = Slot(uri=DCT.relation, name="relation", curie=DCT.curie('relation'),
                   model_uri=DCAT_AP.relation, domain=None, range=Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]])

slots.beginning = Slot(uri=TIME.hasBeginning, name="beginning", curie=TIME.curie('hasBeginning'),
                   model_uri=DCAT_AP.beginning, domain=None, range=Optional[str])

slots.end = Slot(uri=TIME.hasEnd, name="end", curie=TIME.curie('hasEnd'),
                   model_uri=DCAT_AP.end, domain=None, range=Optional[str])

slots.geometry = Slot(uri=LOCN.geometry, name="geometry", curie=LOCN.curie('geometry'),
                   model_uri=DCAT_AP.geometry, domain=None, range=Optional[Union[dict, Geometry]])

slots.Agent_name = Slot(uri=FOAF.name, name="Agent_name", curie=FOAF.curie('name'),
                   model_uri=DCAT_AP.Agent_name, domain=Agent, range=Union[str, list[str]])

slots.Agent_type = Slot(uri=DCT.type, name="Agent_type", curie=DCT.curie('type'),
                   model_uri=DCAT_AP.Agent_type, domain=Agent, range=Optional[Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]]])

slots.Catalogue_title = Slot(uri=DCT.title, name="Catalogue_title", curie=DCT.curie('title'),
                   model_uri=DCAT_AP.Catalogue_title, domain=Catalogue, range=Union[str, list[str]])

slots.Catalogue_description = Slot(uri=DCT.description, name="Catalogue_description", curie=DCT.curie('description'),
                   model_uri=DCAT_AP.Catalogue_description, domain=Catalogue, range=Union[str, list[str]])

slots.Catalogue_publisher = Slot(uri=DCT.publisher, name="Catalogue_publisher", curie=DCT.curie('publisher'),
                   model_uri=DCAT_AP.Catalogue_publisher, domain=Catalogue, range=Union[dict, Agent])

slots.Catalogue_creator = Slot(uri=DCT.creator, name="Catalogue_creator", curie=DCT.curie('creator'),
                   model_uri=DCAT_AP.Catalogue_creator, domain=Catalogue, range=Optional[Union[Union[dict, Agent], list[Union[dict, Agent]]]])

slots.Catalogue_licence = Slot(uri=DCT.license, name="Catalogue_licence", curie=DCT.curie('license'),
                   model_uri=DCAT_AP.Catalogue_licence, domain=Catalogue, range=Optional[Union[dict, "LicenceDocument"]])

slots.Catalogue_homepage = Slot(uri=FOAF.homepage, name="Catalogue_homepage", curie=FOAF.curie('homepage'),
                   model_uri=DCAT_AP.Catalogue_homepage, domain=Catalogue, range=Optional[Union[dict, "Document"]])

slots.Catalogue_rights = Slot(uri=DCT.rights, name="Catalogue_rights", curie=DCT.curie('rights'),
                   model_uri=DCAT_AP.Catalogue_rights, domain=Catalogue, range=Optional[Union[Union[dict, "RightsStatement"], list[Union[dict, "RightsStatement"]]]])

slots.Catalogue_releaseDate = Slot(uri=DCT.issued, name="Catalogue_releaseDate", curie=DCT.curie('issued'),
                   model_uri=DCAT_AP.Catalogue_releaseDate, domain=Catalogue, range=Optional[str])

slots.Catalogue_modificationDate = Slot(uri=DCT.modified, name="Catalogue_modificationDate", curie=DCT.curie('modified'),
                   model_uri=DCAT_AP.Catalogue_modificationDate, domain=Catalogue, range=Optional[str])

slots.CatalogueRecord_primaryTopic = Slot(uri=FOAF.primaryTopic, name="CatalogueRecord_primaryTopic", curie=FOAF.curie('primaryTopic'),
                   model_uri=DCAT_AP.CatalogueRecord_primaryTopic, domain=CatalogueRecord, range=Union[dict, CataloguedResource])

slots.CatalogueRecord_modificationDate = Slot(uri=DCT.modified, name="CatalogueRecord_modificationDate", curie=DCT.curie('modified'),
                   model_uri=DCAT_AP.CatalogueRecord_modificationDate, domain=CatalogueRecord, range=str)

slots.CatalogueRecord_applicationProfile = Slot(uri=DCT.conformsTo, name="CatalogueRecord_applicationProfile", curie=DCT.curie('conformsTo'),
                   model_uri=DCAT_AP.CatalogueRecord_applicationProfile, domain=CatalogueRecord, range=Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]])

slots.CatalogueRecord_listingDate = Slot(uri=DCT.issued, name="CatalogueRecord_listingDate", curie=DCT.curie('issued'),
                   model_uri=DCAT_AP.CatalogueRecord_listingDate, domain=CatalogueRecord, range=Optional[str])

slots.CatalogueRecord_changeType = Slot(uri=ADMS.status, name="CatalogueRecord_changeType", curie=ADMS.curie('status'),
                   model_uri=DCAT_AP.CatalogueRecord_changeType, domain=CatalogueRecord, range=Optional[Union[dict, "Concept"]])

slots.CatalogueRecord_sourceMetadata = Slot(uri=DCT.source, name="CatalogueRecord_sourceMetadata", curie=DCT.curie('source'),
                   model_uri=DCAT_AP.CatalogueRecord_sourceMetadata, domain=CatalogueRecord, range=Optional[Union[dict, "CatalogueRecord"]])

slots.Checksum_algorithm = Slot(uri=SPDX.algorithm, name="Checksum_algorithm", curie=SPDX.curie('algorithm'),
                   model_uri=DCAT_AP.Checksum_algorithm, domain=Checksum, range=Union[dict, "ChecksumAlgorithm"])

slots.Checksum_checksumValue = Slot(uri=SPDX.checksumValue, name="Checksum_checksumValue", curie=SPDX.curie('checksumValue'),
                   model_uri=DCAT_AP.Checksum_checksumValue, domain=Checksum, range=str)

slots.Concept_preferredLabel = Slot(uri=SKOS.prefLabel, name="Concept_preferredLabel", curie=SKOS.curie('prefLabel'),
                   model_uri=DCAT_AP.Concept_preferredLabel, domain=Concept, range=Union[str, list[str]])

slots.ConceptScheme_title = Slot(uri=DCT.title, name="ConceptScheme_title", curie=DCT.curie('title'),
                   model_uri=DCAT_AP.ConceptScheme_title, domain=ConceptScheme, range=Union[str, list[str]])

slots.DataService_title = Slot(uri=DCT.title, name="DataService_title", curie=DCT.curie('title'),
                   model_uri=DCAT_AP.DataService_title, domain=DataService, range=Union[str, list[str]])

slots.DataService_endpointUrl = Slot(uri=DCAT.endpointURL, name="DataService_endpointUrl", curie=DCAT.curie('endpointURL'),
                   model_uri=DCAT_AP.DataService_endpointUrl, domain=DataService, range=Union[Union[dict, Resource], list[Union[dict, Resource]]])

slots.DataService_accessRights = Slot(uri=DCT.accessRights, name="DataService_accessRights", curie=DCT.curie('accessRights'),
                   model_uri=DCAT_AP.DataService_accessRights, domain=DataService, range=Optional[Union[dict, "RightsStatement"]])

slots.DataService_licence = Slot(uri=DCT.license, name="DataService_licence", curie=DCT.curie('license'),
                   model_uri=DCAT_AP.DataService_licence, domain=DataService, range=Optional[Union[dict, "LicenceDocument"]])

slots.DataService_publisher = Slot(uri=DCT.publisher, name="DataService_publisher", curie=DCT.curie('publisher'),
                   model_uri=DCAT_AP.DataService_publisher, domain=DataService, range=Optional[Union[dict, Agent]])

slots.Dataset_title = Slot(uri=DCT.title, name="Dataset_title", curie=DCT.curie('title'),
                   model_uri=DCAT_AP.Dataset_title, domain=Dataset, range=Union[str, list[str]])

slots.Dataset_description = Slot(uri=DCT.description, name="Dataset_description", curie=DCT.curie('description'),
                   model_uri=DCAT_AP.Dataset_description, domain=Dataset, range=Union[str, list[str]])

slots.Dataset_accessRights = Slot(uri=DCT.accessRights, name="Dataset_accessRights", curie=DCT.curie('accessRights'),
                   model_uri=DCAT_AP.Dataset_accessRights, domain=Dataset, range=Optional[Union[dict, "RightsStatement"]])

slots.Dataset_frequency = Slot(uri=DCT.accrualPeriodicity, name="Dataset_frequency", curie=DCT.curie('accrualPeriodicity'),
                   model_uri=DCAT_AP.Dataset_frequency, domain=Dataset, range=Optional[Union[dict, "Frequency"]])

slots.Dataset_modificationDate = Slot(uri=DCT.modified, name="Dataset_modificationDate", curie=DCT.curie('modified'),
                   model_uri=DCAT_AP.Dataset_modificationDate, domain=Dataset, range=Optional[str])

slots.Dataset_publisher = Slot(uri=DCT.publisher, name="Dataset_publisher", curie=DCT.curie('publisher'),
                   model_uri=DCAT_AP.Dataset_publisher, domain=Dataset, range=Optional[Union[dict, Agent]])

slots.Dataset_releaseDate = Slot(uri=DCT.issued, name="Dataset_releaseDate", curie=DCT.curie('issued'),
                   model_uri=DCAT_AP.Dataset_releaseDate, domain=Dataset, range=Optional[str])

slots.Dataset_spatialResolution = Slot(uri=DCAT.spatialResolutionInMeters, name="Dataset_spatialResolution", curie=DCAT.curie('spatialResolutionInMeters'),
                   model_uri=DCAT_AP.Dataset_spatialResolution, domain=Dataset, range=Optional[Union[Decimal, list[Decimal]]])

slots.Dataset_temporalResolution = Slot(uri=DCAT.temporalResolution, name="Dataset_temporalResolution", curie=DCAT.curie('temporalResolution'),
                   model_uri=DCAT_AP.Dataset_temporalResolution, domain=Dataset, range=Optional[str])

slots.Dataset_version = Slot(uri=DCAT.version, name="Dataset_version", curie=DCAT.curie('version'),
                   model_uri=DCAT_AP.Dataset_version, domain=Dataset, range=Optional[str])

slots.DatasetSeries_title = Slot(uri=DCT.title, name="DatasetSeries_title", curie=DCT.curie('title'),
                   model_uri=DCAT_AP.DatasetSeries_title, domain=DatasetSeries, range=Union[str, list[str]])

slots.DatasetSeries_description = Slot(uri=DCT.description, name="DatasetSeries_description", curie=DCT.curie('description'),
                   model_uri=DCAT_AP.DatasetSeries_description, domain=DatasetSeries, range=Union[str, list[str]])

slots.DatasetSeries_publisher = Slot(uri=DCT.publisher, name="DatasetSeries_publisher", curie=DCT.curie('publisher'),
                   model_uri=DCAT_AP.DatasetSeries_publisher, domain=DatasetSeries, range=Optional[Union[dict, Agent]])

slots.DatasetSeries_frequency = Slot(uri=DCT.accrualPeriodicity, name="DatasetSeries_frequency", curie=DCT.curie('accrualPeriodicity'),
                   model_uri=DCAT_AP.DatasetSeries_frequency, domain=DatasetSeries, range=Optional[Union[dict, "Frequency"]])

slots.DatasetSeries_modificationDate = Slot(uri=DCT.modified, name="DatasetSeries_modificationDate", curie=DCT.curie('modified'),
                   model_uri=DCAT_AP.DatasetSeries_modificationDate, domain=DatasetSeries, range=Optional[str])

slots.DatasetSeries_releaseDate = Slot(uri=DCT.issued, name="DatasetSeries_releaseDate", curie=DCT.curie('issued'),
                   model_uri=DCAT_AP.DatasetSeries_releaseDate, domain=DatasetSeries, range=Optional[str])

slots.Distribution_accessUrl = Slot(uri=DCAT.accessURL, name="Distribution_accessUrl", curie=DCAT.curie('accessURL'),
                   model_uri=DCAT_AP.Distribution_accessUrl, domain=Distribution, range=Union[Union[dict, Resource], list[Union[dict, Resource]]])

slots.Distribution_availability = Slot(uri=DCATAP.availability, name="Distribution_availability", curie=DCATAP.curie('availability'),
                   model_uri=DCAT_AP.Distribution_availability, domain=Distribution, range=Optional[Union[dict, Concept]])

slots.Distribution_byteSize = Slot(uri=DCAT.byteSize, name="Distribution_byteSize", curie=DCAT.curie('byteSize'),
                   model_uri=DCAT_AP.Distribution_byteSize, domain=Distribution, range=Optional[int])

slots.Distribution_checksum = Slot(uri=SPDX.checksum, name="Distribution_checksum", curie=SPDX.curie('checksum'),
                   model_uri=DCAT_AP.Distribution_checksum, domain=Distribution, range=Optional[Union[dict, Checksum]])

slots.Distribution_compressionFormat = Slot(uri=DCAT.compressFormat, name="Distribution_compressionFormat", curie=DCAT.curie('compressFormat'),
                   model_uri=DCAT_AP.Distribution_compressionFormat, domain=Distribution, range=Optional[Union[dict, "MediaType"]])

slots.Distribution_format = Slot(uri=DCT.format, name="Distribution_format", curie=DCT.curie('format'),
                   model_uri=DCAT_AP.Distribution_format, domain=Distribution, range=Optional[Union[Union[dict, "MediaType"], list[Union[dict, "MediaType"]]]])

slots.Distribution_hasPolicy = Slot(uri=ODRL.hasPolicy, name="Distribution_hasPolicy", curie=ODRL.curie('hasPolicy'),
                   model_uri=DCAT_AP.Distribution_hasPolicy, domain=Distribution, range=Optional[Union[dict, "Policy"]])

slots.Distribution_licence = Slot(uri=DCT.license, name="Distribution_licence", curie=DCT.curie('license'),
                   model_uri=DCAT_AP.Distribution_licence, domain=Distribution, range=Optional[Union[dict, "LicenceDocument"]])

slots.Distribution_mediaType = Slot(uri=DCAT.mediaType, name="Distribution_mediaType", curie=DCAT.curie('mediaType'),
                   model_uri=DCAT_AP.Distribution_mediaType, domain=Distribution, range=Optional[Union[dict, "MediaType"]])

slots.Distribution_modificationDate = Slot(uri=DCT.modified, name="Distribution_modificationDate", curie=DCT.curie('modified'),
                   model_uri=DCAT_AP.Distribution_modificationDate, domain=Distribution, range=Optional[str])

slots.Distribution_packagingFormat = Slot(uri=DCAT.packageFormat, name="Distribution_packagingFormat", curie=DCAT.curie('packageFormat'),
                   model_uri=DCAT_AP.Distribution_packagingFormat, domain=Distribution, range=Optional[Union[dict, "MediaType"]])

slots.Distribution_releaseDate = Slot(uri=DCT.issued, name="Distribution_releaseDate", curie=DCT.curie('issued'),
                   model_uri=DCAT_AP.Distribution_releaseDate, domain=Distribution, range=Optional[str])

slots.Distribution_rights = Slot(uri=DCT.rights, name="Distribution_rights", curie=DCT.curie('rights'),
                   model_uri=DCAT_AP.Distribution_rights, domain=Distribution, range=Optional[Union[Union[dict, "RightsStatement"], list[Union[dict, "RightsStatement"]]]])

slots.Distribution_spatialResolution = Slot(uri=DCAT.spatialResolutionInMeters, name="Distribution_spatialResolution", curie=DCAT.curie('spatialResolutionInMeters'),
                   model_uri=DCAT_AP.Distribution_spatialResolution, domain=Distribution, range=Optional[Union[Decimal, list[Decimal]]])

slots.Distribution_status = Slot(uri=ADMS.status, name="Distribution_status", curie=ADMS.curie('status'),
                   model_uri=DCAT_AP.Distribution_status, domain=Distribution, range=Optional[Union[dict, Concept]])

slots.Distribution_temporalResolution = Slot(uri=DCAT.temporalResolution, name="Distribution_temporalResolution", curie=DCAT.curie('temporalResolution'),
                   model_uri=DCAT_AP.Distribution_temporalResolution, domain=Distribution, range=Optional[str])

slots.Identifier_notation = Slot(uri=SKOS.notation, name="Identifier_notation", curie=SKOS.curie('notation'),
                   model_uri=DCAT_AP.Identifier_notation, domain=Identifier, range=Optional[str])

slots.LicenceDocument_type = Slot(uri=DCT.type, name="LicenceDocument_type", curie=DCT.curie('type'),
                   model_uri=DCAT_AP.LicenceDocument_type, domain=LicenceDocument, range=Optional[Union[Union[dict, Concept], list[Union[dict, Concept]]]])

slots.Location_bbox = Slot(uri=DCAT.bbox, name="Location_bbox", curie=DCAT.curie('bbox'),
                   model_uri=DCAT_AP.Location_bbox, domain=Location, range=Optional[str])

slots.Location_centroid = Slot(uri=DCAT.centroid, name="Location_centroid", curie=DCAT.curie('centroid'),
                   model_uri=DCAT_AP.Location_centroid, domain=Location, range=Optional[str])

slots.Location_geometry = Slot(uri=LOCN.geometry, name="Location_geometry", curie=LOCN.curie('geometry'),
                   model_uri=DCAT_AP.Location_geometry, domain=Location, range=Optional[Union[dict, Geometry]])

slots.PeriodOfTime_beginning = Slot(uri=TIME.hasBeginning, name="PeriodOfTime_beginning", curie=TIME.curie('hasBeginning'),
                   model_uri=DCAT_AP.PeriodOfTime_beginning, domain=PeriodOfTime, range=Optional[str])

slots.PeriodOfTime_end = Slot(uri=TIME.hasEnd, name="PeriodOfTime_end", curie=TIME.curie('hasEnd'),
                   model_uri=DCAT_AP.PeriodOfTime_end, domain=PeriodOfTime, range=Optional[str])

slots.PeriodOfTime_endDate = Slot(uri=DCAT.endDate, name="PeriodOfTime_endDate", curie=DCAT.curie('endDate'),
                   model_uri=DCAT_AP.PeriodOfTime_endDate, domain=PeriodOfTime, range=Optional[str])

slots.PeriodOfTime_startDate = Slot(uri=DCAT.startDate, name="PeriodOfTime_startDate", curie=DCAT.curie('startDate'),
                   model_uri=DCAT_AP.PeriodOfTime_startDate, domain=PeriodOfTime, range=Optional[str])

slots.Relationship_hadRole = Slot(uri=DCAT.hadRole, name="Relationship_hadRole", curie=DCAT.curie('hadRole'),
                   model_uri=DCAT_AP.Relationship_hadRole, domain=Relationship, range=Union[Union[dict, "Role"], list[Union[dict, "Role"]]])

slots.Relationship_relation = Slot(uri=DCT.relation, name="Relationship_relation", curie=DCT.curie('relation'),
                   model_uri=DCAT_AP.Relationship_relation, domain=Relationship, range=Union[Union[dict, Resource], list[Union[dict, Resource]]])
