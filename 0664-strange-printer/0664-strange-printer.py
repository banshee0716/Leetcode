from typing import List

class Solution:
    def strangePrinter(self, s: str) -> int:
        # Remove consecutive duplicate characters to optimize the problem
        s = ''.join(ch for i, ch in enumerate(s) if i == 0 or ch != s[i-1])
        n = len(s)
        
        # Initialize the DP table
        dp: List[List[int]] = [[0] * n for _ in range(n)]
        
        # Build the DP table bottom-up
        for i in range(n - 1, -1, -1):  # Start from the end of the string
            dp[i][i] = 1  # Base case: single character requires 1 turn
            for j in range(i + 1, n):  # Consider all substrings starting from i
                # Initial assumption: print each character separately
                dp[i][j] = dp[i][j - 1] + 1
                
                # Try to optimize by finding matching characters
                for k in range(i, j):
                    if s[k] == s[j]:
                        # If characters match, we can potentially reduce turns
                        dp[i][j] = min(
                            dp[i][j],
                            dp[i][k] + (dp[k + 1][j - 1] if k + 1 <= j - 1 else 0)
                        )
        
        # The minimum turns for the entire string is stored in dp[0][n-1]
        return dp[0][n - 1]