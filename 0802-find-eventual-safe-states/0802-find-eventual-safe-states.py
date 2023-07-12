class Solution:
    def isSafe(self, s, graph, visited):
        if visited[s] == 1:  # 該節點已經被訪問過並且是安全的
            return True
        if visited[s] == -1:  # 該節點已經被訪問過且是迴圈的一部分
            return False

        visited[s] = -1  # 將當前節點標記為訪問過且是迴圈的一部分
        for it in graph[s]:  # 檢查所有鄰接節點
            if not self.isSafe(it, graph, visited):  # 如果任何一個鄰接節點不是安全的，則當前節點也不是安全的
                return False

        visited[s] = 1  # 將當前節點標記為訪問過且是安全的
        return True

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        v = len(graph)
        visited = [0] * v  # 初始化訪問狀態列表
        checkCycle = []
        for i in range(v):  # 遍歷所有節點
            if self.isSafe(i, graph, visited):  # 如果節點是安全的，則將其添加到結果列表中
                checkCycle.append(i)
        return checkCycle  # 返回結果列表

        
        
        
"""
在給定的有向圖中，所有能夠最終走到終點的節點。這裡的"終點"被定義為出度為0的節點。因此，我們的任務就是要找出所有不會形成迴圈的節點，這些節點被稱為"最終安全的節點"。

1. 我們首先初始化一個訪問狀態列表 visited，其初始值都是0，表示所有節點都尚未訪問。

2. 然後我們遍歷每個節點。對於每個節點，我們都使用深度優先搜索（DFS）來檢查是否存在一條從當前節點出發的路徑能夠達到一個終點。

3. 在深度優先搜索的過程中，我們將當前正在訪問的節點標記為-1，表示這個節點可能會形成一個迴圈。如果我們在搜索的過程中遇到了一個已經被標記為-1的節點，那麼我們就找到了一個迴圈，可以直接返回 False。如果我們成功地遍歷了所有與當前節點相鄰的節點，並且沒有找到任何迴圈，那麼我們就將當前節點標記為1，表示這個節點是安全的。

4. 最後，我們只需要返回所有被標記為1的節點即可。

時間複雜度是 O(N + E)，其中 N 是節點的數量，E 是邊的數量，因為我們需要遍歷每個節點和邊來檢查是否存在迴圈。空間複雜度是 O(N)，用於存儲訪問狀態列表和結果列表。
"""