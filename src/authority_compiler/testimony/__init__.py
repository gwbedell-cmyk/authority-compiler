"""Human Testimony: the source stage of the pipeline.

Responsible for the compiler's source input -- the statements a human provides --
as it enters the pipeline, before it is structured into the Evidence Graph.
"""

from authority_compiler.testimony.interfaces import Testimony, TestimonySource

__all__ = ["Testimony", "TestimonySource"]
