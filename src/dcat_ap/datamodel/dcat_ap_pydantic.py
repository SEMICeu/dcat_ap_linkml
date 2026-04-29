from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.7.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'dcat_ap',
     'default_range': 'string',
     'description': 'A LinkML approximation of the SEMIC DCAT-AP 3.0.1 '
                    'specification. This schema captures the core classes and '
                    'properties of DCAT-AP 3.0.1 as defined by the SHACL shapes at '
                    'https://semiceu.github.io/DCAT-AP/releases/3.0.1/html/shacl/shapes.ttl '
                    'and the JSON-LD context at '
                    'https://semiceu.github.io/DCAT-AP/releases/3.0.1/context/dcat-ap.jsonld '
                    'This is a SCOPING/DEMO schema, not a production '
                    'specification. Some constructs (e.g. property-level '
                    'disjunction shapes, sh:or with multiple datatypes, inverse '
                    'paths) are not directly expressible in LinkML and are '
                    'approximated or omitted.',
     'id': 'https://w3id.org/semic/dcat-ap/3.0.1',
     'imports': ['linkml:types'],
     'license': 'CC-BY-4.0',
     'name': 'dcat_ap',
     'prefixes': {'adms': {'prefix_prefix': 'adms',
                           'prefix_reference': 'http://www.w3.org/ns/adms#'},
                  'dcat': {'prefix_prefix': 'dcat',
                           'prefix_reference': 'http://www.w3.org/ns/dcat#'},
                  'dcat_ap': {'prefix_prefix': 'dcat_ap',
                              'prefix_reference': 'https://w3id.org/semic/dcat-ap/'},
                  'dcatap': {'prefix_prefix': 'dcatap',
                             'prefix_reference': 'http://data.europa.eu/r5r/'},
                  'dct': {'prefix_prefix': 'dct',
                          'prefix_reference': 'http://purl.org/dc/terms/'},
                  'eli': {'prefix_prefix': 'eli',
                          'prefix_reference': 'http://data.europa.eu/eli/ontology#'},
                  'foaf': {'prefix_prefix': 'foaf',
                           'prefix_reference': 'http://xmlns.com/foaf/0.1/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'locn': {'prefix_prefix': 'locn',
                           'prefix_reference': 'http://www.w3.org/ns/locn#'},
                  'odrl': {'prefix_prefix': 'odrl',
                           'prefix_reference': 'http://www.w3.org/ns/odrl/2/'},
                  'owl': {'prefix_prefix': 'owl',
                          'prefix_reference': 'http://www.w3.org/2002/07/owl#'},
                  'prov': {'prefix_prefix': 'prov',
                           'prefix_reference': 'http://www.w3.org/ns/prov#'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'spdx': {'prefix_prefix': 'spdx',
                           'prefix_reference': 'http://spdx.org/rdf/terms#'},
                  'time': {'prefix_prefix': 'time',
                           'prefix_reference': 'http://www.w3.org/2006/time#'},
                  'vcard': {'prefix_prefix': 'vcard',
                            'prefix_reference': 'http://www.w3.org/2006/vcard/ns#'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'source_file': 'src/dcat_ap/schema/dcat_ap.yaml',
     'title': 'DCAT-AP 3.0.1 (LinkML approximation)',
     'types': {'duration': {'base': 'str',
                            'description': 'An XSD duration literal.',
                            'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1',
                            'name': 'duration',
                            'uri': 'xsd:duration'},
               'hexBinary': {'base': 'str',
                             'description': 'A hex-binary encoded value.',
                             'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1',
                             'name': 'hexBinary',
                             'uri': 'xsd:hexBinary'},
               'nonNegativeInteger': {'base': 'int',
                                      'description': 'An XSD non-negative integer.',
                                      'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1',
                                      'minimum_value': 0,
                                      'name': 'nonNegativeInteger',
                                      'uri': 'xsd:nonNegativeInteger'}}} )


class Resource(ConfiguredBaseModel):
    """
    Top-level abstract resource. Used as a generic node range when the DCAT-AP shape only constrains nodeKind to BlankNodeOrIRI/IRI without a specific class.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'rdfs:Resource',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1'})

    pass


class CataloguedResource(Resource):
    """
    Union of Catalogue, Dataset, DataService, DatasetSeries (a.k.a. dcat:Resource).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'dcat:Resource',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1'})

    pass


class Agent(ConfiguredBaseModel):
    """
    An agent (e.g. a person, organisation) responsible for a resource.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'foaf:Agent',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1',
         'slot_usage': {'name': {'multivalued': True, 'name': 'name', 'required': True},
                        'type': {'multivalued': False, 'name': 'type'}}})

    name: list[str] = Field(default=..., description="""A name for an agent.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Agent'], 'slot_uri': 'foaf:name'} })
    type: Optional[Concept] = Field(default=None, description="""The nature or genre of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Agent', 'Dataset', 'LicenceDocument'], 'slot_uri': 'dct:type'} })


class Catalogue(CataloguedResource):
    """
    A curated collection of metadata about resources (e.g. datasets and data services in the context of a data catalogue).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dcat:Catalog',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1',
         'slot_usage': {'creator': {'multivalued': False, 'name': 'creator'},
                        'description': {'multivalued': True,
                                        'name': 'description',
                                        'required': True},
                        'homepage': {'multivalued': False, 'name': 'homepage'},
                        'licence': {'multivalued': False, 'name': 'licence'},
                        'modificationDate': {'multivalued': False,
                                             'name': 'modificationDate'},
                        'publisher': {'multivalued': False,
                                      'name': 'publisher',
                                      'required': True},
                        'releaseDate': {'multivalued': False, 'name': 'releaseDate'},
                        'rights': {'multivalued': False, 'name': 'rights'},
                        'title': {'multivalued': True,
                                  'name': 'title',
                                  'required': True}}})

    title: list[str] = Field(default=..., description="""A name given to the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dct:title'} })
    description: list[str] = Field(default=..., description="""A free-text account of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dct:description'} })
    publisher: Agent = Field(default=..., description="""An entity responsible for making the resource available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'DataService', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dct:publisher'} })
    applicableLegislation: Optional[list[LegalResource]] = Field(default=None, description="""The legislation applicable to the resource (DCAT-AP extension).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dcatap:applicableLegislation'} })
    catalogue: Optional[list[Catalogue]] = Field(default=None, description="""A subordinate catalogue contained in this catalogue.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue'], 'slot_uri': 'dcat:catalog'} })
    creator: Optional[Agent] = Field(default=None, description="""The entity responsible for producing the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'Dataset'], 'slot_uri': 'dct:creator'} })
    dataset: Optional[list[Dataset]] = Field(default=None, description="""A dataset listed by the catalogue.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue'], 'slot_uri': 'dcat:dataset'} })
    geographicalCoverage: Optional[list[Location]] = Field(default=None, description="""The geographic coverage of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dct:spatial'} })
    hasPart: Optional[list[Catalogue]] = Field(default=None, description="""A related resource that is included physically or logically.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue'], 'slot_uri': 'dct:hasPart'} })
    homepage: Optional[Document] = Field(default=None, description="""A web page that is the primary access point for the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue'], 'slot_uri': 'foaf:homepage'} })
    language: Optional[list[LinguisticSystem]] = Field(default=None, description="""A language of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'CatalogueRecord', 'Dataset', 'Distribution'],
         'slot_uri': 'dct:language'} })
    licence: Optional[LicenceDocument] = Field(default=None, description="""A licence under which the resource is made available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'DataService', 'Distribution'],
         'slot_uri': 'dct:license'} })
    modificationDate: Optional[datetime ] = Field(default=None, description="""The date on which the resource was changed. Approximated as xsd:dateTime (see DateOrDateTimeDataType_Shape gap in COMPARISON.md).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dct:modified'} })
    record: Optional[list[CatalogueRecord]] = Field(default=None, description="""A record describing a registration of a resource in the catalogue.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue'], 'slot_uri': 'dcat:record'} })
    releaseDate: Optional[datetime ] = Field(default=None, description="""The date of formal issuance of the resource. The original DCAT-AP shape uses sh:or over xsd:date / xsd:dateTime / xsd:gYear / xsd:gYearMonth; LinkML can express only a single primary type, so this is approximated as xsd:dateTime.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries', 'Distribution'],
         'slot_uri': 'dct:issued'} })
    rights: Optional[RightsStatement] = Field(default=None, description="""Rights statement for the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'Distribution'], 'slot_uri': 'dct:rights'} })
    service: Optional[list[DataService]] = Field(default=None, description="""A data service listed by the catalogue.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue'], 'slot_uri': 'dcat:service'} })
    temporalCoverage: Optional[list[PeriodOfTime]] = Field(default=None, description="""The temporal coverage of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dct:temporal'} })
    themes: Optional[list[ConceptScheme]] = Field(default=None, description="""A theme taxonomy used to classify the catalogue's resources.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue'], 'slot_uri': 'dcat:themeTaxonomy'} })


class CatalogueRecord(ConfiguredBaseModel):
    """
    A description of a single entry in a data catalogue.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dcat:CatalogRecord',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1',
         'slot_usage': {'applicationProfile': {'multivalued': False,
                                               'name': 'applicationProfile'},
                        'changeType': {'multivalued': False, 'name': 'changeType'},
                        'listingDate': {'multivalued': False, 'name': 'listingDate'},
                        'modificationDate': {'multivalued': False,
                                             'name': 'modificationDate',
                                             'required': True},
                        'primaryTopic': {'multivalued': False,
                                         'name': 'primaryTopic',
                                         'required': True},
                        'sourceMetadata': {'multivalued': False,
                                           'name': 'sourceMetadata'}}})

    applicationProfile: Optional[Standard] = Field(default=None, description="""The application profile this catalogue record conforms to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogueRecord'], 'slot_uri': 'dct:conformsTo'} })
    changeType: Optional[Concept] = Field(default=None, description="""The type of update on the cataloged resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogueRecord'], 'slot_uri': 'adms:status'} })
    description: Optional[list[str]] = Field(default=None, description="""A free-text account of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dct:description'} })
    language: Optional[list[LinguisticSystem]] = Field(default=None, description="""A language of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'CatalogueRecord', 'Dataset', 'Distribution'],
         'slot_uri': 'dct:language'} })
    listingDate: Optional[datetime ] = Field(default=None, description="""The date on which the description was listed in the catalogue. Approximated as xsd:dateTime.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogueRecord'], 'slot_uri': 'dct:issued'} })
    modificationDate: datetime  = Field(default=..., description="""The date on which the resource was changed. Approximated as xsd:dateTime (see DateOrDateTimeDataType_Shape gap in COMPARISON.md).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dct:modified'} })
    primaryTopic: CataloguedResource = Field(default=..., description="""The resource described by this catalogue record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogueRecord'], 'slot_uri': 'foaf:primaryTopic'} })
    sourceMetadata: Optional[CatalogueRecord] = Field(default=None, description="""Original metadata source for the catalog record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogueRecord'], 'slot_uri': 'dct:source'} })
    title: Optional[list[str]] = Field(default=None, description="""A name given to the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dct:title'} })


class Checksum(ConfiguredBaseModel):
    """
    A value that allows the contents of a file to be authenticated.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx:Checksum',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1',
         'slot_usage': {'algorithm': {'multivalued': False,
                                      'name': 'algorithm',
                                      'required': True},
                        'checksumValue': {'multivalued': False,
                                          'name': 'checksumValue',
                                          'range': 'hexBinary',
                                          'required': True}}})

    algorithm: ChecksumAlgorithm = Field(default=..., description="""The algorithm used to produce a checksum.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Checksum'], 'slot_uri': 'spdx:algorithm'} })
    checksumValue: str = Field(default=..., description="""A lower-case hexadecimal-encoded checksum value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Checksum'], 'slot_uri': 'spdx:checksumValue'} })


class ChecksumAlgorithm(Resource):
    """
    An algorithm used to produce a checksum.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx:ChecksumAlgorithm',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1'})

    pass


class Concept(ConfiguredBaseModel):
    """
    A concept (e.g. a category, theme, keyword).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'skos:Concept',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1',
         'slot_usage': {'preferredLabel': {'multivalued': True,
                                           'name': 'preferredLabel',
                                           'required': True}}})

    preferredLabel: list[str] = Field(default=..., description="""The preferred lexical label for a resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'skos:prefLabel'} })


class ConceptScheme(ConfiguredBaseModel):
    """
    A controlled vocabulary or category scheme.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'skos:ConceptScheme',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1',
         'slot_usage': {'title': {'multivalued': True,
                                  'name': 'title',
                                  'required': True}}})

    title: list[str] = Field(default=..., description="""A name given to the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dct:title'} })


class DataService(CataloguedResource):
    """
    A collection of operations that provides access to one or more datasets or data processing functions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dcat:DataService',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1',
         'slot_usage': {'accessRights': {'multivalued': False, 'name': 'accessRights'},
                        'endpointUrl': {'multivalued': True,
                                        'name': 'endpointUrl',
                                        'required': True},
                        'licence': {'multivalued': False, 'name': 'licence'},
                        'publisher': {'multivalued': False, 'name': 'publisher'},
                        'title': {'multivalued': True,
                                  'name': 'title',
                                  'required': True}}})

    title: list[str] = Field(default=..., description="""A name given to the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dct:title'} })
    description: Optional[list[str]] = Field(default=None, description="""A free-text account of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dct:description'} })
    endpointUrl: list[Resource] = Field(default=..., description="""The root location of the service.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataService'], 'slot_uri': 'dcat:endpointURL'} })
    accessRights: Optional[RightsStatement] = Field(default=None, description="""Information about who can access the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataService', 'Dataset'], 'slot_uri': 'dct:accessRights'} })
    applicableLegislation: Optional[list[LegalResource]] = Field(default=None, description="""The legislation applicable to the resource (DCAT-AP extension).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dcatap:applicableLegislation'} })
    conformsTo: Optional[list[Standard]] = Field(default=None, description="""An established standard the resource conforms to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataService', 'Dataset'], 'slot_uri': 'dct:conformsTo'} })
    contactPoint: Optional[list[Kind]] = Field(default=None, description="""Contact information for the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataService', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcat:contactPoint'} })
    documentation: Optional[list[Document]] = Field(default=None, description="""A page or document about the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataService', 'Dataset', 'Distribution'],
         'slot_uri': 'foaf:page'} })
    endpointDescription: Optional[list[Resource]] = Field(default=None, description="""A description of the service endpoint, including operations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataService'], 'slot_uri': 'dcat:endpointDescription'} })
    format: Optional[list[MediaType]] = Field(default=None, description="""The file format, physical medium, or dimensions of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataService', 'Distribution'], 'slot_uri': 'dct:format'} })
    keyword: Optional[list[str]] = Field(default=None, description="""A keyword or tag describing the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataService', 'Dataset'], 'slot_uri': 'dcat:keyword'} })
    landingPage: Optional[list[Document]] = Field(default=None, description="""A web page that gives access to the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataService', 'Dataset'], 'slot_uri': 'dcat:landingPage'} })
    licence: Optional[LicenceDocument] = Field(default=None, description="""A licence under which the resource is made available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'DataService', 'Distribution'],
         'slot_uri': 'dct:license'} })
    publisher: Optional[Agent] = Field(default=None, description="""An entity responsible for making the resource available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'DataService', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dct:publisher'} })
    servesDataset: Optional[list[Dataset]] = Field(default=None, description="""A dataset that this service serves.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataService'], 'slot_uri': 'dcat:servesDataset'} })
    theme: Optional[list[Concept]] = Field(default=None, description="""A category of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataService', 'Dataset'], 'slot_uri': 'dcat:theme'} })


class Dataset(CataloguedResource):
    """
    A collection of data, published or curated by a single agent, and available for access or download in one or more representations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dcat:Dataset',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1',
         'slot_usage': {'accessRights': {'multivalued': False, 'name': 'accessRights'},
                        'description': {'multivalued': True,
                                        'name': 'description',
                                        'required': True},
                        'frequency': {'multivalued': False, 'name': 'frequency'},
                        'modificationDate': {'multivalued': False,
                                             'name': 'modificationDate'},
                        'publisher': {'multivalued': False, 'name': 'publisher'},
                        'releaseDate': {'multivalued': False, 'name': 'releaseDate'},
                        'spatialResolution': {'multivalued': False,
                                              'name': 'spatialResolution',
                                              'range': 'decimal'},
                        'temporalResolution': {'multivalued': False,
                                               'name': 'temporalResolution',
                                               'range': 'duration'},
                        'title': {'multivalued': True,
                                  'name': 'title',
                                  'required': True},
                        'version': {'multivalued': False, 'name': 'version'}}})

    title: list[str] = Field(default=..., description="""A name given to the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dct:title'} })
    description: list[str] = Field(default=..., description="""A free-text account of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dct:description'} })
    accessRights: Optional[RightsStatement] = Field(default=None, description="""Information about who can access the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataService', 'Dataset'], 'slot_uri': 'dct:accessRights'} })
    applicableLegislation: Optional[list[LegalResource]] = Field(default=None, description="""The legislation applicable to the resource (DCAT-AP extension).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dcatap:applicableLegislation'} })
    conformsTo: Optional[list[Standard]] = Field(default=None, description="""An established standard the resource conforms to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataService', 'Dataset'], 'slot_uri': 'dct:conformsTo'} })
    contactPoint: Optional[list[Kind]] = Field(default=None, description="""Contact information for the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataService', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcat:contactPoint'} })
    creator: Optional[list[Agent]] = Field(default=None, description="""The entity responsible for producing the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'Dataset'], 'slot_uri': 'dct:creator'} })
    datasetDistribution: Optional[list[Distribution]] = Field(default=None, description="""An available distribution of the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'dcat:distribution'} })
    documentation: Optional[list[Document]] = Field(default=None, description="""A page or document about the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataService', 'Dataset', 'Distribution'],
         'slot_uri': 'foaf:page'} })
    frequency: Optional[Frequency] = Field(default=None, description="""The frequency at which the dataset is updated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'DatasetSeries'],
         'slot_uri': 'dct:accrualPeriodicity'} })
    geographicalCoverage: Optional[list[Location]] = Field(default=None, description="""The geographic coverage of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dct:spatial'} })
    hasVersion: Optional[list[Dataset]] = Field(default=None, description="""A related dataset that is a version of this dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'dcat:hasVersion'} })
    identifier: Optional[list[str]] = Field(default=None, description="""A unique identifier of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'dct:identifier'} })
    inSeries: Optional[list[DatasetSeries]] = Field(default=None, description="""A dataset series of which this dataset is a part.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'dcat:inSeries'} })
    isReferencedBy: Optional[list[Resource]] = Field(default=None, description="""A related resource that references the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'dct:isReferencedBy'} })
    keyword: Optional[list[str]] = Field(default=None, description="""A keyword or tag describing the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataService', 'Dataset'], 'slot_uri': 'dcat:keyword'} })
    landingPage: Optional[list[Document]] = Field(default=None, description="""A web page that gives access to the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataService', 'Dataset'], 'slot_uri': 'dcat:landingPage'} })
    language: Optional[list[LinguisticSystem]] = Field(default=None, description="""A language of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'CatalogueRecord', 'Dataset', 'Distribution'],
         'slot_uri': 'dct:language'} })
    modificationDate: Optional[datetime ] = Field(default=None, description="""The date on which the resource was changed. Approximated as xsd:dateTime (see DateOrDateTimeDataType_Shape gap in COMPARISON.md).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dct:modified'} })
    otherIdentifier: Optional[list[Identifier]] = Field(default=None, description="""A secondary identifier of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'adms:identifier'} })
    provenance: Optional[list[ProvenanceStatement]] = Field(default=None, description="""A statement about provenance of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'dct:provenance'} })
    publisher: Optional[Agent] = Field(default=None, description="""An entity responsible for making the resource available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'DataService', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dct:publisher'} })
    qualifiedAttribution: Optional[list[Attribution]] = Field(default=None, description="""An attribution of an agent to the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'prov:qualifiedAttribution'} })
    qualifiedRelation: Optional[list[Relationship]] = Field(default=None, description="""A qualified relationship to another resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'dcat:qualifiedRelation'} })
    relatedResource: Optional[list[Resource]] = Field(default=None, description="""A related resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'dct:relation'} })
    releaseDate: Optional[datetime ] = Field(default=None, description="""The date of formal issuance of the resource. The original DCAT-AP shape uses sh:or over xsd:date / xsd:dateTime / xsd:gYear / xsd:gYearMonth; LinkML can express only a single primary type, so this is approximated as xsd:dateTime.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries', 'Distribution'],
         'slot_uri': 'dct:issued'} })
    sample: Optional[list[Distribution]] = Field(default=None, description="""A sample distribution of the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'adms:sample'} })
    source: Optional[list[Dataset]] = Field(default=None, description="""A related resource from which the described resource is derived.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'dct:source'} })
    spatialResolution: Optional[Decimal] = Field(default=None, description="""Minimum spatial separation resolvable, in meters.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'Distribution'],
         'slot_uri': 'dcat:spatialResolutionInMeters'} })
    temporalCoverage: Optional[list[PeriodOfTime]] = Field(default=None, description="""The temporal coverage of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dct:temporal'} })
    temporalResolution: Optional[str] = Field(default=None, description="""Minimum time period resolvable in the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'Distribution'],
         'slot_uri': 'dcat:temporalResolution'} })
    theme: Optional[list[Concept]] = Field(default=None, description="""A category of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataService', 'Dataset'], 'slot_uri': 'dcat:theme'} })
    type: Optional[list[Concept]] = Field(default=None, description="""The nature or genre of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Agent', 'Dataset', 'LicenceDocument'], 'slot_uri': 'dct:type'} })
    version: Optional[str] = Field(default=None, description="""The version indicator of a resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'dcat:version'} })
    versionNotes: Optional[list[str]] = Field(default=None, description="""A description of changes between versions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'adms:versionNotes'} })
    wasGeneratedBy: Optional[list[Activity]] = Field(default=None, description="""An activity that generated the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'prov:wasGeneratedBy'} })


class DatasetSeries(CataloguedResource):
    """
    A collection of datasets that share a common schema and represent a change over time.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dcat:DatasetSeries',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1',
         'slot_usage': {'description': {'multivalued': True,
                                        'name': 'description',
                                        'required': True},
                        'frequency': {'multivalued': False, 'name': 'frequency'},
                        'modificationDate': {'multivalued': False,
                                             'name': 'modificationDate'},
                        'publisher': {'multivalued': False, 'name': 'publisher'},
                        'releaseDate': {'multivalued': False, 'name': 'releaseDate'},
                        'title': {'multivalued': True,
                                  'name': 'title',
                                  'required': True}}})

    title: list[str] = Field(default=..., description="""A name given to the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dct:title'} })
    description: list[str] = Field(default=..., description="""A free-text account of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dct:description'} })
    publisher: Optional[Agent] = Field(default=None, description="""An entity responsible for making the resource available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'DataService', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dct:publisher'} })
    applicableLegislation: Optional[list[LegalResource]] = Field(default=None, description="""The legislation applicable to the resource (DCAT-AP extension).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dcatap:applicableLegislation'} })
    contactPoint: Optional[list[Kind]] = Field(default=None, description="""Contact information for the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataService', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcat:contactPoint'} })
    frequency: Optional[Frequency] = Field(default=None, description="""The frequency at which the dataset is updated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'DatasetSeries'],
         'slot_uri': 'dct:accrualPeriodicity'} })
    geographicalCoverage: Optional[list[Location]] = Field(default=None, description="""The geographic coverage of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dct:spatial'} })
    modificationDate: Optional[datetime ] = Field(default=None, description="""The date on which the resource was changed. Approximated as xsd:dateTime (see DateOrDateTimeDataType_Shape gap in COMPARISON.md).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dct:modified'} })
    releaseDate: Optional[datetime ] = Field(default=None, description="""The date of formal issuance of the resource. The original DCAT-AP shape uses sh:or over xsd:date / xsd:dateTime / xsd:gYear / xsd:gYearMonth; LinkML can express only a single primary type, so this is approximated as xsd:dateTime.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries', 'Distribution'],
         'slot_uri': 'dct:issued'} })
    temporalCoverage: Optional[list[PeriodOfTime]] = Field(default=None, description="""The temporal coverage of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dct:temporal'} })


class Distribution(ConfiguredBaseModel):
    """
    A specific representation of a dataset (e.g. a downloadable file or an API access).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dcat:Distribution',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1',
         'slot_usage': {'accessUrl': {'multivalued': True,
                                      'name': 'accessUrl',
                                      'required': True},
                        'availability': {'multivalued': False, 'name': 'availability'},
                        'byteSize': {'multivalued': False,
                                     'name': 'byteSize',
                                     'range': 'nonNegativeInteger'},
                        'checksum': {'multivalued': False, 'name': 'checksum'},
                        'compressionFormat': {'multivalued': False,
                                              'name': 'compressionFormat'},
                        'format': {'multivalued': False, 'name': 'format'},
                        'hasPolicy': {'multivalued': False, 'name': 'hasPolicy'},
                        'licence': {'multivalued': False, 'name': 'licence'},
                        'mediaType': {'multivalued': False, 'name': 'mediaType'},
                        'modificationDate': {'multivalued': False,
                                             'name': 'modificationDate'},
                        'packagingFormat': {'multivalued': False,
                                            'name': 'packagingFormat'},
                        'releaseDate': {'multivalued': False, 'name': 'releaseDate'},
                        'rights': {'multivalued': False, 'name': 'rights'},
                        'spatialResolution': {'multivalued': False,
                                              'name': 'spatialResolution',
                                              'range': 'decimal'},
                        'status': {'multivalued': False, 'name': 'status'},
                        'temporalResolution': {'multivalued': False,
                                               'name': 'temporalResolution',
                                               'range': 'duration'}}})

    accessUrl: list[Resource] = Field(default=..., description="""A URL of the resource that gives access to a distribution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Distribution'], 'slot_uri': 'dcat:accessURL'} })
    accessService: Optional[list[DataService]] = Field(default=None, description="""A data service that provides access to the distribution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Distribution'], 'slot_uri': 'dcat:accessService'} })
    applicableLegislation: Optional[list[LegalResource]] = Field(default=None, description="""The legislation applicable to the resource (DCAT-AP extension).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dcatap:applicableLegislation'} })
    availability: Optional[Concept] = Field(default=None, description="""The availability level of the distribution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Distribution'], 'slot_uri': 'dcatap:availability'} })
    byteSize: Optional[int] = Field(default=None, description="""The size of a distribution in bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Distribution'], 'slot_uri': 'dcat:byteSize'} })
    checksum: Optional[Checksum] = Field(default=None, description="""A checksum of the distribution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Distribution'], 'slot_uri': 'spdx:checksum'} })
    compressionFormat: Optional[MediaType] = Field(default=None, description="""The compression format of the distribution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Distribution'], 'slot_uri': 'dcat:compressFormat'} })
    description: Optional[list[str]] = Field(default=None, description="""A free-text account of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dct:description'} })
    documentation: Optional[list[Document]] = Field(default=None, description="""A page or document about the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataService', 'Dataset', 'Distribution'],
         'slot_uri': 'foaf:page'} })
    downloadUrl: Optional[list[Resource]] = Field(default=None, description="""A URL of the downloadable file in a given format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Distribution'], 'slot_uri': 'dcat:downloadURL'} })
    format: Optional[MediaType] = Field(default=None, description="""The file format, physical medium, or dimensions of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataService', 'Distribution'], 'slot_uri': 'dct:format'} })
    hasPolicy: Optional[Policy] = Field(default=None, description="""An ODRL policy attached to the distribution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Distribution'], 'slot_uri': 'odrl:hasPolicy'} })
    language: Optional[list[LinguisticSystem]] = Field(default=None, description="""A language of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'CatalogueRecord', 'Dataset', 'Distribution'],
         'slot_uri': 'dct:language'} })
    licence: Optional[LicenceDocument] = Field(default=None, description="""A licence under which the resource is made available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'DataService', 'Distribution'],
         'slot_uri': 'dct:license'} })
    linkedSchemas: Optional[list[Standard]] = Field(default=None, description="""A schema that the distribution conforms to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Distribution'], 'slot_uri': 'dct:conformsTo'} })
    mediaType: Optional[MediaType] = Field(default=None, description="""The media type of the distribution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Distribution'], 'slot_uri': 'dcat:mediaType'} })
    modificationDate: Optional[datetime ] = Field(default=None, description="""The date on which the resource was changed. Approximated as xsd:dateTime (see DateOrDateTimeDataType_Shape gap in COMPARISON.md).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dct:modified'} })
    packagingFormat: Optional[MediaType] = Field(default=None, description="""The package format of the distribution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Distribution'], 'slot_uri': 'dcat:packageFormat'} })
    releaseDate: Optional[datetime ] = Field(default=None, description="""The date of formal issuance of the resource. The original DCAT-AP shape uses sh:or over xsd:date / xsd:dateTime / xsd:gYear / xsd:gYearMonth; LinkML can express only a single primary type, so this is approximated as xsd:dateTime.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries', 'Distribution'],
         'slot_uri': 'dct:issued'} })
    rights: Optional[RightsStatement] = Field(default=None, description="""Rights statement for the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue', 'Distribution'], 'slot_uri': 'dct:rights'} })
    spatialResolution: Optional[Decimal] = Field(default=None, description="""Minimum spatial separation resolvable, in meters.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'Distribution'],
         'slot_uri': 'dcat:spatialResolutionInMeters'} })
    status: Optional[Concept] = Field(default=None, description="""The status of the distribution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Distribution'], 'slot_uri': 'adms:status'} })
    temporalResolution: Optional[str] = Field(default=None, description="""Minimum time period resolvable in the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'Distribution'],
         'slot_uri': 'dcat:temporalResolution'} })
    title: Optional[list[str]] = Field(default=None, description="""A name given to the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dct:title'} })


class Document(Resource):
    """
    A foaf:Document.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'foaf:Document',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1'})

    pass


class Frequency(Resource):
    """
    A rate at which something recurs (DC Terms Frequency).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dct:Frequency',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1'})

    pass


class Geometry(Resource):
    """
    A spatial geometry (locn:Geometry).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'locn:Geometry',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1'})

    pass


class Identifier(ConfiguredBaseModel):
    """
    An identifier in a particular context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'adms:Identifier',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1',
         'slot_usage': {'notation': {'multivalued': False, 'name': 'notation'}}})

    notation: Optional[str] = Field(default=None, description="""A string used to identify a concept within a scheme.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Identifier'], 'slot_uri': 'skos:notation'} })


class Kind(Resource):
    """
    A vCard Kind.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'vcard:Kind',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1'})

    pass


class LegalResource(Resource):
    """
    A legal resource (ELI).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'eli:LegalResource',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1'})

    pass


class LicenceDocument(ConfiguredBaseModel):
    """
    A legal document giving official permission to do something with a resource.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dct:LicenseDocument',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1',
         'slot_usage': {'type': {'multivalued': True, 'name': 'type'}}})

    type: Optional[list[Concept]] = Field(default=None, description="""The nature or genre of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Agent', 'Dataset', 'LicenceDocument'], 'slot_uri': 'dct:type'} })


class LinguisticSystem(Resource):
    """
    A linguistic system (DC Terms LinguisticSystem).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dct:LinguisticSystem',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1'})

    pass


class Location(ConfiguredBaseModel):
    """
    A spatial region or named place.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dct:Location',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1',
         'slot_usage': {'bbox': {'multivalued': False, 'name': 'bbox'},
                        'centroid': {'multivalued': False, 'name': 'centroid'},
                        'geometry': {'multivalued': False, 'name': 'geometry'}}})

    bbox: Optional[str] = Field(default=None, description="""The geographic bounding box of a resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location'], 'slot_uri': 'dcat:bbox'} })
    centroid: Optional[str] = Field(default=None, description="""The geographic centroid of a resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location'], 'slot_uri': 'dcat:centroid'} })
    geometry: Optional[Geometry] = Field(default=None, description="""The geometry of a location.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location'], 'slot_uri': 'locn:geometry'} })


class MediaType(Resource):
    """
    An IANA media type (DC Terms MediaType).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dct:MediaType',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1'})

    pass


class PeriodOfTime(ConfiguredBaseModel):
    """
    An interval of time named or defined by its start and end.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dct:PeriodOfTime',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1',
         'slot_usage': {'beginning': {'multivalued': False, 'name': 'beginning'},
                        'end': {'multivalued': False, 'name': 'end'},
                        'endDate': {'multivalued': False, 'name': 'endDate'},
                        'startDate': {'multivalued': False, 'name': 'startDate'}}})

    beginning: Optional[str] = Field(default=None, description="""The start of a period of time.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PeriodOfTime'], 'slot_uri': 'time:hasBeginning'} })
    end: Optional[str] = Field(default=None, description="""The end of a period of time.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PeriodOfTime'], 'slot_uri': 'time:hasEnd'} })
    endDate: Optional[datetime ] = Field(default=None, description="""The end of the period. Approximated as xsd:dateTime.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PeriodOfTime'], 'slot_uri': 'dcat:endDate'} })
    startDate: Optional[datetime ] = Field(default=None, description="""The start of the period. Approximated as xsd:dateTime (see DateOrDateTimeDataType_Shape gap).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PeriodOfTime'], 'slot_uri': 'dcat:startDate'} })


class Policy(Resource):
    """
    An ODRL policy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'odrl:Policy',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1'})

    pass


class ProvenanceStatement(Resource):
    """
    A statement of provenance.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dct:ProvenanceStatement',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1'})

    pass


class Relationship(ConfiguredBaseModel):
    """
    An association between resources where one has a particular role.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dcat:Relationship',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1',
         'slot_usage': {'hadRole': {'multivalued': True,
                                    'name': 'hadRole',
                                    'required': True},
                        'relation': {'multivalued': True,
                                     'name': 'relation',
                                     'required': True}}})

    hadRole: list[Role] = Field(default=..., description="""The role of an agent in the relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'], 'slot_uri': 'dcat:hadRole'} })
    relation: list[Resource] = Field(default=..., description="""The resource related through this relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'], 'slot_uri': 'dct:relation'} })


class RightsStatement(Resource):
    """
    A statement about rights associated with a resource.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dct:RightsStatement',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1'})

    pass


class Role(Resource):
    """
    A role (dcat:Role).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dcat:Role',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1'})

    pass


class Standard(Resource):
    """
    A standard (DC Terms Standard).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dct:Standard',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1'})

    pass


class Activity(Resource):
    """
    A PROV activity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Activity',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1'})

    pass


class Attribution(Resource):
    """
    A PROV attribution.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Attribution',
         'from_schema': 'https://w3id.org/semic/dcat-ap/3.0.1'})

    pass


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Resource.model_rebuild()
CataloguedResource.model_rebuild()
Agent.model_rebuild()
Catalogue.model_rebuild()
CatalogueRecord.model_rebuild()
Checksum.model_rebuild()
ChecksumAlgorithm.model_rebuild()
Concept.model_rebuild()
ConceptScheme.model_rebuild()
DataService.model_rebuild()
Dataset.model_rebuild()
DatasetSeries.model_rebuild()
Distribution.model_rebuild()
Document.model_rebuild()
Frequency.model_rebuild()
Geometry.model_rebuild()
Identifier.model_rebuild()
Kind.model_rebuild()
LegalResource.model_rebuild()
LicenceDocument.model_rebuild()
LinguisticSystem.model_rebuild()
Location.model_rebuild()
MediaType.model_rebuild()
PeriodOfTime.model_rebuild()
Policy.model_rebuild()
ProvenanceStatement.model_rebuild()
Relationship.model_rebuild()
RightsStatement.model_rebuild()
Role.model_rebuild()
Standard.model_rebuild()
Activity.model_rebuild()
Attribution.model_rebuild()
