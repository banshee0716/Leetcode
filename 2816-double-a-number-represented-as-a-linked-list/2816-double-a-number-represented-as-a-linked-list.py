# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 如果頭節點的值大於4，則加一個值為0的節點作為新的頭節點
        if head.val > 4:
            head = ListNode(0, head)
        
        # 初始化節點指針
        node = head
        # 遍歷整個鏈表
        while node:
            # 翻倍當前節點的值，並對10取模
            node.val = (node.val * 2) % 10
            
            # 檢查下一個節點，如果其值大於4則進位（即當前節點的值加1）
            if node.next and node.next.val > 4:
                node.val += 1
            
            # 移動到下一個節點
            node = node.next
            
        return head
    """
    
解題思路
1. 首先，檢查頭節點（head）的值。如果它大於4，我們會需要進位，因此在鏈表前面加一個值為0的新節點。
2. 然後，我們遍歷整個鏈表，每次都將當前節點的值翻倍，並對10取模（為了避免數字過大）。這會得到個位數。
3. 在遍歷過程中，如果下一個節點的值大於4，那麼當前節點應該要加1（進位）。

時間複雜度：O(n)，其中 n 是鏈表的長度。我們只需要遍歷一次鏈表。
空間複雜度：O(1)，因為我們只使用了常數個額外的變量。
    """