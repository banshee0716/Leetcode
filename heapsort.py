
def maxHeapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
  
    if l < n and arr[i] < arr[l]:
        largest = l
  
    if r < n and arr[largest] < arr[r]:
        largest = r
  
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        maxHeapify(arr, n, largest)
  
def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        maxHeapify(arr, n, i)
  
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        maxHeapify(arr, i, 0)

data = [30,20,15,1,10,5]
heapSort(data)
print(data)
#1,5,10,15,20,30
#heap 是一種把二元樹化為陣列來實現的資料結構，可以想像成是index 0為最大值的二元樹，heap sort可視為不斷進行max heap維護的過程
#https://medium.com/starbugs/%E4%BE%86%E5%BE%81%E6%9C%8D%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E8%88%87%E6%BC%94%E7%AE%97%E6%B3%95%E5%90%A7-%E6%90%9E%E6%87%82-binary-heap-%E7%9A%84%E6%8E%92%E5%BA%8F%E5%8E%9F%E7%90%86-96768ea30d3f