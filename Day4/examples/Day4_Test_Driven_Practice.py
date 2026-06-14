# Day 4: Test-Driven Practice
# Complete the functions below so that all assert statements pass without errors!

def is_anagram(s1, s2):
    """
    Return True if s1 and s2 are anagrams, ignoring case and spaces.
    Otherwise return False.
    """
    # YOUR CODE HERE
    pass

def count_vowels_recursive(s):
    """
    Return the number of vowels (a, e, i, o, u) in the string s using RECURSION.
    """
    # YOUR CODE HERE
    pass

def reverse_string_recursive(s):
    """
    Return the reversed version of string s using RECURSION.
    """
    # YOUR CODE HERE
    pass

# ==========================================
# 🛑 DO NOT MODIFY THE CODE BELOW THIS LINE 
# ==========================================
if __name__ == "__main__":
    print("Running tests...")
    
    # Test is_anagram
    try:
        assert is_anagram("Listen", "Silent") == True
        assert is_anagram("hello", "world") == False
        assert is_anagram("Astronomer", "Moon starer") == True
        print("✅ is_anagram tests passed!")
    except AssertionError:
        print("❌ is_anagram tests failed!")

    # Test count_vowels_recursive
    try:
        assert count_vowels_recursive("hello") == 2
        assert count_vowels_recursive("xyz") == 0
        assert count_vowels_recursive("education") == 5
        print("✅ count_vowels_recursive tests passed!")
    except AssertionError:
        print("❌ count_vowels_recursive tests failed!")

    # Test reverse_string_recursive
    try:
        assert reverse_string_recursive("hello") == "olleh"
        assert reverse_string_recursive("Python") == "nohtyP"
        assert reverse_string_recursive("") == ""
        print("✅ reverse_string_recursive tests passed!")
    except AssertionError:
        print("❌ reverse_string_recursive tests failed!")

    print("Test run complete.")
