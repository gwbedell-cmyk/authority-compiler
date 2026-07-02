# specs/

Formal specifications for the Authority Compiler.

Each intermediate representation and each pipeline stage is specified here before
it is implemented. A specification defines the shape of a representation and the
rules a stage must obey, independent of any particular implementation.
Implementations in `src/` conform to these specifications, and tests in `tests/`
validate that conformance.

Specifications are published as numbered **Authority Computing Specifications
(ACS)**.

## Planned specifications

| ID      | Title                                      |
| ------- | ------------------------------------------ |
| ACS-000 | Authority Computing Core Concepts          |
| ACS-001 | Authority Computing Reference Architecture |
| ACS-002 | Authority ABI n[act] Specification         |
| ACS-003 | Authority Graph IR Specification           |
| ACS-004 | Evidence Graph Specification               |
| ACS-005 | Authority Compiler Specification           |
| ACS-006 | Authority Runtime Specification            |
| ACS-007 | Proof Object Specification                 |
| ACS-008 | Conformance Test Suite                     |

These documents are planned. This directory currently records the index; the
specifications themselves are authored as the project proceeds.
