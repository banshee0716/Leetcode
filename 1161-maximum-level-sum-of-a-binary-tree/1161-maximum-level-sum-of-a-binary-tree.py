# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_sum = -float('inf')  # 初始化最大層內元素和為負無窮大
        level, maxLevel = 0, 0  # 初始化層級數與最大和所在的層級數
        q = collections.deque()  # 使用雙端隊列保存節點
        q.append(root)  # 將根節點加入隊列

        while q:  # 當隊列非空時，進行循環
            level += 1  # 層級數加1
            sum = 0  # 初始化當前層的元素和
            for _ in range(len(q)):  # 遍歷當前層的所有節點
                node = q.popleft()  # 取出節點
                sum += node.val  # 將節點的值加入當前層的元素和
                if node.left:  # 如果節點有左子節點，則將左子節點加入隊列
                    q.append(node.left)
                if node.right:  # 如果節點有右子節點，則將右子節點加入隊列
                    q.append(node.right)
            if max_sum < sum:  # 如果當前層的元素和大於最大層內元素和，則更新最大層內元素和與最大和所在的層級數
                max_sum, maxLevel = sum, level        
        return maxLevel  # 返回最大和所在的層級數
"""
解題思路：

1. 初始設定最大層內元素和為負無窮大，層級數與最大和所在的層級數為0，並創建一個雙端隊列。
2. 將根節點加入隊列。
3. 進入循環：每次循環中，層級數加1，並初始化當前層的元素和為0，然後遍歷當前層的所有節點，計算元素和，並將子節點加入隊列。
4. 更新最大層內元素和與最大和所在的層級數。
5. 最後返回最大和所在的層級數。

時間複雜度是O(n)，
其中n是二叉樹的節點數量，因為我們需要遍歷所有的節點。
空間複雜度也是O(n)，
這是因為在最壞的情況下，隊列可能需要保存所有的節點。

"""