class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # 創建一個包含所有節點的集合
        all_nodes = set(range(n))
        
        # 創建一個包含所有目標節點（邊的終點）的集合
        destination_nodes = set(destination for _, destination in edges)
        
        # 計算所有節點和目標節點的差集，這個差集就是我們要找的節點集
        source_nodes = all_nodes - destination_nodes
        
        # 將節點集轉換為列表
        return list(source_nodes)
