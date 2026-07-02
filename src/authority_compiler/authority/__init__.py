"""Authority Graph (IR) stage of the pipeline.

Responsible for the compiler's intermediate representation. Consumes the Evidence
Graph and produces the Authority Graph, the IR that the Constitutional Engine
checks.
"""

from authority_compiler.authority.interfaces import AuthorityBuilder, AuthorityGraph

__all__ = ["AuthorityBuilder", "AuthorityGraph"]
