class Solution:
    def canSplitArray(self, A: List[int], m: int) -> bool:
        return len(A) <= 2 or any(A[i] + A[i + 1] >= m for i in range(len(A) - 1))
        
"""   
Intuition
If n == 1, done.
If n == 2, split once, done.
Otherwise we must have a middle status,
that one array has length 2 and A[i] + A[i + 1] >= m.


Explanation
If n > 2
there is at least one pair satisfies A[i] + A[i + 1] >= m.

This is a necessry and sufficient condition to split array.

So we return if n <= 2 or any A[i] + A[i + 1] >= m.


Complexity
Time O(n)
Space O(1)
    """