#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
        matrix = [[0 for _ in range(n)] for _ in range(n)]  # 初始化 n x n 的矩陣
        left, right, top, bottom, num = 0, n-1, 0, n-1, 1  # 初始化邊界變數和計數變數

        while left <= right and top <= bottom:  # 滿足條件時進行迴圈
            for i in range(left, right+1):  # 從左到右填充上邊界的元素
                matrix[top][i] = num
                num += 1
            top += 1  # 上邊界下移

            for i in range(top, bottom+1):  # 從上到下填充右邊界的元素
                matrix[i][right] = num
                num += 1
            right -= 1  # 右邊界左移

            if top <= bottom:  # 如果上邊界仍小於等於下邊界
                for i in range(right, left-1, -1):  # 從右到左填充下邊界的元素
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1  # 下邊界上移

            if left <= right:  # 如果左邊界仍小於等於右


# @lc code=end

