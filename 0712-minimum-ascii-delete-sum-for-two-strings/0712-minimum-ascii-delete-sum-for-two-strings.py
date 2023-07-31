class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # 兩個字符串的長度
        n=len(s1)
        m=len(s2)
        # 初始化dp矩陣
        dp=[[0 for x in range(m+1)] for x in range(n+1)]
        # 處理邊界條件
        for i in range(1,n+1):
            dp[i][0]=dp[i-1][0]+ord(s1[i-1])

        for i in range(1,m+1):
            dp[0][i]=dp[0][i-1]+ord(s2[i-1])
        # 填充dp矩陣
        for i in range(1,n+1):
            for j in range(1,m+1):
                # 如果字符相同，則直接從前一個狀態轉移過來
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                # 否則，選擇刪除一個字符，然後從兩個可能的狀態中選擇最小的
                else:
                    dp[i][j]=min(dp[i-1][j]+ord(s1[i-1]),dp[i][j-1]+ord(s2[j-1]))

        # 返回最後的結果
        return dp[n][m] 
"""
時間複雜度為 O(nm)，因為我們需要填充一個 nm 的二維陣列，這裡的 n 和 m 分別為兩個字符串的長度。
空間複雜度也是 O(n*m)，因為我們需要一個二維陣列來儲存子問題的結果。
"""