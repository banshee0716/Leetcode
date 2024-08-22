class Solution:
    def findComplement(self, num: int) -> int:
        bit_length = num.bit_length()
        mask = (1 << bit_length) - 1
        return num ^ mask
        
        
    
    #把他的bit拿出來，做一個和他bit長度相同且完全相反的mask，之後與他取xor