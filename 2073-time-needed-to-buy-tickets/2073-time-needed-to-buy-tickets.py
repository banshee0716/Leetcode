from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        secs = 0  # 初始化經過的秒數
        i = 0  # 從隊列的開始位置開始
        
        while tickets[k] != 0:  # 繼續直到第k個人買完票
            if tickets[i] != 0:  # 如果當前人還需要買票
                tickets[i] -= 1  # 該人買一張票
                secs += 1  # 經過時間增加1

            i = (i + 1) % len(tickets)  # 循環遍歷隊列
        
        return secs

"""
解題思路
這個問題可以通過模擬隊列中每個人買票的過程來解決。從隊列的開始逐個檢查每個人是否還需要買票（即tickets[i]是否大於0）。
如果是，則他買一張票（tickets[i]減1），並將經過的時間加1。當到達隊列末尾時，從隊列開始繼續進行檢查，直到第k個人買完他的所有票。
    
時間複雜度分析
這個算法需要遍歷tickets數組直到第k個人買完票，最壞情況下的時間複雜度為O(N)，其中N是tickets數組的長度。

空間複雜度分析
這個算法除了給定的輸入數組外，只使用了幾個固定的額外空間（用於存儲索引i和秒數secs），因此空間複雜度為O(1)。
"""