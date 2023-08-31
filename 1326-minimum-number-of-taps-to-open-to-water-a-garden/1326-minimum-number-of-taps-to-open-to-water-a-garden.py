class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        arr = [0] * (n + 1)
        for i, r in enumerate(ranges):
            if r == 0:
                continue
            left = max(0, i - r)
            arr[left] = max(arr[left], i + r)

        end, far_can_reach, cnt = 0, 0, 0
        
        for i, reach in enumerate(arr):
            if i > end:
                if far_can_reach <= end:
                    return -1
                end, cnt = far_can_reach, cnt + 1
            far_can_reach = max(far_can_reach, reach)

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