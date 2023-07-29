class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        n = len(words)
        for i in range(n):
            for j in range(i+1, n):
                if words[i][0] == words[j][1] and words[i][1] == words[j][0]:
                    ans += 1
        return ans
                
            
            
"""
給您一個由不同字符串組成的 0 索引數組單詞。

字符串words[i]可以與字符串words[j]配對，如果：
    - 字符串words[i]等於反轉後的字符串words[j]。
    - 0 <= i < j < 單詞長度。
    
返回可以從數組單詞形成的最大對數。

請注意，每個字符串最多屬於一對。
"""