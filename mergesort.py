data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]


def merge(left, right):
    result = []

    while len(left) and len(right):
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result = result + left if len(left) else result + right
    return result


def mergeSort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    leftArray = array[:mid]
    rightArray = array[mid:]

    return merge(mergeSort(leftArray), mergeSort(rightArray))


print(mergeSort(data))
# [23, 23, 29, 34, 55, 66, 67, 78, 78, 79, 88, 89, 92, 96, 96, 100]
