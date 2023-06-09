#
# @lc app=leetcode id=652 lang=python
#
# [652] Find Duplicate Subtrees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        res, hmap = [], {}  # 用於存放結果的列表和哈希表

        def recurse(node, path):
            if node is None:
                return "#"  # 如果節點為空，返回特殊字符 "#"
            # 構造節點的序列化字符串表示
            path += ",".join(
                [str(node.val), recurse(node.left, path), recurse(node.right, path)]
            )
            # 如果序列化字符串已經存在雜湊表中，表示已經出現過相同的子樹，將結果加入 res 中
            if path in hmap:
                hmap[path] += 1
                if hmap[path] == 2:
                    res.append(node)
            else:
                hmap[path] = 1  # 否則將序列化字符串加入哈希表中，出現次數初始化為 1
            return path

        recurse(root, "")  # 遞歸構造節點的序列化字符串表示
        return res  # 返回結果列表，其中存放所有重複的子樹節點


"""
時間複雜度：遍歷二元樹，每個節點都需要構造一個序列化字符串，將序列化字符串存入雜湊表中需要 O(1) 的時間，因此時間複雜度為 O(n)，其中 n 為二元樹中節點的個數。
空間複雜度：需要使用雜湊表存儲節點的序列化字符串，最壞情況下雜湊表需要存儲所有節點的序列化字符串，因此空間複雜度為 O(n)。
"""

# @lc code=end
