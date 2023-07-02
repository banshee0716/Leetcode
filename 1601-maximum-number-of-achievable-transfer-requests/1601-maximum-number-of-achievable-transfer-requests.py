class Solution:
    def __init__(self):
        self.ans = 0  # 初始化答案為 0

    def helper(self, start, requests, indegree, n, count):
        if start == len(requests):  # 如果已經遍歷完所有請求
            if all(degree == 0 for degree in indegree):  # 如果所有建築的進出度都為 0
                self.ans = max(self.ans, count)  # 更新答案
            return

        # 選擇當前請求
        indegree[requests[start][0]] -= 1
        indegree[requests[start][1]] += 1
        self.helper(start + 1, requests, indegree, n, count + 1)

        # 不選擇當前請求，並回溯
        indegree[requests[start][0]] += 1
        indegree[requests[start][1]] -= 1
        self.helper(start + 1, requests, indegree, n, count)

    def maximumRequests(self, n, requests):
        indegree = [0] * n  # 初始化每個建築的進出度
        self.helper(0, requests, indegree, n, 0)  # 開始遞迴
        return self.ans  # 返回答案

"""
在 __init__ 函式中，我們初始化答案 self.ans 為 0。
在 helper 函式中，我們透過遞迴的方式嘗試每一個請求。當我們嘗試到請求的末尾時，我們檢查 indegree 是否都為 0，如果是，則更新答案 self.ans。
對於每一個請求，我們有兩種選擇：選擇這個請求（Take）或不選擇這個請求（Not-take）。我們分別遞迴這兩種選擇，並在選擇後更新 indegree 和請求的數量 count。
在 maximumRequests 函式中，我們初始化 indegree，並呼叫 helper 函式開始遞迴。最後返回答案 self.ans。

時間複雜度為 O(2^n)，其中 n 是請求的數量，因為每個請求都有兩種選擇，總共有 2^n 種可能的組合。
空間複雜度為 O(n)，因為我們需要一個長度為 n 的陣列來儲存每個建築的進出度。
"""
