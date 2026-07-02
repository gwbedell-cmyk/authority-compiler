"""Public interface for the Human Testimony stage.

Defines the contract for providing testimony (:class:`TestimonySource`). The
testimony artifact itself is defined in
:mod:`authority_compiler.testimony.artifacts`.
"""

from __future__ import annotations

import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from authority_compiler.testimony.artifacts import Testimony


class TestimonySource(abc.ABC):
    """Contract for a source of testimony input.

    Purpose:
        Provide :class:`~authority_compiler.testimony.artifacts.Testimony` to
        the front of the compilation pipeline, independently of where that
        testimony originates.

    Responsibilities:
        - Yield a single, complete unit of testimony for one compilation.
        - Isolate the pipeline from the origin and encoding of that testimony.

    Inputs:
        None. A source is the origin of the pipeline; it obtains testimony by
        means private to the implementation.

    Outputs:
        A :class:`~authority_compiler.testimony.artifacts.Testimony` artifact.

    Invariants:
        - A source does not interpret, structure, or validate testimony; it only
          provides it.
        - The artifact returned is complete and self-contained with respect to a
          single compilation.
    """

    @abc.abstractmethod
    def read(self) -> Testimony:
        """Return the testimony this source provides."""
