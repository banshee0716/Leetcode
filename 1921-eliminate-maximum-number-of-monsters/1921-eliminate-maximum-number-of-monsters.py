class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time_to_city = [dist[i] / speed[i] for i in range(len(dist))]
        time_to_city.sort()
        for i in range(len(dist)):
            if time_to_city[i] <= i:
                return i
            
        return len(dist)
        
    """
你正在玩一款電玩遊戲，你要保衛你的城市免受 n 個怪物的攻擊。
給定一個大小為 n 的 0 索引整數數組 dist，其中 dist[i] 是第 i 個怪物距城市的初始距離（以公里為單位）。

怪物們以恆定的速度朝城市走去。每個怪物的速度以大小為 n 的整數數組 speed 的形式給出，其中 speed[i] 是第 i 個怪物的速度（以公里每分鐘為單位）。

你擁有一把武器，一旦充滿電，就可以消滅一個怪物。然而，該武器需要一分鐘才能充電。武器一開始就充滿電。

當任何怪物到達你的城市時你就輸了。如果怪物在武器充滿電的同時到達城市，則視為失敗，遊戲在您可以使用武器之前結束。

返回你輸掉之前可以消滅的怪物的最大數量，如果你能在怪物到達城市之前消滅掉所有怪物，則返回n。
    
    """
    
    