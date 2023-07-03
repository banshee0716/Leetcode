class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)

        # 如果s和goal完全相等
        if s == goal:
            temp = set(s)  # 利用set來去除重複字符
            return len(temp) < len(goal)  # 如果set長度小於goal，表示s中存在相同的字符，可以交換相同的字符來達成條件

        i = 0
        j = n - 1

        # 找到s和goal第一個不同的字符
        while i < j and s[i] == goal[i]:
            i += 1

        # 找到s和goal最後一個不同的字符
        while j >= 0 and s[j] == goal[j]:
            j -= 1

        # 交換第一個和最後一個不同的字符
        if i < j:
            s_list = list(s)
            s_list[i], s_list[j] = s_list[j], s_list[i]  # 交換字符
            s = ''.join(s_list)  # 重新組合成字串

        return s == goal  # 檢查交換後的s是否等於goal

    
"""
1. 首先，我們需要確認 s 和 goal 的長度是否一致。如果不一致，那麼一定不能透過交換兩個字符使 s 變為 goal。此部分程式碼未提及，但在實際應用中，我們需要檢查。
2. 如果 s 和 goal 相等，那麼我們需要檢查 s 是否有重複的字符。這是因為我們可以交換相同的字符，使得 s 保持不變。我們使用 set 函數來創建一個集合，並檢查集合的大小是否小於 s 的長度，如果是，則表示 s 中有重複的字符。
3. 如果 s 和 goal 不相等，我們需要找到 s 和 goal 第一個不相等的字符和最後一個不相等的字符，並交換這兩個字符。我們使用兩個變量 i 和 j 來找到這兩個字符，並使用 list 函數和 join 函數來交換字符並重新組合字串。
4. 最後，我們檢查交換字符後的 s 是否等於 goal。

時間複雜度為 O(n)，其中 n 是字串的長度。我們需要遍歷字串一次來找到不同的字符。
空間複雜度為 O(1)，我們只需要常數空間來存儲變量。
"""