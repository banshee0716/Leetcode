class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        for ch in word:
            if not ch.isdigit():
                word = word.replace(ch, ' ')
                
        word = word.split()
        word = set(int(i) for i in word)
        return len(word)
        
        
"""
給你一個由數字和小寫英文字母組成的字符串單詞。
您將用空格替換每個非數字字符。例如，“a123bc34d8ef34”將變為“123 34 8 34”。請注意，剩下的一些整數至少由一個空格分隔：“123”、“34”、“8”和“34”。
返回對word進行替換操作後不同整數的個數。
如果兩個整數的十進製表示形式（不帶任何前導零）不同，則認為兩個整數不同。
"""