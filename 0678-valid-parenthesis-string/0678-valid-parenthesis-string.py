class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin = max(leftMin - 1, 0)
                leftMax -= 1
            else:
                leftMin = max(leftMin - 1, 0)
                leftMax += 1
            
            if leftMax < 0:
                return False
        
        return leftMin == 0

        
        
"""
給定一個僅包含三種類型字元的字串 s：'('、')' 和 '*'，如果 s 有效，則傳回 true。

以下規則定義有效字串：
    -任何左括號「(」必須有對應的右括號「)」。
    -任何右括號 ')' 必須有對應的左括號 '('。
    -左括號「(」必須位於對應的右括號「)」之前。
    -'*' 可視為單一右括號 ')' 或單一左括號 '(' 或空字串 ""。
    
    

解題思路
這個問題可以通過使用兩個變數來跟蹤可能的左括號的最小和最大數量來解決。在遍歷字符串的過程中，更新這兩個數值來考慮所有可能的情況。

1. 初始化：初始化leftMin和leftMax分別為0。leftMin表示在考慮*作為)或空字符串時可能的最少左括號數量，而leftMax表示在考慮*作為(時可能的最多左括號數量。

2. 遍歷字符串：對於字符串s中的每一個字符：
    -如果是(，則leftMin和leftMax都加1。
    -如果是)，則leftMin和leftMax都減1。
    -如果是*，則leftMin減1（考慮*為)），leftMax加1（考慮*為(）。

3. 條件判斷：
    -在任何時候，如果leftMax變為負數，表示右括號過多，字符串無效，直接返回False。
    -如果leftMin變為負數，則將其重置為0，因為*可以被視為空字符串。
    
4.結果判斷：最後，如果leftMin為0，表示所有左括號都可以被匹配，返回True，否則返回False。

時間複雜度分析
遍歷一次字符串s，時間複雜度為O(N)，其中N是字符串s的長度。

空間複雜度分析
這個解法只使用了固定的額外空間（用於存儲leftMin和leftMax變數），因此空間複雜度為O(1)。

"""