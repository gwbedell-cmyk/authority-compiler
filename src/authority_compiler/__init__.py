"""Authority Compiler.

Compiles human testimony into executable authority.

This package is the Python reference implementation of the Authority Compiler.
Its subpackages correspond to the stages of the compilation pipeline. See
``docs/architecture.md`` for the pipeline and ``specs/`` for the governing
specifications.

This module intentionally contains no logic; behavior lives in the stage
subpackages once specified. It re-exports the pipeline's public interface
contracts and their opaque artifact types.
"""

from authority_compiler.abi import NAct, NActGenerator
from authority_compiler.authority import AuthorityBuilder, AuthorityGraph
from authority_compiler.compiler import AuthorityCompiler
from authority_compiler.constitutional import (
    ConstitutionalEngine,
    ConstitutionalVerdict,
)
from authority_compiler.evidence import EvidenceBuilder, EvidenceGraph
from authority_compiler.testimony import Testimony, TestimonySource

__all__ = [
    # Testimony stage
    "Testimony",
    "TestimonySource",
    # Evidence stage
    "EvidenceGraph",
    "EvidenceBuilder",
    # Authority (IR) stage
    "AuthorityGraph",
    "AuthorityBuilder",
    # Constitutional stage
    "ConstitutionalVerdict",
    "ConstitutionalEngine",
    # ABI (n[act]) stage
    "NAct",
    "NActGenerator",
    # Orchestration
    "AuthorityCompiler",
]
