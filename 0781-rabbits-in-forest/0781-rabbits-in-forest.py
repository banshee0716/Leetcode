class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = {}
        res = 0 
        for i in answers:
            if i == 0:
                res += 1
            else:
                if i not in c or c[i] == i:
                    c[i] = 0
                    res += 1+i
                else:
                    c[i] += 1
        return res
        
        
"""
有一片森林，裡面有數量不詳的兔子。我們問n隻兔子“有多少隻兔子和你的顏色一樣？”並將答案收集到整數數組answers中，其中answers[i]是第i隻兔子的答案。

給定數組答案，返回森林中可能存在的兔子的最小數量。
"""