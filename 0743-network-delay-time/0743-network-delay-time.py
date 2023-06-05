class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 建立鄰接列表
        adj_list = defaultdict(list)
        
        # 將所有的邊加入鄰接列表
        for x, y, w in times:
            adj_list[x].append((w, y))
        
        # 建立一個已訪問節點的集合
        visited = set()
        # 建立最小堆，儲存當前節點及從源節點到達該節點的最短路徑
        heap = [(0, k)]
        while heap:
            # 從堆中取出當前最短路徑及對應的節點
            travel_time, node = heapq.heappop(heap)
            # 將該節點加入已訪問集合
            visited.add(node)
            
            # 如果所有的節點都已訪問，返回當前的路徑長度
            if len(visited) == n:
                return travel_time
            
            # 遍歷該節點的所有鄰接節點
            for time, adjacent_node in adj_list[node]:
                # 如果該鄰接節點未被訪問，則加入堆中
                if adjacent_node not in visited:
                    heapq.heappush(heap, (travel_time + time, adjacent_node))
                
        # 如果有節點未被訪問，返回-1
        return -1
"""
解題思路:
1. 首先我們將所有的邊加入鄰接列表中。

2. 接著我們使用 Dijkstra 的演算法來求出從源節點到所有其他節點的最短路徑。我們使用一個最小堆來保存當前的節點以及從源節點到達該節點的路徑長度。我們也維護一個已訪問節點的集合，以避免重複訪問。

3. 當我們訪問到一個新的節點時，我們將它加入已訪問集合，並將其所有的鄰接節點加入堆中。

4. 最後，如果所有的節點都已被訪問，我們返回當前的路徑長度；如果仍有節點未被訪問，我們返回 -1。
"""
"""
時間複雜度:

O(N + ElogN) - 這是 Dijkstra's algorithm 的標準時間複雜度，其中 N 是節點的數量，E 是邊的數量。
空間複雜度:

O(N + E) - 我們需要用到鄰接列表和最小堆，所以空間複雜度是 O(N + E)。
"""