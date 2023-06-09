#
# @lc app=leetcode id=2492 lang=python3
#
# [2492] Minimum Score of a Path Between Two Cities
#

# @lc code=start
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        graph = defaultdict(dict)
        for u, v, w in roads:
            graph[u][v] = graph[v][u] = w

        res = inf
        vis = set()
        dq = deque([1])

        while dq:
            node = dq.popleft()
            for adj, scr in graph[node].items():
                if adj not in vis:
                    dq.append(adj)
                    vis.add(adj)
                res = min(res, scr)

        return res


# @lc code=end
