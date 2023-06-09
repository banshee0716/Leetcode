#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#

# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for num in pushed:
            stack.append(num)  # 將元素推入堆疊
            while len(stack) > 0 and stack[len(stack) - 1] == popped[i]:
                # 當堆疊不為空且堆疊頂部元素等於彈出序列中下一個元素時，從堆疊中彈出元素
                stack.pop()
                i += 1  # 將彈出序列的索引向後移動
        return True if len(stack) == 0 else False
        # 如果堆疊為空，表示壓入序列和彈出序列合法，返回True，否則返回False


# @lc code=end
