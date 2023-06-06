#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#


# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        我們可以利用深度優先搜索（DFS）的策略來解決這個問題。
        1. 一開始，我們建立一個set用於儲存已經訪問過的房間。然後，我們從第0個房間開始進行DFS。
        2. 在進行DFS時，我們會將當前房間加入到訪問過的房間中，然後遍歷該房間中的所有鑰匙，對其對應的房間進行DFS。
        3. 最後，我們只需要檢查訪問過的房間的數量是否等於房間總數即可。"""
        visited = set()  # 儲存已經訪問過的房間

        def dfs(room: int) -> None:  # 深度優先搜索的遞歸函數
            if room not in visited:  # 如果當前房間還未訪問過
                visited.add(room)  # 將當前房間加入到訪問過的房間中
                for key in rooms[room]:  # 遍歷當前房間中的所有鑰匙
                    dfs(key)  # 對鑰匙對應的房間進行DFS

        dfs(0)  # 從第0個房間開始進行DFS

        return len(visited) == len(rooms)  # 檢查訪問過的房間的數量是否等於房間總數


"""
時間複雜度和空間複雜度：

時間複雜度：O(n + e)，其中 n 是房間的數量，e 是鑰匙的數量。我們需要遍歷所有的房間和鑰匙。
空間複雜度：O(n)，其中 n 是房間的數量。這是因為我們需要一個set來儲存訪問過的房間。在最壞的情況下，我們可能需要訪問所有的房間。
"""
# @lc code=end
