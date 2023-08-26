class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        cur, ans = float('-inf'), 0
        for pair in pairs:
            if cur < pair[0]:
                cur = pair[1]
                ans += 1
                
        return ans
                
        
        
        
        
    """
給定一個由 n 對組成的數組，其中pairs[i] = [lefti, righti] 且 lefti < righti。

如果 b < c，則一對 p2 = [c, d] 跟隨一對 p1 = [a, b]。可以以這種方式形成成對的鏈。

返回可以形成的最長鏈的長度。

您不需要用完所有給定的間隔。您可以按任意順序選擇對。

greedy
    """