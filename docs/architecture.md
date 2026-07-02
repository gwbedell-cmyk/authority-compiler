# Architecture

The Authority Compiler is defined by a single linear pipeline. Each stage
consumes the output of the stage above it and produces the input for the stage
below it.

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

## Stages

**Human Testimony** — The source input. The statements a human provides.

**Evidence Graph** — Testimony structured into evidence and the relationships
between it.

**Authority Graph (IR)** — The compiler's intermediate representation, derived
from the Evidence Graph.

**Constitutional Engine** — The checking stage that validates the Authority
Graph.

**Authority ABI (n[act])** — The emitted target format.

**Authority Runtime** — The environment that executes the Authority ABI.
