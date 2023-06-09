#
# @lc app=leetcode id=839 lang=python3
#
# [839] Similar String Groups
#

# @lc code=start
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        groups = 0  # 初始化分組數為 0
        n = len(strs)  # 字符串列表的長度
        vis = [False] * n  # 初始化訪問狀態列表

        # 遍歷字符串列表
        for i in range(n):
            if vis[i]:
                continue  # 如果已訪問過，則跳過
            groups += 1  # 增加一個分組
            self.dfs(i, strs, vis)  # 進行深度優先搜索

        return groups

    def dfs(self, i: int, strs: List[str], vis: List[bool]) -> None:
        vis[i] = True  # 將當前字符串標記為已訪問
        for j in range(len(strs)):
            if vis[j]:
                continue  # 如果已訪問過，則跳過
            if self.is_similar(strs[i], strs[j]):  # 如果 strs[i] 和 strs[j] 相似，則繼續搜索
                self.dfs(j, strs, vis)

    def is_similar(self, a: str, b: str) -> bool:
        count = 0  # 初始化不相同字符的數量
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1  # 如果字符不同，則增加計數
        return count == 2 or count == 0  # 如果有兩個或零個不同字符，則判定為相似字符串


"""
時間複雜度分析：

遍歷字符串列表的時間複雜度為 O(n)，其中 n 為 strs 的長度。
在深度優先搜索中，每次搜索的時間複雜度為 O(n)（遍歷字符串列表）* O(L)（比較字符串），其中 L 為字符串長度。
綜合以上分析，此算法的總時間複雜度為 O(n^2 * L)。

空間複雜度分析：

訪問狀態列表 vis 的空間複雜度為 O(n)。
深度優先搜索的遞迴深度最大為 O(n)。
綜合以上分析，此算法的總空間複雜度為 O(n)。

"""

# @lc code=end
