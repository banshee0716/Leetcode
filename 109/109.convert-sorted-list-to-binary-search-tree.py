#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
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
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # 定義一個遞迴函數，建立平衡二叉搜索樹，並回傳樹根節點
        def BSTCreation(start, end):
            # 若 start == end，表示目前子串列已經建立完畢，回傳 None
            if start == end:
                return None
            # 使用快慢指針，找到中間節點，並建立樹根節點
            slow, fast = start, start.next
            while fast and fast.next and fast != end and fast.next != end:
                slow = slow.next
                fast = fast.next.next
            # 建立樹節點，並將節點分成左右子樹，再遞迴建立子樹
            return TreeNode(
                slow.val, BSTCreation(start, slow), BSTCreation(slow.next, end)
            )

        # 呼叫 BSTCreation 函數，傳入串列的起始節點和結束節點
        return BSTCreation(head, None)


"""
時間複雜度：建立平衡二叉搜索樹的時間複雜度為 O(n)，其中 n 為節點數量，因為每個節點都會被建立一次。快慢指針尋找中間節點的時間複雜度為 O(log n)，因為最多需要遍歷整個串列一次，而串列的長度為 n。因此，總時間複雜度為 O(n log n)。
空間複雜度：建立平衡二叉搜索樹的空間複雜度為 O(n)，因為需要建立 n 個節點。快慢指針的空間複雜度為 O(1)。因此，總空間複雜度為 O(n)。
"""
# @lc code=end
