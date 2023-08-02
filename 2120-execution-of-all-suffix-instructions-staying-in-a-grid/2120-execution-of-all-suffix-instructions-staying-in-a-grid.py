class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        na = len(s)

        def test(i):
            x, y = startPos
            for j in range(i, na):
                o = s[j]
                if o == "L":
                    y -= 1
                if o == "R":
                    y += 1
                if o == "U":
                    x -= 1
                if o == "D":
                    x += 1
                if not (0 <= x < n and 0 <= y < n):
                    return j - i

            return na - i

        return list(map(test, range(na)))

        
        
"""
有一個 n x n 網格，左上角的單元格位於 (0, 0)，右下角的單元格位於 (n - 1, n - 1)。給定整數 n 和整數數組 startPos，其中 startPos = [startrow, startcol] 表示機器人最初位於單元格 (startrow, startcol)。

您還會獲得一個長度為 m 的 0 索引字符串 s，其中 s[i] 是機器人的第 i 條指令：“L”（向左移動）、“R”（向右移動）、“U”（向上移動）、和“D”（向下移動）。

機器人可以從 s 中的任何第 i 條指令開始執行。它在 s 結束時逐條執行指令，但如果滿足以下任一條件，它將停止：

下一條指令將使機器人離開網格。
沒有更多的指令需要執行。
返回長度為 m 的數組answer，其中answer[i] 是機器人從 s 中的第 i 條指令開始執行時機器人可以執行的指令數。
"""