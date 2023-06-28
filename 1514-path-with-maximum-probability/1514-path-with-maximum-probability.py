from collections import defaultdict, deque

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # 建立鄰接表，表示圖的結構
        g = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            g[a].append([b, i])  # 將邊和其相應的成功概率的索引添加到該點的鄰接表中
            g[b].append([a, i])  # 因為是無向邊，所以兩邊都要加
        
        # 初始化 BFS 隊列和概率表
        dq, p = deque([start]), [0.0] * n
        p[start] = 1.0  # 從起點到起點的概率為 1

        # 執行 BFS
        while dq:
            cur = dq.popleft()  # 從隊列中取出當前節點
            for neighbor, i in g.get(cur, []):
                # 如果經過當前節點到達鄰居的概率大於目前已知的到達該鄰居的概率，則更新該概率
                if p[cur] * succProb[i] > p[neighbor]:
                    p[neighbor] = p[cur] * succProb[i]  # 更新概率
                    dq.append(neighbor)  # 將該鄰居加入隊列

        # 返回到達終點的最大概率
        return p[end]
        

"""
給您一個由 n 個節點（0 索引）組成的無向加權圖，由邊列表表示，其中edges[i] = [a, b] 是連接節點 a 和 b 的無向邊，並有成功遍歷該邊的概率邊緣 succProb[i]。

給定兩個節點的起點和終點，找到從起點到終點成功概率最大的路徑，並返回其成功概率。

如果沒有從開始到結束的路徑，則返回 0。如果您的答案與正確答案相差最多 1e-5，則您的答案將被接受。
"""
"""
時間複雜度為 O(E)，其中 E 是邊的數量。這是因為我們需要對每一條邊進行處理，而廣度優先搜索的時間複雜度是和邊的數量相關的。

空間複雜度為 O(V)，其中 V 是頂點的數量。這是因為我們需要儲存每一個頂點的概率值，以及在 BFS 中，我們需要一個隊列來儲存要處理的頂點。
"""