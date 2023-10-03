class Solution:
    def winnerOfGame(self, s: str) -> bool:
        a = b = 0  # 初始化Alice和Bob的刪除次數
        
        # 從第2個字符開始，遍歷到倒數第2個字符
        for i in range(1, len(s) - 1):
            # 檢查是否有三個連續的相同字符
            if s[i - 1] == s[i] == s[i + 1]:
                # 如果當前三個連續字符是A，則更新Alice的刪除次數
                if s[i] == "A":
                    a += 1
                # 否則更新Bob的刪除次數
                else:
                    b += 1
        
        # 判定贏家：如果Alice的刪除次數多於Bob，則Alice是贏家
        return a > b

"""
解題思路：

1. 遍歷字串s，如果某三個連續的字符都相同（也就是AAA或BBB），則根據它是AAA還是BBB來更新Alice或Bob能夠刪除的次數。
2. 比較Alice和Bob的刪除次數，判定誰是贏家。

時間複雜度分析：
我們對字串s進行了一次遍歷，所以時間複雜度是O(n)，其中n是字串s的長度。

空間複雜度分析：
除了輸入外，我們只使用了固定的空間，所以空間複雜度是O(1)。
"""