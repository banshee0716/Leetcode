# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findIntegers(self, num: int) -> int:
        # x, y 用來儲存斐波那契數，其中 x 是 F(i), y 是 F(i+1)
        x, y = 1, 2
        res = 0  # 初始化結果為0

        # num += 1 是因為我們要計算 [0, num] 之間的數，所以考慮到0所以加1
        num += 1

        while num:
            # 檢查 num 的最後兩位是否為11
            # 如果是的話，則 res 重置為0，因為我們不考慮含有連續1的數
            if num & 1 and num & 2:
                res = 0

            # 這裡加上 x * (num & 1) 是為了累加不含連續1的數的總和
            # (num & 1) 會檢查 num 的最低位是否為1
            res += x * (num & 1)

            # 將 num 右移，去掉其最低位
            num >>= 1

            # 更新斐波那契數
            x, y = y, x + y

        return res

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
