from typing import List
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # 將工作按結束時間排序
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        sorted_end_times = [x[1] for x in jobs]
        n = len(jobs)
        
        # 初始化動態規劃數組
        dp = [0] * n
        dp[0] = jobs[0][2]

        # 遍歷每個工作
        for i in range(1, n):
            current_start, _, current_profit = jobs[i]
            # 使用二分查找找到最晚且不與當前工作重疊的工作
            j = bisect.bisect_right(sorted_end_times, current_start) - 1
            if j >= 0:
                current_profit += dp[j]
                
            # 更新動態規劃數組
            dp[i] = max(current_profit, dp[i - 1])

        # 返回最大利潤
        return dp[-1]

# 使用black格式化後的代碼與上述代碼在格式上已經符合標準

"""
LeetCode 1235題「規劃工作以獲得最大利潤」的目標是從給定的工作列表中選擇一些工作來完成，以獲得最大的利潤。每個工作都有一個開始時間、結束時間和從中獲得的利潤。工作不能重疊，即在同一時間只能做一個工作。

解題思路：

1.排序工作：
    -首先將工作按照結束時間排序。這樣可以更容易地確定哪些工作可以在完成其他工作之後進行。

2. 二分查找：
    -使用二分查找來找到對於當前工作，最晚結束的且不與當前工作重疊的先前工作。

3. 動態規劃：
    -使用一個數組 dp 來存儲到目前為止可以獲得的最大利潤。對於每個工作，計算包括這個工作在內的最大利潤，並更新 dp 數組。

4.返回結果：
    -最後的答案是 dp 數組中的最後一個元素，即考慮所有工作後的最大利潤。
    

時間複雜度分析：
    -將工作按結束時間排序的時間複雜度為 O(n log n)，其中 n 是工作的數量。
    -對於每個工作，使用二分查找來找到最晚且不與當前工作重疊的工作，時間複雜度為 O(log n)。
    -因此，總的時間複雜度為 O(n log n)。

空間複雜度分析：
    -需要額外的空間來存儲排序後的工作列表和動態規劃數組，空間複雜度為 O(n)。
"""