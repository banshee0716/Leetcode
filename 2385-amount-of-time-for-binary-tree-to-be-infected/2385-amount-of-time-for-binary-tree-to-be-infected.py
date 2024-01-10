# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import defaultdict, deque
from typing import Optional


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(node):
            if node is None:
                return
            # 將二叉樹轉換為圖
            if node.left:
            #無向圖的操作:把兩個點連接上
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right)

        graph = defaultdict(list)
        dfs(root)  # 構建圖

        visited = set()  # 記錄已訪問的節點
        queue = deque([start])  # BFS的隊列
        time = -1
        while queue:
            time += 1
            # 遍歷當前隊列中的所有節點
            for _ in range(len(queue)):
                current_node = queue.popleft()
                visited.add(current_node)
                # 將鄰接節點添加到隊列中
                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return time  # 返回最大時間


        
        """
您將獲得具有唯一值和整數開頭的二元樹的根。在第 0 分鐘，感染從值為 start 的節點開始。

每分鐘，如果出現以下情況，就會有一個節點被感染：

該節點當前未受感染。
該節點與受感染的節點相鄰。
傳回整棵樹被感染所需的分鐘數。





解題思路
1. 先把二元樹用dfs轉化成一個無向圖，然後把父節點跟子節點之間設置邊使其可以連接
2. 設置queue
3. bfs重新travasal無向圖

時間複雜度分析：
    -構建圖的時間複雜度為 O(n)，其中 n 是樹的節點數量。
    -BFS的時間複雜度也為 O(n)，因為每個節點至多被訪問一次。
    -因此，總的時間複雜度為 O(n)。

空間複雜度分析：
    -需要額外的空間來存儲圖，空間複雜度為 O(n)。
    -BFS隊列和訪問集合的空間複雜度也為 O(n)。
    -因此，總的空間複雜度為 O(n)。






        """