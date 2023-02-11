````mermaid
---
title: User
---
stateDiagram-v2
    direction LR
    [*] --> created
    created --> verified
    created  --> banned
    verified --> banned
    
````