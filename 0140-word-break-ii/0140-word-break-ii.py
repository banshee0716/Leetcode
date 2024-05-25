class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s or not wordDict:
            return []  # Handle special cases where input string or word dictionary is empty
        
        n = len(s)
        wordSet = set(wordDict)  # Convert word list to set for O(1) complexity look-up
        
        @cache  # Use caching to save intermediate results and reduce computation
        def dfs(start):
            # Base case: if we've reached the end of the string, return a list with an empty string
            if start == n:
                return [""]
            
            ans = []
            # Try to match every word in the dictionary from the current start index
            for w in wordSet:
                end = start + len(w)
                # Check if the word can be placed at the current position
                if end <= n and s[start:end] == w:
                    # Recurse to process the rest of the string
                    rest = dfs(end)
                    for r in rest:
                        # Construct the result string based on recursion outcome
                        ans.append(w + (" " + r if r else ""))
            return ans
        
        # Start the recursion from the first character
        return dfs(0)
    
    

    """
核心概念：

遞歸與回溯：從字符串的開頭開始，嘗試每一個字典中的單詞，看它是否是當前位置的前綴。如果是，則對剩餘的字符串進行相同的遞歸處理。
終止條件：當遞歸函數的起始位置 start 等於字符串的長度 n 時，表示已經處理完畢整個字符串，這時候返回一個包含空字符串的列表，作為成功結束的標誌。
記憶化搜索：使用 @cache 裝飾器存儲中間結果，防止重複計算，提高效率。

時間和空間複雜度分析
時間複雜度：O(n^3 * m)，其中 n 是字符串 s 的長度，m 是 wordDict 中單詞的數量。對於每個起始點，可能需要比較所有單詞，並進行遞歸分割。
空間複雜度：O(n)，主要由於遞歸深度最多為 n 和使用 @cache 帶來的額外空間。
"""