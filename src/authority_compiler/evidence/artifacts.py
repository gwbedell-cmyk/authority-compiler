"""Evidence Graph artifact: the structured-evidence value object.

Defines :class:`EvidenceGraph`, the immutable artifact produced from testimony.
Its structural content is owned by the Authority Computing Standards and is not
modeled here.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EvidenceGraph:
    """The Evidence Graph artifact.

    Purpose:
        Represent, as an immutable value, testimony after it has been structured
        into evidence and the relationships between it.

    Universal fields:
        None. The graph's constituents are not universal independently of their
        specified representation.

    Deferred structure:
        The nodes, edges, and evidentiary relationships that constitute an
        Evidence Graph are owned by ACS-004 (Evidence Graph Specification).
        Fields are introduced only when ACS-004 fixes them.
    """

    # Placeholder -- deferred to ACS-004.
    # No structural fields are modeled until that standard fixes them.
