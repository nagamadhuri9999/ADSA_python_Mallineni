# Day 5: List Methods & Algorithms Quiz

Test your knowledge of Day 5 concepts! Choose the best answer for each question.

---

### 1. Are Lists mutable or immutable in Python?
A) Mutable
B) Immutable
C) Both, depending on how they are defined.
D) Immutable only inside loops.

### 2. What does `.append(x)` do to a list?
A) Adds `x` to the beginning of the list.
B) Adds `x` to the end of the list.
C) Replaces the last item with `x`.
D) Creates a new list with `x`.

### 3. What is the difference between `.append()` and `.extend()`?
A) `.append()` adds multiple items; `.extend()` adds one.
B) `.append()` modifies the list; `.extend()` returns a new list.
C) `.append()` adds its argument as a single element; `.extend()` iterates over its argument and adds each element.
D) There is no difference.

### 4. If `x = [1, 2]`, what is the result of `x.append([3, 4])`?
A) `[1, 2, 3, 4]`
B) `[1, 2, [3, 4]]`
C) `[[1, 2], [3, 4]]`
D) `TypeError`

### 5. If `x = [1, 2]`, what is the result of `x.extend([3, 4])`?
A) `[1, 2, 3, 4]`
B) `[1, 2, [3, 4]]`
C) `[[1, 2], [3, 4]]`
D) `TypeError`

### 6. What does `.insert(1, "A")` do on the list `["X", "Y", "Z"]`?
A) Replaces "Y" with "A".
B) Inserts "A" before "X".
C) Inserts "A" at index 1, shifting the rest right -> `["X", "A", "Y", "Z"]`.
D) Inserts "A" at the end.

### 7. What happens if you call `.remove(5)` on the list `[1, 5, 3, 5]`?
A) Removes both 5s.
B) Removes the first 5 only.
C) Removes the last 5 only.
D) Throws an error.

### 8. What happens if you call `.remove(10)` on `[1, 5, 3]`?
A) Nothing.
B) It returns `False`.
C) It raises a `ValueError`.
D) It removes the last item.

### 9. What does `lst.pop()` do if no index is provided?
A) Removes the first item.
B) Removes a random item.
C) Removes and returns the last item.
D) Clears the list.

### 10. If `lst = [10, 20, 30]`, what does `lst.pop(0)` return?
A) `10`
B) `20`
C) `30`
D) `[20, 30]`

### 11. Which method completely empties a list?
A) `.empty()`
B) `.delete()`
C) `.clear()`
D) `.remove_all()`

### 12. If `lst = [4, 1, 3]`, what does `lst.sort()` return?
A) `[1, 3, 4]`
B) `[4, 3, 1]`
C) `None` (it sorts in-place).
D) A copy of the list.

### 13. How do you sort a list `lst` in descending order?
A) `lst.sort(reverse=True)`
B) `lst.sort(descending=True)`
C) `lst.reverse_sort()`
D) `lst.sort(-1)`

### 14. What does the `map(int, ["1", "2"])` function do?
A) Creates a dictionary.
B) Applies the `int()` function to every element in the sequence.
C) Throws an error.
D) Maps indices to strings.

### 15. What is the standard way to read space-separated numbers into a list of integers?
A) `list(int(input().split()))`
B) `list(map(int, input().split()))`
C) `int(input().split(" "))`
D) `[int(x) for x in input()]`

### 16. In the frequency counting algorithm using a dictionary, what does `freq.get(num, 0)` do?
A) Returns 0 if the dictionary is empty.
B) Returns the value for `num`, or 0 if `num` is not yet in the dictionary.
C) Always returns 0.
D) Sets the value of `num` to 0.

### 17. Why is `freq[num] = freq.get(num, 0) + 1` better than `freq[num] = freq[num] + 1`?
A) It is faster.
B) It avoids a `KeyError` when `num` is seen for the very first time.
C) It uses less memory.
D) It sorts the dictionary automatically.

### 18. What is the Time Complexity of checking if an item is in a List (e.g., `x in lst`)?
A) O(1)
B) O(log n)
C) O(n)
D) O(n^2)

### 19. What is the Time Complexity of checking if a key is in a Dictionary (e.g., `key in dict`)?
A) O(1) average
B) O(log n)
C) O(n)
D) O(n^2)

### 20. If you want to print all unique pairs of a list without duplicates like (A,B) and (B,A), how should the inner loop be set up?
A) `for j in range(len(lst)):`
B) `for j in range(i, len(lst)):`
C) `for j in range(i + 1, len(lst)):`
D) `for j in range(len(lst) - 1):`

### 21. What happens if you assign `lst2 = lst1` and then modify `lst2`?
A) Only `lst2` is modified.
B) Both `lst1` and `lst2` are modified because they point to the same memory object.
C) A `TypeError` is raised.
D) Python automatically creates a copy.

### 22. How do you create a "shallow copy" of `lst1` so modifying it doesn't affect `lst1`?
A) `lst2 = lst1.copy()`
B) `lst2 = lst1[:]`
C) `lst2 = list(lst1)`
D) All of the above

### 23. What is the output of `[1, 2] * 3`?
A) `[3, 6]`
B) `[1, 2, 1, 2, 1, 2]`
C) `[[1, 2], [1, 2], [1, 2]]`
D) `TypeError`

### 24. What does the built-in `sum()` function do?
A) Adds a number to a list.
B) Returns the sum of all elements in an iterable (like a list).
C) Concatenates lists.
D) Finds the maximum value.

### 25. Which built-in function returns the largest item in an iterable?
A) `largest()`
B) `top()`
C) `max()`
D) `peak()`

### 26. If `x = [10, 20, 30]`, what is the output of `x.index(20)`?
A) `1`
B) `2`
C) `20`
D) `True`

### 27. What happens if you call `.index(100)` on a list that doesn't contain 100?
A) Returns `-1`
B) Returns `False`
C) Returns `None`
D) Raises a `ValueError`

### 28. Which of these is NOT a valid list method?
A) `.append()`
B) `.push()`
C) `.pop()`
D) `.remove()`

### 29. Can a list contain elements of different data types? (e.g., `[1, "hello", True]`)
A) Yes
B) No, all elements must be of the same type.

### 30. What is the output of `len([1, [2, 3], 4])`?
A) `4`
B) `3`
C) `2`
D) `Error`

### 31. How can you find the number of times `5` appears in `lst`?
A) `lst.find(5)`
B) `lst.search(5)`
C) `lst.count(5)`
D) `count(lst, 5)`

### 32. What does `.reverse()` do?
A) Reverses the list and returns it.
B) Reverses the list in-place and returns `None`.
C) Sorts the list in descending order.
D) Reverses the characters of strings inside the list.

### 33. If `a = [1, 2, 3]`, what does `del a[1]` do?
A) Deletes the number 1.
B) Deletes the element at index 1 (the number 2).
C) Deletes the entire list.
D) Throws an error.

### 34. What is list comprehension used for?
A) A concise way to create lists.
B) A way to understand list memory.
C) Sorting lists faster.
D) Deleting lists.

### 35. What is the boolean evaluation of an empty list `[]`?
A) `True`
B) `False`
C) `None`
D) `Error`

---
<details>
<summary><b>Click here to view the answers</b></summary>

1. **A) Mutable**
2. **B) Adds `x` to the end of the list.**
3. **C) `.append()` adds its argument as a single element; `.extend()` iterates over its argument and adds each element.**
4. **B) `[1, 2, [3, 4]]`**
5. **A) `[1, 2, 3, 4]`**
6. **C) Inserts "A" at index 1, shifting the rest right.**
7. **B) Removes the first 5 only.**
8. **C) It raises a `ValueError`.**
9. **C) Removes and returns the last item.**
10. **A) `10`**
11. **C) `.clear()`**
12. **C) `None` (it sorts in-place).**
13. **A) `lst.sort(reverse=True)`**
14. **B) Applies the `int()` function to every element in the sequence.**
15. **B) `list(map(int, input().split()))`**
16. **B) Returns the value for `num`, or 0 if `num` is not yet in the dictionary.**
17. **B) It avoids a `KeyError` when `num` is seen for the very first time.**
18. **C) O(n)**
19. **A) O(1) average**
20. **C) `for j in range(i + 1, len(lst)):`**
21. **B) Both `lst1` and `lst2` are modified because they point to the same memory object.**
22. **D) All of the above**
23. **B) `[1, 2, 1, 2, 1, 2]`**
24. **B) Returns the sum of all elements in an iterable.**
25. **C) `max()`**
26. **A) `1`**
27. **D) Raises a `ValueError`**
28. **B) `.push()`**
29. **A) Yes**
30. **B) `3`**
31. **C) `lst.count(5)`**
32. **B) Reverses the list in-place and returns `None`.**
33. **B) Deletes the element at index 1 (the number 2).**
34. **A) A concise way to create lists.**
35. **B) `False`**

</details>
