from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # Initialize DP table: max_stones[i][m] represents the maximum number of stones
        # Alice can get starting from index i with a current M value of m
        max_stones = [[0] * (n + 1) for _ in range(n)]

        # Calculate suffix sums for quick range sum queries
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        # Fill the DP table bottom-up
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                if i + 2 * m >= n:
                    # If Alice can take all remaining piles, she does so
                    max_stones[i][m] = suffix_sum[i]
                else:
                    # Try all possible moves and choose the best one
                    for x in range(1, 2 * m + 1):
                        # Alice takes x piles, then Bob plays optimally
                        opponent_best = max_stones[i + x][max(m, x)]
                        alice_gain = suffix_sum[i] - opponent_best
                        max_stones[i][m] = max(max_stones[i][m], alice_gain)

        # Return the maximum stones Alice can get starting from the beginning with M=1
        return max_stones[0][1]