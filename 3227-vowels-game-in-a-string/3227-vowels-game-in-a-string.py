class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for ch in s:
            if ch in 'aeiou':
                return True
            
        return False
    
    
    """
愛麗絲和鮑伯正在玩繩子遊戲。

給你一個字串 s，Alice 和 Bob 將輪流玩以下遊戲，Alice 首先開始：

輪到 Alice 時，她必須從 s 中刪除任何包含奇數個元音的非空子字串。
輪到 Bob 時，他必須從 s 中刪除包含偶數個元音的任何非空子字串。
第一個無法在自己的回合中採取行動的玩家將輸掉遊戲。我們假設 Alice 和 Bob 都處於最佳狀態。

如果 Alice 贏得了遊戲，則傳回 true，否則傳回 false。

英語母音有：a、e、i、o 和 u。
    """