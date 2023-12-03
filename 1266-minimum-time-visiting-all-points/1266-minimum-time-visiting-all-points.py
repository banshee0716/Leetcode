class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(1, len(points)):
            prev, cur = points[i - 1 : i + 1]
            ans += max(map(abs, (prev[0] - cur[0], prev[1] - cur[1])))
        return ans    
        
        
    """
    在 2D 平面上，有 n 個點，其座標為整數點 [i] = [xi, yi]。返回按點給出的順序訪問所有點的最短時間（以秒為單位）。

您可以按照以下規則進行移動：

1 秒內，您可以：
    -垂直移動一個單位，
    -水平移動一個單位，或
    -對角移動 sqrt(2) 個單位（換句話說，在 1 秒內垂直移動一個單位，然後水平移動一個單位）。
您必須按照數組中出現的順序存取這些點。
您可以透過順序中稍後出現的點，但這些不計為存取。
    """