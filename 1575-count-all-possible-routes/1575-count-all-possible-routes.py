class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        # 使用 lru_cache 進行記憶化
        @lru_cache(None)
        def dfs(curr: int, remaining_fuel: int) -> int:
            
            # 如果剩餘油量小於 0，則返回 0
            if remaining_fuel < 0:
                return 0
            
            # 如果當前位置就是終點，則初始化結果為 1，否則初始化為 0
            if curr == finish:
                result = 1
            else:
                result = 0
            
            # 遍歷所有的位置
            for next_loc in range(len(locations)):
                # 如果下一個位置不是當前位置
                if curr != next_loc:
                    # 計算油量消耗
                    cost = abs(locations[curr] - locations[next_loc])
                    # 更新結果
                    result += dfs(next_loc, remaining_fuel - cost)
            
            # 返回結果並取模 1000000007
            return result % 1000000007
        
        # 從起點開始進行深度優先搜索
        return dfs(start, fuel)

"""
在這裡，我們定義一個函數 dfs(curr, remaining_fuel)，表示當前在 curr 位置，剩下 remaining_fuel 的油量時，我們可以到達終點的路線數量。
我們使用 lru_cache 對這個函數進行儲存，避免重複計算。
然後對每個位置，我們都嘗試去往其他位置，並減去消耗的油量，最後得出所有可能的結果。


時間複雜度為 O(n^2 * f)，其中 n 為位置的數量，f 為油量。因為我們需要遍歷每個位置，並且對於每個位置，我們都可能需要遍歷所有的油量。
空間複雜度為 O(n * f)，因為我們需要儲存每個位置對於每種油量的結果。
"""