-- # Abstract Class: Resource Description: Top-level abstract resource. Used as a generic node range when the DCAT-AP shape only constrains nodeKind to BlankNodeOrIRI/IRI without a specific class.
--     * Slot: id
-- # Abstract Class: CataloguedResource Description: Union of Catalogue, Dataset, DataService, DatasetSeries (a.k.a. dcat:Resource).
--     * Slot: id
-- # Class: Agent Description: An agent (e.g. a person, organisation) responsible for a resource.
--     * Slot: id
--     * Slot: type_id Description: The nature or genre of the resource.
-- # Class: Catalogue Description: A curated collection of metadata about resources (e.g. datasets and data services in the context of a data catalogue).
--     * Slot: id
--     * Slot: modificationDate Description: The date on which the resource was changed. Modelled as a DateOrDateTimeDataType disjunction (xsd:date | xsd:dateTime | xsd:gYear | xsd:gYearMonth) to match DCAT-AP's DateOrDateTimeDataType_Shape.
--     * Slot: releaseDate Description: The date of formal issuance of the resource. Modelled as a DateOrDateTimeDataType disjunction (xsd:date | xsd:dateTime | xsd:gYear | xsd:gYearMonth) to match DCAT-AP's DateOrDateTimeDataType_Shape.
--     * Slot: publisher_id Description: An entity responsible for making the resource available.
--     * Slot: creator_id Description: The entity responsible for producing the resource.
--     * Slot: homepage_id Description: A web page that is the primary access point for the resource.
--     * Slot: licence_id Description: A licence under which the resource is made available.
--     * Slot: rights_id Description: Rights statement for the resource.
-- # Class: CatalogueRecord Description: A description of a single entry in a data catalogue.
--     * Slot: id
--     * Slot: listingDate Description: The date on which the description was listed in the catalogue. Modelled as a DateOrDateTimeDataType disjunction (xsd:date | xsd:dateTime | xsd:gYear | xsd:gYearMonth) to match DCAT-AP's DateOrDateTimeDataType_Shape.
--     * Slot: modificationDate Description: The date on which the resource was changed. Modelled as a DateOrDateTimeDataType disjunction (xsd:date | xsd:dateTime | xsd:gYear | xsd:gYearMonth) to match DCAT-AP's DateOrDateTimeDataType_Shape.
--     * Slot: applicationProfile_id Description: The application profile this catalogue record conforms to.
--     * Slot: changeType_id Description: The type of update on the cataloged resource.
--     * Slot: primaryTopic_id Description: The resource described by this catalogue record.
--     * Slot: sourceMetadata_id Description: Original metadata source for the catalog record.
-- # Class: Checksum Description: A value that allows the contents of a file to be authenticated.
--     * Slot: id
--     * Slot: checksumValue Description: A lower-case hexadecimal-encoded checksum value.
--     * Slot: algorithm_id Description: The algorithm used to produce a checksum.
-- # Class: ChecksumAlgorithm Description: An algorithm used to produce a checksum.
--     * Slot: id
-- # Class: Concept Description: A concept (e.g. a category, theme, keyword).
--     * Slot: id
-- # Class: ConceptScheme Description: A controlled vocabulary or category scheme.
--     * Slot: id
-- # Class: DataService Description: A collection of operations that provides access to one or more datasets or data processing functions.
--     * Slot: id
--     * Slot: accessRights_id Description: Information about who can access the resource.
--     * Slot: licence_id Description: A licence under which the resource is made available.
--     * Slot: publisher_id Description: An entity responsible for making the resource available.
-- # Class: Dataset Description: A collection of data, published or curated by a single agent, and available for access or download in one or more representations.
--     * Slot: id
--     * Slot: modificationDate Description: The date on which the resource was changed. Modelled as a DateOrDateTimeDataType disjunction (xsd:date | xsd:dateTime | xsd:gYear | xsd:gYearMonth) to match DCAT-AP's DateOrDateTimeDataType_Shape.
--     * Slot: releaseDate Description: The date of formal issuance of the resource. Modelled as a DateOrDateTimeDataType disjunction (xsd:date | xsd:dateTime | xsd:gYear | xsd:gYearMonth) to match DCAT-AP's DateOrDateTimeDataType_Shape.
--     * Slot: spatialResolution Description: Minimum spatial separation resolvable, in meters.
--     * Slot: temporalResolution Description: Minimum time period resolvable in the dataset.
--     * Slot: version Description: The version indicator of a resource.
--     * Slot: accessRights_id Description: Information about who can access the resource.
--     * Slot: frequency_id Description: The frequency at which the dataset is updated.
--     * Slot: publisher_id Description: An entity responsible for making the resource available.
-- # Class: DatasetSeries Description: A collection of datasets that share a common schema and represent a change over time.
--     * Slot: id
--     * Slot: modificationDate Description: The date on which the resource was changed. Modelled as a DateOrDateTimeDataType disjunction (xsd:date | xsd:dateTime | xsd:gYear | xsd:gYearMonth) to match DCAT-AP's DateOrDateTimeDataType_Shape.
--     * Slot: releaseDate Description: The date of formal issuance of the resource. Modelled as a DateOrDateTimeDataType disjunction (xsd:date | xsd:dateTime | xsd:gYear | xsd:gYearMonth) to match DCAT-AP's DateOrDateTimeDataType_Shape.
--     * Slot: publisher_id Description: An entity responsible for making the resource available.
--     * Slot: frequency_id Description: The frequency at which the dataset is updated.
-- # Class: Distribution Description: A specific representation of a dataset (e.g. a downloadable file or an API access).
--     * Slot: id
--     * Slot: byteSize Description: The size of a distribution in bytes.
--     * Slot: modificationDate Description: The date on which the resource was changed. Modelled as a DateOrDateTimeDataType disjunction (xsd:date | xsd:dateTime | xsd:gYear | xsd:gYearMonth) to match DCAT-AP's DateOrDateTimeDataType_Shape.
--     * Slot: releaseDate Description: The date of formal issuance of the resource. Modelled as a DateOrDateTimeDataType disjunction (xsd:date | xsd:dateTime | xsd:gYear | xsd:gYearMonth) to match DCAT-AP's DateOrDateTimeDataType_Shape.
--     * Slot: spatialResolution Description: Minimum spatial separation resolvable, in meters.
--     * Slot: temporalResolution Description: Minimum time period resolvable in the dataset.
--     * Slot: availability_id Description: The availability level of the distribution.
--     * Slot: checksum_id Description: A checksum of the distribution.
--     * Slot: compressionFormat_id Description: The compression format of the distribution.
--     * Slot: format_id Description: The file format, physical medium, or dimensions of the resource.
--     * Slot: hasPolicy_id Description: An ODRL policy attached to the distribution.
--     * Slot: licence_id Description: A licence under which the resource is made available.
--     * Slot: mediaType_id Description: The media type of the distribution.
--     * Slot: packagingFormat_id Description: The package format of the distribution.
--     * Slot: rights_id Description: Rights statement for the resource.
--     * Slot: status_id Description: The status of the distribution.
-- # Class: Document Description: A foaf:Document.
--     * Slot: id
-- # Class: Frequency Description: A rate at which something recurs (DC Terms Frequency).
--     * Slot: id
-- # Class: Geometry Description: A spatial geometry (locn:Geometry).
--     * Slot: id
-- # Class: Identifier Description: An identifier in a particular context.
--     * Slot: id
--     * Slot: notation Description: A string used to identify a concept within a scheme.
-- # Class: Kind Description: A vCard Kind.
--     * Slot: id
-- # Class: LegalResource Description: A legal resource (ELI).
--     * Slot: id
-- # Class: LicenceDocument Description: A legal document giving official permission to do something with a resource.
--     * Slot: id
-- # Class: LinguisticSystem Description: A linguistic system (DC Terms LinguisticSystem).
--     * Slot: id
-- # Class: Location Description: A spatial region or named place.
--     * Slot: id
--     * Slot: bbox Description: The geographic bounding box of a resource.
--     * Slot: centroid Description: The geographic centroid of a resource.
--     * Slot: geometry_id Description: The geometry of a location.
-- # Class: MediaType Description: An IANA media type (DC Terms MediaType).
--     * Slot: id
-- # Class: PeriodOfTime Description: An interval of time named or defined by its start and end.
--     * Slot: id
--     * Slot: beginning Description: The start of a period of time.
--     * Slot: end Description: The end of a period of time.
--     * Slot: endDate Description: The end of the period. Modelled as a DateOrDateTimeDataType disjunction (xsd:date | xsd:dateTime | xsd:gYear | xsd:gYearMonth) to match DCAT-AP's DateOrDateTimeDataType_Shape.
--     * Slot: startDate Description: The start of the period. Modelled as a DateOrDateTimeDataType disjunction (xsd:date | xsd:dateTime | xsd:gYear | xsd:gYearMonth) to match DCAT-AP's DateOrDateTimeDataType_Shape.
-- # Class: Policy Description: An ODRL policy.
--     * Slot: id
-- # Class: ProvenanceStatement Description: A statement of provenance.
--     * Slot: id
-- # Class: Relationship Description: An association between resources where one has a particular role.
--     * Slot: id
-- # Class: RightsStatement Description: A statement about rights associated with a resource.
--     * Slot: id
-- # Class: Role Description: A role (dcat:Role).
--     * Slot: id
-- # Class: Standard Description: A standard (DC Terms Standard).
--     * Slot: id
-- # Class: Activity Description: A PROV activity.
--     * Slot: id
-- # Class: Attribution Description: A PROV attribution.
--     * Slot: id
-- # Class: Agent_name
--     * Slot: Agent_id Description: Autocreated FK slot
--     * Slot: name Description: A name for an agent.
-- # Class: Catalogue_title
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: title Description: A name given to the resource.
-- # Class: Catalogue_description
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: description Description: A free-text account of the resource.
-- # Class: Catalogue_applicableLegislation
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: applicableLegislation_id Description: The legislation applicable to the resource (DCAT-AP extension).
-- # Class: Catalogue_catalogue
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: catalogue_id Description: A subordinate catalogue contained in this catalogue.
-- # Class: Catalogue_dataset
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: dataset_id Description: A dataset listed by the catalogue.
-- # Class: Catalogue_geographicalCoverage
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: geographicalCoverage_id Description: The geographic coverage of the resource.
-- # Class: Catalogue_hasPart
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: hasPart_id Description: A related resource that is included physically or logically.
-- # Class: Catalogue_language
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: language_id Description: A language of the resource.
-- # Class: Catalogue_record
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: record_id Description: A record describing a registration of a resource in the catalogue.
-- # Class: Catalogue_service
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: service_id Description: A data service listed by the catalogue.
-- # Class: Catalogue_temporalCoverage
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: temporalCoverage_id Description: The temporal coverage of the resource.
-- # Class: Catalogue_themes
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: themes_id Description: A theme taxonomy used to classify the catalogue's resources.
-- # Class: CatalogueRecord_description
--     * Slot: CatalogueRecord_id Description: Autocreated FK slot
--     * Slot: description Description: A free-text account of the resource.
-- # Class: CatalogueRecord_language
--     * Slot: CatalogueRecord_id Description: Autocreated FK slot
--     * Slot: language_id Description: A language of the resource.
-- # Class: CatalogueRecord_title
--     * Slot: CatalogueRecord_id Description: Autocreated FK slot
--     * Slot: title Description: A name given to the resource.
-- # Class: Concept_preferredLabel
--     * Slot: Concept_id Description: Autocreated FK slot
--     * Slot: preferredLabel Description: The preferred lexical label for a resource.
-- # Class: ConceptScheme_title
--     * Slot: ConceptScheme_id Description: Autocreated FK slot
--     * Slot: title Description: A name given to the resource.
-- # Class: DataService_title
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: title Description: A name given to the resource.
-- # Class: DataService_description
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: description Description: A free-text account of the resource.
-- # Class: DataService_endpointUrl
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: endpointUrl_id Description: The root location of the service.
-- # Class: DataService_applicableLegislation
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: applicableLegislation_id Description: The legislation applicable to the resource (DCAT-AP extension).
-- # Class: DataService_conformsTo
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: conformsTo_id Description: An established standard the resource conforms to.
-- # Class: DataService_contactPoint
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: contactPoint_id Description: Contact information for the resource.
-- # Class: DataService_documentation
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: documentation_id Description: A page or document about the resource.
-- # Class: DataService_endpointDescription
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: endpointDescription_id Description: A description of the service endpoint, including operations.
-- # Class: DataService_format
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: format_id Description: The file format, physical medium, or dimensions of the resource.
-- # Class: DataService_keyword
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: DataService_landingPage
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: landingPage_id Description: A web page that gives access to the resource.
-- # Class: DataService_servesDataset
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: servesDataset_id Description: A dataset that this service serves.
-- # Class: DataService_theme
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: theme_id Description: A category of the resource.
-- # Class: Dataset_title
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: title Description: A name given to the resource.
-- # Class: Dataset_description
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: description Description: A free-text account of the resource.
-- # Class: Dataset_applicableLegislation
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: applicableLegislation_id Description: The legislation applicable to the resource (DCAT-AP extension).
-- # Class: Dataset_conformsTo
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: conformsTo_id Description: An established standard the resource conforms to.
-- # Class: Dataset_contactPoint
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: contactPoint_id Description: Contact information for the resource.
-- # Class: Dataset_creator
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: creator_id Description: The entity responsible for producing the resource.
-- # Class: Dataset_datasetDistribution
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: datasetDistribution_id Description: An available distribution of the dataset.
-- # Class: Dataset_documentation
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: documentation_id Description: A page or document about the resource.
-- # Class: Dataset_geographicalCoverage
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: geographicalCoverage_id Description: The geographic coverage of the resource.
-- # Class: Dataset_hasVersion
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: hasVersion_id Description: A related dataset that is a version of this dataset.
-- # Class: Dataset_identifier
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: identifier Description: A unique identifier of the resource.
-- # Class: Dataset_inSeries
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: inSeries_id Description: A dataset series of which this dataset is a part.
-- # Class: Dataset_isReferencedBy
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: isReferencedBy_id Description: A related resource that references the resource.
-- # Class: Dataset_keyword
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the resource.
-- # Class: Dataset_landingPage
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: landingPage_id Description: A web page that gives access to the resource.
-- # Class: Dataset_language
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: language_id Description: A language of the resource.
-- # Class: Dataset_otherIdentifier
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: otherIdentifier_id Description: A secondary identifier of the resource.
-- # Class: Dataset_provenance
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: provenance_id Description: A statement about provenance of the resource.
-- # Class: Dataset_qualifiedAttribution
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: qualifiedAttribution_id Description: An attribution of an agent to the resource.
-- # Class: Dataset_qualifiedRelation
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: qualifiedRelation_id Description: A qualified relationship to another resource.
-- # Class: Dataset_relatedResource
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: relatedResource_id Description: A related resource.
-- # Class: Dataset_sample
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: sample_id Description: A sample distribution of the dataset.
-- # Class: Dataset_source
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: source_id Description: A related resource from which the described resource is derived.
-- # Class: Dataset_temporalCoverage
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: temporalCoverage_id Description: The temporal coverage of the resource.
-- # Class: Dataset_theme
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: theme_id Description: A category of the resource.
-- # Class: Dataset_type
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: type_id Description: The nature or genre of the resource.
-- # Class: Dataset_versionNotes
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: versionNotes Description: A description of changes between versions.
-- # Class: Dataset_wasGeneratedBy
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: wasGeneratedBy_id Description: An activity that generated the resource.
-- # Class: DatasetSeries_title
--     * Slot: DatasetSeries_id Description: Autocreated FK slot
--     * Slot: title Description: A name given to the resource.
-- # Class: DatasetSeries_description
--     * Slot: DatasetSeries_id Description: Autocreated FK slot
--     * Slot: description Description: A free-text account of the resource.
-- # Class: DatasetSeries_applicableLegislation
--     * Slot: DatasetSeries_id Description: Autocreated FK slot
--     * Slot: applicableLegislation_id Description: The legislation applicable to the resource (DCAT-AP extension).
-- # Class: DatasetSeries_contactPoint
--     * Slot: DatasetSeries_id Description: Autocreated FK slot
--     * Slot: contactPoint_id Description: Contact information for the resource.
-- # Class: DatasetSeries_geographicalCoverage
--     * Slot: DatasetSeries_id Description: Autocreated FK slot
--     * Slot: geographicalCoverage_id Description: The geographic coverage of the resource.
-- # Class: DatasetSeries_temporalCoverage
--     * Slot: DatasetSeries_id Description: Autocreated FK slot
--     * Slot: temporalCoverage_id Description: The temporal coverage of the resource.
-- # Class: Distribution_accessUrl
--     * Slot: Distribution_id Description: Autocreated FK slot
--     * Slot: accessUrl_id Description: A URL of the resource that gives access to a distribution.
-- # Class: Distribution_accessService
--     * Slot: Distribution_id Description: Autocreated FK slot
--     * Slot: accessService_id Description: A data service that provides access to the distribution.
-- # Class: Distribution_applicableLegislation
--     * Slot: Distribution_id Description: Autocreated FK slot
--     * Slot: applicableLegislation_id Description: The legislation applicable to the resource (DCAT-AP extension).
-- # Class: Distribution_description
--     * Slot: Distribution_id Description: Autocreated FK slot
--     * Slot: description Description: A free-text account of the resource.
-- # Class: Distribution_documentation
--     * Slot: Distribution_id Description: Autocreated FK slot
--     * Slot: documentation_id Description: A page or document about the resource.
-- # Class: Distribution_downloadUrl
--     * Slot: Distribution_id Description: Autocreated FK slot
--     * Slot: downloadUrl_id Description: A URL of the downloadable file in a given format.
-- # Class: Distribution_language
--     * Slot: Distribution_id Description: Autocreated FK slot
--     * Slot: language_id Description: A language of the resource.
-- # Class: Distribution_linkedSchemas
--     * Slot: Distribution_id Description: Autocreated FK slot
--     * Slot: linkedSchemas_id Description: A schema that the distribution conforms to.
-- # Class: Distribution_title
--     * Slot: Distribution_id Description: Autocreated FK slot
--     * Slot: title Description: A name given to the resource.
-- # Class: LicenceDocument_type
--     * Slot: LicenceDocument_id Description: Autocreated FK slot
--     * Slot: type_id Description: The nature or genre of the resource.
-- # Class: Relationship_hadRole
--     * Slot: Relationship_id Description: Autocreated FK slot
--     * Slot: hadRole_id Description: The role of an agent in the relationship.
-- # Class: Relationship_relation
--     * Slot: Relationship_id Description: Autocreated FK slot
--     * Slot: relation_id Description: The resource related through this relationship.

CREATE TABLE "Resource" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Resource_id" ON "Resource" (id);

CREATE TABLE "CataloguedResource" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CataloguedResource_id" ON "CataloguedResource" (id);

CREATE TABLE "ChecksumAlgorithm" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ChecksumAlgorithm_id" ON "ChecksumAlgorithm" (id);

CREATE TABLE "Concept" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Concept_id" ON "Concept" (id);

CREATE TABLE "ConceptScheme" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ConceptScheme_id" ON "ConceptScheme" (id);

CREATE TABLE "Document" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Document_id" ON "Document" (id);

CREATE TABLE "Frequency" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Frequency_id" ON "Frequency" (id);

CREATE TABLE "Geometry" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Geometry_id" ON "Geometry" (id);

CREATE TABLE "Identifier" (
	id INTEGER NOT NULL,
	notation TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Identifier_id" ON "Identifier" (id);

CREATE TABLE "Kind" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Kind_id" ON "Kind" (id);

CREATE TABLE "LegalResource" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_LegalResource_id" ON "LegalResource" (id);

CREATE TABLE "LicenceDocument" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_LicenceDocument_id" ON "LicenceDocument" (id);

CREATE TABLE "LinguisticSystem" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_LinguisticSystem_id" ON "LinguisticSystem" (id);

CREATE TABLE "MediaType" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MediaType_id" ON "MediaType" (id);

CREATE TABLE "PeriodOfTime" (
	id INTEGER NOT NULL,
	beginning TEXT,
	"end" TEXT,
	"endDate" TEXT,
	"startDate" TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PeriodOfTime_id" ON "PeriodOfTime" (id);

CREATE TABLE "Policy" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Policy_id" ON "Policy" (id);

CREATE TABLE "ProvenanceStatement" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ProvenanceStatement_id" ON "ProvenanceStatement" (id);

CREATE TABLE "Relationship" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Relationship_id" ON "Relationship" (id);

CREATE TABLE "RightsStatement" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_RightsStatement_id" ON "RightsStatement" (id);

CREATE TABLE "Role" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Role_id" ON "Role" (id);

CREATE TABLE "Standard" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Standard_id" ON "Standard" (id);

CREATE TABLE "Activity" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Activity_id" ON "Activity" (id);

CREATE TABLE "Attribution" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Attribution_id" ON "Attribution" (id);

CREATE TABLE "Agent" (
	id INTEGER NOT NULL,
	type_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(type_id) REFERENCES "Concept" (id)
);
CREATE INDEX "ix_Agent_id" ON "Agent" (id);

CREATE TABLE "CatalogueRecord" (
	id INTEGER NOT NULL,
	"listingDate" TEXT,
	"modificationDate" TEXT NOT NULL,
	"applicationProfile_id" INTEGER,
	"changeType_id" INTEGER,
	"primaryTopic_id" INTEGER NOT NULL,
	"sourceMetadata_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("applicationProfile_id") REFERENCES "Standard" (id),
	FOREIGN KEY("changeType_id") REFERENCES "Concept" (id),
	FOREIGN KEY("primaryTopic_id") REFERENCES "CataloguedResource" (id),
	FOREIGN KEY("sourceMetadata_id") REFERENCES "CatalogueRecord" (id)
);
CREATE INDEX "ix_CatalogueRecord_id" ON "CatalogueRecord" (id);

CREATE TABLE "Checksum" (
	id INTEGER NOT NULL,
	"checksumValue" TEXT NOT NULL,
	algorithm_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(algorithm_id) REFERENCES "ChecksumAlgorithm" (id)
);
CREATE INDEX "ix_Checksum_id" ON "Checksum" (id);

CREATE TABLE "Location" (
	id INTEGER NOT NULL,
	bbox TEXT,
	centroid TEXT,
	geometry_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(geometry_id) REFERENCES "Geometry" (id)
);
CREATE INDEX "ix_Location_id" ON "Location" (id);

CREATE TABLE "Concept_preferredLabel" (
	"Concept_id" INTEGER,
	"preferredLabel" TEXT NOT NULL,
	PRIMARY KEY ("Concept_id", "preferredLabel"),
	FOREIGN KEY("Concept_id") REFERENCES "Concept" (id)
);
CREATE INDEX "ix_Concept_preferredLabel_Concept_id" ON "Concept_preferredLabel" ("Concept_id");
CREATE INDEX "ix_Concept_preferredLabel_preferredLabel" ON "Concept_preferredLabel" ("preferredLabel");

CREATE TABLE "ConceptScheme_title" (
	"ConceptScheme_id" INTEGER,
	title TEXT NOT NULL,
	PRIMARY KEY ("ConceptScheme_id", title),
	FOREIGN KEY("ConceptScheme_id") REFERENCES "ConceptScheme" (id)
);
CREATE INDEX "ix_ConceptScheme_title_ConceptScheme_id" ON "ConceptScheme_title" ("ConceptScheme_id");
CREATE INDEX "ix_ConceptScheme_title_title" ON "ConceptScheme_title" (title);

CREATE TABLE "LicenceDocument_type" (
	"LicenceDocument_id" INTEGER,
	type_id INTEGER,
	PRIMARY KEY ("LicenceDocument_id", type_id),
	FOREIGN KEY("LicenceDocument_id") REFERENCES "LicenceDocument" (id),
	FOREIGN KEY(type_id) REFERENCES "Concept" (id)
);
CREATE INDEX "ix_LicenceDocument_type_LicenceDocument_id" ON "LicenceDocument_type" ("LicenceDocument_id");
CREATE INDEX "ix_LicenceDocument_type_type_id" ON "LicenceDocument_type" (type_id);

CREATE TABLE "Relationship_hadRole" (
	"Relationship_id" INTEGER,
	"hadRole_id" INTEGER NOT NULL,
	PRIMARY KEY ("Relationship_id", "hadRole_id"),
	FOREIGN KEY("Relationship_id") REFERENCES "Relationship" (id),
	FOREIGN KEY("hadRole_id") REFERENCES "Role" (id)
);
CREATE INDEX "ix_Relationship_hadRole_hadRole_id" ON "Relationship_hadRole" ("hadRole_id");
CREATE INDEX "ix_Relationship_hadRole_Relationship_id" ON "Relationship_hadRole" ("Relationship_id");

CREATE TABLE "Relationship_relation" (
	"Relationship_id" INTEGER,
	relation_id INTEGER NOT NULL,
	PRIMARY KEY ("Relationship_id", relation_id),
	FOREIGN KEY("Relationship_id") REFERENCES "Relationship" (id),
	FOREIGN KEY(relation_id) REFERENCES "Resource" (id)
);
CREATE INDEX "ix_Relationship_relation_relation_id" ON "Relationship_relation" (relation_id);
CREATE INDEX "ix_Relationship_relation_Relationship_id" ON "Relationship_relation" ("Relationship_id");

CREATE TABLE "Catalogue" (
	id INTEGER NOT NULL,
	"modificationDate" TEXT,
	"releaseDate" TEXT,
	publisher_id INTEGER NOT NULL,
	creator_id INTEGER,
	homepage_id INTEGER,
	licence_id INTEGER,
	rights_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(publisher_id) REFERENCES "Agent" (id),
	FOREIGN KEY(creator_id) REFERENCES "Agent" (id),
	FOREIGN KEY(homepage_id) REFERENCES "Document" (id),
	FOREIGN KEY(licence_id) REFERENCES "LicenceDocument" (id),
	FOREIGN KEY(rights_id) REFERENCES "RightsStatement" (id)
);
CREATE INDEX "ix_Catalogue_id" ON "Catalogue" (id);

CREATE TABLE "DataService" (
	id INTEGER NOT NULL,
	"accessRights_id" INTEGER,
	licence_id INTEGER,
	publisher_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("accessRights_id") REFERENCES "RightsStatement" (id),
	FOREIGN KEY(licence_id) REFERENCES "LicenceDocument" (id),
	FOREIGN KEY(publisher_id) REFERENCES "Agent" (id)
);
CREATE INDEX "ix_DataService_id" ON "DataService" (id);

CREATE TABLE "Dataset" (
	id INTEGER NOT NULL,
	"modificationDate" TEXT,
	"releaseDate" TEXT,
	"spatialResolution" NUMERIC,
	"temporalResolution" TEXT,
	version TEXT,
	"accessRights_id" INTEGER,
	frequency_id INTEGER,
	publisher_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("accessRights_id") REFERENCES "RightsStatement" (id),
	FOREIGN KEY(frequency_id) REFERENCES "Frequency" (id),
	FOREIGN KEY(publisher_id) REFERENCES "Agent" (id)
);
CREATE INDEX "ix_Dataset_id" ON "Dataset" (id);

CREATE TABLE "DatasetSeries" (
	id INTEGER NOT NULL,
	"modificationDate" TEXT,
	"releaseDate" TEXT,
	publisher_id INTEGER,
	frequency_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(publisher_id) REFERENCES "Agent" (id),
	FOREIGN KEY(frequency_id) REFERENCES "Frequency" (id)
);
CREATE INDEX "ix_DatasetSeries_id" ON "DatasetSeries" (id);

CREATE TABLE "Distribution" (
	id INTEGER NOT NULL,
	"byteSize" INTEGER,
	"modificationDate" TEXT,
	"releaseDate" TEXT,
	"spatialResolution" NUMERIC,
	"temporalResolution" TEXT,
	availability_id INTEGER,
	checksum_id INTEGER,
	"compressionFormat_id" INTEGER,
	format_id INTEGER,
	"hasPolicy_id" INTEGER,
	licence_id INTEGER,
	"mediaType_id" INTEGER,
	"packagingFormat_id" INTEGER,
	rights_id INTEGER,
	status_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(availability_id) REFERENCES "Concept" (id),
	FOREIGN KEY(checksum_id) REFERENCES "Checksum" (id),
	FOREIGN KEY("compressionFormat_id") REFERENCES "MediaType" (id),
	FOREIGN KEY(format_id) REFERENCES "MediaType" (id),
	FOREIGN KEY("hasPolicy_id") REFERENCES "Policy" (id),
	FOREIGN KEY(licence_id) REFERENCES "LicenceDocument" (id),
	FOREIGN KEY("mediaType_id") REFERENCES "MediaType" (id),
	FOREIGN KEY("packagingFormat_id") REFERENCES "MediaType" (id),
	FOREIGN KEY(rights_id) REFERENCES "RightsStatement" (id),
	FOREIGN KEY(status_id) REFERENCES "Concept" (id)
);
CREATE INDEX "ix_Distribution_id" ON "Distribution" (id);

CREATE TABLE "Agent_name" (
	"Agent_id" INTEGER,
	name TEXT NOT NULL,
	PRIMARY KEY ("Agent_id", name),
	FOREIGN KEY("Agent_id") REFERENCES "Agent" (id)
);
CREATE INDEX "ix_Agent_name_name" ON "Agent_name" (name);
CREATE INDEX "ix_Agent_name_Agent_id" ON "Agent_name" ("Agent_id");

CREATE TABLE "CatalogueRecord_description" (
	"CatalogueRecord_id" INTEGER,
	description TEXT,
	PRIMARY KEY ("CatalogueRecord_id", description),
	FOREIGN KEY("CatalogueRecord_id") REFERENCES "CatalogueRecord" (id)
);
CREATE INDEX "ix_CatalogueRecord_description_CatalogueRecord_id" ON "CatalogueRecord_description" ("CatalogueRecord_id");
CREATE INDEX "ix_CatalogueRecord_description_description" ON "CatalogueRecord_description" (description);

CREATE TABLE "CatalogueRecord_language" (
	"CatalogueRecord_id" INTEGER,
	language_id INTEGER,
	PRIMARY KEY ("CatalogueRecord_id", language_id),
	FOREIGN KEY("CatalogueRecord_id") REFERENCES "CatalogueRecord" (id),
	FOREIGN KEY(language_id) REFERENCES "LinguisticSystem" (id)
);
CREATE INDEX "ix_CatalogueRecord_language_language_id" ON "CatalogueRecord_language" (language_id);
CREATE INDEX "ix_CatalogueRecord_language_CatalogueRecord_id" ON "CatalogueRecord_language" ("CatalogueRecord_id");

CREATE TABLE "CatalogueRecord_title" (
	"CatalogueRecord_id" INTEGER,
	title TEXT,
	PRIMARY KEY ("CatalogueRecord_id", title),
	FOREIGN KEY("CatalogueRecord_id") REFERENCES "CatalogueRecord" (id)
);
CREATE INDEX "ix_CatalogueRecord_title_title" ON "CatalogueRecord_title" (title);
CREATE INDEX "ix_CatalogueRecord_title_CatalogueRecord_id" ON "CatalogueRecord_title" ("CatalogueRecord_id");

CREATE TABLE "Catalogue_title" (
	"Catalogue_id" INTEGER,
	title TEXT NOT NULL,
	PRIMARY KEY ("Catalogue_id", title),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id)
);
CREATE INDEX "ix_Catalogue_title_Catalogue_id" ON "Catalogue_title" ("Catalogue_id");
CREATE INDEX "ix_Catalogue_title_title" ON "Catalogue_title" (title);

CREATE TABLE "Catalogue_description" (
	"Catalogue_id" INTEGER,
	description TEXT NOT NULL,
	PRIMARY KEY ("Catalogue_id", description),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id)
);
CREATE INDEX "ix_Catalogue_description_Catalogue_id" ON "Catalogue_description" ("Catalogue_id");
CREATE INDEX "ix_Catalogue_description_description" ON "Catalogue_description" (description);

CREATE TABLE "Catalogue_applicableLegislation" (
	"Catalogue_id" INTEGER,
	"applicableLegislation_id" INTEGER,
	PRIMARY KEY ("Catalogue_id", "applicableLegislation_id"),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id),
	FOREIGN KEY("applicableLegislation_id") REFERENCES "LegalResource" (id)
);
CREATE INDEX "ix_Catalogue_applicableLegislation_applicableLegislation_id" ON "Catalogue_applicableLegislation" ("applicableLegislation_id");
CREATE INDEX "ix_Catalogue_applicableLegislation_Catalogue_id" ON "Catalogue_applicableLegislation" ("Catalogue_id");

CREATE TABLE "Catalogue_catalogue" (
	"Catalogue_id" INTEGER,
	catalogue_id INTEGER,
	PRIMARY KEY ("Catalogue_id", catalogue_id),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id),
	FOREIGN KEY(catalogue_id) REFERENCES "Catalogue" (id)
);
CREATE INDEX "ix_Catalogue_catalogue_catalogue_id" ON "Catalogue_catalogue" (catalogue_id);
CREATE INDEX "ix_Catalogue_catalogue_Catalogue_id" ON "Catalogue_catalogue" ("Catalogue_id");

CREATE TABLE "Catalogue_dataset" (
	"Catalogue_id" INTEGER,
	dataset_id INTEGER,
	PRIMARY KEY ("Catalogue_id", dataset_id),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id),
	FOREIGN KEY(dataset_id) REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Catalogue_dataset_Catalogue_id" ON "Catalogue_dataset" ("Catalogue_id");
CREATE INDEX "ix_Catalogue_dataset_dataset_id" ON "Catalogue_dataset" (dataset_id);

CREATE TABLE "Catalogue_geographicalCoverage" (
	"Catalogue_id" INTEGER,
	"geographicalCoverage_id" INTEGER,
	PRIMARY KEY ("Catalogue_id", "geographicalCoverage_id"),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id),
	FOREIGN KEY("geographicalCoverage_id") REFERENCES "Location" (id)
);
CREATE INDEX "ix_Catalogue_geographicalCoverage_geographicalCoverage_id" ON "Catalogue_geographicalCoverage" ("geographicalCoverage_id");
CREATE INDEX "ix_Catalogue_geographicalCoverage_Catalogue_id" ON "Catalogue_geographicalCoverage" ("Catalogue_id");

CREATE TABLE "Catalogue_hasPart" (
	"Catalogue_id" INTEGER,
	"hasPart_id" INTEGER,
	PRIMARY KEY ("Catalogue_id", "hasPart_id"),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id),
	FOREIGN KEY("hasPart_id") REFERENCES "Catalogue" (id)
);
CREATE INDEX "ix_Catalogue_hasPart_Catalogue_id" ON "Catalogue_hasPart" ("Catalogue_id");
CREATE INDEX "ix_Catalogue_hasPart_hasPart_id" ON "Catalogue_hasPart" ("hasPart_id");

CREATE TABLE "Catalogue_language" (
	"Catalogue_id" INTEGER,
	language_id INTEGER,
	PRIMARY KEY ("Catalogue_id", language_id),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id),
	FOREIGN KEY(language_id) REFERENCES "LinguisticSystem" (id)
);
CREATE INDEX "ix_Catalogue_language_Catalogue_id" ON "Catalogue_language" ("Catalogue_id");
CREATE INDEX "ix_Catalogue_language_language_id" ON "Catalogue_language" (language_id);

CREATE TABLE "Catalogue_record" (
	"Catalogue_id" INTEGER,
	record_id INTEGER,
	PRIMARY KEY ("Catalogue_id", record_id),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id),
	FOREIGN KEY(record_id) REFERENCES "CatalogueRecord" (id)
);
CREATE INDEX "ix_Catalogue_record_record_id" ON "Catalogue_record" (record_id);
CREATE INDEX "ix_Catalogue_record_Catalogue_id" ON "Catalogue_record" ("Catalogue_id");

CREATE TABLE "Catalogue_service" (
	"Catalogue_id" INTEGER,
	service_id INTEGER,
	PRIMARY KEY ("Catalogue_id", service_id),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id),
	FOREIGN KEY(service_id) REFERENCES "DataService" (id)
);
CREATE INDEX "ix_Catalogue_service_service_id" ON "Catalogue_service" (service_id);
CREATE INDEX "ix_Catalogue_service_Catalogue_id" ON "Catalogue_service" ("Catalogue_id");

CREATE TABLE "Catalogue_temporalCoverage" (
	"Catalogue_id" INTEGER,
	"temporalCoverage_id" INTEGER,
	PRIMARY KEY ("Catalogue_id", "temporalCoverage_id"),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id),
	FOREIGN KEY("temporalCoverage_id") REFERENCES "PeriodOfTime" (id)
);
CREATE INDEX "ix_Catalogue_temporalCoverage_Catalogue_id" ON "Catalogue_temporalCoverage" ("Catalogue_id");
CREATE INDEX "ix_Catalogue_temporalCoverage_temporalCoverage_id" ON "Catalogue_temporalCoverage" ("temporalCoverage_id");

CREATE TABLE "Catalogue_themes" (
	"Catalogue_id" INTEGER,
	themes_id INTEGER,
	PRIMARY KEY ("Catalogue_id", themes_id),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id),
	FOREIGN KEY(themes_id) REFERENCES "ConceptScheme" (id)
);
CREATE INDEX "ix_Catalogue_themes_Catalogue_id" ON "Catalogue_themes" ("Catalogue_id");
CREATE INDEX "ix_Catalogue_themes_themes_id" ON "Catalogue_themes" (themes_id);

CREATE TABLE "DataService_title" (
	"DataService_id" INTEGER,
	title TEXT NOT NULL,
	PRIMARY KEY ("DataService_id", title),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id)
);
CREATE INDEX "ix_DataService_title_DataService_id" ON "DataService_title" ("DataService_id");
CREATE INDEX "ix_DataService_title_title" ON "DataService_title" (title);

CREATE TABLE "DataService_description" (
	"DataService_id" INTEGER,
	description TEXT,
	PRIMARY KEY ("DataService_id", description),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id)
);
CREATE INDEX "ix_DataService_description_DataService_id" ON "DataService_description" ("DataService_id");
CREATE INDEX "ix_DataService_description_description" ON "DataService_description" (description);

CREATE TABLE "DataService_endpointUrl" (
	"DataService_id" INTEGER,
	"endpointUrl_id" INTEGER NOT NULL,
	PRIMARY KEY ("DataService_id", "endpointUrl_id"),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id),
	FOREIGN KEY("endpointUrl_id") REFERENCES "Resource" (id)
);
CREATE INDEX "ix_DataService_endpointUrl_DataService_id" ON "DataService_endpointUrl" ("DataService_id");
CREATE INDEX "ix_DataService_endpointUrl_endpointUrl_id" ON "DataService_endpointUrl" ("endpointUrl_id");

CREATE TABLE "DataService_applicableLegislation" (
	"DataService_id" INTEGER,
	"applicableLegislation_id" INTEGER,
	PRIMARY KEY ("DataService_id", "applicableLegislation_id"),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id),
	FOREIGN KEY("applicableLegislation_id") REFERENCES "LegalResource" (id)
);
CREATE INDEX "ix_DataService_applicableLegislation_applicableLegislation_id" ON "DataService_applicableLegislation" ("applicableLegislation_id");
CREATE INDEX "ix_DataService_applicableLegislation_DataService_id" ON "DataService_applicableLegislation" ("DataService_id");

CREATE TABLE "DataService_conformsTo" (
	"DataService_id" INTEGER,
	"conformsTo_id" INTEGER,
	PRIMARY KEY ("DataService_id", "conformsTo_id"),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id),
	FOREIGN KEY("conformsTo_id") REFERENCES "Standard" (id)
);
CREATE INDEX "ix_DataService_conformsTo_conformsTo_id" ON "DataService_conformsTo" ("conformsTo_id");
CREATE INDEX "ix_DataService_conformsTo_DataService_id" ON "DataService_conformsTo" ("DataService_id");

CREATE TABLE "DataService_contactPoint" (
	"DataService_id" INTEGER,
	"contactPoint_id" INTEGER,
	PRIMARY KEY ("DataService_id", "contactPoint_id"),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id),
	FOREIGN KEY("contactPoint_id") REFERENCES "Kind" (id)
);
CREATE INDEX "ix_DataService_contactPoint_DataService_id" ON "DataService_contactPoint" ("DataService_id");
CREATE INDEX "ix_DataService_contactPoint_contactPoint_id" ON "DataService_contactPoint" ("contactPoint_id");

CREATE TABLE "DataService_documentation" (
	"DataService_id" INTEGER,
	documentation_id INTEGER,
	PRIMARY KEY ("DataService_id", documentation_id),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id),
	FOREIGN KEY(documentation_id) REFERENCES "Document" (id)
);
CREATE INDEX "ix_DataService_documentation_DataService_id" ON "DataService_documentation" ("DataService_id");
CREATE INDEX "ix_DataService_documentation_documentation_id" ON "DataService_documentation" (documentation_id);

CREATE TABLE "DataService_endpointDescription" (
	"DataService_id" INTEGER,
	"endpointDescription_id" INTEGER,
	PRIMARY KEY ("DataService_id", "endpointDescription_id"),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id),
	FOREIGN KEY("endpointDescription_id") REFERENCES "Resource" (id)
);
CREATE INDEX "ix_DataService_endpointDescription_endpointDescription_id" ON "DataService_endpointDescription" ("endpointDescription_id");
CREATE INDEX "ix_DataService_endpointDescription_DataService_id" ON "DataService_endpointDescription" ("DataService_id");

CREATE TABLE "DataService_format" (
	"DataService_id" INTEGER,
	format_id INTEGER,
	PRIMARY KEY ("DataService_id", format_id),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id),
	FOREIGN KEY(format_id) REFERENCES "MediaType" (id)
);
CREATE INDEX "ix_DataService_format_format_id" ON "DataService_format" (format_id);
CREATE INDEX "ix_DataService_format_DataService_id" ON "DataService_format" ("DataService_id");

CREATE TABLE "DataService_keyword" (
	"DataService_id" INTEGER,
	keyword TEXT,
	PRIMARY KEY ("DataService_id", keyword),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id)
);
CREATE INDEX "ix_DataService_keyword_keyword" ON "DataService_keyword" (keyword);
CREATE INDEX "ix_DataService_keyword_DataService_id" ON "DataService_keyword" ("DataService_id");

CREATE TABLE "DataService_landingPage" (
	"DataService_id" INTEGER,
	"landingPage_id" INTEGER,
	PRIMARY KEY ("DataService_id", "landingPage_id"),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id),
	FOREIGN KEY("landingPage_id") REFERENCES "Document" (id)
);
CREATE INDEX "ix_DataService_landingPage_DataService_id" ON "DataService_landingPage" ("DataService_id");
CREATE INDEX "ix_DataService_landingPage_landingPage_id" ON "DataService_landingPage" ("landingPage_id");

CREATE TABLE "DataService_servesDataset" (
	"DataService_id" INTEGER,
	"servesDataset_id" INTEGER,
	PRIMARY KEY ("DataService_id", "servesDataset_id"),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id),
	FOREIGN KEY("servesDataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_DataService_servesDataset_servesDataset_id" ON "DataService_servesDataset" ("servesDataset_id");
CREATE INDEX "ix_DataService_servesDataset_DataService_id" ON "DataService_servesDataset" ("DataService_id");

CREATE TABLE "DataService_theme" (
	"DataService_id" INTEGER,
	theme_id INTEGER,
	PRIMARY KEY ("DataService_id", theme_id),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id),
	FOREIGN KEY(theme_id) REFERENCES "Concept" (id)
);
CREATE INDEX "ix_DataService_theme_theme_id" ON "DataService_theme" (theme_id);
CREATE INDEX "ix_DataService_theme_DataService_id" ON "DataService_theme" ("DataService_id");

CREATE TABLE "Dataset_title" (
	"Dataset_id" INTEGER,
	title TEXT NOT NULL,
	PRIMARY KEY ("Dataset_id", title),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_title_title" ON "Dataset_title" (title);
CREATE INDEX "ix_Dataset_title_Dataset_id" ON "Dataset_title" ("Dataset_id");

CREATE TABLE "Dataset_description" (
	"Dataset_id" INTEGER,
	description TEXT NOT NULL,
	PRIMARY KEY ("Dataset_id", description),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_description_Dataset_id" ON "Dataset_description" ("Dataset_id");
CREATE INDEX "ix_Dataset_description_description" ON "Dataset_description" (description);

CREATE TABLE "Dataset_applicableLegislation" (
	"Dataset_id" INTEGER,
	"applicableLegislation_id" INTEGER,
	PRIMARY KEY ("Dataset_id", "applicableLegislation_id"),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("applicableLegislation_id") REFERENCES "LegalResource" (id)
);
CREATE INDEX "ix_Dataset_applicableLegislation_applicableLegislation_id" ON "Dataset_applicableLegislation" ("applicableLegislation_id");
CREATE INDEX "ix_Dataset_applicableLegislation_Dataset_id" ON "Dataset_applicableLegislation" ("Dataset_id");

CREATE TABLE "Dataset_conformsTo" (
	"Dataset_id" INTEGER,
	"conformsTo_id" INTEGER,
	PRIMARY KEY ("Dataset_id", "conformsTo_id"),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("conformsTo_id") REFERENCES "Standard" (id)
);
CREATE INDEX "ix_Dataset_conformsTo_conformsTo_id" ON "Dataset_conformsTo" ("conformsTo_id");
CREATE INDEX "ix_Dataset_conformsTo_Dataset_id" ON "Dataset_conformsTo" ("Dataset_id");

CREATE TABLE "Dataset_contactPoint" (
	"Dataset_id" INTEGER,
	"contactPoint_id" INTEGER,
	PRIMARY KEY ("Dataset_id", "contactPoint_id"),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("contactPoint_id") REFERENCES "Kind" (id)
);
CREATE INDEX "ix_Dataset_contactPoint_Dataset_id" ON "Dataset_contactPoint" ("Dataset_id");
CREATE INDEX "ix_Dataset_contactPoint_contactPoint_id" ON "Dataset_contactPoint" ("contactPoint_id");

CREATE TABLE "Dataset_creator" (
	"Dataset_id" INTEGER,
	creator_id INTEGER,
	PRIMARY KEY ("Dataset_id", creator_id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY(creator_id) REFERENCES "Agent" (id)
);
CREATE INDEX "ix_Dataset_creator_Dataset_id" ON "Dataset_creator" ("Dataset_id");
CREATE INDEX "ix_Dataset_creator_creator_id" ON "Dataset_creator" (creator_id);

CREATE TABLE "Dataset_datasetDistribution" (
	"Dataset_id" INTEGER,
	"datasetDistribution_id" INTEGER,
	PRIMARY KEY ("Dataset_id", "datasetDistribution_id"),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("datasetDistribution_id") REFERENCES "Distribution" (id)
);
CREATE INDEX "ix_Dataset_datasetDistribution_datasetDistribution_id" ON "Dataset_datasetDistribution" ("datasetDistribution_id");
CREATE INDEX "ix_Dataset_datasetDistribution_Dataset_id" ON "Dataset_datasetDistribution" ("Dataset_id");

CREATE TABLE "Dataset_documentation" (
	"Dataset_id" INTEGER,
	documentation_id INTEGER,
	PRIMARY KEY ("Dataset_id", documentation_id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY(documentation_id) REFERENCES "Document" (id)
);
CREATE INDEX "ix_Dataset_documentation_documentation_id" ON "Dataset_documentation" (documentation_id);
CREATE INDEX "ix_Dataset_documentation_Dataset_id" ON "Dataset_documentation" ("Dataset_id");

CREATE TABLE "Dataset_geographicalCoverage" (
	"Dataset_id" INTEGER,
	"geographicalCoverage_id" INTEGER,
	PRIMARY KEY ("Dataset_id", "geographicalCoverage_id"),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("geographicalCoverage_id") REFERENCES "Location" (id)
);
CREATE INDEX "ix_Dataset_geographicalCoverage_Dataset_id" ON "Dataset_geographicalCoverage" ("Dataset_id");
CREATE INDEX "ix_Dataset_geographicalCoverage_geographicalCoverage_id" ON "Dataset_geographicalCoverage" ("geographicalCoverage_id");

CREATE TABLE "Dataset_hasVersion" (
	"Dataset_id" INTEGER,
	"hasVersion_id" INTEGER,
	PRIMARY KEY ("Dataset_id", "hasVersion_id"),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("hasVersion_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_hasVersion_Dataset_id" ON "Dataset_hasVersion" ("Dataset_id");
CREATE INDEX "ix_Dataset_hasVersion_hasVersion_id" ON "Dataset_hasVersion" ("hasVersion_id");

CREATE TABLE "Dataset_identifier" (
	"Dataset_id" INTEGER,
	identifier TEXT,
	PRIMARY KEY ("Dataset_id", identifier),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_identifier_Dataset_id" ON "Dataset_identifier" ("Dataset_id");
CREATE INDEX "ix_Dataset_identifier_identifier" ON "Dataset_identifier" (identifier);

CREATE TABLE "Dataset_inSeries" (
	"Dataset_id" INTEGER,
	"inSeries_id" INTEGER,
	PRIMARY KEY ("Dataset_id", "inSeries_id"),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("inSeries_id") REFERENCES "DatasetSeries" (id)
);
CREATE INDEX "ix_Dataset_inSeries_inSeries_id" ON "Dataset_inSeries" ("inSeries_id");
CREATE INDEX "ix_Dataset_inSeries_Dataset_id" ON "Dataset_inSeries" ("Dataset_id");

CREATE TABLE "Dataset_isReferencedBy" (
	"Dataset_id" INTEGER,
	"isReferencedBy_id" INTEGER,
	PRIMARY KEY ("Dataset_id", "isReferencedBy_id"),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("isReferencedBy_id") REFERENCES "Resource" (id)
);
CREATE INDEX "ix_Dataset_isReferencedBy_Dataset_id" ON "Dataset_isReferencedBy" ("Dataset_id");
CREATE INDEX "ix_Dataset_isReferencedBy_isReferencedBy_id" ON "Dataset_isReferencedBy" ("isReferencedBy_id");

CREATE TABLE "Dataset_keyword" (
	"Dataset_id" INTEGER,
	keyword TEXT,
	PRIMARY KEY ("Dataset_id", keyword),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_keyword_Dataset_id" ON "Dataset_keyword" ("Dataset_id");
CREATE INDEX "ix_Dataset_keyword_keyword" ON "Dataset_keyword" (keyword);

CREATE TABLE "Dataset_landingPage" (
	"Dataset_id" INTEGER,
	"landingPage_id" INTEGER,
	PRIMARY KEY ("Dataset_id", "landingPage_id"),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("landingPage_id") REFERENCES "Document" (id)
);
CREATE INDEX "ix_Dataset_landingPage_Dataset_id" ON "Dataset_landingPage" ("Dataset_id");
CREATE INDEX "ix_Dataset_landingPage_landingPage_id" ON "Dataset_landingPage" ("landingPage_id");

CREATE TABLE "Dataset_language" (
	"Dataset_id" INTEGER,
	language_id INTEGER,
	PRIMARY KEY ("Dataset_id", language_id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY(language_id) REFERENCES "LinguisticSystem" (id)
);
CREATE INDEX "ix_Dataset_language_language_id" ON "Dataset_language" (language_id);
CREATE INDEX "ix_Dataset_language_Dataset_id" ON "Dataset_language" ("Dataset_id");

CREATE TABLE "Dataset_otherIdentifier" (
	"Dataset_id" INTEGER,
	"otherIdentifier_id" INTEGER,
	PRIMARY KEY ("Dataset_id", "otherIdentifier_id"),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("otherIdentifier_id") REFERENCES "Identifier" (id)
);
CREATE INDEX "ix_Dataset_otherIdentifier_Dataset_id" ON "Dataset_otherIdentifier" ("Dataset_id");
CREATE INDEX "ix_Dataset_otherIdentifier_otherIdentifier_id" ON "Dataset_otherIdentifier" ("otherIdentifier_id");

CREATE TABLE "Dataset_provenance" (
	"Dataset_id" INTEGER,
	provenance_id INTEGER,
	PRIMARY KEY ("Dataset_id", provenance_id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY(provenance_id) REFERENCES "ProvenanceStatement" (id)
);
CREATE INDEX "ix_Dataset_provenance_Dataset_id" ON "Dataset_provenance" ("Dataset_id");
CREATE INDEX "ix_Dataset_provenance_provenance_id" ON "Dataset_provenance" (provenance_id);

CREATE TABLE "Dataset_qualifiedAttribution" (
	"Dataset_id" INTEGER,
	"qualifiedAttribution_id" INTEGER,
	PRIMARY KEY ("Dataset_id", "qualifiedAttribution_id"),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("qualifiedAttribution_id") REFERENCES "Attribution" (id)
);
CREATE INDEX "ix_Dataset_qualifiedAttribution_qualifiedAttribution_id" ON "Dataset_qualifiedAttribution" ("qualifiedAttribution_id");
CREATE INDEX "ix_Dataset_qualifiedAttribution_Dataset_id" ON "Dataset_qualifiedAttribution" ("Dataset_id");

CREATE TABLE "Dataset_qualifiedRelation" (
	"Dataset_id" INTEGER,
	"qualifiedRelation_id" INTEGER,
	PRIMARY KEY ("Dataset_id", "qualifiedRelation_id"),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("qualifiedRelation_id") REFERENCES "Relationship" (id)
);
CREATE INDEX "ix_Dataset_qualifiedRelation_qualifiedRelation_id" ON "Dataset_qualifiedRelation" ("qualifiedRelation_id");
CREATE INDEX "ix_Dataset_qualifiedRelation_Dataset_id" ON "Dataset_qualifiedRelation" ("Dataset_id");

CREATE TABLE "Dataset_relatedResource" (
	"Dataset_id" INTEGER,
	"relatedResource_id" INTEGER,
	PRIMARY KEY ("Dataset_id", "relatedResource_id"),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("relatedResource_id") REFERENCES "Resource" (id)
);
CREATE INDEX "ix_Dataset_relatedResource_Dataset_id" ON "Dataset_relatedResource" ("Dataset_id");
CREATE INDEX "ix_Dataset_relatedResource_relatedResource_id" ON "Dataset_relatedResource" ("relatedResource_id");

CREATE TABLE "Dataset_sample" (
	"Dataset_id" INTEGER,
	sample_id INTEGER,
	PRIMARY KEY ("Dataset_id", sample_id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY(sample_id) REFERENCES "Distribution" (id)
);
CREATE INDEX "ix_Dataset_sample_sample_id" ON "Dataset_sample" (sample_id);
CREATE INDEX "ix_Dataset_sample_Dataset_id" ON "Dataset_sample" ("Dataset_id");

CREATE TABLE "Dataset_source" (
	"Dataset_id" INTEGER,
	source_id INTEGER,
	PRIMARY KEY ("Dataset_id", source_id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY(source_id) REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_source_Dataset_id" ON "Dataset_source" ("Dataset_id");
CREATE INDEX "ix_Dataset_source_source_id" ON "Dataset_source" (source_id);

CREATE TABLE "Dataset_temporalCoverage" (
	"Dataset_id" INTEGER,
	"temporalCoverage_id" INTEGER,
	PRIMARY KEY ("Dataset_id", "temporalCoverage_id"),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("temporalCoverage_id") REFERENCES "PeriodOfTime" (id)
);
CREATE INDEX "ix_Dataset_temporalCoverage_Dataset_id" ON "Dataset_temporalCoverage" ("Dataset_id");
CREATE INDEX "ix_Dataset_temporalCoverage_temporalCoverage_id" ON "Dataset_temporalCoverage" ("temporalCoverage_id");

CREATE TABLE "Dataset_theme" (
	"Dataset_id" INTEGER,
	theme_id INTEGER,
	PRIMARY KEY ("Dataset_id", theme_id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY(theme_id) REFERENCES "Concept" (id)
);
CREATE INDEX "ix_Dataset_theme_theme_id" ON "Dataset_theme" (theme_id);
CREATE INDEX "ix_Dataset_theme_Dataset_id" ON "Dataset_theme" ("Dataset_id");

CREATE TABLE "Dataset_type" (
	"Dataset_id" INTEGER,
	type_id INTEGER,
	PRIMARY KEY ("Dataset_id", type_id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY(type_id) REFERENCES "Concept" (id)
);
CREATE INDEX "ix_Dataset_type_type_id" ON "Dataset_type" (type_id);
CREATE INDEX "ix_Dataset_type_Dataset_id" ON "Dataset_type" ("Dataset_id");

CREATE TABLE "Dataset_versionNotes" (
	"Dataset_id" INTEGER,
	"versionNotes" TEXT,
	PRIMARY KEY ("Dataset_id", "versionNotes"),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_versionNotes_versionNotes" ON "Dataset_versionNotes" ("versionNotes");
CREATE INDEX "ix_Dataset_versionNotes_Dataset_id" ON "Dataset_versionNotes" ("Dataset_id");

CREATE TABLE "Dataset_wasGeneratedBy" (
	"Dataset_id" INTEGER,
	"wasGeneratedBy_id" INTEGER,
	PRIMARY KEY ("Dataset_id", "wasGeneratedBy_id"),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("wasGeneratedBy_id") REFERENCES "Activity" (id)
);
CREATE INDEX "ix_Dataset_wasGeneratedBy_Dataset_id" ON "Dataset_wasGeneratedBy" ("Dataset_id");
CREATE INDEX "ix_Dataset_wasGeneratedBy_wasGeneratedBy_id" ON "Dataset_wasGeneratedBy" ("wasGeneratedBy_id");

CREATE TABLE "DatasetSeries_title" (
	"DatasetSeries_id" INTEGER,
	title TEXT NOT NULL,
	PRIMARY KEY ("DatasetSeries_id", title),
	FOREIGN KEY("DatasetSeries_id") REFERENCES "DatasetSeries" (id)
);
CREATE INDEX "ix_DatasetSeries_title_title" ON "DatasetSeries_title" (title);
CREATE INDEX "ix_DatasetSeries_title_DatasetSeries_id" ON "DatasetSeries_title" ("DatasetSeries_id");

CREATE TABLE "DatasetSeries_description" (
	"DatasetSeries_id" INTEGER,
	description TEXT NOT NULL,
	PRIMARY KEY ("DatasetSeries_id", description),
	FOREIGN KEY("DatasetSeries_id") REFERENCES "DatasetSeries" (id)
);
CREATE INDEX "ix_DatasetSeries_description_DatasetSeries_id" ON "DatasetSeries_description" ("DatasetSeries_id");
CREATE INDEX "ix_DatasetSeries_description_description" ON "DatasetSeries_description" (description);

CREATE TABLE "DatasetSeries_applicableLegislation" (
	"DatasetSeries_id" INTEGER,
	"applicableLegislation_id" INTEGER,
	PRIMARY KEY ("DatasetSeries_id", "applicableLegislation_id"),
	FOREIGN KEY("DatasetSeries_id") REFERENCES "DatasetSeries" (id),
	FOREIGN KEY("applicableLegislation_id") REFERENCES "LegalResource" (id)
);
CREATE INDEX "ix_DatasetSeries_applicableLegislation_applicableLegislation_id" ON "DatasetSeries_applicableLegislation" ("applicableLegislation_id");
CREATE INDEX "ix_DatasetSeries_applicableLegislation_DatasetSeries_id" ON "DatasetSeries_applicableLegislation" ("DatasetSeries_id");

CREATE TABLE "DatasetSeries_contactPoint" (
	"DatasetSeries_id" INTEGER,
	"contactPoint_id" INTEGER,
	PRIMARY KEY ("DatasetSeries_id", "contactPoint_id"),
	FOREIGN KEY("DatasetSeries_id") REFERENCES "DatasetSeries" (id),
	FOREIGN KEY("contactPoint_id") REFERENCES "Kind" (id)
);
CREATE INDEX "ix_DatasetSeries_contactPoint_DatasetSeries_id" ON "DatasetSeries_contactPoint" ("DatasetSeries_id");
CREATE INDEX "ix_DatasetSeries_contactPoint_contactPoint_id" ON "DatasetSeries_contactPoint" ("contactPoint_id");

CREATE TABLE "DatasetSeries_geographicalCoverage" (
	"DatasetSeries_id" INTEGER,
	"geographicalCoverage_id" INTEGER,
	PRIMARY KEY ("DatasetSeries_id", "geographicalCoverage_id"),
	FOREIGN KEY("DatasetSeries_id") REFERENCES "DatasetSeries" (id),
	FOREIGN KEY("geographicalCoverage_id") REFERENCES "Location" (id)
);
CREATE INDEX "ix_DatasetSeries_geographicalCoverage_geographicalCoverage_id" ON "DatasetSeries_geographicalCoverage" ("geographicalCoverage_id");
CREATE INDEX "ix_DatasetSeries_geographicalCoverage_DatasetSeries_id" ON "DatasetSeries_geographicalCoverage" ("DatasetSeries_id");

CREATE TABLE "DatasetSeries_temporalCoverage" (
	"DatasetSeries_id" INTEGER,
	"temporalCoverage_id" INTEGER,
	PRIMARY KEY ("DatasetSeries_id", "temporalCoverage_id"),
	FOREIGN KEY("DatasetSeries_id") REFERENCES "DatasetSeries" (id),
	FOREIGN KEY("temporalCoverage_id") REFERENCES "PeriodOfTime" (id)
);
CREATE INDEX "ix_DatasetSeries_temporalCoverage_temporalCoverage_id" ON "DatasetSeries_temporalCoverage" ("temporalCoverage_id");
CREATE INDEX "ix_DatasetSeries_temporalCoverage_DatasetSeries_id" ON "DatasetSeries_temporalCoverage" ("DatasetSeries_id");

CREATE TABLE "Distribution_accessUrl" (
	"Distribution_id" INTEGER,
	"accessUrl_id" INTEGER NOT NULL,
	PRIMARY KEY ("Distribution_id", "accessUrl_id"),
	FOREIGN KEY("Distribution_id") REFERENCES "Distribution" (id),
	FOREIGN KEY("accessUrl_id") REFERENCES "Resource" (id)
);
CREATE INDEX "ix_Distribution_accessUrl_Distribution_id" ON "Distribution_accessUrl" ("Distribution_id");
CREATE INDEX "ix_Distribution_accessUrl_accessUrl_id" ON "Distribution_accessUrl" ("accessUrl_id");

CREATE TABLE "Distribution_accessService" (
	"Distribution_id" INTEGER,
	"accessService_id" INTEGER,
	PRIMARY KEY ("Distribution_id", "accessService_id"),
	FOREIGN KEY("Distribution_id") REFERENCES "Distribution" (id),
	FOREIGN KEY("accessService_id") REFERENCES "DataService" (id)
);
CREATE INDEX "ix_Distribution_accessService_Distribution_id" ON "Distribution_accessService" ("Distribution_id");
CREATE INDEX "ix_Distribution_accessService_accessService_id" ON "Distribution_accessService" ("accessService_id");

CREATE TABLE "Distribution_applicableLegislation" (
	"Distribution_id" INTEGER,
	"applicableLegislation_id" INTEGER,
	PRIMARY KEY ("Distribution_id", "applicableLegislation_id"),
	FOREIGN KEY("Distribution_id") REFERENCES "Distribution" (id),
	FOREIGN KEY("applicableLegislation_id") REFERENCES "LegalResource" (id)
);
CREATE INDEX "ix_Distribution_applicableLegislation_applicableLegislation_id" ON "Distribution_applicableLegislation" ("applicableLegislation_id");
CREATE INDEX "ix_Distribution_applicableLegislation_Distribution_id" ON "Distribution_applicableLegislation" ("Distribution_id");

CREATE TABLE "Distribution_description" (
	"Distribution_id" INTEGER,
	description TEXT,
	PRIMARY KEY ("Distribution_id", description),
	FOREIGN KEY("Distribution_id") REFERENCES "Distribution" (id)
);
CREATE INDEX "ix_Distribution_description_Distribution_id" ON "Distribution_description" ("Distribution_id");
CREATE INDEX "ix_Distribution_description_description" ON "Distribution_description" (description);

CREATE TABLE "Distribution_documentation" (
	"Distribution_id" INTEGER,
	documentation_id INTEGER,
	PRIMARY KEY ("Distribution_id", documentation_id),
	FOREIGN KEY("Distribution_id") REFERENCES "Distribution" (id),
	FOREIGN KEY(documentation_id) REFERENCES "Document" (id)
);
CREATE INDEX "ix_Distribution_documentation_Distribution_id" ON "Distribution_documentation" ("Distribution_id");
CREATE INDEX "ix_Distribution_documentation_documentation_id" ON "Distribution_documentation" (documentation_id);

CREATE TABLE "Distribution_downloadUrl" (
	"Distribution_id" INTEGER,
	"downloadUrl_id" INTEGER,
	PRIMARY KEY ("Distribution_id", "downloadUrl_id"),
	FOREIGN KEY("Distribution_id") REFERENCES "Distribution" (id),
	FOREIGN KEY("downloadUrl_id") REFERENCES "Resource" (id)
);
CREATE INDEX "ix_Distribution_downloadUrl_Distribution_id" ON "Distribution_downloadUrl" ("Distribution_id");
CREATE INDEX "ix_Distribution_downloadUrl_downloadUrl_id" ON "Distribution_downloadUrl" ("downloadUrl_id");

CREATE TABLE "Distribution_language" (
	"Distribution_id" INTEGER,
	language_id INTEGER,
	PRIMARY KEY ("Distribution_id", language_id),
	FOREIGN KEY("Distribution_id") REFERENCES "Distribution" (id),
	FOREIGN KEY(language_id) REFERENCES "LinguisticSystem" (id)
);
CREATE INDEX "ix_Distribution_language_language_id" ON "Distribution_language" (language_id);
CREATE INDEX "ix_Distribution_language_Distribution_id" ON "Distribution_language" ("Distribution_id");

CREATE TABLE "Distribution_linkedSchemas" (
	"Distribution_id" INTEGER,
	"linkedSchemas_id" INTEGER,
	PRIMARY KEY ("Distribution_id", "linkedSchemas_id"),
	FOREIGN KEY("Distribution_id") REFERENCES "Distribution" (id),
	FOREIGN KEY("linkedSchemas_id") REFERENCES "Standard" (id)
);
CREATE INDEX "ix_Distribution_linkedSchemas_linkedSchemas_id" ON "Distribution_linkedSchemas" ("linkedSchemas_id");
CREATE INDEX "ix_Distribution_linkedSchemas_Distribution_id" ON "Distribution_linkedSchemas" ("Distribution_id");

CREATE TABLE "Distribution_title" (
	"Distribution_id" INTEGER,
	title TEXT,
	PRIMARY KEY ("Distribution_id", title),
	FOREIGN KEY("Distribution_id") REFERENCES "Distribution" (id)
);
CREATE INDEX "ix_Distribution_title_Distribution_id" ON "Distribution_title" ("Distribution_id");
CREATE INDEX "ix_Distribution_title_title" ON "Distribution_title" (title);
