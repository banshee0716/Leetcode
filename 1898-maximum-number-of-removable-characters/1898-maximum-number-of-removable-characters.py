class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int: 
        def check(m) -> bool:
            i = j = 0
            remove = set(removable[:m+1])
            while i < len(s) and j < len(p):
                if i in remove:
                    i += 1
                    continue
                if s[i] == p[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            
            return j == len(p)
            
                
        # search interval is [lo, hi)
        low, high = 0, len(removable)+1
        
        while low < high:
            mid = low + (high - low) // 2
            if check(mid):
                low = mid + 1
            else:
                high = mid
                
        return low if low < len(removable) else low-1