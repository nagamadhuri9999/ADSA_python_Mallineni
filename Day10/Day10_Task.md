# Day 10 Capstone Task: Text Editor Undo Simulator

## Objective
Build a program that simulates a text editor's typing and "Undo" mechanism using a **Stack**. This tests your understanding of LIFO (Last In, First Out) operations.

## Requirements

1. **The System:**
   - You have an empty document (which is represented by a Stack of actions).
   - You receive a stream of actions as a list of strings.
   - An action can either be a word to type, e.g., `"Hello"`, OR the command `"UNDO"`.

2. **The Logic:**
   - If the action is a word, you **push** it onto the stack.
   - If the action is `"UNDO"`, you **pop** the most recently added word from the stack (if the stack is not empty).

3. **Execution:**
   - Define your actions: `actions = ["Hello", "World", "UNDO", "Python", "Rocks", "UNDO", "!"]`
   - Process the actions using your stack.
   - At the end, format the stack into a single sentence by joining the remaining words with spaces.
   - Print the final document.

## Example Output
```text
Processing actions...
Type: 'Hello'
Type: 'World'
UNDO! Removing 'World'
Type: 'Python'
Type: 'Rocks'
UNDO! Removing 'Rocks'
Type: '!'

--- Final Document ---
Hello Python !
```

Good luck! This is exactly how your favorite code editor handles your `Ctrl+Z` or `Cmd+Z` inputs!
