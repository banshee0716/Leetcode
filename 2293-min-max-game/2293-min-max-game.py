class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        l = nums
        while len(l) > 1:
            is_min = True
            tmp=[]
            for i in range(0,len(l),2):
                if is_min:
                    tmp.append(min(l[i:i+2]))
                else:
                    tmp.append(max(l[i:i+2]))
                
                is_min = not is_min
            
            l = tmp
            
        return l[0]