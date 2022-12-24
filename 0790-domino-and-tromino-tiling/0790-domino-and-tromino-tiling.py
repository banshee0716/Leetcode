class Solution:
    def numTilings(self, n):
        dp = [[0, 0] for _ in range(n+2)]
        dp[1], dp[2] = [1, 1], [2, 2]
        
        for i in range(3, n+1):
            dp[i][0] = dp[i-1][0] + dp[i-2][0] + 2 * dp[i-2][1]
            dp[i][1] = dp[i-1][0] + dp[i-1][1]
            
        return dp[n][0] % 1_000_000_007
            
    # Given an integer n, return the number of ways to tile an 2*n board.
    # dp[i][0]: (number of ways to tile till ith column leaving no gap)
    # dp[i][1]: (number of ways to tile till ith column leaving a gap in i+1th column)