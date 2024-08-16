class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest = arrays[0][0]
        biggest = arrays[0][-1]
        max_distance = 0
        
        for i in range(1, len(arrays)):
            arr = arrays[i]
            max_distance = max(max_distance, abs(biggest - arr[0]), abs(arr[-1] - smallest))
            smallest = min(smallest, arr[0])
            biggest = max(biggest, arr[-1])
            
        return max_distance
            
        
    
    
    """
給定 m 個數組，其中每個數組按升序排序。

您可以從兩個不同的陣列中選取兩個整數（每個陣列選取一個）並計算距離。我們將兩個整數 a 和 b 之間的距離定義為它們的絕對差 |a - b|。

返回最大距離。
    """