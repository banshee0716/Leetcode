class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
    # 將 k 轉換成字符串，計算其長度
        m, n = len(str(k)), len(s)

    # 初始化 dp，dp[i] 表示 s[:i] 的分割方法數
        dp = [1] * (n + 1)

    # 遍歷 s 的每個字符，計算以該字符結尾的分割方法數
        for i in range(n):
            res, cur = 0, ""

        # 從 i 遍歷到 i - m（不超過第一個字符）
            for idx in range(i, max(-1, i - m), -1):
            # 從右往左構建當前數字 cur
                cur = s[idx] + cur

            # 判斷當前數字是否有效（無前導 0 且不大於 k）
                if cur[0] != "0" and int(cur) <= k:
                    # 當前數字有效，將 dp[idx] 累加到 res
                    res += dp[idx]

        # 如果 res 為 0，表示無法找到有效的分割方法
            if res == 0:
                return 0
            else:
            # 更新 dp[i+1]，取模以防止溢出
                dp[i + 1] = res % (10 ** 9 + 7)

    # 返回最終結果
        return dp[-1]
