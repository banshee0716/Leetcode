from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ans = 0
        # 遍歷矩陣的每一行
        for i, r in enumerate(matrix):
            # 更新每個元素為該列中從該點向上連續1的個數
            for j, c in enumerate(r):
                if i and c:
                    matrix[i][j] += matrix[i - 1][j]
            
            # 對行進行排序並計算面積
            for k, v in enumerate(sorted(r)[::-1], 1):
                ans = max(ans, k * v)
        return ans

        
        #可以隨便排序column，要你處理
        
"""
解題思路：

1.計算連續的1：
    -遍歷矩陣的每一行，對於每一個元素，如果它是1且不在第一行，則將其值更新為它上面元素的值加1。這代表該列中從該點向上連續1的個數。

2.排序並計算面積：
    -對每一行進行排序，然後遍歷排序後的行，計算以當前行中每個數字為高的矩形面積（長度為當前元素在行中的位置，寬度為元素的值），並更新最大面積。

3.返回結果：
    -返回遍歷過程中計算出的最大面積。
    
時間複雜度分析：
計算連續的1的遍歷時間複雜度為 O(m * n)，其中 m 為矩陣的行數，n 為矩陣的列數。
對每一行進行排序的時間複雜度為 O(n log n)，並且需要對 m 行都進行排序，所以總的排序時間複雜度為 O(m * n log n)。
最終的時間複雜度為 O(m * n log n)。

空間複雜度分析：
除了給定的矩陣外，本解法只使用了固定的額外空間，因此空間複雜度為 O(1)。
"""