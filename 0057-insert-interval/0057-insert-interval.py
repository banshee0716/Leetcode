class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new = []
        for i in intervals:
            if i[1] < newInterval[0]:
                new.append(i)
            elif i[0] > newInterval[1]:
                new.append(newInterval)
                newInterval = i
            else:
                newInterval[0] = min(i[0], newInterval[0])
                newInterval[1] = max(i[1], newInterval[1])
        
        new.append(newInterval)
        return new

        