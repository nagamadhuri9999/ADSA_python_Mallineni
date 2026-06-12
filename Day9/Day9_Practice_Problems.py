# Day 9: Practice Problems on Advanced Sorting Deep Dive
# --------------------------------------------------------

# ==========================================
# PROBLEM 1: Hoare Partition Scheme
# ==========================================
def quick_sort_hoare(arr, low, high):
    if low < high:
        pi = hoare_partition(arr, low, high)
        # Note: The pivot element is not necessarily placed in its final 
        # sorted position like in Lomuto. We include it in the left sub-array.
        quick_sort_hoare(arr, low, pi)
        quick_sort_hoare(arr, pi + 1, high)

def hoare_partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1
    
    while True:
        # Move right while elements are smaller than pivot
        i += 1
        while arr[i] < pivot:
            i += 1
            
        # Move left while elements are strictly greater than pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1
            
        # If pointers cross, partition is done
        if i >= j:
            return j
            
        # Swap elements on the wrong side of the pivot
        arr[i], arr[j] = arr[j], arr[i]


# ==========================================
# PROBLEM 2: QuickSelect (Kth Smallest Element)
# ==========================================
def quick_select(arr, low, high, k):
    if low == high:
        return arr[low]
        
    pivot_index = lomuto_partition(arr, low, high)
    
    # If the pivot is at the exact Kth position, we found it!
    if k == pivot_index:
        return arr[k]
    # If K is less than the pivot index, search the left sub-array
    elif k < pivot_index:
        return quick_select(arr, low, pivot_index - 1, k)
    # If K is greater, search the right sub-array
    else:
        return quick_select(arr, pivot_index + 1, high, k)

def lomuto_partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


# ==========================================
# PROBLEM 3: Count Inversions using Merge Sort
# ==========================================
def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0
        
    mid = len(arr) // 2
    left, inv_left = count_inversions(arr[:mid])
    right, inv_right = count_inversions(arr[mid:])
    
    merged, inv_merge = merge_and_count(left, right)
    
    return merged, inv_left + inv_right + inv_merge

def merge_and_count(left, right):
    merged = []
    i = j = inversions = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            # Since left array is sorted, if left[i] > right[j],
            # then ALL remaining elements in left array are also > right[j]
            inversions += len(left) - i
            
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, inversions


if __name__ == "__main__":
    print("Testing Quick Sort (Hoare Partitioning):")
    arr1 = [10, 7, 8, 9, 1, 5]
    quick_sort_hoare(arr1, 0, len(arr1)-1)
    print(f"Sorted array: {arr1}")
    
    print("\nTesting QuickSelect (Find 2nd Smallest Element):")
    arr2 = [7, 10, 4, 3, 20, 15]
    # 2nd smallest element is at index 1 in a sorted 0-indexed array
    k_index = 1 
    result = quick_select(arr2.copy(), 0, len(arr2)-1, k_index)
    print(f"2nd smallest element is: {result}")
    
    print("\nTesting Count Inversions:")
    arr3 = [2, 4, 1, 3, 5] # Inversions: (2,1), (4,1), (4,3) -> Total 3
    _, inv_count = count_inversions(arr3)
    print(f"Number of inversions in {arr3}: {inv_count}")
