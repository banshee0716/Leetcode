"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def intersect(self, q1: 'Node', q2: 'Node') -> 'Node':
        
        # 若節點1是葉子節點
        if q1.isLeaf:
            # 若節點1的值為真，則返回節點1，否則返回節點2
            return q1 if q1.val else q2

        # 若節點2是葉子節點
        elif q2.isLeaf:
            # 若節點2的值為真，則返回節點2，否則返回節點1
            return q2 if q2.val else q1

        else:
            # 若兩個節點都不是葉子節點，則對其子節點進行交集操作
            tLeft = self.intersect(q1.topLeft, q2.topLeft)
            tRight = self.intersect(q1.topRight, q2.topRight)
            bLeft = self.intersect(q1.bottomLeft, q2.bottomLeft)
            bRight = self.intersect(q1.bottomRight, q2.bottomRight)

            # 如果所有新的子節點都是葉子節點，且他們的值都相同
            if all(node.isLeaf for node in (tLeft, tRight, bLeft, bRight)) and len(set(node.val for node in (tLeft, tRight, bLeft, bRight))) == 1:
                # 返回一個新的葉子節點，其值為子節點的共同值
                node = Node(tLeft.val, True, None, None, None, None)
            else:
                # 返回一個新的非葉子節點，其子節點為新的子節點
                node = Node(False, False, tLeft, tRight, bLeft, bRight)
        
        return node
    
"""
時間複雜度是 O(N)，其中 N 是節點的數量，因為我們可能需要遍歷每個節點。
空間複雜度是 O(D)，其中 D 是樹的深度，對應於我們的遞歸深度。
"""