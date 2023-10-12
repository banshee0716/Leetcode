# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # 定義一個函數，用來找到山脈的頂點
        def findPeak(mountain_arr):
            left, right = 0, mountain_arr.length()-1
            while left < right:
                mid = left + (right-left)//2
                if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid
            return left
        
        # 定義一個二分查找函數
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
        
        # 首先找到山頂        
        peak_index = findPeak(mountain_arr)
        # 在山的左側進行二分查找
        result = binary_search(0, peak_index, True)
        # 如果左側找不到，則在山的右側進行二分查找
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
        
解題思路：      
山脈數組是先嚴格遞增，然後嚴格遞減的數組。這個問題給定一個 MountainArray 接口，提供了兩個API：get(index) 用於取得下標為 index 的元素，以及 length() 用於獲取數組長度。並且給定一個目標值 target，要求我們找出這個目標值在山脈數組中的下標，如果存在多個，返回最小的下標，如果不存在，返回 -1。

解題思路：
1. 找到山頂元素：使用二分查找方法找到數組中的最大元素（山頂）。
2. 在山的左側查找目標元素：在 0 到 山頂的區間進行正常的二分查找。
3. 在山的右側查找目標元素：如果在左側沒有找到目標元素，則在山頂到數組末尾的區間進行反向的二分查找（因為是遞減的）。

時間複雜度：
找山頂：O(logN)，其中N 是 MountainArray 的長度。
兩次二分查找：各自 O(logN)。
所以總時間複雜度為：O(logN)。

空間複雜度：
由於我們只用到了常數個額外變數，所以空間複雜度為：O(1)。
        """