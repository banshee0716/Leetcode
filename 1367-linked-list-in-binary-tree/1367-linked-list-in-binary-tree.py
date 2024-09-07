# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # Initialize a queue for BFS traversal of the tree nodes
        queue = deque()
        queue.append(root)

        # Helper function to perform DFS and check if linked list matches from current tree node
        def dfs(tree_node, list_node):
            if not list_node:
                # Reached end of linked list, path matches
                return True
            if not tree_node or tree_node.val != list_node.val:
                # Tree node is null or values do not match
                return False
            # Recurse on left and right subtrees
            return dfs(tree_node.left, list_node.next) or dfs(tree_node.right, list_node.next)

        # Perform BFS traversal of the tree
        while queue:
            curr = queue.popleft()
            # If current node matches head of linked list, check for matching path
            if curr.val == head.val and dfs(curr, head):
                return True
            # Add left child to queue if it exists
            if curr.left:
                queue.append(curr.left)
            # Add right child to queue if it exists
            if curr.right:
                queue.append(curr.right)

        # No matching path found
        return False

    """
Time Complexity (時間複雜度):
樹的層次遍歷需要遍歷每個節點，這部分的時間複雜度為 O(N)，其中 N 是二元樹中的節點數。
在最壞情況下，每次啟動的深度優先搜索（DFS）可能會遍歷鏈結串列的每一個節點，這部分的時間複雜度為 O(L)，其中 L 是鏈結串列的長度。
因此，最壞情況下，總時間複雜度為 O(N * L)。

Space Complexity (空間複雜度):
層次遍歷使用的 deque 需要 O(W) 的空間，W 是樹的最大寬度。在最壞情況下，這個寬度可能是 O(N)。
深度優先搜索使用的遞迴堆疊最多會有 O(L) 的深度，因此空間複雜度是 O(L)。
總的來說，空間複雜度為 O(N + L)（取決於最寬的層次與鏈結串列的長度）。
    """
            