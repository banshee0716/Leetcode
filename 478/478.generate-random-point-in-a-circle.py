#
# @lc app=leetcode id=478 lang=python3
#
# [478] Generate Random Point in a Circle
#

# @lc code=start
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        # 初始化圓的半徑和中心點
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        # 這裡的 x, y, r 與 x_center, y_center, radius 是一樣的，可以不用再宣告 x, y, r
        self.x = x_center
        self.y = y_center
        self.r = radius

    def randPoint(self) -> List[float]:
        while True:
            # 在圓的外接正方形內隨機選擇一個點
            x = random.uniform(self.x - self.r, self.x + self.r)
            y = random.uniform(self.y - self.r, self.y + self.r)
            # 檢查這個點是否位於圓內，即檢查點到圓心的距離是否小於或等於半徑
            if (x - self.x) ** 2 + (y - self.y) ** 2 <= self.r ** 2:
                return [x, y]  # 如果在圓內，返回這個點


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
# @lc code=end

