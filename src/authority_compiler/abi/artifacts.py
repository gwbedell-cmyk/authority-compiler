"""n[act] artifact: the compiler's emitted-target value object.

Defines :class:`NAct`, the immutable artifact the compiler emits and the
Authority Runtime consumes. Its structural content is owned by the Authority
Computing Standards and is not modeled here.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NAct:
    """The n[act] artifact: the compiler's emitted target format.

    Purpose:
        Represent, as an immutable value, the Authority ABI produced by the
        compiler and consumed by the Authority Runtime.

    Universal fields:
        None. The ABI's structure is not fixed independently of its
        specification.

    Deferred structure:
        The structure of an n[act] is owned by ACS-002 (Authority ABI n[act]
        Specification). Fields are introduced only when ACS-002 fixes them.
    """

    # Placeholder -- deferred to ACS-002.
    # No structural fields are modeled until that standard fixes them.
