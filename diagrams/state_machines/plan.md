````mermaid
---
title: Plan
---
stateDiagram-v2
    direction LR
    [*] --> Draft
    Draft --> created
    created --> published
    published --> hidden
    hidden --> published
    hidden --> finished
    published --> finished
    
````