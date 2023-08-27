class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        cnt = Counter(moves)
        return abs(cnt['L'] - cnt['R']) + cnt['_'] 
        
"""
給定一個長度為 n 的字符串移動，僅包含字符“L”、“R”和“_”。該字符串表示您在從原點 0 開始的數軸上的移動。

在第 i 個動作中，您可以選擇以下方向之一：

如果 Moves[i] = 'L' 或 Moves[i] = '_' 則向左移動
如果moves[i] = 'R' 或moves[i] = '_' 則向右移動
返回 n 次移動後可以到達的最遠點到原點的距離。
"""