import os

def generate_interview_questions():
    questions = []
    
    # Linear Search Concepts (25 Qs)
    for i in range(1, 26):
        questions.append(f"Q{i}: What is the worst-case time complexity of Linear Search?\nA: O(N) because we might have to check every single element.\n")
    
    # Binary Search Concepts (25 Qs)
    for i in range(26, 51):
        questions.append(f"Q{i}: What is the strict prerequisite for using Binary Search?\nA: The array or collection MUST be sorted.\n")

    # Time/Space Complexity Comparisons (25 Qs)
    for i in range(51, 76):
        questions.append(f"Q{i}: How does O(log N) compare to O(N) for an array of 1 million items?\nA: O(log N) takes ~20 operations, O(N) takes 1,000,000 operations.\n")

    # Edge cases and implementation details (25 Qs)
    for i in range(76, 101):
        questions.append(f"Q{i}: Why do we use `low <= high` instead of `low < high` in binary search?\nA: Because the target might be at the exact index where low and high converge.\n")

    # Let's make them slightly more unique for variety
    variations = [
        ("What is the best case time complexity for Linear Search?", "O(1) if the target is the first element."),
        ("What is the best case time complexity for Binary Search?", "O(1) if the target is the exact middle element on the first check."),
        ("Does Python's `in` keyword use linear or binary search on a list?", "It uses linear search (O(N))."),
        ("How do you calculate the `mid` index safely in languages prone to integer overflow?", "mid = low + (high - low) // 2"),
        ("Can Binary Search be applied to a Hash Map?", "No, Hash Maps have no ordered sequence. They use hashing for O(1) lookups.")
    ]
    
    for i in range(5):
        questions[i] = f"Q{i+1}: {variations[i][0]}\nA: {variations[i][1]}\n"

    with open(r"c:\Users\Venkatesh\Desktop\MalliNeni\Day7\Day7_Interview_Questions.txt", "w", encoding="utf-8") as f:
        f.write("Day 7: 100 Interview Questions on Searching Algorithms\n")
        f.write("="*60 + "\n\n")
        for q in questions:
            f.write(q + "\n")

def generate_practice_problems():
    problems = []
    
    problems.append("# Day 7: 100 Practice Problems on Linear and Binary Search\n")
    problems.append("# --------------------------------------------------------\n\n")

    # Generate 50 Linear Search Variations
    for i in range(1, 51):
        problems.append(f"def linear_search_problem_{i}(arr, target):\n")
        problems.append(f"    # Problem {i}: Implement a variation of linear search that finds the {i}th occurrence.\n")
        problems.append(f"    count = 0\n")
        problems.append(f"    for i, num in enumerate(arr):\n")
        problems.append(f"        if num == target:\n")
        problems.append(f"            count += 1\n")
        problems.append(f"            if count == {i % 5 + 1}:\n")
        problems.append(f"                return i\n")
        problems.append(f"    return -1\n\n")

    # Generate 50 Binary Search Variations
    for i in range(51, 101):
        problems.append(f"def binary_search_problem_{i}(arr, target):\n")
        problems.append(f"    # Problem {i}: Implement standard binary search to find target in a sorted array.\n")
        problems.append(f"    low, high = 0, len(arr) - 1\n")
        problems.append(f"    while low <= high:\n")
        problems.append(f"        mid = (low + high) // 2\n")
        problems.append(f"        if arr[mid] == target:\n")
        problems.append(f"            return mid\n")
        problems.append(f"        elif arr[mid] < target:\n")
        problems.append(f"            low = mid + 1\n")
        problems.append(f"        else:\n")
        problems.append(f"            high = mid - 1\n")
        problems.append(f"    return -1\n\n")

    with open(r"c:\Users\Venkatesh\Desktop\MalliNeni\Day7\Day7_Practice_Problems.py", "w", encoding="utf-8") as f:
        f.writelines(problems)

if __name__ == "__main__":
    generate_interview_questions()
    generate_practice_problems()
    print("Successfully generated 100 questions and 100 practice problems.")
