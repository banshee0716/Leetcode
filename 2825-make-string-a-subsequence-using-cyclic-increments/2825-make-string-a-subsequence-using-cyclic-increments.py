class Solution:
    def canMakeSubsequence(self, s1: str, s2: str) -> bool:
        # 初始化 j 為 0，n 和 m 分別為兩個字串的長度
        j, n, m = 0, len(s1), len(s2)
        
        # 遍歷 str1
        for i in range(n):
            # 檢查當前的 str1[i] 是否能與 str2[j] 匹配，或者透過一次操作能匹配
            if j < m and (ord(s2[j]) - ord(s1[i])) % 26 <= 1:
                # 如果能，則將 j 指針向前移動一位
                j += 1
                
        # 檢查 j 是否移動到了 str2 的末尾，如果是，則 str2 是 str1 的子序列
        return j == m

        
        
    """
解題思路
1. 初始化兩個指針 i 和 j，i 用來遍歷 str1，j 用來遍歷 str2。
2. 遍歷 str1 的每一個字元。
3. 每當找到一個能匹配 str2[j] 的字元或者只需要循環一次就能匹配的字元，就移動指針 j。
4. 最後檢查 j 是否等於 str2 的長度，如果是，則表示 str2 是 str1 的一個子序列。
    
時間複雜度：O(n)，其中 n 是 str1 的長度。我們只需要遍歷一次 str1。
空間複雜度：O(1)，我們只使用了常數個額外的變量。    
    """