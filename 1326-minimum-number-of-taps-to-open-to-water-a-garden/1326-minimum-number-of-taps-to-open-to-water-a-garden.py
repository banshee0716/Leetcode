from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # 初始化 arr 陣列，用於儲存每個點能達到的最遠距離
        arr = [0] * (n+1)
        for i, r in enumerate(ranges):
            if r == 0:
                continue
            # 計算這個灌溉設備能覆蓋的左側邊界
            left = max(0, i-r)
            # 更新 arr[left]，也就是說，從 left 點出發能到達的最遠距離
            arr[left] = max(arr[left], i+r)
        
        # 初始化變數
        end, far_can_reach, cnt = 0, 0, 0
        for i, reach in enumerate(arr):
            # 如果 i 超過了 end，表示需要開啟一個新的灌溉設備
            if i > end:
                if far_can_reach <= end:
                    return -1  # 無法覆蓋整個區域
                # 更新 end 和 cnt
                end, cnt = far_can_reach, cnt + 1
            
            # 更新 far_can_reach，也就是到目前為止能達到的最遠距離
            far_can_reach = max(far_can_reach, reach)
        
        # 如果 end 還沒達到 n，cnt 需要加 1
        return cnt + (end < n)

        
        
        
"""
    這個 LeetCode 1326 題的問題是給定一個長度為 n+1 的陣列 ranges，其中 ranges[i] 表示位置 i 的灌溉設備能覆蓋 [i-ranges[i], i+ranges[i]] 的區域。問題是要找出最少需要開啟多少個灌溉設備來覆蓋 [0, n] 的區域。

解題思路：
1. 首先，創建一個長度為 n+1 的陣列 arr，並初始化為 0。這個 arr 用來儲存每個位置能達到的最遠距離。
2. 遍歷 ranges 陣列，用來更新 arr。
3. 再次遍歷 arr 陣列，用貪心算法來找出最少需要的灌溉設備數量。

時間複雜度: 程式碼中有兩個主要的迴圈，每個迴圈的時間複雜度都是 O(n)，所以總的時間複雜度是 O(n)。
空間複雜度: 我們創建了一個長度為 n+1 的陣列 arr，以及幾個額外的變數，所以總的空間複雜度是 O(n)。
"""