#
# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#


# @lc code=start
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        # m和n分別是二維矩陣的行和列
        m, n = len(A), len(A[0])
        # 尋找第一個1所在的位置
        i, j = next((i, j) for i in range(m) for j in range(n) if A[i][j])

        # 使用stack來進行深度優先搜索
        stack = [(i, j)]
        # 使用seen來記錄已經訪問過的點
        seen = set(stack)
        # 開始深度優先搜索
        while stack:
            i, j = stack.pop()
            # 標記當前點為已訪問
            seen.add((i, j))
            # 檢查四個方向的鄰居
            for ii, jj in (i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j):
                if 0 <= ii < m and 0 <= jj < n and A[ii][jj] and (ii, jj) not in seen:
                    stack.append((ii, jj))
                    seen.add((ii, jj))

        # 初始橋長為0
        ans = 0
        # 使用queue來進行廣度優先搜索
        queue = list(seen)
        # 開始廣度優先搜索
        while queue:
            newq = []
            for i, j in queue:
                for ii, jj in (i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j):
                    if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in seen:
                        # 如果找到了第二座島，則返回ans
                        if A[ii][jj] == 1:
                            return ans
                        newq.append((ii, jj))
                        seen.add((ii, jj))
            queue = newq
            ans += 1


"""
解題思路：
這題的解法主要是使用深度優先搜索(DFS)和廣度優先搜索(BFS)。
首先，我們用DFS找出第一座島，然後將其所有節點加入到佇列中，
接著再用BFS從這些節點出發，擴張到下一層，直到找到第二座島。
"""

"""
時間複雜度：
這個算法的時間複雜度是 O(mn)，這是因為在最壞的情況下，我們可能需要訪問所有的節點。

空間複雜度：
這個算法的空間複雜度也是 O(mn)，這是因為我們需要使用seen和queue來儲存訪問過的節點。
"""

# @lc code=end
