class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        digit_length = len(str(n))
        
        for d in range(digit_length):
            factor = 10 ** d
            lower = n % factor
            current = (n // factor) % 10
            higher = n // (factor * 10)
            
            if current == 0:
                count += higher * factor
            elif current == 1:
                count += higher * factor + lower + 1
            else:
                count += (higher + 1) * factor
                
        return count
