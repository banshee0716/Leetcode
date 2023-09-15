from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # 初始化 dp 陣列
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        # 遍歷 ranges 陣列
        for i, r in enumerate(ranges):
            # 計算覆蓋區域的起點和終點
            start, end = max(0, i - r), min(n, i + r)

            # 更新 dp 陣列
            for j in range(start + 1, end + 1):
                dp[j] = min(dp[j], dp[start] + 1)

        # 返回答案
        return dp[-1] if dp[-1] != float('inf') else -1


"""
解題思路：
初始化一個長度為 n+1 的 dp 陣列，其中 dp[i] 會儲存覆蓋區域 [0, i] 所需的最少灌溉設備數量。將所有的 dp[i] 初始化為 float('inf')（無窮大），並將 dp[0] 設為 0。
遍歷 ranges 陣列，對於每個灌溉設備 i，計算出它能覆蓋的區域 [start, end]。
使用動態規劃的方法更新 dp 陣列。對於每個 j 在 [start+1, end] 區間內，dp[j] = min(dp[j], dp[start] + 1)。

時間複雜度和空間複雜度
時間複雜度: 理論上最壞情況下，每個 ranges[i] 都能覆蓋 [0, n]，所以時間複雜度會是 O(n^2)。
空間複雜度: 使用了一個長度為 n+1 的 dp 陣列，所以空間複雜度是 O(n)。


第一種解法（貪心算法）：
    優點: 時間複雜度較低，為 O(n)。
    缺點: 程式碼較為直觀，但需要仔細管理多個變數。
第二種解法（動態規劃）：
    優點: 程式碼較容易理解，且概念廣泛適用於其他問題。
    缺點: 時間複雜度可能高達 O(n^2)，在 n 很大時會較慢。

總體來說，如果問題規模（n 的大小）不是很大，那麼動態規劃的解法會更為直觀和容易理解。然而，對於非常大的 n，第一種貪心算法的解法會更加高效。
"""
