class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 如果矩陣不存在或者矩陣的第一行不存在，返回 False
        if not matrix or not matrix[0]:
            return False

        row, col = len(matrix), len(matrix[0])  # 獲取矩陣的行數和列數

        left, right = 0, row * col - 1  # 定義二分查找的起始和結束索引

        # 進行二分查找
        while left < right:
            mid = left + (right - left) // 2  # 計算中間索引

            # 如果中間索引對應的元素小於目標值，則把左邊界移動到 mid + 1
            if matrix[mid // col][mid % col] < target:
                left = mid + 1
            # 如果中間索引對應的元素大於或等於目標值，則把右邊界移動到 mid
            else:
                right = mid

        # 最後檢查左邊界對應的元素是否等於目標值
        return target == matrix[left // col][left % col]

"""
時間複雜度是 O(log(mn))，其中 m 是 matrix 的行數，n 是列數。這是因為我們將矩陣視為一個長度為 mn 的排序列表並進行二分查找，二分查找的時間複雜度為 O(logN)。

空間複雜度是 O(1)。我們只使用了數個額外變量，並未使用與輸入數據規模相關的額外空間。
"""