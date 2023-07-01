class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        
        for k in range(1, 61):
            if (num1 - k * num2).bit_count() <= k <= num1 - k * num2:
                return k
        return -1

"""
Start from k = 1,
to check if num = num1 - num2 * k can be the sum of k pow sof 2.

The maximum operations is num, num = (2 ^ 0) * num.
The minimum operations is num bits count.

If num.bit_count() <= k <= num,
then num can be the sum of k pows of 2.

Time O(60log(num1 + num2))
Space O(1)
"""