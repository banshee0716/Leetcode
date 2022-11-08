class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        for i in range(len(str(num))-k+1):
            n = str(num)
            val = int (n[i:i+k])
            if val and num % val == 0:
                count += 1
                
        return count
            
            
            
            
    #找有k位數的beauty number有幾個