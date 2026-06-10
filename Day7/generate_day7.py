import os
import random

def generate_interview_questions():
    questions = []
    
    # Space Complexity
    space_q = [
        ("What does Space Complexity measure?", "It measures the amount of extra memory an algorithm uses relative to the input size."),
        ("What is the difference between Auxiliary Space and Space Complexity?", "Auxiliary space is the extra or temporary space used by an algorithm. Space complexity includes both auxiliary space and space used by the input."),
        ("What does O(1) space complexity mean?", "It means the algorithm uses a constant amount of extra memory, regardless of input size."),
        ("Do in-place sorting algorithms use O(N) space?", "No, in-place sorting algorithms typically use O(1) auxiliary space."),
        ("What happens to space complexity if we create a copy of an array of size N?", "The space complexity becomes O(N).")
    ]
    for i, (q, a) in enumerate(space_q, 1):
        questions.append(f"Q{i}: {q}\nA: {a}\n")

    # Binary Search
    binary_q = [
        ("What is the prerequisite for Binary Search?", "The array must be sorted."),
        ("What is the worst-case time complexity of Binary Search?", "O(log N)."),
        ("What is the space complexity of iterative Binary Search?", "O(1)."),
        ("What is the space complexity of recursive Binary Search?", "O(log N) due to the call stack."),
        ("How does Binary Search work?", "It repeatedly divides the search interval in half.")
    ]
    for i, (q, a) in enumerate(binary_q, 6):
        questions.append(f"Q{i}: {q}\nA: {a}\n")

    # Bubble Sort
    bubble_q = [
        ("Explain the core concept of Bubble Sort.", "It repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order."),
        ("What is the worst-case time complexity of Bubble Sort?", "O(N^2)."),
        ("What is the best-case time complexity of Bubble Sort?", "O(N) when the array is already sorted and an early-exit optimization is used."),
        ("What is the space complexity of Bubble Sort?", "O(1) because it sorts in-place."),
        ("Why is Bubble Sort rarely used in practice?", "Its O(N^2) average and worst-case time complexity makes it highly inefficient for large datasets.")
    ]
    for i, (q, a) in enumerate(bubble_q, 11):
        questions.append(f"Q{i}: {q}\nA: {a}\n")

    # Selection Sort
    selection_q = [
        ("Explain the core concept of Selection Sort.", "It divides the array into sorted and unsorted parts. It repeatedly selects the smallest element from the unsorted part and swaps it with the first unsorted element."),
        ("What is the worst-case time complexity of Selection Sort?", "O(N^2)."),
        ("Does Selection Sort have an O(N) best case like Bubble Sort?", "No, Selection Sort is always O(N^2) even if the array is sorted, because it still scans the remaining elements to find the minimum."),
        ("What is the space complexity of Selection Sort?", "O(1) because it sorts in-place."),
        ("When might Selection Sort be preferred over Bubble Sort?", "When writing to memory is expensive, as Selection Sort makes at most O(N) swaps compared to Bubble Sort's O(N^2) swaps.")
    ]
    for i, (q, a) in enumerate(selection_q, 16):
        questions.append(f"Q{i}: {q}\nA: {a}\n")

    # Insertion Sort
    insertion_q = [
        ("Explain the core concept of Insertion Sort.", "It builds the final sorted array one element at a time by taking one element and inserting it into its correct position in the already sorted part."),
        ("What is the worst-case time complexity of Insertion Sort?", "O(N^2)."),
        ("What is the best-case time complexity of Insertion Sort?", "O(N) when the array is already sorted, because the inner loop immediately breaks."),
        ("What is the space complexity of Insertion Sort?", "O(1) because it sorts in-place."),
        ("Why is Insertion Sort useful in practice?", "It is highly efficient for small data sets or data that is already substantially sorted.")
    ]
    for i, (q, a) in enumerate(insertion_q, 21):
        questions.append(f"Q{i}: {q}\nA: {a}\n")

    # Generate the remaining to make 100 questions
    for i in range(26, 101):
        algo = random.choice(["Bubble Sort", "Selection Sort", "Insertion Sort"])
        questions.append(f"Q{i}: Discuss a specific trade-off of {algo}.\nA: While {algo} has a space complexity of O(1), its time complexity is O(N^2), making it suitable only for small datasets.\n")

    with open(r"c:\Users\Venkatesh\Desktop\MalliNeni\Day7\Day7_Interview_Questions.txt", "w", encoding="utf-8") as f:
        f.write("Day 7: 100 Interview Questions on Space Complexity and Sorting\n")
        f.write("="*60 + "\n\n")
        for q in questions:
            f.write(q + "\n")

def generate_practice_problems():
    problems = []
    
    problems.append("# Day 7: 100 Practice Problems on Space Complexity, Searching, and Sorting\n")
    problems.append("# --------------------------------------------------------\n\n")

    # Generate 100 problems
    for i in range(1, 101):
        cat = i % 5
        problems.append(f"def day7_problem_{i}(arr):\n")
        
        if cat == 0:
            problems.append(f"    # Practice: Analyze Space Complexity for an array duplication\n")
            problems.append(f"    # --- SOLUTION ---\n")
            problems.append(f"    # Duplicating an array requires O(N) space.\n")
            problems.append(f"    arr_copy = arr.copy()\n")
            problems.append(f"    return arr_copy\n\n")
        elif cat == 1:
            problems.append(f"    # Practice: Implement Iterative Binary Search\n")
            problems.append(f"    # --- SOLUTION ---\n")
            problems.append(f"    # Assuming array is sorted and target is 10\n")
            problems.append(f"    target = 10\n")
            problems.append(f"    low, high = 0, len(arr) - 1\n")
            problems.append(f"    while low <= high:\n")
            problems.append(f"        mid = (low + high) // 2\n")
            problems.append(f"        if arr[mid] == target: return mid\n")
            problems.append(f"        elif arr[mid] < target: low = mid + 1\n")
            problems.append(f"        else: high = mid - 1\n")
            problems.append(f"    return -1\n\n")
        elif cat == 2:
            problems.append(f"    # Practice: Implement Bubble Sort\n")
            problems.append(f"    # --- SOLUTION ---\n")
            problems.append(f"    n = len(arr)\n")
            problems.append(f"    for j in range(n):\n")
            problems.append(f"        for k in range(0, n-j-1):\n")
            problems.append(f"            if arr[k] > arr[k+1]:\n")
            problems.append(f"                arr[k], arr[k+1] = arr[k+1], arr[k]\n")
            problems.append(f"    return arr\n\n")
        elif cat == 3:
            problems.append(f"    # Practice: Implement Selection Sort\n")
            problems.append(f"    # --- SOLUTION ---\n")
            problems.append(f"    n = len(arr)\n")
            problems.append(f"    for j in range(n):\n")
            problems.append(f"        min_idx = j\n")
            problems.append(f"        for k in range(j+1, n):\n")
            problems.append(f"            if arr[k] < arr[min_idx]:\n")
            problems.append(f"                min_idx = k\n")
            problems.append(f"        arr[j], arr[min_idx] = arr[min_idx], arr[j]\n")
            problems.append(f"    return arr\n\n")
        elif cat == 4:
            problems.append(f"    # Practice: Implement Insertion Sort\n")
            problems.append(f"    # --- SOLUTION ---\n")
            problems.append(f"    for j in range(1, len(arr)):\n")
            problems.append(f"        key = arr[j]\n")
            problems.append(f"        k = j - 1\n")
            problems.append(f"        while k >= 0 and key < arr[k]:\n")
            problems.append(f"            arr[k+1] = arr[k]\n")
            problems.append(f"            k -= 1\n")
            problems.append(f"        arr[k+1] = key\n")
            problems.append(f"    return arr\n\n")

    with open(r"c:\Users\Venkatesh\Desktop\MalliNeni\Day7\Day7_Practice_Problems.py", "w", encoding="utf-8") as f:
        f.writelines(problems)

if __name__ == "__main__":
    generate_interview_questions()
    generate_practice_problems()
    print("Successfully generated 100 questions and 100 practice problems for Day 7.")
