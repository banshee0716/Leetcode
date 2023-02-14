class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = ''
        a, b = list(a), list(b)
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
                
            ans += str(carry % 2)
            carry //= 2
        
        return ans[::-1]