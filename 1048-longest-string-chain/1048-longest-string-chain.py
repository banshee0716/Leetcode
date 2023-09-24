class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # 根據單詞的長度對單詞進行排序
        words.sort(key=len)
        
        # 初始化字典來存儲每個單詞的最長單詞鏈長度
        dic = {}
        
        # 遍歷每個單詞
        for i in words:
            dic[i] = 1
            # 計算當前單詞的所有可能的前導單詞
            for j in range(len(i)):
                successor = i[:j] + i[j+1:]
                # 如果前導單詞存在於字典中，更新當前單詞的單詞鏈長度
                if successor in dic:
                    dic[i] = max(dic[i], 1 + dic[successor])
        
        # 返回最長的單詞鏈長度
        return max(dic.values())


"""
解題思路：
1. 根據單詞的長度對單詞列表進行排序。這樣，當我們處理一個特定的單詞時，我們可以確保所有可能的前導單詞都已經被考慮過了。
2. 使用字典 dic 來儲存每個單詞的最長單詞鏈長度。
3. 遍歷每個單詞，並計算它的所有可能的前導單詞。對於每個可能的前導單詞，我們更新當前單詞的鏈長度。
4. 最後，從 dic 中找到最長的單詞鏈長度。

時間複雜度：O(N*M^2)，其中 N 是單詞的數量，M 是單詞的平均長度。這是因為我們需要遍歷每個單詞，並計算它的所有可能的前導單詞。
空間複雜度：O(N)。我們需要一個字典來存儲每個單詞的最長單詞鏈長度。
"""