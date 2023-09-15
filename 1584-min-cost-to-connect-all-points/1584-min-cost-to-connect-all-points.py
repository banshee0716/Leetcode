from heapq import heappop, heappush

def manhattan_distance(p1: List[int], p2: List[int]) -> int:
    # 計算兩點之間的曼哈頓距離
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n  # 標記每個點是否已被訪問
        heap_dict = {0: 0}  # 用於存儲每個點到MST的距離
        min_heap = [(0, 0)]  # 初始化最小堆
        
        mst_weight = 0  # 存儲MST的權重
        
        while min_heap:
            w, u = heappop(min_heap)  # 從堆中取出距離最小的點
            
            # 檢查該點是否已被訪問或距離是否已更新
            if visited[u] or heap_dict.get(u, float('inf')) < w:
                continue
            
            visited[u] = True
            mst_weight += w  # 將該點的權重加到MST的權重中
            
            # 計算該點到所有其他未訪問點的距離，更新最小堆
            for v in range(n):
                if not visited[v]:
                    new_distance = manhattan_distance(points[u], points[v])
                    if new_distance < heap_dict.get(v, float('inf')):
                        heap_dict[v] = new_distance
                        heappush(min_heap, (new_distance, v))
        
        return mst_weight

"""
最小生成樹

解題思路：
1. 定義一個函數 manhattan_distance 來計算兩點之間的曼哈頓距離。
2. 使用Prim算法來建立最小生成樹。初始化一個未訪問點的集合，一個用於存儲最小生成樹權重的變量，和一個最小堆。
3. 從任意一個點開始，找到該點到其他所有未訪問點的距離，並將這些距離放入最小堆中。
4. 從最小堆中取出距離最小的點，檢查該點是否已被訪問。如果沒有，將其添加到MST中，並計算該點到所有其他未訪問點的距離，更新最小堆。
5. 重複步驟4，直到所有的點都被訪問。

時間複雜度和空間複雜度：
時間複雜度：O(n^2)，其中 n 是給定點的數量。Prim算法的每個迭代中，我們都要考慮到所有的邊。
空間複雜度：O(n)，我們需要額外的空間來存儲 visited、heap_dict 和 min_heap。
"""