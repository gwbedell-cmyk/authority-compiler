# src/

Implementation of the Authority Compiler.

This project uses a Python **src layout**. The distribution is a single
top-level import package, `authority_compiler`, whose subpackages correspond to
the stages of the compilation pipeline. Nesting the stages under one package
keeps them namespaced (rather than seven flat, collision-prone top-level
packages) while preserving the stage names exactly.

```
src/
└── authority_compiler/
    ├── testimony/       Human Testimony (source input)
    ├── evidence/        Evidence Graph
    ├── authority/       Authority Graph (IR)
    ├── compiler/        Pipeline orchestration
    ├── constitutional/  Constitutional Engine
    ├── abi/             Authority ABI (n[act])
    └── common/          Shared definitions
```

Each subpackage currently contains only an `__init__.py` whose docstring states
its responsibility. The packages exchange the intermediate representations
defined in `specs/`.
