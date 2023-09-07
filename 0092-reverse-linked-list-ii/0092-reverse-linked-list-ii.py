# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 第一步：建立虛擬頭節點
        dummy = ListNode(0)
        dummy.next = head
        
        # 初始化兩個指針 pre 和 post
        pre = dummy
        post = dummy.next
        
        # 第二步：定位到反轉的起點
        for i in range(1, left):
            post = post.next
            pre = pre.next
        
        # 第三步：進行反轉
        for i in range(right - left):
            temp = post.next
            post.next = temp.next
            temp.next = pre.next
            pre.next = temp
        
        # 返回虛擬頭節點的下一個節點，即連結串列的頭節點
        return dummy.next

"""
解題思路
1. 建立虛擬頭節點：為了方便操作，建立一個虛擬的頭節點連接到原始連結串列的頭部。

2. 定位到反轉的起點：遍歷連結串列，直到 pre 指向反轉開始的前一個節點，post 指向反轉開始的第一個節點。

3.進行反轉：將 post 的下一個節點移動到 pre 的後面，直到達到指定的反轉範圍。

時間複雜度: 我們遍歷了連結串列一次，並進行了一次局部反轉，所以時間複雜度是 O(n)。

空間複雜度: 我們只使用了幾個額外的變數（dummy, pre, post, temp），所以空間複雜度是 O(1)。
"""