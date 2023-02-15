class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans, i = [], len(num) - 1
        while k > 0 or i >= 0:
            k, rmd = divmod(k + (num[i] if i >= 0 else 0), 10)
            ans.append(rmd)
            i -= 1
        return reversed(ans)