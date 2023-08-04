class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)  # 將 wordDict 轉換成集合
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i: j + 1] in wordSet:  # 將 wordDict 改為 wordSet
                    dp[j + 1] = True
        return dp[-1]


        
        
"""

時間複雜度：O(n^3)，其中 n 是字串 s 的長度。兩層迴圈花費 O(n^2) 的時間，字串分割操作花費 O(n) 的時間。
空間複雜度：O(n)，其中 n 是字串 s 的長度。只需存儲 dp 陣列。

"""