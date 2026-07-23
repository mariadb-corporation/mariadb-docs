# Understanding the Network Database Model

The network database model was a progression from the [hierarchical database model](understanding-the-hierarchical-database-model.md) and was designed to solve some of that model's problems, specifically the lack of flexibility. Instead of only allowing each child to have one parent, this model allows each child to have multiple parents (it calls the children _members_ and the parents _owners_). It addresses the need to model more complex relationships such as the orders/parts many-to-many relationship mentioned in the [hierarchical article](understanding-the-hierarchical-database-model.md). As you can see in the figure below, _A1_ has two members, _B1_ and _B2_. _B1._ is the owner of _C1_, _C2_, _C3_ and _C4_. However, in this model, _C4_ has two owners, _B1_ and _B2_.

```mermaid
flowchart TD
    accTitle: Network database model
    accDescr {
        A1 owns two members, B1 and B2. B1 owns C1, C2, C3 and C4, while B2 owns
        C4, C5 and C6, so C4 has two owners, B1 and B2. C3 owns D1, D2, D3 and D4,
        while C4 also owns D4, so D4 likewise has two owners, C3 and C4.
    }
    A1["A1"] --> B1["B1"]
    A1 --> B2["B2"]
    B1 --> C1["C1"]
    B1 --> C2["C2"]
    B1 --> C3["C3"]
    B1 --> C4["C4"]
    B2 --> C4
    B2 --> C5["C5"]
    B2 --> C6["C6"]
    C3 --> D1["D1"]
    C3 --> D2["D2"]
    C3 --> D3["D3"]
    C3 --> D4["D4"]
    C4 --> D4
    classDef n fill:#e2f0f2,stroke:#0a5a6b,stroke-width:2px,color:#111;
    class A1,B1,B2,C1,C2,C3,C4,C5,C6,D1,D2,D3,D4 n
```

_In the network model, a record such as C4 or D4 can have more than one owner._

Of course, this model has its problems, or everyone would still be using it. It is more difficult to implement and maintain, and, although more flexible than the hierarchical model, it still has flexibility problems, Not all relations can be satisfied by assigning another owner, and the programmer still has to understand the data structure well in order to make the model efficient.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
