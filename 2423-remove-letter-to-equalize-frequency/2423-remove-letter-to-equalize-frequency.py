class Solution:
    def equalFrequency(self, word: str) -> bool:
        wordC = Counter(word)
        temp = wordC.copy()
        for i in wordC:
            temp[i] -= 1
            if temp[i] == 0:
                del temp[i]
            if len(set(temp.values())) == 1:
                return True
            if i not in temp:
                temp[i] = 0
            temp[i] += 1
            
        return False
        
        
"""
給你一個 0 索引的字符串單詞，由小寫英文字母組成。您需要選擇一個索引並從單詞中刪除該索引處的字母，以便單詞中每個字母出現的頻率相等。

如果可以刪除一個字母以使單詞中所有字母的頻率相等，則返回 true，否則返回 false。

筆記：

字母 x 的頻率是它在字符串中出現的次數。
您必須恰好刪除一個字母，並且不能選擇什麼也不做。
    """