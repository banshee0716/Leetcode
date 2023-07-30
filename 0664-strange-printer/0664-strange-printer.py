import sys

class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        if not s:
            # 如果字符串為空，則返回0
            return 0

        # 用最大可能的整數初始化 dp 陣列
        dp = [[sys.maxsize] * n for _ in range(n)]

        for i in range(n):
            # 打印一個字符需要一個轉數
            dp[i][i] = 1

        # 迭代所有長度大於1的子串
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                # 假設我們需要比 dp[i+1][j] 多一個轉數
                dp[i][j] = dp[i + 1][j] + 1

                for k in range(i + 1, j + 1):
                    if s[i] == s[k]:
                        # 如果在位置 k 後找到與 s[i] 相同的字符，則我們取目前的 dp[i][j] 和 dp[i][k-1] + dp[k+1][j] 的最小值
                        dp[i][j] = min(
                            dp[i][j],
                            dp[i][k - 1] + (dp[k + 1][j] if j > k else 0),
                        )

        # 返回打印字符串 s 所需的最小轉數
        return dp[0][n - 1]
    
    
"""
這個問題使用動態規劃方法來解決。關鍵思想在於反向思考，即如果子串的最後一個字符與第一個字符相同，則我們不需要額外的轉換。
時間複雜度是 O(n^3)，因為有 n^2 個子問題（s 的子串），並且每個子問題的解決時間是 O(n)（我們需要檢查子串中的每個字符來更新 dp[i][j]）。
空間複雜度是 O(n^2)，因為使用了一個 2D dp 陣列。
"""