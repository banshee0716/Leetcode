class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visit = {(0, 0)}
        for direction in path:
            x += 1 if direction == "E" else (-1 if direction == 'W' else 0)
            y += 1 if direction == "N" else (-1 if direction == 'S' else 0)
            if (x, y) in visit:
                return True
            visit.add((x, y))
            
        return False
            
        
        
        
    """
給定一個字串路徑，其中 path[i] = 'N'、'S'、'E' 或 'W'，每個分別代表向北、向南、向東或向西移動一個單位。您從 2D 平面上的原點 (0, 0) 開始，沿著 path 指定的路徑行走。

如果路徑在任何點與自身相交，即，如果您在任何時候位於之前訪問過的位置，則傳回 true。否則返回 false。
    """