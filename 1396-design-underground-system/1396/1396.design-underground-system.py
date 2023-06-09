#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#


# @lc code=start
class UndergroundSystem:
    def __init__(self):
        self.checkInMap = {}  # Uid - [StationName, Time]，保存每個乘客的進站資訊
        self.routeTotalTime = defaultdict(int)  # 保存每個路線的總旅行時間
        self.routeCount = defaultdict(int)  # 保存每個路線的旅行次數

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # 乘客進站，記錄其id、進站站名和時間
        self.checkInMap[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # 乘客出站，計算其旅行時間並更新路線的總旅行時間和旅行次數
        checkIn = self.checkInMap.pop(id)  # 取出乘客的進站資訊
        routeName = (checkIn[0], stationName)  # 建立路線名稱

        # 更新路線的總旅行時間和旅行次數
        self.routeTotalTime[routeName] += t - checkIn[1]
        self.routeCount[routeName] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # 計算特定路線的平均旅行時間
        routeName = (startStation, endStation)
        return self.routeTotalTime[routeName] / self.routeCount[routeName]


"""
時間複雜度：
所有操作的時間複雜度都是 O(1)，也就是說，checkIn、checkOut 和 getAverageTime 函數的運行時間都是常數。

空間複雜度：
O(n)，其中 n 是進行 checkIn 操作的乘客數。這是因為我們需要保存每個進站乘客的資訊。在這裡，我們使用了字典和 defaultdict 來保存這些資訊。
"""
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end
