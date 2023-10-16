class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        ans = []
        num = []
        k = 0
        for each in words:
            if each.isdigit():
                num.append(int(each))
                k = 0
            else:
                k += 1
                if k > len(num):
                    ans.append(-1)
                else:
                    ans.append(num[-k])
                    
        return ans