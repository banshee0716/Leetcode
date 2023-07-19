class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 對區間按照結束時間進行排序
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)

        # 選擇第一個區間
        prev = 0
        count = 1

        # 遍歷後續的區間
        for i in range(1, n):
            # 如果當前區間的開始時間大於或等於前一個選擇的區間的結束時間
            if intervals[i][0] >= intervals[prev][1]:
                # 選擇這個區間
                prev = i
                count += 1

        # 返回需要移除的最小區間數
        return n - count

"""
時間複雜度為O(N log N)，其中N是區間的數量。這是由於我們需要對區間進行排序，排序操作的時間複雜度為O(N log N)。遍歷區間的操作時間複雜度為O(N)，

空間複雜度為O(1)，我們只使用了常數個額外的變數來存儲中間結果，並未使用與輸入規模相關的額外空間。
"""