# Day 1 Capstone Task: The Bill Splitter Calculator

## Objective
Build a "Bill Splitter" program to solidify your understanding of variables, data types, type casting, arithmetic operators, and basic input/output.

## Requirements

1. **User Input & Type Casting:**
   - Ask the user for the total bill amount (e.g., `"Enter the total bill amount: $"`). Remember that `input()` returns a string, so you must cast it to a `float`.
   - Ask the user for the tip percentage they want to leave (e.g., 10, 15, or 20). Cast this to an `int` or `float`.
   - Ask the user how many people are splitting the bill. Cast this to an `int`.

2. **Calculations (Arithmetic Operators):**
   - Calculate the tip amount: `tip_amount = total_bill * (tip_percentage / 100)`
   - Calculate the total amount to pay: `total_to_pay = total_bill + tip_amount`
   - Calculate the amount each person must pay: `amount_per_person = total_to_pay / number_of_people`

3. **Output (String Formatting):**
   - Use an f-string to print a friendly summary of the calculations.
   - Example Output: `"Each person should pay: $25.50"`
   - *Bonus:* Try to use the `round()` function to round the final amount to 2 decimal places.

## Example Dry Run

- **Input:** Bill = 100, Tip = 15%, People = 4
- **Variables in Memory:**
  - `total_bill = 100.0`
  - `tip_percentage = 15`
  - `number_of_people = 4`
- **Logic:**
  - `tip_amount = 100.0 * (15 / 100)` -> `15.0`
  - `total_to_pay = 100.0 + 15.0` -> `115.0`
  - `amount_per_person = 115.0 / 4` -> `28.75`
- **Output:** `"Each person should pay: $28.75"`

Good luck!
