class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope = 0
        for i in range(len(coordinates)-1):
            x1, y1=coordinates[i]
            x2, y2=coordinates[i+1]

            if x2-x1==0:
            #vertical line #m=slope
                m=float('inf')
            else:
                m=(y2-y1)/(x2-x1)

            if slope == 0:
                slope = m
            else:
                if slope != m:
                    return False
            
        return True
