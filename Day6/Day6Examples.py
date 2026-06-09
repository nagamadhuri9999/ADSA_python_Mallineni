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
