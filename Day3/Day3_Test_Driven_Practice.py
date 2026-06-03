# Day 3: Test-Driven Practice
# Complete the functions below so that all assert statements pass!

def find_max_in_list(lst):
    """
    Return the maximum number in the list without using the built-in max() function.
    """
    # YOUR CODE HERE
    pass

def remove_duplicates(lst):
    """
    Return a new list with duplicates removed, preserving the original order.
    """
    # YOUR CODE HERE
    pass

def sum_even_numbers(lst):
    """
    Return the sum of all even numbers in the list.
    """
    # YOUR CODE HERE
    pass

# ==========================================
# 🛑 DO NOT MODIFY THE CODE BELOW THIS LINE 
# ==========================================
if __name__ == "__main__":
    print("Running tests...")
    
    # Test find_max_in_list
    try:
        assert find_max_in_list([1, 5, 3, 9, 2]) == 9
        assert find_max_in_list([-10, -5, -20]) == -5
        print("✅ find_max_in_list tests passed!")
    except AssertionError:
        print("❌ find_max_in_list tests failed!")

    # Test remove_duplicates
    try:
        assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
        assert remove_duplicates(["a", "b", "a"]) == ["a", "b"]
        print("✅ remove_duplicates tests passed!")
    except AssertionError:
        print("❌ remove_duplicates tests failed!")

    # Test sum_even_numbers
    try:
        assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12
        assert sum_even_numbers([1, 3, 5]) == 0
        print("✅ sum_even_numbers tests passed!")
    except AssertionError:
        print("❌ sum_even_numbers tests failed!")

    print("Test run complete.")
