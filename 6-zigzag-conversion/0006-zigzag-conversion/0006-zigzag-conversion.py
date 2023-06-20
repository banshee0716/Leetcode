class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [''] * numRows
        index, step = 0, 1
        for char in s:
            rows[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(rows)
    
    #chatGPT寫的
    #首先，檢查字符串長度是否小於或等於numRows，或者numRows是否等於1，如果是，則返回原字符串。
    #然後，使用一個列表rows存儲每一行的字符。使用兩個變量index和step分別跟蹤下一個字符應該放置在哪一行以及下一個字符應該往哪一個方向移動。
    #在每次迭代中，將字符添加到適當的行，並將index和step更新為適當的值。最後，使用join函數將所有行連接起來並返回結果。