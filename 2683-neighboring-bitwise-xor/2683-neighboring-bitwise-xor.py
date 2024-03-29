class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return sum(derived) % 2 == 0
        
        

"""

orginal: A[0], A[1], .... A[n-1]
derived: A[0]^A[1], A[1]^A[2] .... A[n-1]^A[0]

xor(derived) = (A[0]^A[1])^(A[1]^A[2])^ .... ^(A[n-1]^A[0]) = 0

The necessary and suffisant condition for derived to have an original is
xor(derived) == 0

Whend original and derived is binary sequence,
this equals to sum(derived) % 2 == 0.
"""