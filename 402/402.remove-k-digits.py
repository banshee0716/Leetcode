#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []  # 使用 stack 紀錄每個數字
        remain = len(num) - k  # 要留下多少個數字
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()  # 若目前數字小於 stack 的最後一個數字，則刪除最後一個數字
                k -= 1  # 刪除一個數字後，k 減一
            stack.append(digit)  # 把目前數字放入 stack
        return (
            "".join(stack[:remain]).lstrip("0") or "0"
        )  # 轉換成字串，移除左側的 0，若結果為空字串，則返回 "0"


"""時間複雜度為O(n)，其中 n 是字串 num 的長度。
空間複雜度為 O(n)。"""

# @lc code=end
