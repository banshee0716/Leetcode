class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        pigs = 0
        # 計算測試輪數
        rounds = minutesToTest // minutesToDie
        # 使用豬的數量來確定能測試多少桶水
        while (rounds + 1) ** pigs < buckets:
            pigs += 1
        return pigs
"""
解題思路：

1. 考慮在有x只豬和t輪測試的情況下，你能測試多少桶水。每只豬可以提供t+1種信息（不喝水，第1輪喝水死，第2輪喝水死，...，第t輪喝水死），
x只豬就能提供(t+1) ^ x種信息。
2. 所以當(t+1) ^ x 大於等於桶的數量時，你就能確定哪個桶有毒。

時間複雜度分析：

-理論上時間複雜度是O(log_buckets)，因為每增加一只豬，能測試的桶的數量就會指數增加。
-但實際上，由於通常情況下pigs和rounds的數量會非常小（因為他們能代表的信息量是指數增長的），這個循環會非常快地結束。所以在實際情況下，這個算法的運行時間非常快。

空間複雜度分析：
程序中沒有使用額外的數據結構，空間複雜度是O(1)。
"""