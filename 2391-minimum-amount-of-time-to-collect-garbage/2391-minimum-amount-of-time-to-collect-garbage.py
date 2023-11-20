class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        total_minutes = 0  # Total minutes needed for garbage collection
        current_travel_time = 0  # Current travel time

        # Add the initial minutes required to collect garbage at the first house
        total_minutes += len(garbage[0])

        last_garbage_indices = [-1, -1, -1]  # Keep track of the last occurrence of each type of garbage

        # Iterate through each house starting from the second house
        for house_index in range(1, len(garbage)):
            # Add the minutes required to collect garbage at the current house
            total_minutes += len(garbage[house_index])

            # Update the indices of the last occurrence of each type of garbage
            if "M" in garbage[house_index]:
                last_garbage_indices[0] = house_index - 1
            if "P" in garbage[house_index]:
                last_garbage_indices[1] = house_index - 1
            if "G" in garbage[house_index]:
                last_garbage_indices[2] = house_index - 1

        # Iterate through each travel segment
        for travel_index in range(len(travel)):
            # Add the current travel time
            current_travel_time += travel[travel_index]

            # Add the minutes required to collect garbage if a garbage truck is at the corresponding house
            for truck_index in range(3):
                if last_garbage_indices[truck_index] == travel_index:
                    total_minutes += current_travel_time

        return total_minutes

        
        
        """
給你一個 0 個索引的垃圾字串數組，其中垃圾 [i] 代表第 i 個房子的垃圾分類。垃圾[i]僅由字元「M」、「P」和「G」組成，分別代表一個單位的金屬、紙張和玻璃垃圾。撿起一件任何類型的垃圾都需要 1 分鐘。

您還會獲得一個 0 索引的整數數組 Travel，其中 Travel[i] 是從房屋 i 到房屋 i + 1 所需的分鐘數。

全市共有三輛垃圾車，每輛負責撿拾一種垃圾。每輛垃圾車從0號房屋出發，必須依序訪問每棟房屋；然而，他們不需要拜訪每戶人家。

任何特定時刻只能使用一輛垃圾車。當其中一輛卡車正在行駛或撿拾垃圾時，另外兩輛卡車卻無能為力。

傳回撿起所有垃圾所需的最少分鐘數。
        """