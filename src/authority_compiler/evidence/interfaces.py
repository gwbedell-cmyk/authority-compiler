"""Public interface for the Evidence Graph stage.

Defines the contract for deriving an Evidence Graph from testimony
(:class:`EvidenceBuilder`). The Evidence Graph artifact itself is defined in
:mod:`authority_compiler.evidence.artifacts`.
"""

from __future__ import annotations

import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from authority_compiler.evidence.artifacts import EvidenceGraph
    from authority_compiler.testimony.artifacts import Testimony


class EvidenceBuilder(abc.ABC):
    """Contract for deriving an Evidence Graph from testimony.

    Purpose:
        Transform a
        :class:`~authority_compiler.testimony.artifacts.Testimony` into an
        :class:`~authority_compiler.evidence.artifacts.EvidenceGraph`.

    Responsibilities:
        - Structure testimony into evidence and the relationships between it.
        - Produce a graph suitable as input to the Authority Graph stage.

    Inputs:
        A :class:`~authority_compiler.testimony.artifacts.Testimony` artifact.

    Outputs:
        An :class:`~authority_compiler.evidence.artifacts.EvidenceGraph`
        artifact.

    Invariants:
        - The builder derives; it does not author. Every element of the produced
          graph is grounded in the supplied testimony.
        - The transformation depends only on its input testimony.
    """

    @abc.abstractmethod
    def build(self, testimony: Testimony) -> EvidenceGraph:
        """Return the Evidence Graph derived from ``testimony``."""
