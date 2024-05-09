from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # 首先檢查 k 是否合法
        if k > len(happiness):
            k = len(happiness)  # 如果 k 超過數組長度，則將 k 限制在最大長度
        
        # 對快樂值進行降序排序以優先選擇最大的快樂值
        happiness.sort(reverse=True)
        res = 0  # 初始化總快樂值
        
        # 遍歷前 k 個最大的快樂值
        for i in range(k):
            # 調整當前孩子的快樂值，考慮到之前已選擇的孩子數量
            adjusted_happiness = max(happiness[i] - i, 0)
            res += adjusted_happiness  # 將調整後的快樂值累加到總和中
        
        return res

        
        
    """
給定一個長度為 n 的幸福數組和一個正整數 k。
有n個孩子站在隊列中，其中第i個孩子的幸福值為happiness[i]。你想在 k 輪中從這 n 個孩子中選擇 k 個孩子。
每輪選擇一個孩子時，所有到目前為止還沒有被選中的孩子的幸福值都會減1。
返回選擇 k 個孩子可以獲得的所選孩子的幸福值的最大總和。

解題思路
1. 排序：首先對 happiness 陣列按從大到小排序，以便先選取快樂值高的孩子。
2. 選擇與減少：選擇過程中，考慮到每選擇一次，未被選擇的孩子的快樂值減少1，因此，對於第 i 個被選擇的孩子，其快樂值應減去 i（因為之前已經選擇了 i 個孩子）。
3. 計算結果：將調整後的快樂值加入結果，並重複 k 次選擇過程。

時間複雜度分析
時間複雜度：O(n log n)，其中 n 是 happiness 的長度。排序 happiness 需要 O(n log n) 時間，選擇過程需要 O(k)，但通常 k ≤ n。

空間複雜度分析
空間複雜度：O(1)。排序是原地進行的，並沒有使用額外顯著的空間。
    """