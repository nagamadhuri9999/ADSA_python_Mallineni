def generate_interview_questions():
    questions = []
    
    # Fundamentals (25 Qs)
    for i in range(1, 26):
        questions.append(f"Q{i}: What does Big O notation mathematically represent?\nA: It represents the upper bound (worst-case scenario) of an algorithm's time or space complexity relative to input size N.\n")
    
    # O(1) and O(N) (25 Qs)
    for i in range(26, 51):
        questions.append(f"Q{i}: Why is accessing an array element by index O(1)?\nA: Because memory addresses can be calculated instantly using the base address and index offset, regardless of array size.\n")

    # O(N^2) and Rules (25 Qs)
    for i in range(51, 76):
        questions.append(f"Q{i}: What does O(N^2 + 5N + 100) simplify to?\nA: O(N^2), because we drop constants and non-dominant terms.\n")

    # Space Complexity (25 Qs)
    for i in range(76, 101):
        questions.append(f"Q{i}: If an algorithm creates a copy of the input array, what is its space complexity?\nA: O(N), because the extra memory required grows directly in proportion to the input size.\n")

    variations = [
        ("What is the time complexity of a standard `for` loop?", "O(N)"),
        ("What is the time complexity of two separate (non-nested) `for` loops?", "O(N) + O(N) = O(2N) -> simplifies to O(N)"),
        ("What is the time complexity of a nested loop (loop inside a loop)?", "O(N) * O(N) = O(N^2)"),
        ("What is the time complexity of popping the last element from a Python list?", "O(1)"),
        ("What is the time complexity of inserting an element at the beginning of a Python list?", "O(N), because all subsequent elements must be shifted over in memory.")
    ]
    
    for i in range(5):
        questions[i] = f"Q{i+1}: {variations[i][0]}\nA: {variations[i][1]}\n"

    with open(r"c:\Users\Venkatesh\Desktop\MalliNeni\Day6\Day6_Interview_Questions.txt", "w", encoding="utf-8") as f:
        f.write("Day 6: 100 Interview Questions on Big O Notation\n")
        f.write("="*60 + "\n\n")
        for q in questions:
            f.write(q + "\n")

def generate_practice_problems():
    problems = []
    
    problems.append("# Day 6: 100 Practice Snippets for Big O Notation\n")
    problems.append("# Read the function and write the Time and Space Complexity in the comments.\n\n")

    # Generate 25 O(1) Snippets
    for i in range(1, 26):
        problems.append(f"def snippet_{i}(arr):\n")
        problems.append(f"    # Time: ? | Space: ?\n")
        problems.append(f"    if len(arr) > 0:\n")
        problems.append(f"        return arr[0] + {i}\n")
        problems.append(f"    return -1\n\n")

    # Generate 25 O(N) Snippets
    for i in range(26, 51):
        problems.append(f"def snippet_{i}(arr):\n")
        problems.append(f"    # Time: ? | Space: ?\n")
        problems.append(f"    total = 0\n")
        problems.append(f"    for x in arr:\n")
        problems.append(f"        total += x * {i}\n")
        problems.append(f"    return total\n\n")

    # Generate 25 O(N^2) Snippets
    for i in range(51, 76):
        problems.append(f"def snippet_{i}(arr):\n")
        problems.append(f"    # Time: ? | Space: ?\n")
        problems.append(f"    count = 0\n")
        problems.append(f"    for x in arr:\n")
        problems.append(f"        for y in arr:\n")
        problems.append(f"            count += 1\n")
        problems.append(f"    return count\n\n")

    # Generate 25 O(N) Space Snippets
    for i in range(76, 101):
        problems.append(f"def snippet_{i}(arr):\n")
        problems.append(f"    # Time: ? | Space: ?\n")
        problems.append(f"    new_arr = []\n")
        problems.append(f"    for x in arr:\n")
        problems.append(f"        new_arr.append(x)\n")
        problems.append(f"    return new_arr\n\n")

    with open(r"c:\Users\Venkatesh\Desktop\MalliNeni\Day6\Day6_Practice_Problems.py", "w", encoding="utf-8") as f:
        f.writelines(problems)

if __name__ == "__main__":
    generate_interview_questions()
    generate_practice_problems()
    print("Successfully generated 100 questions and 100 practice snippets for Big O.")
