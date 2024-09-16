class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        M = 1440
        times = [False] * M
        for time in timePoints:
            minute = self.minute(time)
            if times[minute]:
                return 0
            times[minute] = True
        
        minutes = [i for i in range(M) if times[i]]
        return min((minutes[i] - minutes[i-1]) % M for i in range(len(minutes)))
        
    def minute(self, time: str) -> int:
        h, m = map(int, time.split(':'))
        return 60*h + m