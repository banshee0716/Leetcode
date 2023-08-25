class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        m, n, l = len(s1), len(s2), len(s3)
        
        # 檢查長度
        if m + n != l:
            return False

        # 確保 s1 不比 s2 長，減少空間使用
        if m < n:
            return self.isInterleave(s2, s1, s3)
        
        # 初始化 dp
        dp = [False] * (n + 1)
        dp[0] = True

        # 處理當 s1 為空的情況
        for j in range(1, n + 1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]

        # 雙層迴圈，更新 dp
        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, n + 1):
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])

        return dp[n]

        
"""
解題思路：
動態規劃可以解決這個問題。使用二維的DP矩陣，但這裡的代碼進行了優化，將其壓縮成一維，降低空間複雜度。

邊界情況：首先檢查s1和s2的長度之和是否等於s3的長度，如果不是，直接返回False。

初始化DP：dp是一個一維的布爾型數組，dp[j]表示s1的前i個字符和s2的前j個字符能否交錯形成s3的前i+j個字符。

填充DP：通過檢查當前字符是否匹配，並參考之前的結果來更新dp。

時間複雜度:
O(m * n)，其中 m 是s1的長度，n 是s2的長度。因為我們對每個字符位置都進行了一次檢查。

空間複雜度: 
O(n)，其中 n 是s2的長度。儘管動態規劃需要一個二維矩陣，但由於我們只使用了一個維度的數組，空間複雜度得到了優化。
        """