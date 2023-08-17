from typing import List

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        
        # 從左上到右下進行第一次遍歷
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                # 如果當前值是1，則更新當前值為從左或上到當前的最短距離
                if cell:
                    top = matrix[i-1][j] if i else float('inf')
                    left = matrix[i][j-1] if j else float('inf')
                    matrix[i][j] = min(top, left) + 1
        
        # 從右下到左上進行第二次遍歷
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                # 如果當前值是1，則更新當前值為從右或下到當前的最短距離
                if cell := matrix[i][j]:
                    bottom = matrix[i+1][j] if i < m - 1 else float('inf')
                    right = matrix[i][j+1] if j < n - 1 else float('inf')
                    matrix[i][j] = min(cell, bottom + 1, right + 1)

        return matrix

"""

解決這個問題的一個有效方法是使用動態規劃，分兩階段進行。

從左上到右下：對於每個位置，它到左邊或上邊的0的距離是其左邊或上邊的值加一。
從右下到左上：對於每個位置，它到右邊或下邊的0的距離是其右邊或下邊的值加一。

時間複雜度: O(m * n)，其中m和n分別是矩陣的行數和列數。因為我們遍歷整個矩陣兩次。

空間複雜度: O(1)。儘管我們使用了額外的空間來保存輸出，但它不隨輸入的大小而變化，所以空間複雜度是常數的。
"""