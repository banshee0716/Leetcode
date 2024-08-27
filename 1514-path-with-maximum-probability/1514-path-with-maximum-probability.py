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
維護一個機率表，BFS圖然後紀錄每個節點下機率最大的值，最後返回他
    """