#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#


# @lc code=start
class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        root = {}

        # 定義一個 find 函數來找到 x 的根節點
        # xr 表示 x 和它的根節點的比例
        def find(x):
            p, xr = root.setdefault(x, (x, 1.0))
            if x != p:
                r, pr = find(p)
                root[x] = (r, xr * pr)
            return root[x]

        # union 函數用來連接兩個節點
        # 如果兩個節點的根節點相同，則可以計算 x / y
        # 如果兩個節點的根節點不同，則更新其中一個節點的根節點
        def union(x, y, ratio):
            px, xr, py, yr = *find(x), *find(y)
            if not ratio:
                return xr / yr if px == py else -1.0
            if px != py:
                root[px] = (py, yr / xr * ratio)

        # 構建並查集
        for (x, y), v in zip(equations, values):
            union(x, y, v)

        # 處理查詢
        return [union(x, y, 0) if x in root and y in root else -1.0 for x, y in queries]


"""
時間複雜度：
這個算法的時間複雜度為 O(E + Q)，其中 E 是 equations 的長度，Q 是 queries 的長度。這是因為我們在構建並查集和處理查詢時，需要遍歷 equations 和 queries。

空間複雜度：
這個算法的空間複雜度為 O(E)，因為我們需要一個字典來存儲每個節點的根節點和比例。
"""

"""

解題思路：
這個問題是用並查集（Union Find）的方式來解決的。
我們首先構建一個並查集，將每個變量看作節點。
對於等式 A / B = k，我們可以將其看作 A 和 B 的連接，連接值為 k。
在查詢階段，我們找到兩個節點的根節點，並根據根節點的比例來找出答案。
"""
# @lc code=end
