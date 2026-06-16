# Day 11 Capstone Tasks: Stacks & Queues

## Objective
Today's tasks will test your understanding of both **LIFO (Stacks)** and **FIFO (Queues)** mechanics. You will build a system for each.

---

## Task 1: Printer Spooler Simulator (Queue)

### Requirements
1. **The System:**
   - You have a printer that holds multiple print jobs in a queue.
   - You receive a stream of actions as a list of dictionaries.
   - Actions: add a new job to the queue, or print the next job.

2. **The Logic:**
   - Use `collections.deque` for efficient queue operations.
   - If action is `{"type": "add", "document": "Resume.pdf"}`, you **enqueue** it.
   - If action is `{"type": "print"}`, you **dequeue** the next document and print it. If the queue is empty, print "No jobs to print."

### Example Execution
```python
actions = [
    {"type": "add", "document": "Resume.pdf"},
    {"type": "add", "document": "Photo.jpg"},
    {"type": "print"},
    {"type": "add", "document": "Notes.txt"},
    {"type": "print"},
    {"type": "print"},
    {"type": "print"}
]
```

### Expected Output
```text
Processing printer actions...
Added 'Resume.pdf' to the print queue.
Added 'Photo.jpg' to the print queue.
Printing: Resume.pdf
Added 'Notes.txt' to the print queue.
Printing: Photo.jpg
Printing: Notes.txt
Printer Error: No jobs to print.
```

---

## Task 2: Valid Parentheses Checker (Stack)

### Requirements
1. **The System:**
   - Build a function `isValid(s: str) -> bool` that determines if a string of brackets is valid.
   - Allowed characters: `()`, `[]`, `{}`.

2. **The Logic:**
   - Use a Python `list` as a Stack.
   - If you encounter an opening bracket, **push** it onto the stack.
   - If you encounter a closing bracket, **pop** the top of the stack. If it doesn't match the correct opening bracket (or if the stack is empty), return `False`.
   - At the end, if the stack is empty, return `True`, otherwise `False`.

### Visualizer Academy!
> **Note:** If you want to see exactly how the Stack processes the parentheses step-by-step, check out the **Interactive Valid Parentheses Visualizer** we built in the `valid-parentheses-visualizer` folder. 
> To run it locally:
> ```bash
> cd valid-parentheses-visualizer
> npm run dev
> ```
> Then open `http://localhost:3000` in your browser!
