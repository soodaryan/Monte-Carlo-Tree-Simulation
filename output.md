Output of POST COMMAND using postman locally :
[
    [
        "A",
        "A.A",
        "A.A.B",
        "A.A.B.A",
        "A.A.B.A.A"
    ],
    [
        "A",
        "A.A",
        "A.A.A",
        "A.A.A.A",
        "A.A.A.A.B"
    ],
    [
        "A",
        "A.A",
        "A.A.B",
        "A.A.B.A",
        "A.A.B.A.A"
    ],
    [
        "A",
        "A.A",
        "A.A.B",
        "A.A.B.A",
        "A.A.B.A.A"
    ],
    [
        "A",
        "A.A",
        "A.A.B",
        "A.A.B.A",
        "A.A.B.A.A"
    ],
    [
        "A",
        "A.A",
        "A.A.A",
        "A.A.A.A",
        "A.A.A.A.C"
    ],
    [
        "A",
        "A.A",
        "A.A.A",
        "A.A.A.A",
        "A.A.A.A.B"
    ],
    [
        "A",
        "A.A",
        "A.A.A",
        "A.A.A.A",
        "A.A.A.A.B"
    ],
    [
        "A",
        "A.A",
        "A.A.B",
        "A.A.B.A",
        "A.A.B.A.A"
    ],
    [
        "A",
        "A.A",
        "A.A.B",
        "A.A.B.A",
        "A.A.B.A.A"
    ]
]


Full Output of the MCTS : 

A -> A.B -> A.B.A -> A.B.A.B -> A.B.A.B.B -> A.B.A.B.B.A -> A.B.A.B.B.A.A -> A.B.A.B.B.A.A.A -> A.B.A.B.B.A.A.A.B -> A.B.A.B.B.A.A.A.B.A
A -> A.A -> A.A.A -> A.A.A.B -> A.A.A.B.A -> A.A.A.B.A.B -> A.A.A.B.A.B.A -> A.A.A.B.A.B.A.A -> A.A.A.B.A.B.A.A.A -> A.A.A.B.A.B.A.A.A.A
A -> A.A -> A.A.A -> A.A.A.B -> A.A.A.B.A -> A.A.A.B.A.A -> A.A.A.B.A.A.A -> A.A.A.B.A.A.A.B -> A.A.A.B.A.A.A.B.A -> A.A.A.B.A.A.A.B.A.A
A -> A.A -> A.A.A -> A.A.A.A -> A.A.A.A.A -> A.A.A.A.A.A -> A.A.A.A.A.A.B -> A.A.A.A.A.A.B.B -> A.A.A.A.A.A.B.B.A -> A.A.A.A.A.A.B.B.A.A
A -> A.B -> A.B.A -> A.B.A.B -> A.B.A.B.B -> A.B.A.B.B.A -> A.B.A.B.B.A.A -> A.B.A.B.B.A.A.B -> A.B.A.B.B.A.A.B.A -> A.B.A.B.B.A.A.B.A.B
A -> A.B -> A.B.A -> A.B.A.B -> A.B.A.B.B -> A.B.A.B.B.A -> A.B.A.B.B.A.A -> A.B.A.B.B.A.A.A -> A.B.A.B.B.A.A.A.A -> A.B.A.B.B.A.A.A.A.B
A -> A.B -> A.B.A -> A.B.A.A -> A.B.A.A.C -> A.B.A.A.C.C -> A.B.A.A.C.C.A -> A.B.A.A.C.C.A.A -> A.B.A.A.C.C.A.A.A -> A.B.A.A.C.C.A.A.A.A
A -> A.B -> A.B.A -> A.B.A.A -> A.B.A.A.B -> A.B.A.A.B.B -> A.B.A.A.B.B.A -> A.B.A.A.B.B.A.A -> A.B.A.A.B.B.A.A.B -> A.B.A.A.B.B.A.A.B.A
A -> A.B -> A.B.B -> A.B.B.A -> A.B.B.A.B -> A.B.B.A.B.C -> A.B.B.A.B.C.A -> A.B.B.A.B.C.A.A -> A.B.B.A.B.C.A.A.C -> A.B.B.A.B.C.A.A.C.A
A -> A.A -> A.A.A -> A.A.A.A ->