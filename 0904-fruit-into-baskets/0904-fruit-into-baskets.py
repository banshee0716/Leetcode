class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, num, res = 0, collections.Counter(), 0
        for i in range(len(fruits)):
            num[fruits[i]] += 1
            while len(num) > 2:
                num[fruits[l]] -= 1
                if not num[fruits[l]]:
                    num.pop(fruits[l])
                l += 1
            res = max(res, i-l+1)
        
        return res
            
        #integer array fruits where fruits[i] is the type of fruit the ith tree produces.
        #有兩個籃子,每個籃子只能放一種水果,如果走到不是那個種類的話就要跳出
