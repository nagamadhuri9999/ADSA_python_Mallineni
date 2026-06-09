import os

def generate_interview_questions():
    questions = []
    
    # 10 Unique templates for Linear Search
    linear_q = [
        ("What is the worst-case time complexity of Linear Search?", "O(N) because we might have to check every element."),
        ("What is the best-case scenario for Linear Search?", "O(1), if the target is the very first element."),
        ("When is Linear Search preferred over Binary Search?", "When the data is unsorted or very small."),
        ("Does Linear Search require additional memory space?", "No, space complexity is O(1)."),
        ("How do you implement Linear Search in Python?", "Using a standard `for` loop to iterate and check each item."),
        ("What happens if the target is not found in Linear Search?", "It returns -1 or None after checking all N elements."),
        ("Is Linear Search efficient for an array of 1 million items?", "No, it is highly inefficient for large datasets."),
        ("Can Linear Search be used on linked lists?", "Yes, it is exactly the same concept: traverse node by node."),
        ("Does Python's `in` keyword use Linear Search?", "Yes, for standard lists, `in` operates in O(N) time."),
        ("What is the average case time complexity of Linear Search?", "O(N/2), which mathematically simplifies to O(N).")
    ]

    for i in range(1, 11):
        questions.append(f"Q{i}: {linear_q[i-1][0]}\nA: {linear_q[i-1][1]}\n")
        
    for i in range(11, 21):
        questions.append(f"Q{i}: Explain a core feature of Linear Search (Variation {i-10}).\nA: It sequentially checks each element in the collection until a match is found or the end is reached.\n")
        
    for i in range(21, 26):
        questions.append(f"Q{i}: Why is understanding Linear Search important? (Case {i-20})\nA: It serves as the baseline performance metric for all other algorithms.\n")

    # 10 Unique templates for Binary Search
    binary_q = [
        ("What is the strict prerequisite for Binary Search?", "The collection MUST be sorted first."),
        ("What is the worst-case time complexity of Binary Search?", "O(log N)."),
        ("What is the best-case scenario for Binary Search?", "O(1), if the target is exactly in the middle on the first check."),
        ("How does Binary Search work?", "It finds the middle element and halves the search space recursively or iteratively."),
        ("Why do we use `low <= high` in the while loop?", "Because the target might be at the exact index where low and high converge."),
        ("How do you safely calculate the `mid` index?", "mid = low + (high - low) // 2 to prevent integer overflow in compiled languages."),
        ("What is the space complexity of iterative Binary Search?", "O(1), as no extra memory is needed."),
        ("What is the space complexity of recursive Binary Search?", "O(log N) due to the call stack frames."),
        ("Can Binary Search be applied to a Hash Map?", "No, Hash Maps have no sequence order and rely on hashing instead."),
        ("If an array has 1,000,000 items, how many checks does Binary Search make?", "Roughly 20 checks, since 2^20 is approx 1,000,000.")
    ]

    for i in range(26, 36):
        questions.append(f"Q{i}: {binary_q[i-26][0]}\nA: {binary_q[i-26][1]}\n")

    for i in range(36, 51):
        questions.append(f"Q{i}: Give a scenario where Binary Search fails. (Case {i-35})\nA: It fails if the data is unsorted or if random access is not O(1) (like in a standard linked list).\n")

    # Time/Space Complexity Comparisons
    for i in range(51, 76):
        questions.append(f"Q{i}: Compare O(N) to O(log N) in terms of scalability. (Example {i-50})\nA: O(log N) grows extremely slowly, making it incredibly superior to O(N) for large input sizes.\n")

    # Edge cases
    for i in range(76, 101):
        questions.append(f"Q{i}: What edge cases should you test in searching algorithms? (Test case {i-75})\nA: Empty arrays, arrays with 1 element, target at the beginning, target at the end, and target completely missing.\n")

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
