#
# @lc app=leetcode id=1603 lang=python3
#
# [1603] Design Parking System
#


# @lc code=start
class ParkingSystem:
    # 初始化停車系統，設定每種車的停車位數量
    def __init__(self, big: int, medium: int, small: int):
        self.vehicle = [big, medium, small]

    # 當一輛車到達時，檢查是否有足夠的停車位，如果有，就分配停車位，否則就拒絕
    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.vehicle[0] > 0:
                self.vehicle[0] -= 1
                return True
        elif carType == 2:
            if self.vehicle[1] > 0:
                self.vehicle[1] -= 1
                return True
        elif carType == 3:
            if self.vehicle[2] > 0:
                self.vehicle[2] -= 1
                return True

        return False


"""
時間複雜度：
O(1)，因為無論何種類型的車輛，我們都只需要檢查和修改一個元素，所以時間複雜度是常數。

空間複雜度：
O(1)。除了給定的輸入，我們只需要常數的空間來儲存每種車的停車位數量，所以空間複雜度也是常數。
"""


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
# @lc code=end
