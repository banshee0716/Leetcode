#
# @lc app=leetcode id=2218 lang=python3
#
# [2218] Maximum Value of K Coins From Piles
#

# @lc code=start
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # n: number of piles
        # m: total number of coins
        n, m = len(piles), 0

        # Calculate prefix sum for each pile
        # prefixSum[i][j]: sum of the first j coins in the i-th pile
        prefixSum = []
        for i in range(n):
            temp = [0]
            for j in range(len(piles[i])):
                temp.append(temp[-1] + piles[i][j])
                m += 1
            prefixSum.append(temp)

        # If the total number of coins is equal to k, return the sum of all coins
        if m == k:
            return sum(temp[-1] for temp in prefixSum)

        # Initialize a dynamic programming table
        # dp[i][j]: maximum value of coins we can get by picking j coins from the first i piles
        dp = [[0] * (k + 1) for _ in range(n)]

        # Initialize the base case for the first pile
        for j in range(1, k + 1):
            if j < len(prefixSum[0]):
                dp[0][j] = prefixSum[0][j]

        # Iterate through all piles and number of coins
        for i in range(1, n):
            for j in range(1, k + 1):
                # Try all possible combinations of coins from the current pile
                for l in range(len(prefixSum[i])):
                    # If the number of coins from the current pile is greater than j, stop the loop
                    if l > j:
                        break
                    # Update the dp table
                    dp[i][j] = max(dp[i][j], prefixSum[i][l] + dp[i - 1][j - l])

        # Return the maximum value of coins we can get by picking k coins from all piles
        return dp[n - 1][k]


"""
時間複雜度分析：

1. 計算前綴和：O(n * m)，其中n為piles的數量，m為所有pile中硬幣的總數。
2. 初始化DP表格：O(n * k)。
3. 填充DP表格：O(n * k * m)。
綜合起來，時間複雜度為O(n * m * k)。

空間複雜度分析：
我們使用了兩個二維陣列prefixSum和dp，所以空間複雜度為O(n * m + n * k)。
"""

# @lc code=end
