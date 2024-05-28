class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        start = 0
        current_cost = 0
        max_length = 0
        
        for end in range(n):
            current_cost += abs(ord(s[end]) - ord(t[end]))
            
            while current_cost > maxCost:
                current_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
             
            max_length = max(max_length, end - start + 1)
            
        return max_length
    
    
    """
給定兩個長度相同的字串 s 和 t 以及一個整數 maxCost。
您想要將 s 更改為 t。將 s 的第 i 個字元改為 t 的第 i 個字元的成本為 |s[i] - t[i]| （即字元的 ASCII 值之間的絕對差）。
傳回 s 的子字串的最大長度，該子字串可以更改為與 t 的相應子字串相同，且成本小於或等於 maxCost。如果 s 中沒有可以變更為 t 中對應子字串的子字串，則傳回 0。
    """