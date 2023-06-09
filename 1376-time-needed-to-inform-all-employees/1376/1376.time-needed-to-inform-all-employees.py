#
# @lc app=leetcode id=1376 lang=python3
#
# [1376] Time Needed to Inform All Employees
#

# @lc code=start
"""
這段程式碼採用了深度優先搜索(DFS)的策略，
從每一個員工開始，追蹤回他們的經理，直到達到頂點（頭部ID，其經理為-1）。
過程中會累計需要的時間，並將累計的時間儲存在informTime裡，且將經理設為-1來表示這個節點已被處理過，避免重複處理。最後，返回所有員工中最大的informTime，即傳播訊息所需的最長時間。
"""
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def finder(i):
            # 如果i的經理不是-1（即i不是頭部ID）
            if manager[i] != -1:
                # 將i的經理所需的時間加到i所需的時間上
                informTime[i] += finder(manager[i])
                # 將i的經理設為-1，表示i已經被處理過
                manager[i] = -1
            # 返回i所需的時間
            return informTime[i]

        # 對每個員工執行finder，找到最大的時間
        return max(map(finder, range(n)))
"""

時間複雜度：
O(n)，其中 n 是員工的數量。我們需要遍歷每個員工並對其進行處理。

空間複雜度：
O(n)，其中 n 是員工的數量。深度優先搜索需要的遞迴棧的深度可能達到 n，因此空間複雜度是 O(n)。
"""
# @lc code=end

