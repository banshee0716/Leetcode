class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # 初始化DP數組，每個位置對應26個英文字母的最長理想子序列長度
        dp = [0] * 26
        
        for ch in s:
            # 獲取當前字符對應的索引
            i = ord(ch) - ord('a')
            # 計算在動態規劃數組中可以考慮的範圍，確保不超出邊界
            start = max(0, i - k)
            end = min(26, i + k + 1)
            # 更新dp[i]為其自身加上(i-k, i+k)範圍內的dp值的最大值加1
            # 因為當前字符可以增加的最長子序列長度至少為1
            dp[i] = 1 + max(dp[start:end])
        
        # 返回dp數組中的最大值，這是最長理想子序列的長度
        return max(dp)


    """
計算範圍優化：原來的代碼在計算每個字符的理想子序列長度時會重複計算範圍。上述代碼通過計算start和end變數來明確範圍，減少不必要的計算，特別是當k較大時，可以避免對超出範圍的無效訪問。
    """