# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, path, smallest):
            if not node:
                return
            
            # 將當前節點的字符加入到路徑中
            path.append(chr(node.val + ord('a')))
            
            # 如果是葉節點，更新最小字符串
            if not node.left and not node.right:
                current_string = ''.join(path[::-1])
                smallest[0] = min(smallest[0], current_string)
                
            # 繼續遞迴左右子樹
            dfs(node.left, path, smallest)
            dfs(node.right, path, smallest)
            
            # 回溯，移除當前節點的字符
            path.pop()
        
        # 初始化最小字符串，設置為比所有可能字符都大的字符串
        smallest = [chr(ord('z') + 1)]
        dfs(root, [], smallest)
        
        return smallest[0]

    """
解題思路
這個問題可以通過深度優先搜索（DFS）解決。從根節點開始，向下到達每個葉節點，並在到達葉節點時記錄從該葉節點到根節點的路徑字符串。然後比較所有的路徑字符串，找到最小的一個。

1. 遞迴DFS：遞迴地訪問每個節點，將當前節點的字符加入到路徑列表中。
2. 到達葉節點時比較字符串：如果當前節點是葉節點（無子節點），則生成從葉節點到根節點的字符串，並與當前保存的最小字符串進行比較和更新。
3. 回溯：遞迴返回前，從路徑列表中移除當前節點的字符。

時間複雜度分析
遍歷每個節點一次，時間複雜度為O(N)，其中N是二叉樹中節點的數量。
每次遇到葉節點時，創建一個字符串，時間複雜度為O(H)，其中H是樹的高度。
總體時間複雜度為O(N*H)。

空間複雜度分析
需要額外的空間來存儲路徑字符串，最壞情況下，空間複雜度為O(H)，其中H是樹的高度，即遞迴棧的最大深度。
    """