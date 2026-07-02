"""Public interface for the Authority Graph (IR) stage.

Defines the Authority Graph artifact (:class:`AuthorityGraph`), the compiler's
intermediate representation, and the contract for deriving it from an Evidence
Graph (:class:`AuthorityBuilder`).

The representation of :class:`AuthorityGraph` is fixed by specification, not by
this module; it is intentionally left opaque here.
"""

from __future__ import annotations

import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from authority_compiler.evidence.interfaces import EvidenceGraph


class AuthorityGraph(abc.ABC):
    """The Authority Graph artifact: the compiler's intermediate representation.

    An opaque handle representing authority as an intermediate representation,
    derived from the Evidence Graph and consumed by the Constitutional Engine.
    Its concrete representation is defined by the relevant ACS specification and
    is not fixed by this interface.
    """


class AuthorityBuilder(abc.ABC):
    """Contract for deriving an Authority Graph from an Evidence Graph.

    Purpose:
        Transform an
        :class:`~authority_compiler.evidence.interfaces.EvidenceGraph` into an
        :class:`AuthorityGraph`.

    Responsibilities:
        - Lower structured evidence into the compiler's intermediate
          representation.
        - Produce an Authority Graph suitable for constitutional evaluation.

    Inputs:
        An :class:`~authority_compiler.evidence.interfaces.EvidenceGraph`
        artifact.

    Outputs:
        An :class:`AuthorityGraph` artifact.

    Invariants:
        - The builder lowers; it does not evaluate admissibility. Judging the
          graph is the Constitutional Engine's responsibility, not this stage's.
        - The transformation depends only on its input Evidence Graph.
    """

    @abc.abstractmethod
    def build(self, evidence: EvidenceGraph) -> AuthorityGraph:
        """Return the Authority Graph derived from ``evidence``."""
