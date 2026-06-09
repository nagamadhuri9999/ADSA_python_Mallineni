# Day 3: Slicing Mastery (Positive vs Negative Steps)
# 
# RULE 1: Positive Step (+1, +2): You are moving FORWARD (Left to Right).
#         Therefore, START index must be LESS THAN STOP index (start < stop). 
#         If start > stop, you get an empty string/list.
#
# RULE 2: Negative Step (-1, -2): You are moving BACKWARD (Right to Left).
#         Therefore, START index must be GREATER THAN STOP index (start > stop).
#         If start < stop, you get an empty string/list.
# --------------------------------------------------------------------------------

text = "PythonProgramming"
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("--- SCENARIO 1: POSITIVE STEP (Moving Forward) ---")
print("Expected Rule: start < stop -> Returns data")
print("Expected Rule: start > stop -> Returns EMPTY")
print()

# Example 1: Valid Positive Step (Strings)
print("1.", "text[0:6:1]    ->", text[0:6:1])    # 'Python' (0 < 6)

# Example 2: Valid Positive Step (Lists)
print("2.", "nums[2:7:1]    ->", nums[2:7:1])    # [2, 3, 4, 5, 6] (2 < 7)

# Example 3: Valid Positive Step with Jump
print("3.", "text[0:10:2]   ->", text[0:10:2])   # 'PtoPo' (0 < 10)

# Example 4: Defaults (Start defaults to 0, stop to end)
print("4.", "nums[:5]       ->", nums[:5])       # [0, 1, 2, 3, 4] (0 < 5)

# Example 5: Negative Indexing but still moving forward!
print("5.", "text[-11:-1:1] ->", text[-11:-1:1]) # 'Programmin' (-11 < -1)

# Example 6: INVALID Positive Step (Start > Stop)
print("6.", "text[6:0:1]    ->", repr(text[6:0:1])) # '' (6 > 0, returns empty)

# Example 7: INVALID Positive Step (Lists)
print("7.", "nums[8:2:1]    ->", nums[8:2:1])    # [] (8 > 2, returns empty)

# Example 8: INVALID Positive Step with Negative Indices
print("8.", "text[-1:-5:1]  ->", repr(text[-1:-5:1])) # '' (-1 > -5, returns empty)

# Example 9: Valid Positive Step across negative to positive index boundaries
# Note: text has length 17. Index -5 is 'm'. Index 15 is 'n'.
print("9.", "text[-5:15:1]  ->", text[-5:15:1])  # 'mi' (-5 < 15 conceptually)

# Example 10: Valid Positive Step where start is extremely small (defaults to 0)
print("10.","nums[-100:3:1] ->", nums[-100:3:1]) # [0, 1, 2] (Start clamped to 0)


print("\n--- SCENARIO 2: NEGATIVE STEP (Moving Backward) ---")
print("Expected Rule: start > stop -> Returns data")
print("Expected Rule: start < stop -> Returns EMPTY")
print()

# Example 11: Valid Negative Step (Strings)
print("11.", "text[6:0:-1]   ->", text[6:0:-1])   # 'Pnohty' (6 > 0)

# Example 12: Valid Negative Step (Lists)
print("12.", "nums[8:2:-1]   ->", nums[8:2:-1])   # [8, 7, 6, 5, 4, 3] (8 > 2)

# Example 13: Valid Negative Step with Jump
print("13.", "nums[9:0:-2]   ->", nums[9:0:-2])   # [9, 7, 5, 3, 1] (9 > 0)

# Example 14: Defaults (Start defaults to END, stop defaults to BEGINNING)
print("14.", "text[::-1]     ->", text[::-1])     # 'gnimmargorPnohtyP' (Reverses)

# Example 15: Valid Negative Step using Negative Indices
print("15.", "text[-1:-11:-1]->", text[-1:-11:-1]) # 'gnimmargor' (-1 > -11)

# Example 16: INVALID Negative Step (Start < Stop)
print("16.", "text[0:6:-1]   ->", repr(text[0:6:-1])) # '' (0 < 6, returns empty)

# Example 17: INVALID Negative Step (Lists)
print("17.", "nums[2:8:-1]   ->", nums[2:8:-1])   # [] (2 < 8, returns empty)

# Example 18: INVALID Negative Step with Negative Indices
print("18.", "text[-5:-1:-1] ->", repr(text[-5:-1:-1])) # '' (-5 < -1, returns empty)

# Example 19: Valid Negative Step spanning index boundary types
print("19.", "text[15:-5:-1] ->", text[15:-5:-1]) # 'ni' (15 > -5 conceptually)

# Example 20: Reversing a specific sub-list correctly
# We want to get elements from index 4 to 1 backwards [4, 3, 2]
print("20.", "nums[4:0:-1]   ->", nums[4:0:-1])   # [4, 3, 2, 1] (4 > 0)

print("\n--- CONCLUSION ---")
print("If step is POSITIVE, start MUST be to the left of stop.")
print("If step is NEGATIVE, start MUST be to the right of stop.")
