# Contributing to the Authority Compiler

The Authority Compiler is a compiler project and is developed with the
discipline that implies. These guidelines exist to keep the repository coherent
as it grows.

## Principles

- **This is a compiler.** Contributions are evaluated by their role in the
  compilation pipeline. Features outside the pipeline are out of scope.
- **Specification precedes implementation.** New behavior is specified in
  `specs/` (and documented in `docs/` where appropriate) before it is written in
  `src/`.
- **Respect stage boundaries.** Each pipeline stage — testimony, evidence,
  authority, constitutional, ABI — is separable. Do not couple stages beyond the
  representations they exchange.
- **No invented scope.** Implement the architecture as designed. Do not
  introduce features, integrations, or abstractions that the pipeline does not
  call for.

## Workflow

1. Open an issue describing the change and the pipeline stage it affects.
2. Ensure the relevant specification exists or is updated in the same change.
3. Implement against that specification in the appropriate `src/` package.
4. Add or update tests under `tests/`.
5. Submit a pull request that references the issue and specification.

## Commit and Pull Request Conventions

- Keep commits focused; one logical change per commit.
- Reference the affected pipeline stage in the description.
- Explain *why* a change is made, not only *what* changed.

## Development Setup

The reference implementation is written in Python and uses a `src` layout with
`pyproject.toml`.

```sh
python -m venv .venv
# Windows:  .venv\Scripts\activate
# Unix:     source .venv/bin/activate
pip install -e ".[dev]"
```

- Run tests with `pytest`.
- Lint with `ruff check`.

## Code Review

Every change is reviewed against the architecture. Reviewers verify that the
change belongs to a defined stage, matches its specification, and does not
expand the project's scope.
