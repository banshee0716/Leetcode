# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def doubleIt(self, head: ListNode) -> ListNode:
        # 反轉鏈表
        reversed_list = self.reverse_list(head)
        carry = 0
        current, previous = reversed_list, None

        # 遍歷反轉後的鏈表
        while current:
            # 計算新的值
            new_value = current.val * 2 + carry
            current.val = new_value % 10
            carry = new_value // 10
            previous, current = current, current.next

        # 如果有進位，添加新的節點
        if carry:
            previous.next = ListNode(carry)

        # 反轉回原始順序
        return self.reverse_list(reversed_list)

    # 反轉鏈表
    def reverse_list(self, node: ListNode) -> ListNode:
        previous, current = None, node
        while current:
            next_node = current.next
            current.next = previous
            previous, current = current, next_node
        return previous

"""
解題思路
1. 鏈表反轉：首先反轉鏈表，這樣可以從最低有效位開始遍歷，方便處理進位問題。
2. 遍歷計算：從反轉的鏈表頭節點開始遍歷，將每個節點的值乘以2，並添加之前計算的進位。
3. 處理進位：如果節點的計算結果超過9，則在下一個迭代中繼續使用進位。
4. 處理進位結束：在遍歷完鏈表後，如果仍有進位需要處理，則在鏈表末尾添加一個新節點表示進位。
5. 反轉回原始順序：再次反轉鏈表以返回正確順序的結果。

時間複雜度分析
時間複雜度：O(N)，其中N是鏈表節點的數量。需要兩次完整遍歷（兩次反轉和一次計算）。

空間複雜度分析
空間複雜度：O(1)，只使用了一些額外的變量來跟蹤當前節點和進位，不會使用額外的數據結構。
"""