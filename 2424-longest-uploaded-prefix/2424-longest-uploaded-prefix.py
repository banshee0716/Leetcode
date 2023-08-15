class LUPrefix:
    def __init__(self, n: int):
        # 初始化一個大小為n+1的布林值陣列來記錄每個視頻的上傳狀態
        self.videos = [False] * (n + 1)
        # 用來儲存目前已上傳的最長連續前綴
        self.ans = 0

    def upload(self, video: int) -> None:
        # 標記該視頻已上傳
        self.videos[video] = True
        # 檢查當前的視頻是否是目前最長連續前綴的下一個
        if video == self.ans + 1:
            while video < len(self.videos):
                # 如果該視頻未上傳，則中止循環
                if not self.videos[video]:
                    break
                # 更新最長連續前綴
                self.ans += 1
                video += 1

    def longest(self) -> int:
        # 返回目前已上傳的最長連續前綴
        return self.ans



# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()

"""
你會得到一個n影片流，每個影片都由一個不同的數字1表示n，你需要“上傳”到服務器。
- 您需要實現一個數據結構，在上傳過程中的各個點計算最長上傳前綴的長度。
    - 如果到（含）範圍內的所有視頻都已上傳到服務器，我們認為i是上傳前綴。最長上傳前綴是滿足此定義的最大值。

解題思路：

1. 使用一個陣列來記錄每個視頻的上傳狀態。
2. 每次上傳一個視頻時，檢查它是否是目前最長連續前綴的下一個。
3. 如果是，則更新最長連續前綴。
4. 使用一個方法來返回目前已上傳的最長連續前綴。

時間複雜度：

upload 方法的時間複雜度是 O(n) ，其中 n 是視頻的數量。
longest 方法的時間複雜度是 O(1) 。
空間複雜度：O(n)，其中 n 是視頻的數量，主要是用於儲存視頻的上傳狀態。
"""