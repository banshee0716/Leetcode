class Solution:
    def minimumMoves(self, s: str) -> int:
        ans = i = 0
        while i < len(s): 
            if s[i] == "X": 
                ans += 1
                i += 3
            else: i += 1
        return ans 
        
        
        
        
        
    """
    給定一個由 n 個字元組成的字串 s，這些字元要么是“X”，要么是“O”。

移動被定義為選擇 s 的三個連續字元並將它們轉換為“O”。請注意，如果對角色“O”應用移動，它將保持不變。

傳回將 s 的所有字元轉換為「O」所需的最小移動次數。
    """