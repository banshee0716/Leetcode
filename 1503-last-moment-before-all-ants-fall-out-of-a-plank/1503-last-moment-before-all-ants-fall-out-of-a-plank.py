class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        time = 0
        for pos in left:
            time = max(time, pos)
        for pos in right:
            time = max(time, n-pos)
            
        return time
        
    
    
    """
我們有一塊長度為 n 個單位的木板。有些螞蟻在木板上行走，每隻螞蟻以每秒1個單位的速度移動。有些螞蟻向左移動，有些則向右移動。

當兩隻向兩個不同方向移動的螞蟻在某個時刻相遇時，它們會改變方向並再次繼續移動。假設改變方向不需要任何額外的時間。

當一隻螞蟻在時間 t 到達木板一端時，它立即從木板上掉下來。

給定一個整數 n 和兩個整數數組 left 和 right，螞蟻向左和向右移動的位置，返回最後一隻螞蟻掉出木板的時刻。
    """