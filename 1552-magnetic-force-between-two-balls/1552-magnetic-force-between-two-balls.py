class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # - input is not sorted.
        position.sort()

        # - BS between 1 and R.
        # - R = maxDif/m
        # - maxDif = max(position) - min(position)
        lo, hi, ans = 1, (max(position) - min(position)) // (m - 1) + 1, 0
        while lo < hi:
            mid, cnt, pre = (lo + hi) // 2, 1, position[0]
            # - Ball placement
            for p in position[1:]:
                if p - pre >= mid:
                    cnt += 1
                    pre = p
                    if cnt > m:
                        break
            if cnt >= m:
                ans = max(ans, mid)
                lo = mid + 1
            else:
                hi = mid
        return ans

