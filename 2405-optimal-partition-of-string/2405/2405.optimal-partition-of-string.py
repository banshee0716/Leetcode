#
# @lc app=leetcode id=2405 lang=python3
#
# [2405] Optimal Partition of String
#

# @lc code=start
class Solution:
    def partitionString(self, s: str) -> int:
        ans = 1  # 初始切割數為1
        ls = []  # 用一個 list ls 存儲當前切割的子串
        for i in s:
            if i in ls:
                ls = [i]  #  如果字符 i 已經出現在 ls 中，將 ls 清空並添加當前字符 i，並將切割數+1
                ans += 1
            else:
                ls += [i]  # 否則將字符 i 添加到 ls 中
        return ans


"""

遍歷一遍字符串S的時間複雜度為O(n)（n為S中的字符數）。
在ls中查找一個字符的時間複雜度為O(n)，但因為每個字符只會被查找一次，所以總時間複雜度為O(n)。
因此，總時間複雜度為O(n)。

空間複雜度
取決於最差情況下ls的長度，即S中的每個字符都不相同，此時ls的長度為n，因此空間複雜度為O(n)。
但由於每個字符最多只會被添加到ls中一次，因此最差情況也只會發生一次，所以平均情況下空間複雜度為O(1)。

"""

# @lc code=end
