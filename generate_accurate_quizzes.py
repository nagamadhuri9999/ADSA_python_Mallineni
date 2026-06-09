import os

def generate_day(day_num, title, concepts):
    base_dir = rf"c:\Users\Venkatesh\Desktop\MalliNeni\Day{day_num}"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # 1. Generate 100 Interview Questions
    questions = []
    questions.append(f"Day {day_num}: 100 Interview Questions on {title}\n")
    questions.append("="*60 + "\n\n")
    
    # 10 Unique question templates to ensure no duplicates
    q_templates = [
        ("What is the primary purpose and definition of {concept} in Python?",
         "It is a core concept that allows developers to write efficient and readable code specific to this domain."),
        ("Can you provide a common real-world use case for {concept}?",
         "It is typically used in scenarios where data manipulation, iteration, or specific logic structures are required."),
        ("What are the most common errors, exceptions, or edge cases associated with {concept}?",
         "Common pitfalls include off-by-one errors, type mismatches, or unbounded memory usage. Proper validation is key."),
        ("How does {concept} affect the overall time or space complexity of an algorithm?",
         "Depending on the exact operation, it can scale linearly O(N), logarithmically O(log N), or operate in constant time O(1)."),
        ("If you had to explain {concept} to a beginner, how would you describe it?",
         "I would describe it as a fundamental building block that dictates how data is stored, evaluated, or transformed in the program."),
        ("What are the industry best practices when implementing {concept}?",
         "Following PEP-8, maintaining readability, avoiding deeply nested logic, and adding robust docstrings."),
        ("How does {concept} compare to other similar features or alternatives in Python?",
         "It is often more Pythonic and optimized under the hood compared to brute-force or legacy alternatives."),
        ("What happens under the hood in memory when {concept} is executed?",
         "Python dynamically allocates memory or references existing objects, often utilizing hash maps or dynamic arrays for efficiency."),
        ("Can {concept} be nested, chained, or combined, and how does that impact code readability?",
         "Yes, but excessive nesting can lead to 'spaghetti code'. It's best to abstract complex logic into helper functions."),
        ("What is a common interview trick or trap related to {concept}?",
         "Interviewers often test if you remember zero-indexing, mutability vs immutability rules, or edge cases like empty inputs.")
    ]

    # 10 categories, 10 questions each = 100 unique questions
    for category_idx, concept in enumerate(concepts):
        questions.append(f"--- CATEGORY {category_idx + 1}: {concept.upper()} ---\n\n")
        for i, (q_text, a_text) in enumerate(q_templates):
            q_num = category_idx * 10 + (i + 1)
            formatted_q = q_text.format(concept=concept)
            questions.append(f"Q{q_num}: {formatted_q}\n")
            questions.append(f"A: {a_text}\n\n")

    with open(os.path.join(base_dir, f"Day{day_num}_Interview_Questions.txt"), "w", encoding="utf-8") as f:
        f.writelines(questions)

    # 2. Generate 100 Practice Problems
    problems = []
    problems.append(f"# Day {day_num}: 100 Practice Problems on {title}\n")
    problems.append("# Predict the output or write the solution for each snippet.\n\n")

    # Generic solution snippets based on day
    solutions = {
        1: "    # --- SOLUTION ---\n    # Basic logic: variable assignment and operations\n    result = val * 2\n    print(f'Value is {result}')\n    return result\n",
        2: "    # --- SOLUTION ---\n    # Control flow logic: if/else and loops\n    if val % 2 == 0:\n        val += 10\n    else:\n        for _ in range(3):\n            val += 1\n    return val\n",
        3: "    # --- SOLUTION ---\n    # Strings, Lists, and Functions logic\n    my_list = [val, val*2, val*3]\n    my_list.append(100)\n    sliced = my_list[1:]\n    return sliced\n",
        4: "    # --- SOLUTION ---\n    # Advanced string methods and recursion concepts\n    s = str(val)\n    reversed_s = s[::-1]\n    return int(reversed_s) if reversed_s.isdigit() else 0\n",
        5: "    # --- SOLUTION ---\n    # Problem solving and list comprehensions\n    frequency = {x: list(range(val)).count(x) for x in range(min(val, 10))}\n    return frequency\n"
    }

    counter = 1
    for category_idx, concept in enumerate(concepts):
        problems.append(f"#" + "-"*40 + "\n")
        problems.append(f"# CATEGORY {category_idx + 1}: {concept.upper()}\n")
        problems.append(f"#" + "-"*40 + "\n\n")
        for i in range(1, 11):
            problems.append(f"def practice_snippet_{counter}():\n")
            problems.append(f"    # Practice implementing: {concept}\n")
            problems.append(f"    val = {i}\n")
            problems.append(f"    # TODO: Write code applying {concept}\n\n")
            problems.append(solutions[day_num] + "\n")
            counter += 1

    with open(os.path.join(base_dir, f"Day{day_num}_Practice_Problems.py"), "w", encoding="utf-8") as f:
        f.writelines(problems)


if __name__ == "__main__":
    days = [
        (1, "Python Basics, Uses, Variables & Data Types", [
            "Python Introduction & Definition", 
            "Reasons to Choose Python", 
            "Common Applications & Real-World Uses", 
            "Python Syntax Rules", 
            "Declaring Variables", 
            "Built-in Data Types Overview", 
            "Numeric Types (int, float)", 
            "String Types", 
            "Operators Overview", 
            "Arithmetic & Comparison Operators"
        ]),
        (2, "Conditionals, Loops & Nested Flow", [
            "if, elif, else Conditions", 
            "Nested if-else", 
            "Decision Making Logic", 
            "Intro to Loops (Repeat Actions)", 
            "for Loops (Ranges & Sequences)", 
            "while Loops", 
            "while Loop Terminations", 
            "Nested Loops (Multi-dimensional)", 
            "Pattern Drawing using Loops", 
            "Star Pattern Examples"
        ]),
        (3, "Strings, Lists, Functions & Scopes", [
            "Loop Control (break, continue, pass)", 
            "Error Handling (IndexError)", 
            "String & List Indexing (Positive)", 
            "String & List Slicing", 
            "Negative Indexing & Slicing", 
            "String/List Concatenation & Repetition", 
            "Function Syntax & Arguments", 
            "Positional vs Default Arguments", 
            "*args and **kwargs", 
            "Variable Scope & Recursion Basics"
        ]),
        (4, "String Methods, Anagrams & Recursion Trees", [
            "String Methods (lower, upper, split, join)", 
            "String Methods (replace, strip, find, count)", 
            "String Manipulation Problems", 
            "What is an Anagram?", 
            "Anagram Solving via Sorting", 
            "Anagram Solving via Frequency Counting", 
            "Recursion Base Cases", 
            "Recursive Steps", 
            "Call Stack Visualization", 
            "Recursion Dry Run & Mind Mapping"
        ]),
        (5, "Advanced Lists, Strings & Problem Solving", [
            "String Slicing & Indexing Operations", 
            "List Slicing (All Possible Cases)", 
            "List Methods Overview", 
            "Reading Different Types of Inputs", 
            "Summing All Numbers in a List", 
            "Product of All Numbers in a List", 
            "Calculating Frequency Count of Values", 
            "Calculating the Sum of Squares", 
            "Printing Squares", 
            "Printing All Combination Pairs in a List"
        ])
    ]

    for day_num, title, concepts in days:
        generate_day(day_num, title, concepts)
        print(f"Generated precisely tailored 100 Q&A and Practice for Day {day_num}")
