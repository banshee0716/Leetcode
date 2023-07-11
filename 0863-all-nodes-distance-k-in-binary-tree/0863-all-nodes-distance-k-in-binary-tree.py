class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # 建立空的鄰接列表圖
        graph = {}
        
        # 用遞迴的方式建立二叉樹的鄰接列表圖
        self.buildGraph(root, None, graph)

        # 初始化廣度優先搜尋的隊列和訪問過的節點集合
        queue = [(target, 0)]
        visited = set([target])
        
        # 初始化結果列表
        result = []
        
        # 開始進行廣度優先搜尋
        while queue:
            # 從隊列中取出一個節點和它的距離
            node, distance = queue.pop(0)
            
            # 如果這個節點的距離等於k，那麼把它加入結果列表
            if distance == k:
                result.append(node.val)
            
            # 如果距離大於k，則可以提前停止搜索
            if distance > k:
                break
            
            # 瀏覽當前節點的所有鄰居
            for neighbor in graph[node]:
                # 如果這個鄰居節點還沒有被訪問過，那麼就把它加入隊列並標記為已訪問
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))
        
        # 返回結果列表
        return result

    def buildGraph(self, node: TreeNode, parent: TreeNode, graph: Dict[TreeNode, List[TreeNode]]):
        # 如果節點為空，則直接返回
        if not node:
            return
        
        # 如果節點不在圖中，則在圖中為它建立一個新的條目
        if node not in graph:
            graph[node] = []
        
        # 如果有父節點，那麼把父節點加入節點的鄰居列表，並把節點加入父節點的鄰居列表
        if parent:
            graph[node].append(parent)
            graph[parent].append(node)
        
        # 遞歸地對左子樹和右子樹進行相同的操作
        self.buildGraph(node.left, node, graph)
        self.buildGraph(node.right, node, graph)

