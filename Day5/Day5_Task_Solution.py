# Day 5 Task Solutions: Data Analyzer & Two Sum

def data_analyzer():
    print("--- TASK 1: THE DATA ANALYZER ---")
    print("Enter a list of numbers separated by spaces: ", end="")
    user_input = input()
    
    if not user_input.strip():
        print("No numbers provided. Exiting Data Analyzer.")
        return

    nums = list(map(int, user_input.split()))

    # Basic Analytics
    total_sum = 0
    total_product = 1
    for num in nums:
        total_sum += num
        total_product *= num
        
    average = total_sum / len(nums)

    print("\n--- Analysis Results ---")
    print(f"Sum: {total_sum}")
    print(f"Product: {total_product}")
    print(f"Average: {average}")

    # Frequencies
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    print("\n--- Frequencies ---")
    for key, value in freq.items():
        print(f"Number {key} appears {value} time(s)")

    # Pair Generation
    pairs = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            pairs.append((nums[i], nums[j]))

    print("\n--- Unique Pairs ---")
    print(f"Generated {len(pairs)} unique pairs.")
    print(", ".join(str(p) for p in pairs))


def two_sum_brute_force(nums, target):
    """O(N^2) Solution using nested loops."""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def two_sum_optimized(nums, target):
    """O(N) Solution using a dictionary (hash map)."""
    num_map = {} # val -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []


def main():
    # Run Task 1
    data_analyzer()
    
    print("\n\n--- TASK 2: TWO SUM ---")
    nums = [2, 7, 11, 15]
    target = 9
    print(f"Input: nums = {nums}, target = {target}")
    
    res1 = two_sum_brute_force(nums, target)
    print(f"Brute Force Result: {res1}")
    
    res2 = two_sum_optimized(nums, target)
    print(f"Optimized Result: {res2}")

if __name__ == "__main__":
    main()
