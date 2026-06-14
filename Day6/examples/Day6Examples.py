# Day 6 Examples: Time and Space Complexity

print("--- O(1) Constant Time ---")
def print_first_element(arr):
    # No matter how massive the array is, this takes 1 step.
    # Time: O(1)
    # Space: O(1)
    if len(arr) > 0:
        print(arr[0])

print_first_element([10, 20, 30, 40, 50])


print("\n--- O(N) Linear Time ---")
def print_all_elements(arr):
    # The loop runs N times.
    # Time: O(N)
    # Space: O(1) -> We are only printing, not storing extra data.
    for item in arr:
        pass # In a real scenario, print(item)
    print("Finished looping N times.")

print_all_elements([10, 20, 30, 40, 50])


print("\n--- O(N) Time, O(N) Space ---")
def create_copy(arr):
    # The loop runs N times. We also create a new list of size N.
    # Time: O(N)
    # Space: O(N)
    new_list = []
    for item in arr:
        new_list.append(item * 2)
    return new_list

print(create_copy([1, 2, 3]))


print("\n--- Dropping Constants: O(N) ---")
def drop_constants(arr):
    # Loop 1: O(N)
    for i in arr:
        pass
        
    # Loop 2: O(N)
    for j in arr:
        pass
        
    # Total is O(2N), which simplifies to O(N).
    print("Finished 2N loops.")


print("\n--- O(N^2) Quadratic Time ---")
def print_all_pairs(arr):
    # A loop inside a loop. Runs N * N times.
    # Time: O(N^2)
    # Space: O(1) -> We are just printing, not storing.
    count = 0
    for i in arr:
        for j in arr:
            count += 1
    print(f"For {len(arr)} elements, the inner loop ran {count} times!")

print_all_pairs([1, 2, 3, 4, 5]) # N=5, Output will be 25


print("\n--- Linear Search O(N) ---")
def linear_search(arr, target):
    # Time: O(N)
    # Space: O(1)
    for i in range(len(arr)):
        if arr[i] == target:
            return i # Found target
    return -1 # Not found

print(f"Linear search for 30: index {linear_search([10, 20, 30, 40], 30)}")


print("\n--- Factors Program Optimization ---")
def get_factors_brute_force(n):
    # Time: O(N)
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def get_factors_optimized(n):
    # Time: O(sqrt(N))
    factors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
        i += 1
    return factors

print("Factors of 36 (Brute O(N)):", get_factors_brute_force(36))
print("Factors of 36 (Optimized O(sqrt(N))):", sorted(get_factors_optimized(36)))


print("\n--- Prime Number Program Optimization ---")
def is_prime_brute_force(n):
    # Time: O(N)
    if n <= 1: return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime_optimized(n):
    # Time: O(sqrt(N))
    if n <= 1: return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print("Is 29 prime (Brute)?", is_prime_brute_force(29))
print("Is 29 prime (Optimized)?", is_prime_optimized(29))


print("\n--- Nested Loops Dry Run O(N^2) ---")
def nested_loops_dry_run(n):
    # Time: O(N^2)
    # Outer loop runs N times. Inner loop runs N times for EVERY outer loop iteration.
    total_executions = 0
    print(f"Dry Run for n={n}:")
    for i in range(n):
        for j in range(n):
            print(f"  Outer i={i}, Inner j={j}")
            total_executions += 1
    print(f"Total internal executions: {total_executions}")

nested_loops_dry_run(3)
