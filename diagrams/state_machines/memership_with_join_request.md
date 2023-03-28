````mermaid
---
title: Membership compose with Join Request
---
stateDiagram-v2
    direction LR

    %% State for membership
    state "Active" as A
    state "Removed" as R
    state "Suspended" as S
    state "Inactive" as IN
    %% states for JoinRequest
    state "Pending" as P
    state "Accepted" as AC
    state "Rejected" as RE


    [*] --> P
    note left of [*]
            Join Request
        end note
    P --> AC
    state AC {
        [*] --> A
        A --> IN
        A --> R
    A --> S
    }
     note right of AC
            Membership
        end note
    P --> RE



  
````