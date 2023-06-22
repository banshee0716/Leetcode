"""
lumoto partitioning
"""


def QuickSort(arr, start, end):
    if start < end:
        pivotIndex = partition(arr, start, end)
        QuickSort(arr, start, pivotIndex - 1)
        QuickSort(arr, pivotIndex + 1, end)
    return arr


def partition(arr, start, end):
    n = len(arr)
    pivot = arr[end]
    nextIndex = start
    for i in range(start, n-1):
        if arr[i] < pivot:
            arr[nextIndex], arr[i] = arr[i], arr[nextIndex]
            nextIndex += 1
    arr[nextIndex], arr[end] = arr[end], arr[nextIndex]
    return nextIndex


data = [50, 90, 70, 20, 10, 30, 40, 60, 80]

print(QuickSort(data, 0, len(data)-1))
# [10, 20, 30, 40, 50, 60, 70, 80, 90]
"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] # 把中心當成pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


print(quick_sort([3, 6, 8, 10, 1, 2, 1]))
"""