"""Public interface for the Constitutional Engine stage.

Defines the contract for constitutionally evaluating an Authority Graph
(:class:`ConstitutionalEngine`). The Constitutional Verdict artifact itself is
defined in :mod:`authority_compiler.constitutional.artifacts`.
"""

from __future__ import annotations

import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from authority_compiler.authority.artifacts import AuthorityGraph
    from authority_compiler.constitutional.artifacts import ConstitutionalVerdict


class ConstitutionalEngine(abc.ABC):
    """Contract for constitutionally evaluating an Authority Graph.

    Purpose:
        Evaluate an
        :class:`~authority_compiler.authority.artifacts.AuthorityGraph` and
        return a
        :class:`~authority_compiler.constitutional.artifacts.ConstitutionalVerdict`.

    Responsibilities:
        - Judge the admissibility of an Authority Graph against the
          constitutional rules.
        - Report the outcome as a verdict that carries its own grounds.

    Inputs:
        An :class:`~authority_compiler.authority.artifacts.AuthorityGraph`
        artifact.

    Outputs:
        A
        :class:`~authority_compiler.constitutional.artifacts.ConstitutionalVerdict`
        artifact.

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
