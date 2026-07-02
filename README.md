# Authority Compiler

The Authority Compiler is a compiler.

It is not an AI application, an agent framework, or an automation platform. It
is a compiler in the traditional sense: it accepts a well-defined input,
transforms it through a sequence of intermediate representations, and emits a
well-defined output. The subject matter it compiles is *authority* — the
grounds on which an action is permitted, obligated, or forbidden.

## Purpose

The Authority Compiler translates human testimony into executable authority.

It exists to make the reasoning that grants authority explicit, inspectable, and
mechanically checkable. Rather than treating permission and obligation as opaque
runtime decisions, the compiler lowers them through a series of intermediate
representations, each of which can be validated on its own terms before the next
stage consumes it.

## High-Level Compilation Pipeline

```
Human Testimony
      │
      ▼
Evidence Graph
      │
      ▼
Authority Graph (IR)
      │
      ▼
Constitutional Engine
      │
      ▼
Authority ABI (n[act])
      │
      ▼
Authority Runtime
```

Each stage is a distinct phase with a distinct representation. Testimony is the
source language. The Evidence Graph and Authority Graph are intermediate
representations. The Constitutional Engine performs checking and validation. The
Authority ABI is the emitted target format. The Authority Runtime is the
execution environment that consumes the ABI.

A more detailed treatment of the pipeline lives in
[`docs/architecture.md`](docs/architecture.md).

## Repository Principles

- **This is a compiler, not a product.** Every component is justified by its
  role in the compilation pipeline.
- **Representations are first-class.** Each intermediate representation has a
  specification before it has an implementation.
- **Specification precedes code.** Behavior is defined in `specs/` and `docs/`
  before it is implemented in `src/`.
- **Stages are separable.** Each phase can be reasoned about, tested, and
  validated in isolation.
- **No invented features.** The scope is the pipeline as designed and nothing
  beyond it.

## Build Philosophy

The Authority Compiler is engineered with the discipline expected of a serious
compiler project such as LLVM, Rust, Go, or Clang:

- Clear separation between phases of compilation.
- Intermediate representations that are stable, documented contracts.
- A structure that reflects the pipeline it implements.
- Correctness and inspectability valued over convenience.

This repository currently establishes that structure. It contains the skeleton
of the project — its directories, its documented responsibilities, and its
governing conventions — so that implementation can proceed against a foundation
that already reflects the seriousness of the work.

## Reference Implementation

The reference implementation is written in **Python**, chosen for the fastest
path to a clear compiler prototype: strong graph tooling, straightforward
testing, and readable, standards-aligned code. The project uses a modern Python
`src` layout with `pyproject.toml`; the compiler lives in the
`authority_compiler` package under `src/`.

## Repository Layout

| Path             | Responsibility                                            |
| ---------------- | --------------------------------------------------------- |
| `docs/`          | Project documentation, including the architecture.        |
| `specs/`         | Formal specifications (ACS) for each representation and stage. |
| `src/`           | Implementation of the compiler (`authority_compiler` package), organized by pipeline stage. |
| `tests/`         | Tests validating the compiler and its stages.             |
| `examples/`      | Illustrative inputs and worked pipeline examples.         |
| `scripts/`       | Development, build, and maintenance scripts.              |
| `pyproject.toml` | Python project definition and tooling configuration.      |

## License

Copyright 2026 iThoth Systems Inc. Licensed under the Apache License, Version
2.0. See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md).
