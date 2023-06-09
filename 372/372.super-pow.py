#
# @lc app=leetcode id=372 lang=python3
#
# [372] Super Pow
#


# @lc code=start
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        # 初始化結果為1
        result = 1
        # 遍歷b的每一位數字
        for digit in b:
            # result = (result^10 * a^digit) % 1337
            # 使用pow(x, y, z)函數計算次方並取模，這樣可以避免大數的計算
            result = pow(result, 10, 1337) * pow(a, digit, 1337) % 1337
        # 返回結果
        return result


"""
時間複雜度：O(n)，其中n是列表b的長度。因為我們需要遍歷列表b的每一個數字。
空間複雜度：O(1)。除了給定的輸入列表b，我們只需要常數的空間來儲存結果，所以空間複雜度是常數。
"""

# @lc code=end
