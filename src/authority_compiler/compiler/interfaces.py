"""Public interface for the compilation pipeline orchestrator.

Defines the contract for the end-to-end pipeline (:class:`AuthorityCompiler`),
which composes the stage contracts into a single compilation.
"""

from __future__ import annotations

import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from authority_compiler.abi.interfaces import NAct
    from authority_compiler.testimony.interfaces import TestimonySource


class AuthorityCompiler(abc.ABC):
    """Contract for the end-to-end Authority compilation pipeline.

    Purpose:
        Orchestrate the ordered lowering of human testimony into an n[act],
        driving each stage in turn: testimony -> Evidence Graph -> Authority
        Graph -> constitutional evaluation -> n[act].

    Responsibilities:
        - Obtain testimony from a
          :class:`~authority_compiler.testimony.interfaces.TestimonySource`.
        - Drive the stage transformations in pipeline order.
        - Gate emission on the Constitutional Engine's verdict.

    Inputs:
        A :class:`~authority_compiler.testimony.interfaces.TestimonySource`
        supplying the testimony to compile.

    Outputs:
        An :class:`~authority_compiler.abi.interfaces.NAct` for testimony that
        compiles and is constitutionally admitted. The disposition of testimony
        that is not admitted is fixed by specification and is out of scope for
        this interface.

    Invariants:
        - Stages are driven strictly in pipeline order; no stage runs before its
          input has been produced.
        - No n[act] is emitted for an Authority Graph the Constitutional Engine
          does not admit.
        - Orchestration composes the stage contracts; it does not perform the
          work of any stage itself.
    """

    @abc.abstractmethod
    def compile(self, source: TestimonySource) -> NAct:
        """Compile the testimony provided by ``source`` into an n[act]."""
