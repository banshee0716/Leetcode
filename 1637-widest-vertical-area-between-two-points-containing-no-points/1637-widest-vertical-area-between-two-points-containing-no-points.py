class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[0])
        max_width = 0
        for i in range(1, len(points)):
            width = points[i][0] - points[i-1][0]
            max_width = max(max_width, width)
            
        return max_width
        
        
        
        
    
    """
給定 2D 平面上的 n 個點，其中點[i] = [xi, yi]，傳回兩點之間最寬的垂直區域，使得沒有點位於該區域內。

垂直區域是沿著 y 軸無限延伸（即無限高度）的固定寬度區域。最寬的垂直區域是寬度最大的區域。

請注意，垂直區域邊緣上的點不被視為包含在該區域中。
    
    """