class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]  # 建立鄰接表
        indegree = [0] * n  # 建立入度表
        ans = []  # 建立結果列表

        # 處理所有的前置課程需求
        for pair in prerequisites:
            course = pair[0]
            prerequisite = pair[1]
            adj[prerequisite].append(course)  # 將 course 加入 prerequisite 的鄰接表
            indegree[course] += 1  # 將 course 的入度加 1

        # 將所有入度為 0 的節點加入隊列
        queue = deque([i for i in range(n) if indegree[i] == 0])

        # 進行拓撲排序
        while queue:
            current = queue.popleft()  # 取出一個節點
            ans.append(current)  # 將該節點加入結果列表

            # 處理所有以 current 為前置課程的課程
            for next_course in adj[current]:
                indegree[next_course] -= 1  # 入度減 1
                if indegree[next_course] == 0:  # 如果入度變為 0，將其加入隊列
                    queue.append(next_course)

        # 判斷是否可以完成所有的課程
        return len(ans) == n


"""
1. 一個拓樸排序問題，我們首先建立每個節點（也就是每個課程）的鄰接表 adj 和入度表 indegree。adj[i] 包含了所有的 i 的後繼節點（也就是所有需要 i 作為前置課程的課程），indegree[i] 則是節點 i 的入度（也就是有多少課程需要 i 作為前置課程）。

2. 接著，我們將所有入度為 0 的節點加入隊列 queue 中。這些節點表示不需要任何前置課程，可以直接開始的課程。

3. 我們進行一個迴圈，每次從隊列中取出一個節點，將其加入結果列表 ans 中，並將所有以該節點為前置課程的節點的入度減 1。如果某一節點的入度變為 0，那麼我們將其加入隊列。

4. 如果所有的課程都被加入了結果列表，那麼我們就可以完成所有的課程，返回 True；否則，返回 False。

時間複雜度是 O(N + E)，其中 N 是課程的數量，E 是前置課程需求的數量，因為我們需要遍歷每個節點和每條邊。
空間複雜度是 O(N)，主要用於存儲鄰接表和隊列。
"""