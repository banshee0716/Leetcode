class Solution:
    def champagneTower(self, poured: int, r: int, c: int) -> float:
        dp = [[0] * i for i in range(1, 102)]
        dp[0][0] = poured
        
        for i in range(100):
            go_to_next_level = False #set a flag to judge if you go to next level or not
            for j in range(i + 1):
                if dp[i][j] > 1:
                    go_to_next_level = True
                    drip = dp[i][j] - 1
                    dp[i + 1][j] += drip / 2
                    dp[i + 1][j + 1] += drip / 2
                    dp[i][j] = 1
                    #模擬香檳塔落下的狀況，若是超過１，溢出的部分均勻落入下層的兩旁杯中
            if not go_to_next_level: break
        
        return dp[r][c]