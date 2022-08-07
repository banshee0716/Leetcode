
class Solution:
    def countVowelPermutation(self, n: int) -> int:

        # Initialize all vowels counts to 1
		# This is n==1 case
        a, e, i, o, u = 1, 1, 1, 1, 1

        # Iterate from 2 to n
        for _ in range(2, n+1):
            a,e,i,o,u = e+i+u, a+i, e+o, i, i+o
        
        return (a+e+i+o+u) % 1000000007