class Solution:
    def minimumDeletions(self, s: str) -> int:
        cntA, ans=0, 0
        for i in range(len(s)-1, -1, -1):
            if s[i]=='a': cntA+=1
            else: ans=min(ans+1, cntA)
        return ans
        
        
        
        

        
"""
給定一個僅由字元 'a' 和 'b'組成的字串 s。
您可以刪除 s 中任意數量的字元以使 s 平衡。如果不存在滿足 i < j 且 s[i] = 'b' 且 s[j]= 'a' 的索引對 (i,j)，則 s 是平衡的。
傳回使 s 平衡所需的最小刪除次數。
"""