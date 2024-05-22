from functools import cache

class Solution:
    @cache  # Cache results to avoid redundant computations
    def partition(self, s: str) -> List[List[str]]:
        # Base case: return a list containing an empty list if the input is empty
        if not s:
            return [[]]
        ans = []
        # Check every prefix of the string
        for i in range(1, len(s) + 1):
            # If the prefix is a palindrome
            if s[:i] == s[:i][::-1]:
                # Recursively process the suffix
                for suf in self.partition(s[i:]):
                    # Combine the current palindrome partition with the result of the suffix
                    ans.append([s[:i]] + suf)
        return ans


    
    """
解題思路：
這題是 LeetCode 第 131 題，目的是返回一個字符串所有可能的回文分割結果。這種問題的一個常見解法是使用回溯法，也就是遞歸地檢查每一個子串是否為回文串，並進行分割。

遞歸分割：對字符串 s 從頭開始，如果當前前綴子串 s[:i] 是一個回文串，那麼將其作為一個潛在的分割點。
回文驗證：通過簡單的字符串反轉來檢查一個字符串是否是回文：s[:i] == s[:i][::-1]。
後綴處理：對剩下的子串 s[i:] 進行遞歸調用，將返回的每個分割結果與當前前綴組合。
返回結果：如果 s 是空字符串，則返回包含空列表的列表，表示沒有更多分割方式。

Cache 的作用及運作原理：
在這段代碼中，@cache 裝飾器（從 Python 3.9+ 開始提供）用於自動記錄函數的輸入和相應的輸出。當同樣的輸入再次發生時，直接從記錄中提取結果，而不是重新執行函數。這樣可以顯著提高效率，特別是在解決重複計算多次的問題時。

這種方法在這個問題中特別有用，因為我們可能會多次調用相同的子串分割，特別是當輸入字符串包含重複字符時。

時間和空間複雜度分析：
時間複雜度：O(n * 2^n)，每個字符都可以選擇分割或不分割，最壞情況下，每種可能都會探索。
空間複雜度：O(n)，主要由遞歸深度決定，最壞情況下遞歸深度等於字符串長度。
    
    """