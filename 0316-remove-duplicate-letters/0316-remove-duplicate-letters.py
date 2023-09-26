class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []  # 儲存結果字串的字母
        seen = set()  # 追踪哪些字母已經在結果字串中
        last_occ = {c: i for i, c in enumerate(s)}  # 每個字母的最後出現位置
        
        for i, c in enumerate(s):
            # 若當前字母已在結果中，則跳過
            if c not in seen:
                # 若堆疊不為空，且當前字母小於堆疊頂部的字母，且堆疊頂部的字母在後面還會再次出現
                while stack and c < stack[-1] and i < last_occ[stack[-1]]:
                    # 從 `seen` 中移除堆疊頂部的字母，並將其彈出
                    seen.discard(stack.pop())
                # 將當前字母加入 `seen` 和堆疊
                seen.add(c)
                stack.append(c)
                
        # 將堆疊轉換為字串並返回
        return "".join(stack)
"""
解題思路：
1. 創建一個堆疊 stack 用於存放結果字串的字母。
2. 創建一個集合 seen 用於追踪哪些字母已經在結果字串中。
3. 創建一個字典 last_occ 來追踪每個字母在原始字串中的最後出現的位置。
4. 迭代原始字串中的每個字母。對於每個字母，如果它不在 seen 中，則將其加入堆疊。但是在這之前，要確保加入此字母後堆疊仍然是遞增的。

時間複雜度：O(n)，其中 n 是字串的長度。我們只需遍歷字串一次。
空間複雜度：O(1)。即使使用了幾個輔助數據結構，但字母的數量是固定的（最多 26 個字母）。
"""
        