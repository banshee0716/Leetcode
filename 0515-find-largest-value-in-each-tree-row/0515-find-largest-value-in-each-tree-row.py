# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        res = []
        while queue:
            max_level = float('-inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                max_level = max(max_level, node.val)
                queue.extend([node.left, node.right])
            
            if max_level != float('-inf'):
                res.append(max_level)
                
        return res