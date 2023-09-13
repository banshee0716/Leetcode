class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n  # 初始化每個孩子分配 1 顆糖果

        # 從左至右遍歷，確保評分高的孩子比左鄰居得到更多糖果
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        # 從右至左遍歷，確保評分高的孩子比右鄰居得到更多糖果
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)  # 返回糖果總數

    
    
    """
每個孩子至少分到一顆糖果。
1評分較高的孩子必須得到比其鄰居更多的糖果。
2問題是如何分配糖果，使得總糖果數量最少。
    
解題思路：
1. 初始化一個 candies 數組，給每個孩子分配 1 顆糖果。
2. 從左至右遍歷 ratings。如果當前孩子的評分比左鄰居高，那麼給當前孩子分配比左鄰居多一顆的糖果。
3. 再從右至左遍歷 ratings。如果當前孩子的評分比右鄰居高且當前的糖果數量不多於右鄰居，那麼給當前孩子分配比右鄰居多一顆的糖果。
4. 返回所有孩子的糖果總數。


時間複雜度：O(n)。兩次遍歷 ratings 數組，其中 n 是 ratings 的長度。
空間複雜度：O(n)。用了一個 candies 數組來存儲每個孩子的糖果數量。
    """