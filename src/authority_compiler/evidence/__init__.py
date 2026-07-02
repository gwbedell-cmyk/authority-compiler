"""Evidence Graph stage of the pipeline.

Responsible for structuring human testimony into evidence and the relationships
between it. Consumes testimony and produces the Evidence Graph that the Authority
Graph is derived from.
"""

from authority_compiler.evidence.interfaces import EvidenceBuilder, EvidenceGraph

__all__ = ["EvidenceBuilder", "EvidenceGraph"]
