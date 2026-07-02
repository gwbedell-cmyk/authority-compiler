"""Public interface for the Authority ABI (n[act]) stage.

Defines the n[act] artifact (:class:`NAct`), the compiler's emitted target
format, and the contract for generating it from a constitutionally valid
Authority Graph (:class:`NActGenerator`).

The representation of :class:`NAct` is fixed by specification, not by this
module; it is intentionally left opaque here.
"""

from __future__ import annotations

import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from authority_compiler.authority.interfaces import AuthorityGraph


class NAct(abc.ABC):
    """The n[act] artifact: the compiler's emitted target format.

    An opaque handle representing the Authority ABI produced by the compiler and
    consumed by the Authority Runtime. Its concrete representation is defined by
    the relevant ACS specification and is not fixed by this interface.
    """


class NActGenerator(abc.ABC):
    """Contract for generating an n[act] from an Authority Graph.

    Purpose:
        Transform a constitutionally valid
        :class:`~authority_compiler.authority.interfaces.AuthorityGraph` into an
        :class:`NAct`.

    Responsibilities:
        - Emit the Authority ABI (n[act]) for an admitted Authority Graph.
        - Produce output suitable for consumption by the Authority Runtime.

    Inputs:
        An :class:`~authority_compiler.authority.interfaces.AuthorityGraph` that
        has been admitted by the Constitutional Engine.

    Outputs:
        An :class:`NAct` artifact.

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
