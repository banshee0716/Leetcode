class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def finder(i):
            if manager[i] != -1:
                informTime[i] += finder(manager[i])
                manager[i] = -1
            return informTime[i]
        return max(map(finder, range(n)))