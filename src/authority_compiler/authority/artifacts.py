"""Authority Graph artifact: the compiler's intermediate-representation value object.

Defines :class:`AuthorityGraph`, the immutable IR artifact produced from an
Evidence Graph. Its structural content is owned by the Authority Computing
Standards and is not modeled here.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AuthorityGraph:
    """The Authority Graph artifact: the compiler's intermediate representation.

    Purpose:
        Represent authority, as an immutable value, in the compiler's
        intermediate representation, derived from the Evidence Graph and
        consumed by the Constitutional Engine.

    Universal fields:
        None. The IR's constituents are not universal independently of their
        specified representation.

    Deferred structure:
        The nodes, edges, and authority relationships that constitute an
        Authority Graph are owned by ACS-003 (Authority Graph IR Specification).
        Fields are introduced only when ACS-003 fixes them.
    """

    # Placeholder -- deferred to ACS-003.
    # No structural fields are modeled until that standard fixes them.
