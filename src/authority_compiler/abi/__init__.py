"""Authority ABI (n[act]) stage of the pipeline.

Responsible for the compiler's emitted target format. Produces the Authority ABI
that the Authority Runtime consumes.
"""

from authority_compiler.abi.interfaces import NAct, NActGenerator

__all__ = ["NAct", "NActGenerator"]
