# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        pos, a_node = 0, list1

        # 將 a_node 移動到 list1 中索引為 a - 1 的節點
        while pos < a - 1:
            a_node = a_node.next
            pos += 1

        b_node = a_node

        # 將 b_node 移動到 list1 中索引為 b + 1 的節點
        while pos < b + 1:
            b_node = b_node.next
            pos += 1

        # 把 list2 連接到 a_node 之後
        a_node.next = list2

        # 將 list2 移動到其末尾
        while list2.next:
            list2 = list2.next

        # 把 list2 的末尾節點連接到 b_node
        list2.next = b_node
        return list1  # 返回結果的頭節點

    """
    解題思路:

將 a_node 移動到 list1 中索引為 a - 1 的節點。
將 b_node 移動到 list1 中索引為 b + 1 的節點。
連接 list2 到 a_node 之後，並將 list2 的末尾節點連接到 b_node。
時間複雜度:
在這個解法中，我們需要遍歷 list1 直到 b 的位置，且還需再次遍歷 list2。所以最壞情況下，時間複雜度是 O(b + len(list2))，其中 len(list2) 是 list2 的長度。

空間複雜度:
此方法的空間複雜度是 O(1)，因為我們只使用了固定的額外空間。
    """
