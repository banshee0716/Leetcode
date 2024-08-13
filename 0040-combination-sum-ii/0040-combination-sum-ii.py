from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort the candidates to facilitate pruning and duplicate skipping
        candidates.sort()
        res = []  # List to store the final result

        def dfs(target: int, start: int, comb: List[int]):
            # Base case: If the target becomes negative, no valid combination
            if target < 0:
                return
            # Base case: If the target is 0, we found a valid combination
            if target == 0:
                res.append(comb)  # Add the current combination to the result
                return
            # Iterate through the candidates starting from 'start' index
            for i in range(start, len(candidates)):
                # Skip duplicate elements to avoid identical combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # If the current candidate exceeds the remaining target, stop further exploration
                if candidates[i] > target:
                    break
                # Recursively explore further by including the current candidate
                dfs(target - candidates[i], i + 1, comb + [candidates[i]])

        # Start the DFS with the initial target and an empty combination
        dfs(target, 0, [])
        return res  # Return the list of all valid combinations


"""
給定一組候選數字 (candidates) 和一個目標數字 (target)，找出候選數字中候選數字總和達到目標值的所有唯一組合。
候選中的每個數字只能在組合中使用一次。
注意：解決方案集不得包含重複的組合。

方法：
排序：第一步是對候選清單進行排序。排序有助於輕鬆跳過重複項，並且還允許在當前候選超出剩餘目標時提前終止。
深度優先搜尋（DFS）：主要方法是使用DFS（回溯）來探索總和為目標的所有可能的數字組合。 DFS 函數遞歸地嘗試將每個候選者新增至目前組合（梳）並相應地減少目標。
修剪和跳過重複：如果目前候選與前一個候選相同，則跳過它以避免重複組合。如果目前候選超過剩餘目標，則循環將中斷以停止進一步探索，因為清單已排序。


"""