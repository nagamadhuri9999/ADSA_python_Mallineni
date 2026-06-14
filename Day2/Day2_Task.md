# Day 2 Capstone Task: The Number Guessing Game

## Objective
Build a text-based "Number Guessing Game" to solidify your understanding of `while` loops, `if/elif/else` conditionals, and loop control statements (`break`).

## Requirements

1. **Setup:**
   - The program should store a "secret number" (e.g., `secret_number = 42`).
   - Give the player a set number of `attempts` (e.g., 5 attempts).

2. **The Game Loop:**
   - Use a `while` loop to repeatedly ask the user to guess the number.
   - You can use the `input()` function to get the user's guess (don't forget to wrap it in `int()` to convert it to an integer!).

3. **Conditionals:**
   - If the guess is **higher** than the secret number, print `"Too high! Try again."`
   - If the guess is **lower** than the secret number, print `"Too low! Try again."`
   - If the guess is **correct**, print `"Congratulations! You guessed the number!"` and instantly exit the loop using `break`.

4. **Attempt Tracking:**
   - Decrease the number of `attempts` by 1 after every wrong guess.
   - If `attempts` reaches 0, print `"Game Over! The secret number was X."` and end the loop.

## Bonus Challenge (Optional)
- Add a "Play Again?" prompt at the end. If the user types "yes", restart the game (Hint: you'll need a giant outer `while True:` loop!).

---
### 💡 Hints & Dry Run Example

If `secret_number = 42` and `attempts = 3`:
- **Iteration 1:** User guesses `50`. Condition `50 > 42` is True. Prints "Too high!". `attempts` becomes `2`.
- **Iteration 2:** User guesses `30`. Condition `30 < 42` is True. Prints "Too low!". `attempts` becomes `1`.
- **Iteration 3:** User guesses `42`. Condition `42 == 42` is True. Prints "Congratulations!". Loop `break` executes.

Good luck!
