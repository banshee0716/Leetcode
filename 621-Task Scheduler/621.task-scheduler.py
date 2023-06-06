#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#


# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = dict()  # 計數每種任務的數量
        for task in tasks:
            counter[task] = counter.get(task, 0) + 1

        # 建立一個最大堆，儲存每種任務的數量
        hq = list()
        for task, count in counter.items():
            heappush(hq, (-count, task))  # Python 的 heapq 是最小堆，所以我們儲存 -count 來模擬最大堆

        time = 0  # 總時間
        while hq:  # 當堆不為空時，表示還有任務未完成
            tmp = []  # 暫存這一輪取出的任務
            for _ in range(n + 1):  # 每輪最多執行 n+1 個任務
                if hq:
                    tmp.append(heappop(hq))

            for count, task in tmp:
                if count + 1 < 0:
                    heappush(hq, (count + 1, task))

            time += len(tmp) if not hq else n + 1

        return time


""" 
解題思路如下：
1. 我們首先對每個任務進行計數，並將它們儲存在字典中。

2. 接著，我們將字典中的每一項放入最大堆中。這是為了確保我們每次都先執行次數最多的任務。

3. 我們將設計一個迴圈，直到所有任務都完成（也就是堆為空）。

    * 在每一個迴圈中，我們會嘗試執行 n+1 個不同的任務。我們首先將這些任務從堆中取出，並將它們放入一個暫存列表中。

    * 然後，我們會將暫存列表中的任務放回堆中，除非它們的數量已經降到0。

    * 如果堆已經為空（這表示所有任務已經完成），我們就加上暫存列表中的任務數量到總時間；否則，我們就加上 n+1 到總時間。

4. 最後，我們返回總時間。

"""
"""
時間複雜度：
O(mlogm)，其中 m 是任務種類的數量。這是因為我們需要在每一輪中對堆進行操作。

空間複雜度：
O(m)，其中 m 是任務種類的數量。這是因為我們需要用一個字典來儲存每種任務的數量，以及一個最大堆來儲存每種任務的數量。
"""
# @lc code=end
