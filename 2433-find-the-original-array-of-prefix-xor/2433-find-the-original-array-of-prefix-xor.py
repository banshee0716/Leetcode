class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        return map(xor, pref, [0] + pref[:-1])
        
        
    
    """
給定一個大小為 n 的整數數組 pref。尋找並傳回大小為 n 且符合以下條件的陣列 arr：

pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]。
注意，^ 表示位元異或運算。

可以證明答案是唯一的。
    """