def task1_bubble_sort_visualizer():
    user_input = input("Enter space-separated integers: ")
    arr = list(map(int, user_input.split()))
    swaps = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                print(f"Swap {swaps}: {arr}")
    print(f"Total Swaps: {swaps}")

def task2_insertion_sort_strings(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            # Condition: sort by length first, then alphabetically
            if len(arr[j]) > len(key) or (len(arr[j]) == len(key) and arr[j] > key):
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    print("Task 2 Example:", task2_insertion_sort_strings(["apple", "banana", "kiwi", "pear", "fig"]))
