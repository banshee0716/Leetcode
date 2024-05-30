from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]
        
        count = 0
        for i in range(n):
            for k in range(i + 1, n):
                if prefix[i] == prefix[k + 1]:
                    count += (k - i)
        
        return count
    
"""
解題思路
我們可以利用前綴異或數組來解決這個問題。前綴異或數組 prefix 的第 i 個元素表示 arr 從 0 到 i-1 的所有元素的異或和。這樣，我們可以將問題轉換為檢查是否存在 prefix[i] == prefix[k + 1] 來確定是否滿足條件。

建立一個前綴異或數組 prefix。
使用兩個嵌套迴圈來檢查所有可能的 (i, k) 組合。
當 prefix[i] == prefix[k + 1] 時，表示 arr[i] ^ ... ^ arr[k] = 0，因此有 k - i 個滿足條件的 j。
"""