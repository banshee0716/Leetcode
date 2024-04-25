class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26  # 初始化DP數組
        for ch in s:
            i = ord(ch) - ord('a')  # 獲取當前字符對應的索引
            # 更新dp[i]為其自身加上(i-k, i+k)範圍內的dp值的最大值
            dp[i] = 1 + max(dp[max(0, i - k) : min(26, i + k + 1)])
        return max(dp)  # 返回dp數組中的最大值

    """
解題思路
此問題可以利用動態規劃（DP）來解決。使用一個數組dp來記錄每個字符作為子序列結尾時的最長理想子序列長度。

初始化DP數組：初始化一個長度為26（對應26個英文字母）的數組dp，其中每個位置初始化為0。
遍歷字符串：對於字符串s中的每個字符ch，更新dp數組。計算每個字符所對應的索引i，然後更新dp[i]為其自身加上其在範圍(i-k, i+k)內所有字符的dp值的最大值。
結果：最後，返回dp數組中的最大值，這代表了最長理想子序列的長度。
    """