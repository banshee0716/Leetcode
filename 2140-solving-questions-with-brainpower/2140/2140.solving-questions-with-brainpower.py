#
# @lc app=leetcode id=2140 lang=python3
#
# [2140] Solving Questions With Brainpower
#


# @lc code=start
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)  # n 是問題的數量

        max_points = [0] * (n + 1)  # 初始化 max_points 列表

        for i in range(n - 1, -1, -1):  # 從最後一個問題開始，向前遍歷每一個問題
            points, jump = questions[i]  # 當前問題的分數和可以跳過的問題數量

            next_question = min(jump + i + 1, n)  # 解答完這個問題後，下一個要解答的問題的索引
            points_from_this_question = (
                points + max_points[next_question]
            )  # 解答完這個問題後，能獲得的最高分數
            max_points[i] = max(
                points_from_this_question, max_points[i + 1]
            )  # 更新 max_points[i]

        return max_points[0]  # 從第一個問題開始，能獲得的最高分數


"""
解題思路：

初始化一個名為 max_points 的列表，長度為問題數量加一，所有元素為 0。這個列表的每一個元素 max_points[i] 代表從第 i 個問題開始，能獲得的最高分數。
從最後一個問題開始，向前遍歷每一個問題。
對於每一個問題，計算出解答完這個問題並跳過指定數量的問題後，能獲得的最高分數。如果這個分數大於直接跳過這個問題能獲得的最高分數，則更新 max_points[i]。
返回 max_points[0]，這就是從第一個問題開始，能獲得的最高分數。
"""
"""
時間複雜度：
此算法的時間複雜度為 O(n)，因為每一個問
題都被遍歷一次，且每次的操作都是常數時間複雜度。

空間複雜度：
此算法的空間複雜度為 O(n)，因為我們需要一個長度為 n+1 的列表來儲存最高分數。這裡的 n 是問題的數量。
"""
# @lc code=end
