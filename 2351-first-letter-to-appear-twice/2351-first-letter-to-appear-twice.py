class Solution:
    def repeatedCharacter(self, s: str) -> str:
        visit = set()
        for i in s:
            if i in visit:
                return i
            else:
                visit.add(i)