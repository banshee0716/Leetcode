#
# @lc app=leetcode id=1472 lang=python3
#
# [1472] Design Browser History
#

# @lc code=start
class BrowserHistory:
    def __init__(self, homepage: str):
        # 初始化歷史紀錄、當前指標和邊界指標
        self.history = [homepage]
        self.curr = 0
        self.bound = 0

    def visit(self, url: str) -> None:
        # 訪問新的url時，當前指標增加1
        self.curr += 1
        # 如果當前指標等於歷史紀錄長度，就把新的url加入歷史紀錄中
        if self.curr == len(self.history):
            self.history.append(url)
        else:
            # 如果當前指標小於歷史紀錄長度，就把新的url插入到當前指標的位置
            self.history[self.curr] = url
        # 更新邊界指標
        self.bound = self.curr

    def back(self, steps: int) -> str:
        # 計算後退的位置
        self.curr = max(self.curr - steps, 0)
        # 返回當前指標對應的url
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        # 計算前進的位置
        self.curr = min(self.curr + steps, self.bound)
        # 返回當前指標對應的url
        return self.history[self.curr]


"""
時間複雜度分析：

__init__方法的時間複雜度為O(1)，因為只是對數據結構進行了初始化。
visit方法的時間複雜度為O(1)，因為只是對數據結構進行了修改，而不需要遍歷數據。
back方法和forward方法的時間複雜度都為O(1)，因為只是根據當前指標和步數計算出新的當前指標，並返回相應位置上的url，不需要遍歷數據。
空間複雜度分析：

history數組佔用的空間為O(n)，其中n為訪問的url數量。
curr和bound指標佔用的空間為O(1)。因此，總空間複雜度為O(n)。
"""
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# @lc code=end
