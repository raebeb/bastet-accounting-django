````mermaid
---
title: Membership
---
stateDiagram-v2
    direction LR
    [*] --> Created
    Created --> Invited
    Created --> Active
    Invited --> Active
    Active --> Inactive
    Active --> Removed
    Active --> Suspended
````