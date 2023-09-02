from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        max_val = len(s) + 1
        # 初始化 dp 數組
        dp = [max_val] * (len(s) + 1)
        dp[0] = 0
        # 將 dictionary 轉換成 set
        dictionary_set = set(dictionary)
        
        # 遍歷 s 的每個字符
        for i in range(1, len(s)+1):
            # dp[i] 可以由 dp[i-1] 得到
            dp[i] = dp[i-1] + 1
            # 考慮所有以 s[i] 結尾的子字符串 s[i-l:i]
            for l in range(1, i+1):
                # 如果 s[i-l:i] 在 dictionary_set 中，則 dp[i] 可以由 dp[i-l] 得到
                if s[i-l:i] in dictionary_set:
                    dp[i] = min(dp[i], dp[i-l])
                    
        return dp[-1]

"""
給定一個字符串 s 和一個單詞字典 dictionary，你需要將 s 分割成一個或多個不重疊的子字符串，使得每個子字符串都出現在 dictionary 中。 s 中可能包含一些不在任何子字符串中的額外字符。

我們的目標是找到一種分割方法，使得剩下的額外字符最少。

解題思路
1. 初始化一個 dp 數組，其中 dp[i] 表示分割字符串 s 的前 i 個字符所得到的最小額外字符數。
2. 初始化一個 dictionary_set，將 dictionary 轉換成一個集合，以便於快速查找。
3. 遍歷 s 的每個字符，對於每個字符 s[i]，考慮所有以 s[i] 結尾的子字符串 s[i-l:i]，其中 1 <= l <= i。
4. 如果 s[i-l:i] 在 dictionary_set 中，則 dp[i] 可以由 dp[i-l] 得到。
5. 最後，dp[len(s)] 就是我們的答案。
        
時間複雜度: 程式遍歷了 s 的每個字符，並且對於每個字符 s[i]，都考慮了所有以 s[i] 結尾的子字符串 s[i-l:i]，其中 1 <= l <= i。因此，時間複雜度是 
O(n^2)，其中 n 是字符串 s 的長度。

空間複雜度: 我們使用了一個長度為 n+1 的 dp 數組，因此空間複雜度是 
O(n)。
"""