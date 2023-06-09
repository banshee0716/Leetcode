#
# @lc app=leetcode id=2316 lang=python3
#
# [2316] Count Unreachable Pairs of Nodes in an Undirected Graph
#

# @lc code=start
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]  # 初始化根節點為節點本身
        self.rank = [1] * size  # 初始化秩為1

    def find(self, x):
        if x == self.root[x]:  # 如果x是自己的根節點，返回x
            return x
        self.root[x] = self.find(self.root[x])  # 否則遞歸地找到根節點，同時將x的父節點設置為根節點，以加快下次查找速度
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:  # 如果x和y不屬於同一個集合
            if (
                self.rank[rootX] > self.rank[rootY]
            ):  # 如果x所在的集合的秩比y所在的集合的秩高，將y的根節點設置為x的根節點
                self.root[rootY] = rootX
            elif (
                self.rank[rootX] < self.rank[rootY]
            ):  # 如果x所在的集合的秩比y所在的集合的秩低，將x的根節點設置為y的根節點
                self.root[rootX] = rootY
            else:  # 如果x所在的集合的秩等於y所在的集合的秩，將y的根節點設置為x的根節點，x的秩加1
                self.root[rootY] = rootX
                self.rank[rootX] += 1


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind(n)  # 初始化一個大小為n的並查集
        for u, v in edges:
            dsu.union(u, v)  # 合併所有邊的端點所在的集合
        C = Counter([dsu.find(i) for i in range(n)])  # 計算每個集合的大小
        groupCounts = list(C.values())
        ans = 0
        firstGroupCount = groupCounts[0]
        for i in range(1, len(groupCounts)):
            ans += firstGroupCount * groupCounts[i]  # 求出任意兩個集合之間的邊的數量之和
            firstGroupCount += groupCounts[i]  # 更新第一個集合的大小
        return ans  # 返回邊的數量之和


# @lc code=end
