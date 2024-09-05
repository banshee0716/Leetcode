class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        cur_sum = sum(rolls)
        required_sum = (n + m) * mean
        missing_sum = required_sum - cur_sum
        if missing_sum < n or missing_sum > n * 6:
            return []
        ans = [1] * n
        missing_sum -= n

        for i in range(n):
            ans[i] += min(5, missing_sum)
            missing_sum -= 5
            if missing_sum <= 0:
                break

        return ans