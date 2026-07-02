"""Public interface for the Authority Graph (IR) stage.

Defines the contract for deriving an Authority Graph from an Evidence Graph
(:class:`AuthorityBuilder`). The Authority Graph artifact itself is defined in
:mod:`authority_compiler.authority.artifacts`.
"""

from __future__ import annotations

import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from authority_compiler.authority.artifacts import AuthorityGraph
    from authority_compiler.evidence.artifacts import EvidenceGraph


class AuthorityBuilder(abc.ABC):
    """Contract for deriving an Authority Graph from an Evidence Graph.

    Purpose:
        Transform an
        :class:`~authority_compiler.evidence.artifacts.EvidenceGraph` into an
        :class:`~authority_compiler.authority.artifacts.AuthorityGraph`.

    Responsibilities:
        - Lower structured evidence into the compiler's intermediate
          representation.
        - Produce an Authority Graph suitable for constitutional evaluation.

    Inputs:
        An :class:`~authority_compiler.evidence.artifacts.EvidenceGraph`
        artifact.

    Outputs:
        An :class:`~authority_compiler.authority.artifacts.AuthorityGraph`
        artifact.

    Invariants:
        - The builder lowers; it does not evaluate admissibility. Judging the
          graph is the Constitutional Engine's responsibility, not this stage's.
        - The transformation depends only on its input Evidence Graph.
    """

    @abc.abstractmethod
    def build(self, evidence: EvidenceGraph) -> AuthorityGraph:
        """Return the Authority Graph derived from ``evidence``."""
