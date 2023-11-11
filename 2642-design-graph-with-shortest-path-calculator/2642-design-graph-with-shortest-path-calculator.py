import heapq
from typing import List

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        # 初始化鄰接列表
        self.adj_list = [[] for _ in range(n)]
        for a, b, cost in edges:
            self.adj_list[a].append((b, cost))

    def addEdge(self, edge: List[int]) -> None:
        # 添加邊到圖中
        a, b, cost = edge
        self.adj_list[a].append((b, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        # 初始化變量
        n, pq = len(self.adj_list), [(0, node1)]
        dist = [float('inf')] * n
        dist[node1] = 0

        # 使用Dijkstra算法
        while pq:
            d, node = heapq.heappop(pq)
            if node == node2: 
                return d
            if d > dist[node]: 
                continue
            for neighbor, cost in self.adj_list[node]:
                new_dist = d + cost
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        
        return -1

        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)


"""
有一個有向加權圖，由編號從 0 到 n - 1 的 n 個節點組成。圖的邊最初由給定的數組邊表示，其中 Edges[i] = [fromi, toi, edgeCosti] 意味著有一個從fromi 到toi 的邊，成本為edgeCosti。

實作Graph類：
    -Graph(int n, int[][] Edges) 以 n 個節點和給定的邊初始化物件。
    -addEdge(int[] edge) 將一邊加入邊列表中，其中edge = [from, to, edgeCost]。在加入這個節點之前保證兩個節點之間不存在邊。
    -intshortestPath(intnode1,intnode2)傳回從node1到node2的路徑的最小成本。如果不存在路徑，則返回-1。路徑的成本是路徑中邊的成本總和。
    
## 解題思路

1. **建立圖的表示**：
   - 使用鄰接列表 `adj_list` 來表示圖，這是一個二維列表，其中 `adj_list[i]` 包含一個列表，表示從節點 `i` 可以達到的所有鄰居及其對應的邊權重。

2. **添加邊**：
   - `addEdge` 方法用於向圖中添加新的邊。

3. **計算最短路徑**：
   - 使用 Dijkstra 算法來計算從 `node1` 到 `node2` 的最短路徑。
   - 使用一個最小堆 `pq` 來存儲待處理的節點及其到 `node1` 的當前距離。
   - `dist` 數組用於存儲從 `node1` 到每個節點的最短距離，初始時，除了 `node1` 到自身的距離為 0，其他所有距離都設置為無窮大。

4. **Dijkstra 算法的執行**：
   - 從 `node1` 開始，將其距離 0 加入最小堆。
   - 持續從最小堆中取出距離最小的節點，更新其鄰居的距離。
   - 如果到達 `node2`，則返回當前的距離作為答案。

## 複雜度分析

- **時間複雜度**：在最壞情況下，每個節點和每條邊都會至少被處理一次，所以時間複雜度為 `O(V + E * logV)`，其中 `V` 是節點數，`E` 是邊數。
- **空間複雜度**：鄰接列表的空間複雜度為 `O(V + E)`。`dist` 數組和最小堆的空間複雜度為 `O(V)`。總的空間複雜度為 `O(V + E)`。

"""