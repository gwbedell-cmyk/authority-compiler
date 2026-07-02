"""Public interface for the Constitutional Engine stage.

Defines the Constitutional Verdict artifact (:class:`ConstitutionalVerdict`)
and the contract for producing it from an Authority Graph
(:class:`ConstitutionalEngine`).

The representation of :class:`ConstitutionalVerdict` is fixed by specification,
not by this module; it is intentionally left opaque here.
"""

from __future__ import annotations

import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from authority_compiler.authority.interfaces import AuthorityGraph


class ConstitutionalVerdict(abc.ABC):
    """The Constitutional Verdict artifact.

    An opaque handle representing the outcome of constitutionally evaluating an
    Authority Graph — whether the graph is admissible, together with the grounds
    for that outcome. Its concrete representation is defined by the relevant ACS
    specification and is not fixed by this interface.
    """


class ConstitutionalEngine(abc.ABC):
    """Contract for constitutionally evaluating an Authority Graph.

    Purpose:
        Evaluate an
        :class:`~authority_compiler.authority.interfaces.AuthorityGraph` and
        return a :class:`ConstitutionalVerdict`.

    Responsibilities:
        - Judge the admissibility of an Authority Graph against the
          constitutional rules.
        - Report the outcome as a verdict that carries its own grounds.

    Inputs:
        An :class:`~authority_compiler.authority.interfaces.AuthorityGraph`
        artifact.

    Outputs:
        A :class:`ConstitutionalVerdict` artifact.

    Invariants:
        - The engine evaluates; it does not transform. The Authority Graph it is
          given is not altered by evaluation.
        - Every verdict is determined solely by the input graph and the
          constitutional rules.
        - The engine is the sole authority on admissibility; no other stage
          judges a graph.
    """

    @abc.abstractmethod
    def evaluate(self, authority: AuthorityGraph) -> ConstitutionalVerdict:
        """Return the constitutional verdict for ``authority``."""
