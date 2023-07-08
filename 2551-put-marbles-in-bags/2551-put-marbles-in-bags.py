class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        B = [a + b for a,b in pairwise(weights)]
        return sum(nlargest(k-1, B)) - sum(nsmallest(k-1,B))

        
        
        
        
        
        #return sum(nlargest(k - 1, B)) - sum(nsmallest(k - 1, B))
        
        
        
        
"""
你有 k 個袋子。給定一個 0 索引的整數數組weights，其中weights[i]是第i個彈珠的重量。您還將獲得整數 k。

按照以下規則將彈珠分為k個袋：

沒有一個袋子是空的。
如果第 i 個彈珠和第 j 個彈珠在一個袋子中，那麼所有索引在第 i 個和第 j 個索引之間的彈珠也應該在同一個袋子中。
如果一個袋子由索引從 i 到 j 的所有彈珠組成，則該袋子的成本為weights[i]+weights[j]。
分配彈珠後的得分是所有 k 個袋子的成本之和。

返回彈珠分佈中最大和最小分數之間的差異。
"""