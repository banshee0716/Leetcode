class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        # 定義模數 MOD，對結果取模
        MOD = 10**9 + 7

        # 初始化動態規劃矩陣，大小為 (minProfit + 1) x (n + 1)
        dp = [[0] * (n + 1) for i in range(minProfit + 1)]

        # 將 dp[0][0] 設置為 1，表示不選擇任何計劃的情況
        dp[0][0] = 1

        # 遍歷所有計劃，每個計劃包括成員數量 g 和盈利 p
        for g, p in zip(group, profit):
            # 從 minProfit 開始遍歷到 0，避免重複計算
            for i in range(minProfit, -1, -1):
                # 從 n - g 開始遍歷到 0，避免超過成員限制
                for j in range(n - g, -1, -1):
                    # 更新動態規劃矩陣，將當前計劃的盈利和成員納入考慮
                    dp[min(i + p, minProfit)][j + g] += dp[i][j]
                    # 取模以防止溢出
                    dp[min(i + p, minProfit)][j + g] %= MOD

        # 返回 dp[minProfit] 的和，即所有達到或超過 minProfit 的計劃數量之和
        return sum(dp[minProfit]) % MOD
