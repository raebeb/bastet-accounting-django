````mermaid
---
title: PlanOrganization
---
stateDiagram-v2
    direction LR
    state "Created" as C
    state "Active" as A
    state "Inactive" as I

    [*] --> C
    C --> A
    A --> I
````