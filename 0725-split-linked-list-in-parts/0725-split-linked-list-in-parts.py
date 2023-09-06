# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional, List

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        # 第一步：計算連結串列的長度
        length, current = 0, head
        while current:
            length += 1
            current = current.next
        
        # 第二步：確定基礎大小和多餘的節點
        base_size, extra = divmod(length, k)
        
        # 初始化返回結果和當前節點
        parts = []
        current = head
        
        # 第三步：分割連結串列
        for _ in range(k):
            dummy = ListNode()
            part_head = dummy
            
            # 按照基礎大小添加節點
            for _ in range(base_size + (extra > 0)):
                dummy.next, current, dummy = current, current.next, current
            if extra > 0:
                extra -= 1
            
            # 切斷連結串列的連接
            dummy.next = None
            parts.append(part_head.next)
            
        return parts

"""
解題思路：
1. 先確定整個連結串列有多少個節點，因此我們需要遍歷整個串列以計算它的長度。

2. 確定基礎大小和多餘的節點：使用divmod，可以一次性取得基礎大小（每部分的節點數）和多餘的節點數。

3. 分割連結串列：按照基礎大小和多餘的節點數，進行分割。

時間複雜度: 我們遍歷了連結串列兩次，所以時間複雜度是 O(n)。
空間複雜度: 我們僅使用了幾個額外的變數和一個存放結果的串列，所以空間複雜度是 O(k)，其中 
k 是給定的分割數量。
"""