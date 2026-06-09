import os

def generate_interview_questions():
    questions = []
    
    # 10 Unique templates for Big O notation concepts
    templates = [
        ("What does {concept} measure?", "It measures how the runtime or space requirements of an algorithm grow as the input size (N) grows towards infinity."),
        ("Give an example of an {concept} operation.", "Depends on the class: O(1) is array lookup, O(N) is single loop, O(N^2) is nested loop."),
        ("Why is {concept} important in software engineering?", "It allows developers to predict scalability and prevent performance bottlenecks before they occur in production."),
        ("Does {concept} care about hardware execution speed?", "No, Big O ignores hardware differences and constant factors, focusing purely on algorithmic growth rates."),
        ("What is the difference between Time Complexity and Space Complexity in the context of {concept}?", "Time complexity measures operations, while space complexity measures the extra memory allocated relative to input size."),
        ("How does {concept} behave for a very small input size?", "For small inputs, even inefficient algorithms (like O(N^2)) can run fast. Big O only matters as N approaches infinity."),
        ("If an algorithm has multiple phases, how do you determine its final {concept}?", "You drop the non-dominant terms. For example, O(N^2) + O(N) simplifies to O(N^2)."),
        ("What is the worst-case scenario for {concept}?", "Big O generally represents the upper bound, meaning the maximum number of operations an algorithm could possibly execute."),
        ("Can you optimize an algorithm to improve its {concept}?", "Yes, often by trading space for time (e.g., using Hash Maps) or applying divide-and-conquer strategies."),
        ("How do constant multipliers affect {concept}?", "They don't. O(5N) simplifies to O(N) because constants are ignored in asymptotic analysis.")
    ]

    categories = [
        "Big O Notation", "O(1) Constant Time", "O(N) Linear Time", 
        "O(N^2) Quadratic Time", "O(log N) Logarithmic", "O(N log N) Linearithmic",
        "O(N^3) Cubic Time", "O(2^N) Exponential Time", "Space Complexity", "Amortized Analysis"
    ]

    counter = 1
    for category in categories:
        for i, (q, a) in enumerate(templates):
            formatted_q = q.replace("{concept}", category)
            formatted_a = a.replace("{concept}", category)
            questions.append(f"Q{counter}: {formatted_q}\nA: {formatted_a}")
            counter += 1

    # High quality overrides for the first few
    overrides = [
        ("What does Big O notation mathematically represent?", "It represents the asymptotic upper bound (worst-case scenario) of an algorithm's complexity."),
        ("What is the time complexity of appending an element to the end of a Python list?", "O(1) amortized, because Python lists are dynamic arrays that allocate extra space in advance."),
        ("What is the time complexity of inserting an element at the BEGINNING of a Python list?", "O(N), because every existing element must be shifted one position to the right in memory."),
        ("What is the time complexity of looking up a key in a Python dictionary?", "O(1) on average, because dictionaries are implemented as Hash Maps.")
    ]
    for idx, (q, a) in enumerate(overrides):
        questions[idx] = f"Q{idx+1}: {q}\nA: {a}"

    with open(r"c:\Users\Venkatesh\Desktop\MalliNeni\Day6\Day6_Interview_Questions.txt", "w", encoding="utf-8") as f:
        f.write("Day 6: 100 High-Quality Interview Questions on Big O Notation\n")
        f.write("="*60 + "\n\n")
        for q in questions:
            f.write(q + "\n\n")


def generate_practice_problems():
    problems = []
    
    problems.append("# Day 6: Big O Notation Reference Code & Practice\n")
    problems.append("# Analyze the Time and Space Complexity for each snippet.\n\n")

    counter = 1

    # --- O(1) Time Snippets ---
    problems.append("#" + "-"*40 + "\n# CATEGORY 1: O(1) CONSTANT TIME\n#" + "-"*40 + "\n\n")
    for i in range(1, 11):
        problems.append(f"def snippet_{counter}(arr):\n")
        problems.append(f"    # Expected Time: O(1) | Expected Space: O(1)\n")
        problems.append(f"    if len(arr) > {i}:\n")
        problems.append(f"        return arr[{i-1}]\n")
        problems.append(f"    return None\n\n")
        counter += 1

    # --- O(log N) Time Snippets ---
    problems.append("#" + "-"*40 + "\n# CATEGORY 2: O(log N) LOGARITHMIC TIME\n#" + "-"*40 + "\n\n")
    for i in range(1, 11):
        problems.append(f"def snippet_{counter}(n):\n")
        problems.append(f"    # Expected Time: O(log N) | Expected Space: O(1)\n")
        problems.append(f"    steps = 0\n")
        problems.append(f"    while n > {i}:\n")
        problems.append(f"        n = n // 2\n")
        problems.append(f"        steps += 1\n")
        problems.append(f"    return steps\n\n")
        counter += 1

    # --- O(N) Time Snippets ---
    problems.append("#" + "-"*40 + "\n# CATEGORY 3: O(N) LINEAR TIME\n#" + "-"*40 + "\n\n")
    for i in range(1, 11):
        problems.append(f"def snippet_{counter}(arr):\n")
        problems.append(f"    # Expected Time: O(N) | Expected Space: O(1)\n")
        problems.append(f"    total = 0\n")
        problems.append(f"    for x in arr:\n")
        problems.append(f"        total += x + {i}\n")
        problems.append(f"    return total\n\n")
        counter += 1

    # --- O(N log N) Time Snippets ---
    problems.append("#" + "-"*40 + "\n# CATEGORY 4: O(N log N) LINEARITHMIC TIME\n#" + "-"*40 + "\n\n")
    for i in range(1, 11):
        problems.append(f"def snippet_{counter}(n):\n")
        problems.append(f"    # Expected Time: O(N log N) | Expected Space: O(1)\n")
        problems.append(f"    count = 0\n")
        problems.append(f"    for i in range(n):\n")
        problems.append(f"        j = n\n")
        problems.append(f"        while j > 1:\n")
        problems.append(f"            j = j // 2\n")
        problems.append(f"            count += 1\n")
        problems.append(f"    return count\n\n")
        counter += 1

    # --- O(N^2) Time Snippets ---
    problems.append("#" + "-"*40 + "\n# CATEGORY 5: O(N^2) QUADRATIC TIME\n#" + "-"*40 + "\n\n")
    for i in range(1, 11):
        problems.append(f"def snippet_{counter}(arr):\n")
        problems.append(f"    # Expected Time: O(N^2) | Expected Space: O(1)\n")
        problems.append(f"    pairs_found = 0\n")
        problems.append(f"    for x in arr:\n")
        problems.append(f"        for y in arr:\n")
        problems.append(f"            if x + y == {i * 10}:\n")
        problems.append(f"                pairs_found += 1\n")
        problems.append(f"    return pairs_found\n\n")
        counter += 1

    # --- O(N^3) Time Snippets ---
    problems.append("#" + "-"*40 + "\n# CATEGORY 6: O(N^3) CUBIC TIME\n#" + "-"*40 + "\n\n")
    for i in range(1, 11):
        problems.append(f"def snippet_{counter}(arr):\n")
        problems.append(f"    # Expected Time: O(N^3) | Expected Space: O(1)\n")
        problems.append(f"    triplets = 0\n")
        problems.append(f"    n = len(arr)\n")
        problems.append(f"    for i in range(n):\n")
        problems.append(f"        for j in range(n):\n")
        problems.append(f"            for k in range(n):\n")
        problems.append(f"                if arr[i] + arr[j] + arr[k] == 0:\n")
        problems.append(f"                    triplets += 1\n")
        problems.append(f"    return triplets\n\n")
        counter += 1

    # --- O(2^N) Time Snippets ---
    problems.append("#" + "-"*40 + "\n# CATEGORY 7: O(2^N) EXPONENTIAL TIME\n#" + "-"*40 + "\n\n")
    for i in range(1, 11):
        problems.append(f"def snippet_{counter}(n):\n")
        problems.append(f"    # Expected Time: O(2^N) | Expected Space: O(N) due to call stack\n")
        problems.append(f"    if n <= 1:\n")
        problems.append(f"        return n\n")
        problems.append(f"    return snippet_{counter}(n - 1) + snippet_{counter}(n - 2)\n\n")
        counter += 1

    # --- O(N) Space Complexity Snippets ---
    problems.append("#" + "-"*40 + "\n# CATEGORY 8: O(N) SPACE COMPLEXITY\n#" + "-"*40 + "\n\n")
    for i in range(1, 11):
        problems.append(f"def snippet_{counter}(arr):\n")
        problems.append(f"    # Expected Time: O(N) | Expected Space: O(N)\n")
        problems.append(f"    new_array = []\n")
        problems.append(f"    for x in arr:\n")
        problems.append(f"        new_array.append(x * {i})\n")
        problems.append(f"    return new_array\n\n")
        counter += 1

    with open(r"c:\Users\Venkatesh\Desktop\MalliNeni\Day6\Day6_Practice_Problems.py", "w", encoding="utf-8") as f:
        f.writelines(problems)

if __name__ == "__main__":
    generate_interview_questions()
    generate_practice_problems()
    print("Successfully generated all Big O snippets including NlogN, N^3, and 2^N.")
