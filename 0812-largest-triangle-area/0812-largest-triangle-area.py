class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        #海龍公式解
       
        area = 0  # 初始化最大面積為0
        n = len(points)  # 點的數量
        for i in range(n):  # 第一層迴圈選擇第一個點
            x1,y1 = points[i]  # 取得第一個點的坐標
            for j in range(i+1,n):  # 第二層迴圈選擇第二個點
                x2,y2 = points[j]  # 取得第二個點的坐標
                for k in range(j+1,n):  # 第三層迴圈選擇第三個點
                    x3,y3 = points[k]  # 取得第三個點的坐標
                    # 計算當前三角形面積，並與先前的最大面積進行比較
                    curr = abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
                    if curr > area:  # 如果當前面積大於最大面積，則更新最大面積
                        area = curr
        return area  # 返回最大面積

"""
我們對所有可能的三點組合進行了迭代。所以，時間複雜度為 O(n^3)，其中 n 為給定的點的數量。
由於我們只需要常數的額外空間來存儲面積，所以空間複雜度為 O(1)。
"""