"""Testimony artifact: the compiler's source-language value object.

Defines :class:`Testimony`, the immutable artifact that enters the pipeline. Its
structural content is owned by the Authority Computing Standards and is not
modeled here.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Testimony:
    """The compiler's source-language artifact: human testimony.

    Purpose:
        Represent testimony as an immutable value as it enters the pipeline,
        before any structuring into evidence.

    Universal fields:
        None. Testimony carries no field that is universal and independent of
        its detailed representation.

    Deferred structure:
        The content and internal structure of testimony are owned by ACS-000
        (Authority Computing Core Concepts); how testimony is read and admitted
        into a compilation is governed by ACS-005 (Authority Compiler
        Specification). Fields are introduced only when those standards fix them.
    """

    # Placeholder -- deferred to ACS-000 / ACS-005.
    # No structural fields are modeled until those standards fix them.
