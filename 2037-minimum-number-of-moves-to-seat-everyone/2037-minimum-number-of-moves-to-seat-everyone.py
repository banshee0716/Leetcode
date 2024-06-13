class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(x - y) for x, y in zip(sorted(seats), sorted(students)))
        
    """
一個房間裡有n個座位和n個學生。給定一個長度為 n 的陣列席位，其中席位 [i] 是第 i 個席位的位置。您還會得到長度為 n 的陣列 Students，其中 Students[j] 是第 j 個學生的位置。

您可以執行多次以下移動：

將第 i 位學生的位置增加或減少 1（即將第 i 位學生從位置 x 移動到 x + 1 或 x - 1）
返回將每個學生移動到一個座位所需的最少移動次數，這樣不會有兩個學生坐在同一個座位上。

請注意，一開始可能會有多個座位或同一位置的學生。

先sort再greedy
    """