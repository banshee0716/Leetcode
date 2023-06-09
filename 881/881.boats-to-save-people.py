#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 初始化船數量為0，左右指針分別指向陣列的起點和終點
        boat, low, high = 0, 0, len(people) - 1
        # 將人按體重排序
        people.sort()
        while low <= high:
            # 如果最重的人和最輕的人的體重和小於等於限制，那麼兩個人可以坐在同一艘船上
            if people[low] + people[high] <= limit:
                low += 1
            # 如果最重的人和最輕的人的體重和大於限制，那麼最重的人只能坐在一艘船上
            # 開一艘新船
            boat += 1
            high -= 1
        # 返回船的數量
        return boat


"""
時間複雜度：
排序時間複雜度為O(nlogn)，while循環時間複雜度為O(n)，因此總時間複雜度為O(nlogn)。

空間複雜度：
只使用了常數額外空間，因此空間複雜度為O(1)。
"""
# @lc code=end
