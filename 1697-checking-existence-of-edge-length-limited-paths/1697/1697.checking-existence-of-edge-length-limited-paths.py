#
# @lc app=leetcode id=1697 lang=python3
#
# [1697] Checking Existence of Edge Length Limited Paths
#

# @lc code=start
class UnionFind:
    def __init__(self, N: int):
        self.parent = list(range(N))  # 初始化父節點列表
        self.rank = [1] * N  # 初始化節點的秩

    def find(self, p: int) -> int:
        # 查找節點 p 的根節點
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p: int, q: int) -> bool:
        prt, qrt = self.find(p), self.find(q)  # 找到 p 和 q 的根節點
        if prt == qrt:
            return False  # 如果根節點相同，表示已經在同一個集合中
        if self.rank[prt] > self.rank[qrt]:
            prt, qrt = qrt, prt  # 保證 prt 的秩小於等於 qrt 的秩
        self.parent[prt] = qrt  # 將 prt 的父節點設為 qrt
        self.rank[qrt] += self.rank[prt]  # 更新 qrt 的秩
        return True


class Solution:
    def distanceLimitedPathsExist(
        self, n: int, edgeList: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        # 對查詢按權重排序，並保留原始索引
        queries = sorted((w, p, q, i) for i, (p, q, w) in enumerate(queries))
        # 對邊列表按權重排序
        edgeList = sorted((w, u, v) for u, v, w in edgeList)

        uf = UnionFind(n)  # 初始化並查集

        ans = [None] * len(queries)  # 初始化答案列表
        ii = 0
        for w, p, q, i in queries:
            # 根據查詢中的權重限制，合併邊
            while ii < len(edgeList) and edgeList[ii][0] < w:
                _, u, v = edgeList[ii]
                uf.union(u, v)
                ii += 1
            # 判斷查詢中的兩個節點是否連通
            ans[i] = uf.find(p) == uf.find(q)
        return ans


# @lc code=end
