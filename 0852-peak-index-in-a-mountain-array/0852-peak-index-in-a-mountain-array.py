class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1
        while left < right:
            mid = left + (right - left)//2
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid
                
        return left
        
        
"""
其實就是一個裸的binary search，如果arr[mid] < arr[mid + 1]，說明我們現在正在上山，所以我們將左指針移動到mid + 1，尋找mid右側的山峰。
否則，我們正在下山或已經到達山頂。在這種情況下，我們將右指針移動到 mid 來搜索 mid 左側的峰值。

Time complexity: O(log n)
Space complexity: O(1)
"""


