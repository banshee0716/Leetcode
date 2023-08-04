class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)  # 轉換 wordDict 為集合以優化查找效率
        dp = [False] * (len(s) + 1)  # 初始化動態規劃陣列
        dp[0] = True  # 空字串可以被拆分
        
        for i in range(len(s)):  # 遍歷字串的每一個字符
            for j in range(i, len(s)):  # 從當前字符開始遍歷後續字符
                # 如果字串 s 的前 i 個字符可以被拆分，且 s[i: j+1] 是 wordSet 中的單詞
                # 則字串 s 的前 j+1 個字符可以被拆分
                if dp[i] and s[i: j + 1] in wordSet:
                    dp[j + 1] = True
        return dp[-1]  # 返回最終結果

        
        
"""
這個問題是在求給定的字串 s 是否能被拆分為 wordDict 中的單詞。我們使用動態規劃來解決這個問題。首先，我們建立一個布林型態的動態規劃陣列 dp，dp[i] 表示字串 s 的前 i 個字符是否可以被 wordDict 中的單詞拆分。dp[0] 為 True，表示空字串可以被拆分。

接下來，我們遍歷整個字串，對於每一個字串的位置，我們都嘗試用 wordDict 中的單詞去匹配字串的後續部分。如果能匹配到，並且 dp[i] 為 True，那麼我們就設置 dp[j+1] 為 True。

原先的時間複雜度：

初始化 dp 陣列：這部分的時間複雜度為 O(n)，其中 n 為字串 s 的長度。
外部 for 迴圈：這部分的時間複雜度為 O(n)，其中 n 為字串 s 的長度。迴圈遍歷字串 s 的每個字元一次。
內部 for 迴圈：這部分的時間複雜度為 O(n)，其中 n 為字串 s 的長度。在最壞的情況下，對於每個 i，內部迴圈可能需要遍歷字串 s 的 n - i 個字元。
s[i: j + 1] in wordDict：這部分的時間複雜度為 O(n * m)，其中 n 為字串 s[i: j + 1] 的長度，m 為字典 wordDict 的長度。在最壞的情況下，需要遍歷字典 wordDict 的每個元素以確認 s[i: j + 1] 是否在字典中。
綜合以上，總時間複雜度為 O(n^3 * m)。這是因為內部迴圈與字串 s[i: j + 1] in wordDict 的操作在外部迴圈的每次迭代中都被執行。

空間複雜度：空間複雜度為 O(n)，這是因為我們創建了一個長度為 n 的 dp 陣列來存儲結果。這裡 n 為字串 s 的長度。

時間複雜度可能還可以進一步優化。將 wordDict 轉換成一個集合（set）可以將 s[i: j + 1] in wordDict 的時間複雜度從 O(m) 降低到 O(1)。
這樣，總的時間複雜度將降低到 O(n^3)。


"""