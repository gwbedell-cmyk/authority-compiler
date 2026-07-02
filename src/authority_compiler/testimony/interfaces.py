"""Public interface for the Human Testimony stage.

Defines the source-language artifact (:class:`Testimony`) and the contract for
providing it (:class:`TestimonySource`).

The representation of :class:`Testimony` is fixed by specification, not by this
module; it is intentionally left opaque here so that the interface remains
stable while the representation is elaborated.
"""

from __future__ import annotations

import abc


class Testimony(abc.ABC):
    """The compiler's source-language artifact: human testimony.

    An opaque handle representing testimony as it enters the pipeline, prior to
    any structuring into evidence. Its concrete representation is defined by the
    relevant ACS specification and is deliberately not fixed by this interface.
    """


class TestimonySource(abc.ABC):
    """Contract for a source of testimony input.

    Purpose:
        Provide :class:`Testimony` to the front of the compilation pipeline,
        independently of where that testimony originates.

    Responsibilities:
        - Yield a single, complete unit of testimony for one compilation.
        - Isolate the pipeline from the origin and encoding of that testimony.

    Inputs:
        None. A source is the origin of the pipeline; it obtains testimony by
        means private to the implementation.

    Outputs:
        A :class:`Testimony` artifact.

    Invariants:
        - A source does not interpret, structure, or validate testimony; it only
          provides it.
        - The artifact returned is complete and self-contained with respect to a
          single compilation.
    """

    @abc.abstractmethod
    def read(self) -> Testimony:
        """Return the testimony this source provides."""
