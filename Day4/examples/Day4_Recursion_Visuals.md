# Day 4: Recursion Visualizations

Understanding recursion is much easier when you can visualize the Call Stack and the Recursion Tree. Below are visual representations of common recursive algorithms.

## 1. Factorial Recursion Tree & Call Stack
A linear recursion tree where each call waits for the next one to complete.

```mermaid
graph TD
    A["fact(3)"] -->|calls| B["fact(2)"]
    B -->|calls| C["fact(1)"]
    C -->|calls| D["fact(0)"]
    D -.->|returns 1| C
    C -.->|returns 1 * 1 = 1| B
    B -.->|returns 2 * 1 = 2| A
    A -.->|returns 3 * 2 = 6| E((Result: 6))
```

## 2. Fibonacci Recursion Tree (Overlapping Subproblems)
Notice how `fib(2)` is calculated multiple times. This is why naive recursive Fibonacci is slow!

```mermaid
graph TD
    F4["fib(4)"] --> F3["fib(3)"]
    F4 --> F2_1["fib(2)"]
    
    F3 --> F2_2["fib(2)"]
    F3 --> F1_1["fib(1)"]
    
    F2_1 --> F1_2["fib(1)"]
    F2_1 --> F0_1["fib(0)"]
    
    F2_2 --> F1_3["fib(1)"]
    F2_2 --> F0_2["fib(0)"]
    
    style F2_1 fill:#ff9999,stroke:#333,stroke-width:2px
    style F2_2 fill:#ff9999,stroke:#333,stroke-width:2px
```
*(Nodes in red highlight overlapping subproblems - the exact same calculation being performed multiple times).*
