"""Public interface for the Authority ABI (n[act]) stage.

Defines the contract for generating an n[act] from a constitutionally valid
Authority Graph (:class:`NActGenerator`). The n[act] artifact itself is defined
in :mod:`authority_compiler.abi.artifacts`.
"""

from __future__ import annotations

import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from authority_compiler.abi.artifacts import NAct
    from authority_compiler.authority.artifacts import AuthorityGraph


class NActGenerator(abc.ABC):
    """Contract for generating an n[act] from an Authority Graph.

    Purpose:
        Transform a constitutionally valid
        :class:`~authority_compiler.authority.artifacts.AuthorityGraph` into an
        :class:`~authority_compiler.abi.artifacts.NAct`.

    Responsibilities:
        - Emit the Authority ABI (n[act]) for an admitted Authority Graph.
        - Produce output suitable for consumption by the Authority Runtime.

    Inputs:
        An :class:`~authority_compiler.authority.artifacts.AuthorityGraph` that
        has been admitted by the Constitutional Engine.

    Outputs:
        An :class:`~authority_compiler.abi.artifacts.NAct` artifact.

    Invariants:
        - Generation presupposes admissibility. The generator is invoked only on
          an Authority Graph the Constitutional Engine has admitted; it does not
          itself judge admissibility.
        - The generator emits; it does not alter the meaning of the graph it is
          given.
        - The emitted n[act] is determined solely by the input Authority Graph.
    """

    @abc.abstractmethod
    def generate(self, authority: AuthorityGraph) -> NAct:
        """Return the n[act] generated from the admitted ``authority`` graph."""
