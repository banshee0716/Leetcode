from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        def check(arr):
            # 檢查數組是否可以通過排序後形成等差數列
            arr.sort()
            diff = arr[1] - arr[0]
            for i in range(2, len(arr)):
                if arr[i] - arr[i - 1] != diff:
                    return False
            return True
        
        ans = []
        # 處理每個查詢
        for i in range(len(l)):
            arr = nums[l[i]: r[i] + 1]
            ans.append(check(arr))
        
        return ans


    
"""
「判斷子數組是否可以通過排序後形成等差數列」的目標是對於給定的數組 nums 和一系列查詢（由兩個列表 l 和 r 表示），檢查每個查詢定義的子數組是否可以通過排序後形成等差數列。

解題思路：

檢查等差數列：
定義一個輔助函數 check 來判斷一個數組是否可以通過排序後形成等差數列。這個函數首先對數組進行排序，然後檢查數組中任意兩個相鄰元素的差是否相等。

處理每個查詢：
遍歷查詢列表 l 和 r，對於每個查詢，取出 nums 中對應的子數組，並使用 check 函數檢查這個子數組是否能形成等差數列。

返回結果：
對於每個查詢，將 check 函數的結果存入結果列表 ans 中，最後返回這個列表。

時間複雜度分析：

    -對於每個查詢，需要對子數組進行排序，所以每次查詢的時間複雜度為 O(m log m)，其中 m 是子數組的長度。
    -如果有 k 個查詢，則總的時間複雜度為 O(k * m log m)。

空間複雜度分析：
    -需要額外的空間來存儲每次查詢的結果，所以空間複雜度為 O(k)。
"""