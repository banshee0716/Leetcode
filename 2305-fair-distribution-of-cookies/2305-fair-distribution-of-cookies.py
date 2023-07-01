class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float("inf")  # 初始化答案為正無窮大
        fair = [0] * k  # 初始化每個人的餅乾數

        def recursion(i: int):
            nonlocal ans, fair #可以在內嵌函數中修改外部變量的值
            if i == len(cookies):  # 如果所有餅乾已經分配完畢
                ans = min(ans, max(fair))  # 更新答案
                return
            # 如果當前最大不公平度已經超過了已知最小不公平度，則停止當前搜索分支
            if ans <= max(fair):
                return
            for j in range(k):  # 對於每一個人
                fair[j] += cookies[i]  # 將當前餅乾分配給他
                recursion(i + 1)  # 對下一塊餅乾進行分配
                fair[j] -= cookies[i]  # 撤銷剛才的分配

        recursion(0)  # 從第一塊餅乾開始分配
        return ans

    
"""

1. 在主函數 distributeCookies 中，我們首先初始化答案 ans 為正無窮大，以及一個長度為 k 的列表 fair 來記錄每個人所得的餅乾數。
2. 接著我們定義一個遞迴函數 recursion 來實現深度優先搜索。在這個函數中，如果已經沒有餅乾可以分配，那麼我們就更新答案 ans 為 ans 和 fair 中的最大值的最小值。
3. 如果當前的最大不公平度已經超過了已知的最小不公平度，那麼我們就停止當前的搜索分支，這是一種剪枝的策略。
4. 對於每一塊餅乾，我們都嘗試將它分配給每一個人，然後繼續對下一塊餅乾進行分配。
"""
"""
時間複雜度為 O(n^k)，其中 n 是餅乾的數量，k 是人數，因為我們需要遍歷所有可能的分配方案。
空間複雜度為 O(n)，因為我們需要一個長度為 n 的陣列來記錄每一個人所得的餅乾數。
"""
