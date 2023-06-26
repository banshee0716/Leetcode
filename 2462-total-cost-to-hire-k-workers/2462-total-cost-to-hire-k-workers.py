from typing import List
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        i, j = 0, len(costs) - 1
        pq1, pq2 = [], [] # 初始化兩個優先權隊列
        ans = 0 # 初始化總成本為0
        while k > 0:
            # 為左邊的隊列填充候選成本
            while len(pq1) < candidates and i <= j:
                heapq.heappush(pq1, costs[i]) # 將成本加入隊列
                i += 1
            # 為右邊的隊列填充候選成本
            while len(pq2) < candidates and i <= j:
                heapq.heappush(pq2, costs[j]) # 將成本加入隊列
                j -= 1

            # 獲取兩個隊列中的最小值
            t1 = pq1[0] if pq1 else float('inf')
            t2 = pq2[0] if pq2 else float('inf')

            # 如果左邊的最小值小於等於右邊的最小值
            if t1 <= t2:
                ans += t1 # 增加總成本
                heapq.heappop(pq1) # 從隊列中移除這個成本
            else:
                ans += t2 # 增加總成本
                heapq.heappop(pq2) # 從隊列中移除這個成本

            k -= 1 # 減少一次操作

        return ans # 返回總成本

        
        
        
        
        
"""
給定一個 0 索引的整數數組 cost，其中 cost[i] 是僱用第 i 個工人的成本。

您還將獲得兩個整數 k 和候選數。我們希望根據以下規則僱用恰好 k 個工人：

1. 您將運行 k 個會話，並在每個會話中僅僱用一名工人。
2. 在每次招聘中，從第一批候選人或最後一批候選人中選擇成本最低的工人。以最小的index打破平局。
    - 例如，如果成本 = [3,2,7,7,1,2] 且候選人 = 2，那麼在第一次招聘中，
    - 我們將選擇第 4 個工人，因為他們的成本最低 [3,2,7, 7,1,2]。
    - 在第二次招聘中，我們將選擇第 1 個工人，因為他們與第 4 個工人具有相同的最低成本，但他們的索引最小[3,2,7,7,2]。請注意，在此過程中索引可能會發生變化。
3. 如果剩下的候選工人少於候選工人，則選擇其中成本最低的工人。以最小的index打破平局。
4. 一個工人只能被選擇一次。

返回僱用恰好 k 個工人的總成本。
"""

"""

這段程式碼的時間複雜度為 O(n log n)，其中 n 是 costs 陣列的長度。這是因為我們需要對每個成本進行一次堆操作，而堆操作的時間複雜度為 log n。

空間複雜度為 O(n)，因為我們需要用兩個優先權隊列存儲所有的成本。
"""