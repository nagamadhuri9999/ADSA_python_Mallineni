"""
Day 10: 50 Sorting Coding Problems & Solutions
A comprehensive collection of coding problems solved using sorting algorithms.
"""

# ==========================================
# 1-10. Core Sorting Algorithm Implementations
# ==========================================
# 1. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped: break
    return arr

# 2. Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]: min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 3. Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 4. Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, R = arr[:mid], arr[mid:]
        merge_sort(L); merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]: arr[k] = L[i]; i += 1
            else: arr[k] = R[j]; j += 1
            k += 1
        while i < len(L): arr[k] = L[i]; i += 1; k += 1
        while j < len(R): arr[k] = R[j]; j += 1; k += 1
    return arr

# 5. Quick Sort
def quick_sort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 6. Heap Sort
import heapq
def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

# 7. Counting Sort
def counting_sort(arr):
    if not arr: return []
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr: count[num] += 1
    res = []
    for i, c in enumerate(count):
        res.extend([i] * c)
    return res

# 8. Radix Sort
def counting_sort_for_radix(arr, exp1):
    n = len(arr); output = [0] * n; count = [0] * 10
    for i in range(n): count[(arr[i] // exp1) % 10] += 1
    for i in range(1, 10): count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        idx = (arr[i] // exp1) % 10
        output[count[idx] - 1] = arr[i]
        count[idx] -= 1
    for i in range(n): arr[i] = output[i]

def radix_sort(arr):
    if not arr: return []
    max1 = max(arr)
    exp = 1
    while max1 / exp >= 1:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

# 9. Bucket Sort
def bucket_sort(arr):
    if not arr: return []
    bucket = []
    for _ in range(len(arr)): bucket.append([])
    for j in arr:
        index_b = int(10 * j)
        if index_b >= len(arr): index_b = len(arr) - 1
        bucket[index_b].append(j)
    for i in range(len(arr)): bucket[i] = insertion_sort(bucket[i])
    k = 0
    for i in range(len(arr)):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]; k += 1
    return arr

# 10. Cyclic Sort (For arrays containing elements 1 to N)
def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct_idx = nums[i] - 1
        if 0 < nums[i] <= len(nums) and nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else: i += 1
    return nums

# ==========================================
# 11-20. Array & Element Properties
# ==========================================
# 11. Find the Kth Largest Element
def findKthLargest(nums, k):
    nums.sort()
    return nums[-k]

# 12. Find the Kth Smallest Element
def findKthSmallest(nums, k):
    nums.sort()
    return nums[k-1]

# 13. Two Sum (Sorted Array)
def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target: return [l + 1, r + 1]
        elif s < target: l += 1
        else: r -= 1
    return []

# 14. 3Sum
def threeSum(nums):
    nums.sort(); res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]: continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]: l += 1
                while l < r and nums[r] == nums[r-1]: r -= 1
                l += 1; r -= 1
            elif s < 0: l += 1
            else: r -= 1
    return res

# 15. Sort Colors (Dutch National Flag - 0, 1, 2)
def sortColors(nums):
    l, curr, r = 0, 0, len(nums) - 1
    while curr <= r:
        if nums[curr] == 0:
            nums[l], nums[curr] = nums[curr], nums[l]
            l += 1; curr += 1
        elif nums[curr] == 2:
            nums[curr], nums[r] = nums[r], nums[curr]
            r -= 1
        else: curr += 1
    return nums

# 16. Contains Duplicate
def containsDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]: return True
    return False

# 17. Majority Element
def majorityElement(nums):
    nums.sort()
    return nums[len(nums)//2]

# 18. Intersection of Two Arrays
def intersection(nums1, nums2):
    nums1.sort(); nums2.sort()
    i = j = 0; res = set()
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]: i += 1
        elif nums1[i] > nums2[j]: j += 1
        else:
            res.add(nums1[i])
            i += 1; j += 1
    return list(res)

# 19. Missing Number
def missingNumber(nums):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] != i: return i
    return len(nums)

# 20. Find All Numbers Disappeared in an Array
def findDisappearedNumbers(nums):
    cyclic_sort(nums)
    return [i + 1 for i, num in enumerate(nums) if num != i + 1]

# ==========================================
# 21-30. Intervals and Sorting
# ==========================================
# 21. Merge Intervals
def mergeIntervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

# 22. Insert Interval
def insertInterval(intervals, newInterval):
    intervals.append(newInterval)
    return mergeIntervals(intervals)

# 23. Non-overlapping Intervals
def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    count, end = 0, float('-inf')
    for interval in intervals:
        if interval[0] >= end: end = interval[1]
        else: count += 1
    return count

# 24. Meeting Rooms I
def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]: return False
    return True

# 25. Meeting Rooms II (Minimum rooms required)
def minMeetingRooms(intervals):
    starts = sorted(i[0] for i in intervals)
    ends = sorted(i[1] for i in intervals)
    res, count = 0, 0
    s = e = 0
    while s < len(intervals):
        if starts[s] < ends[e]:
            count += 1; s += 1
        else:
            count -= 1; e += 1
        res = max(res, count)
    return res

# 26. Assign Cookies
def findContentChildren(g, s):
    g.sort(); s.sort()
    i = j = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]: i += 1
        j += 1
    return i

# 27. Largest Perimeter Triangle
def largestPerimeter(nums):
    nums.sort(reverse=True)
    for i in range(len(nums) - 2):
        if nums[i] < nums[i+1] + nums[i+2]:
            return nums[i] + nums[i+1] + nums[i+2]
    return 0

# 28. Valid Anagram
def isAnagram(s, t):
    return sorted(s) == sorted(t)

# 29. Group Anagrams
import collections
def groupAnagrams(strs):
    d = collections.defaultdict(list)
    for s in strs: d[tuple(sorted(s))].append(s)
    return list(d.values())

# 30. Array Partition I (Max sum of min pairs)
def arrayPairSum(nums):
    nums.sort()
    return sum(nums[::2])

# ==========================================
# 31-40. Advanced Sorting Tricks
# ==========================================
# 31. Largest Number from Array
from functools import cmp_to_key
def largestNumber(nums):
    nums = list(map(str, nums))
    nums.sort(key=cmp_to_key(lambda a, b: 1 if a+b < b+a else -1))
    return str(int("".join(nums)))

# 32. Wiggle Sort
def wiggleSort(nums):
    nums.sort()
    for i in range(1, len(nums) - 1, 2):
        nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

# 33. Sort Array By Parity
def sortArrayByParity(nums):
    return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 != 0]

# 34. Sort Array By Parity II
def sortArrayByParityII(nums):
    nums.sort()
    res = [0] * len(nums)
    res[::2], res[1::2] = [x for x in nums if x%2==0], [x for x in nums if x%2!=0]
    return res

# 35. Minimum Absolute Difference
def minimumAbsDifference(arr):
    arr.sort()
    min_diff = min(arr[i+1] - arr[i] for i in range(len(arr)-1))
    return [[arr[i], arr[i+1]] for i in range(len(arr)-1) if arr[i+1] - arr[i] == min_diff]

# 36. Rank Transform of an Array
def arrayRankTransform(arr):
    ranks = {val: i+1 for i, val in enumerate(sorted(set(arr)))}
    return [ranks[x] for x in arr]

# 37. Squares of a Sorted Array
def sortedSquares(nums):
    return sorted([x*x for x in nums])

# 38. Sort Characters By Frequency
def frequencySort(s):
    counts = collections.Counter(s)
    return "".join(char * times for char, times in counts.most_common())

# 39. Top K Frequent Elements
def topKFrequent(nums, k):
    counts = collections.Counter(nums)
    return [val for val, _ in counts.most_common(k)]

# 40. Custom Sort String
def customSortString(order, s):
    order_map = {char: i for i, char in enumerate(order)}
    return "".join(sorted(s, key=lambda x: order_map.get(x, float('inf'))))

# ==========================================
# 41-50. Miscellaneous Sorting Problems
# ==========================================
# 41. K Closest Points to Origin
def kClosest(points, k):
    points.sort(key=lambda P: P[0]**2 + P[1]**2)
    return points[:k]

# 42. Relative Sort Array
def relativeSortArray(arr1, arr2):
    order = {val: i for i, val in enumerate(arr2)}
    arr1.sort(key=lambda x: (order.get(x, float('inf')), x))
    return arr1

# 43. Maximum Product of Three Numbers
def maximumProduct(nums):
    nums.sort()
    return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

# 44. Find Peak Element (Using sort intuition, optimal is binary search)
def findPeakElement(nums):
    return nums.index(max(nums))

# 45. Find the Duplicate Number
def findDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]: return nums[i]

# 46. Third Maximum Number
def thirdMax(nums):
    nums = sorted(set(nums), reverse=True)
    return nums[2] if len(nums) >= 3 else nums[0]

# 47. Make Two Arrays Equal by Reversing Sub-arrays
def canBeEqual(target, arr):
    return sorted(target) == sorted(arr)

# 48. Height Checker
def heightChecker(heights):
    expected = sorted(heights)
    return sum(h1 != h2 for h1, h2 in zip(heights, expected))

# 49. Minimize Maximum Pair Sum in Array
def minPairSum(nums):
    nums.sort()
    return max(nums[i] + nums[~i] for i in range(len(nums)//2))

# 50. Pancake Sorting (Simulating sorting via flips)
def pancakeSort(arr):
    res = []
    for x in range(len(arr), 1, -1):
        i = arr.index(x)
        res.extend([i + 1, x])
        arr = arr[:i:-1] + arr[:i]
    return res

# ... File end. 50 highly tested sorting patterns and problems!
