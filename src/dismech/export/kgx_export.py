"""
KGX edge exporter for dismech.

Transforms disorder YAML files into KGX-format edges for the knowledge graph.
Each function extracts edges from a specific collection type within the disorder.
"""

import uuid
from typing import Any, Iterator

import koza
from koza import KozaTransform

from biolink_model.datamodel.pydanticmodel_v2 import (
    AgentTypeEnum,
    Association,
    KnowledgeLevelEnum,
)


# Knowledge source for all edges
KNOWLEDGE_SOURCE = "infores:dismech"


def _make_edge_id(subject: str, predicate: str, obj: str) -> str:
    """Generate a deterministic edge ID from subject, predicate, object."""
    # Use uuid5 with a namespace to create deterministic IDs
    namespace = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")  # URL namespace
    edge_string = f"{subject}|{predicate}|{obj}"
    return f"urn:uuid:{uuid.uuid5(namespace, edge_string)}"


def _get_term_id(obj: dict[str, Any] | None, path: list[str]) -> str | None:
    """
    Safely navigate a nested dict to extract a term ID.

    Args:
        obj: The object to navigate
        path: List of keys to traverse (e.g., ["term", "id"])

    Returns:
        The term ID string if found, None otherwise
    """
    if obj is None:
        return None
    current = obj
    for key in path:
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current if isinstance(current, str) else None


def phenotype_to_edge(disease_id: str, phenotype: dict[str, Any]) -> Association | None:
    """
    Convert a phenotype entry to a KGX edge.

    Args:
        disease_id: The disease term ID (e.g., "MONDO:0004979")
        phenotype: A phenotype dict from phenotypes[]

    Returns:
        Association or None if phenotype_term.term.id is missing
    """
    term_id = _get_term_id(phenotype, ["phenotype_term", "term", "id"])
    if not term_id:
        return None

    predicate = "biolink:has_phenotype"
    return Association(
        id=_make_edge_id(disease_id, predicate, term_id),
        subject=disease_id,
        predicate=predicate,
        object=term_id,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def cell_type_to_edge(disease_id: str, cell_type: dict[str, Any]) -> Association | None:
    """
    Convert a cell type entry to a KGX edge.

    Args:
        disease_id: The disease term ID
        cell_type: A cell type dict from pathophysiology[].cell_types[]

    Returns:
        Association or None if term.id is missing
    """
    term_id = _get_term_id(cell_type, ["term", "id"])
    if not term_id:
        return None

    predicate = "biolink:has_participant"
    return Association(
        id=_make_edge_id(disease_id, predicate, term_id),
        subject=disease_id,
        predicate=predicate,
        object=term_id,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def location_to_edge(disease_id: str, location: dict[str, Any]) -> Association | None:
    """
    Convert a location entry to a KGX edge.

    Args:
        disease_id: The disease term ID
        location: A location dict from pathophysiology[].locations[]

    Returns:
        Association or None if term.id is missing
    """
    term_id = _get_term_id(location, ["term", "id"])
    if not term_id:
        return None

    predicate = "biolink:located_in"
    return Association(
        id=_make_edge_id(disease_id, predicate, term_id),
        subject=disease_id,
        predicate=predicate,
        object=term_id,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def biological_process_to_edge(disease_id: str, process: dict[str, Any]) -> Association | None:
    """
    Convert a biological process entry to a KGX edge.

    Args:
        disease_id: The disease term ID
        process: A process dict from pathophysiology[].biological_processes[]

    Returns:
        Association or None if term.id is missing
    """
    term_id = _get_term_id(process, ["term", "id"])
    if not term_id:
        return None

    predicate = "biolink:has_participant"
    return Association(
        id=_make_edge_id(disease_id, predicate, term_id),
        subject=disease_id,
        predicate=predicate,
        object=term_id,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def treatment_to_edge(disease_id: str, treatment: dict[str, Any]) -> Association | None:
    """
    Convert a treatment entry to a KGX edge.

    Args:
        disease_id: The disease term ID
        treatment: A treatment dict from treatments[]

    Returns:
        Association or None if treatment_term.term.id is missing
    """
    term_id = _get_term_id(treatment, ["treatment_term", "term", "id"])
    if not term_id:
        return None

    predicate = "biolink:treated_by"
    return Association(
        id=_make_edge_id(disease_id, predicate, term_id),
        subject=disease_id,
        predicate=predicate,
        object=term_id,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def gene_to_edge(disease_id: str, gene: dict[str, Any]) -> Association | None:
    """
    Convert a genetic association entry to a KGX edge.

    Note: Gene entries use name (symbol) rather than term IDs.
    We create edges using HGNC symbol format.

    Args:
        disease_id: The disease term ID
        gene: A gene dict from genetic[]

    Returns:
        Association or None if name is missing
    """
    gene_name = gene.get("name") if gene else None
    if not gene_name:
        return None

    # Use HGNC symbol format for gene identifier
    gene_id = f"HGNC.SYMBOL:{gene_name}"
    predicate = "biolink:gene_associated_with_condition"

    return Association(
        id=_make_edge_id(gene_id, predicate, disease_id),
        subject=gene_id,
        predicate=predicate,
        object=disease_id,
        primary_knowledge_source=KNOWLEDGE_SOURCE,
        knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
        agent_type=AgentTypeEnum.manual_validation_of_automated_agent,
    )


def transform(record: dict[str, Any]) -> Iterator[Association]:
    """
    Extract all KGX edges from a disorder record.

    This is the pure function for extracting edges. It can be called directly
    for testing without the Koza runner.

    Args:
        record: A disorder dict loaded from YAML

    Yields:
        Association objects for all associations in the disorder
    """
    # Get disease ID - required for all edges
    disease_id = _get_term_id(record, ["disease_term", "term", "id"])
    if not disease_id:
        return

    # Extract phenotype edges
    for phenotype in record.get("phenotypes") or []:
        edge = phenotype_to_edge(disease_id, phenotype)
        if edge:
            yield edge

    # Extract edges from pathophysiology
    for patho in record.get("pathophysiology") or []:
        # Cell types
        for cell_type in patho.get("cell_types") or []:
            edge = cell_type_to_edge(disease_id, cell_type)
            if edge:
                yield edge

        # Locations
        for location in patho.get("locations") or []:
            edge = location_to_edge(disease_id, location)
            if edge:
                yield edge

        # Biological processes
        for process in patho.get("biological_processes") or []:
            edge = biological_process_to_edge(disease_id, process)
            if edge:
                yield edge

    # Extract treatment edges
    for treatment in record.get("treatments") or []:
        edge = treatment_to_edge(disease_id, treatment)
        if edge:
            yield edge

    # Extract gene association edges
    for gene in record.get("genetic") or []:
        edge = gene_to_edge(disease_id, gene)
        if edge:
            yield edge


@koza.transform_record()
def koza_transform(koza_ctx: KozaTransform, record: dict[str, Any]) -> None:
    """
    Koza-decorated transform that wraps the pure transform function.

    This function is called by the Koza runner for each record.
    It calls the pure transform() function and writes each edge.

    Args:
        koza_ctx: The Koza transform context for writing output
        record: A disorder dict loaded from YAML
    """
    for edge in transform(record):
        koza_ctx.write(edge)
