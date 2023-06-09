#
# @lc app=leetcode id=1894 lang=python3
#
# [1894] Find the Student that Will Replace the Chalk
#

# @lc code=start

# 找要換第n個粉筆的人
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # 每一輪用到的粉筆數量都是固定的，
        # 所以只要去計算出總數和每一輪用的粉筆數量的餘數，再去搜尋就可以找到要換粉筆的人
        for i in range(1, len(chalk)):
            chalk[i] += chalk[i - 1]
        k = k % chalk[-1]
        left, right = 0, len(chalk)
        while left < right:
            mid = left + (right - left) // 2
            if chalk[mid] > k:
                right = mid
            else:
                left = mid + 1
        return left


"""
一個班級有n個學生，編號從0到n-1，老師會給每個學生出一道題，從0號學生開始，然後是1號學生，以此類推，直到老師給到n-1號學生。
之後，老師將重新啟動該過程，再次從學號 0 開始。
給定一個索引為 0 的整數數組 chalk 和一個整數 k。最初有 k 支粉筆。當給學生編號 i 一個問題來解決時，他們將使用 chalk[i] 支粉筆來解決該問題。
但是，如果當前的粉筆數嚴格小於 chalk[i]，那麼就會要求第 i 個學號更換粉筆。
返回將替換粉筆的學生的索引。
"""


# @lc code=end
