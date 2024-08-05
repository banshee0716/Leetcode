class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        for v in arr:
            if counter[v] == 1:
                k -= 1
                if k == 0:
                    return v
                
        return ''
        
        
    
    
    """
不同字串是在陣列中僅出現一次的字串。

給定一個字串陣列 arr 和一個整數 k，傳回 arr 中出現的第 k 個不同的字串。如果不同字串少於 k 個，則傳回空字串「」。

請注意，字串會按照它們在陣列中出現的順序進行考慮。
    """