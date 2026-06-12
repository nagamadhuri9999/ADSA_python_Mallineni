### 704. Binary Search

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
```

---

### 69. Sqrt(x)

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
```

---

### 35. Search Insert Position

```python
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
```

### Common Binary Search Template

```python
left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

Memorize this template first. Problems 704 and 35 are almost identical, and 69 is the same pattern applied to the search space `0...x` instead of an array.
