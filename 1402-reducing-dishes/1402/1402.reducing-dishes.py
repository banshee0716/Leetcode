#
# @lc app=leetcode id=1402 lang=python3
#
# [1402] Reducing Dishes
#

# @lc code=start
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        res = total = 0  # res 紀錄目前的滿意度總和，total 紀錄目前餐點加總的滿意度總和
        satisfaction.sort()  # 將餐點的滿意度排序
        while satisfaction and satisfaction[-1] + total > 0:  # 當還有餐點且加上新餐點後滿意度總和大於0
            total += satisfaction.pop()  # 將最後一個滿意度最高的餐點加入並從餐點列表中刪除
            res += total  # 更新滿意度總和
        return res  # 回傳最大滿意度總和

    """
時間複雜度：

對餐點滿意度進行排序的時間複雜度為 O(nlogn)，其中 n 為餐點的數量。
while 迴圈最多執行 n 次，因此其時間複雜度為 O(n)。
總時間複雜度為 O(nlogn)。

空間複雜度：

沒有使用額外的空間，只使用了固定數量的變數，因此空間複雜度為 O(1)。
    """


# @lc code=end
