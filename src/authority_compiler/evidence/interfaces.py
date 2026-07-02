"""Public interface for the Evidence Graph stage.

Defines the Evidence Graph artifact (:class:`EvidenceGraph`) and the contract
for deriving it from testimony (:class:`EvidenceBuilder`).

The representation of :class:`EvidenceGraph` is fixed by specification, not by
this module; it is intentionally left opaque here.
"""

from __future__ import annotations

import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from authority_compiler.testimony.interfaces import Testimony


class EvidenceGraph(abc.ABC):
    """The Evidence Graph artifact.

    An opaque handle representing testimony after it has been structured into
    evidence and the relationships between it. Its concrete representation is
    defined by the relevant ACS specification and is not fixed by this
    interface.
    """


class EvidenceBuilder(abc.ABC):
    """Contract for deriving an Evidence Graph from testimony.

    Purpose:
        Transform :class:`~authority_compiler.testimony.interfaces.Testimony`
        into an :class:`EvidenceGraph`.

    Responsibilities:
        - Structure testimony into evidence and the relationships between it.
        - Produce a graph suitable as input to the Authority Graph stage.

    Inputs:
        A :class:`~authority_compiler.testimony.interfaces.Testimony` artifact.

    Outputs:
        An :class:`EvidenceGraph` artifact.

    Invariants:
        - The builder derives; it does not author. Every element of the produced
          graph is grounded in the supplied testimony.
        - The transformation depends only on its input testimony.
    """

    @abc.abstractmethod
    def build(self, testimony: Testimony) -> EvidenceGraph:
        """Return the Evidence Graph derived from ``testimony``."""
