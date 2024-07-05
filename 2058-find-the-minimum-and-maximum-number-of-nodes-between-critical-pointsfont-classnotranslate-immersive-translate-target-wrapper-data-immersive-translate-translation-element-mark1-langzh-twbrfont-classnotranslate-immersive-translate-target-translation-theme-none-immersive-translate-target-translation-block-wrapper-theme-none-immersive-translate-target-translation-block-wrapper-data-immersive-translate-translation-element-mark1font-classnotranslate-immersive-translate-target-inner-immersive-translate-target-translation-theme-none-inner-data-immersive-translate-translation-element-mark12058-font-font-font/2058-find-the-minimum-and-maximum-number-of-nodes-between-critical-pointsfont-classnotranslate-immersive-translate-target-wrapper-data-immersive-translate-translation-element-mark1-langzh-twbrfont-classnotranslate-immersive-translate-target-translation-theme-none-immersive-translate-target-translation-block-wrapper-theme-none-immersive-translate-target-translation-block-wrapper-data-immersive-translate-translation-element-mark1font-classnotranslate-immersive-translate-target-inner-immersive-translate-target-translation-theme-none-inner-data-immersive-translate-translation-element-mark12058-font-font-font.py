# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        indexNode = 2
        firstLocal = lastLocal = 0
        lastValue = head.val
        head = head.next
        output = [-1,-1]
        while head:
            if head.val < lastValue and head.next and head.val < head.next.val or head.val > lastValue and head.next and head.val > head.next.val:
                if firstLocal == 0: 
                    firstLocal = indexNode
                else:
                    output[0] = min(output[0], indexNode-lastLocal) if output[0] != -1 else indexNode-lastLocal
                    output[1] = indexNode-firstLocal
                lastLocal = indexNode
            indexNode += 1
            lastValue = head.val
            head = head.next
        return output
        
        
        
        
        """
鏈接列表中的關鍵點定義為本地最大值或本地最小值。

如果當前節點的值嚴格大於上一個節點和下一個節點，則節點是局部最大值。

如果當前節點的值嚴格小於上一個節點和下一個節點，則節點是局部最小值。

請注意，在存在上一個節點和下一個節點時，節點只能是本地最大值/最小值。

給定一個鏈接的列表頭，返回一個長度2的陣列，其中包含[Indifistance，maxDistance]，其中識別是任意兩個不同的兩個差異點和MaxDistance之間的最小距離是任何兩個不同的臨界點之間的最大距離。如果關鍵點少於兩個，請返回[-1，-1]。
        """