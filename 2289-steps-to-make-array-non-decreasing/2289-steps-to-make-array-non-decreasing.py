class Solution:
    def totalSteps(self, A: List[int]) -> int:
        dp = [0] * len(A)
        stack = []
        for i, a in enumerate(A):
            cur = 0
            while stack and a >= A[stack[-1]]:
                cur = max(cur, dp[stack.pop()])
            if stack:
                dp[i] = cur + 1
            stack.append(i)
        return max(dp)