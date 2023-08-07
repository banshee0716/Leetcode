class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        can = capacity
        for i, x in enumerate(plants):
            if can < x:
                # 因為如果沒了就要走回去把水裝滿再走回來，所以把步數*2
                ans += 2 * i
                can = capacity
            ans += 1
            can -= x

        return ans


"""
您想用噴壺給花園裡的植物澆水。這些植物排成一排，從左到右標記為 0 到 n - 1，其中第 i 株植物位於 x = i 處。 x = -1 處有一條河流，您可以在那裡重新裝滿噴壺。

每種植物都需要特定量的水。您將通過以下方式給植物澆水：

按照從左到右的順序給植物澆水。
給當前植物澆水後，如果沒有足夠的水來完全澆灌下一個植物，請返回河中將噴壺重新裝滿。
您不能提前給噴壺加水。
您最初位於河邊（即 x = -1）。在 x 軸上移動一個單位需要一步。

給定一個由 n 個整數組成的 0 索引整數數組植物，其中 plant[i] 是第 i 個植物所需的水量，以及代表噴壺容量的整數容量，返回澆灌所有植物所需的步驟數。
"""
