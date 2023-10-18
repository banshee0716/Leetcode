class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # 根據課程數量n創建一個空的鄰接表
        graph = [[] for _ in range(n)]

        # 根據relations填充鄰接表
        for prev, next in relations:
            graph[prev - 1].append(next - 1)

        # 初始化一個memo列表，用於記錄每個課程的最大完成時間
        memo = [-1] * n

        # 定義一個遞歸函數來計算給定課程的最大完成時間
        def calculateTime(course):
            # 如果這個課程的時間已經計算過了，就直接返回它
            if memo[course] != -1:
                return memo[course]

            # 如果這個課程沒有先決條件，則其完成時間就是其本身的時間
            if not graph[course]:
                memo[course] = time[course]
                return memo[course]

            # 尋找所有先決條件中所需時間最長的
            max_prerequisite_time = 0
            for prereq in graph[course]:
                max_prerequisite_time = max(
                    max_prerequisite_time, calculateTime(prereq)
                )

            # 計算當前課程的最大完成時間並記錄到memo中
            memo[course] = max_prerequisite_time + time[course]
            return memo[course]

        # 初始化一個變數來記錄所有課程中的最大完成時間
        overall_min_time = 0
        # 計算每個課程的最大完成時間，並更新overall_min_time
        for course in range(n):
            overall_min_time = max(overall_min_time, calculateTime(course))

        # 返回完成所有課程所需的最短時間
        return overall_min_time
    
    
"""
這個問題是一個經典的圖論問題，其中包含了有向圖和動態規劃的元素。基本的想法是，每個課程可以視為一個節點，每個節點都有一個完成所需的時間，而節點間的關係代表了課程間的依賴。要找到完成所有課程所需的最短時間，我們需要對每個節點進行深度優先搜索（DFS），同時記錄每個節點所需的最長時間。

解題思路：
首先，根據relations建立一個圖的表示，這裡我們使用鄰接表。
然後，對每個課程（節點）進行深度優先搜索，計算完成該課程所需的最大時間（包括其所有先決條件）。
我們使用memo列表來避免重複計算同一課程的時間。
最後，從所有課程的最大時間中找出全局的最大值，這將是完成所有課程所需的最短時間。

時間複雜度：
O(V + E)：其中V是節點的數量（課程的數量），E是邊的數量（關係的數量）。這是因為每個節點和每條邊我們只訪問一次。
空間複雜度：
O(V)：存儲圖的鄰接表和memo列表所需的空間。

"""