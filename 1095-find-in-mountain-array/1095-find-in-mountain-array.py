# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def findPeak(mountain_arr):
            left, right = 0, mountain_arr.length()-1
            while left < right:
                mid = left + (right-left)//2
                if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                    left = mid+1
                else:
                    right = mid
            return left
        
        def binary_search(left, right, is_increasing):
            while left <= right:
                mid = left + (right - left) // 2
                mid_val = mountain_arr.get(mid)
                if mid_val == target:
                    return mid
                if mid_val < target:
                    if is_increasing:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if is_increasing:
                        right = mid - 1
                    else:
                        left = mid + 1
            return -1        
        
        peak_index = findPeak(mountain_arr)
        result = binary_search(0, peak_index, True)
        if result == -1:
            result = binary_search(peak_index + 1, mountain_arr.length() - 1, False)
        return result
        
        """
（這個問題是交互問題。）

您可能還記得，數組 arr 是山數組當且僅當：

- arr.length >= 3
- 存在一些 0 < i < arr.length - 1 的 i ，這樣：
    - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

給定一個山數組 mountainArr，傳回滿足 mountainArr.get(index) == target 的最小索引。如果這樣的索引不存在，則傳回-1。

無法直接進入山陣。您只能使用 MountainArray 介面存取該陣列：

- MountainArray.get(k) 傳回索引 k（從 0 開始索引）處的陣列元素。
- MountainArray.length() 傳回數組的長度。
調用 MountainArray.get 超過 100 次的提交將被判定為錯誤答案。此外，任何試圖規避法官的解決方案都將導致取消資格。
        """