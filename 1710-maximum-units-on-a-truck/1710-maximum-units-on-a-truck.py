class Solution:
    def maximumUnits(self, B: List[List[int]], T: int) -> int:
        B.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        for b,n in B:
            boxes = min(b, T)
            ans += boxes * n
            T -= boxes
            if T == 0: return ans
        return ans

# B:numberOfBoxesi is the number of boxes of type i.
# numberOfUnitsPerBoxi is the number of units in each box of the type i.
# t:卡車載運量