class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []  # 初始化堆疊
        for asteroid in asteroids:  # 遍歷每個行星
            if not stack or asteroid > 0:  # 如果堆疊為空或行星向右
                stack.append(asteroid)  # 將行星加入到堆疊中
            else:  # 否則
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):  # 如果堆疊非空且堆疊頂部的行星向右且小於當前行星的絕對值
                    stack.pop()  # 彈出堆疊頂部的行星
                if stack and stack[-1] == abs(asteroid):  # 如果堆疊非空且堆疊頂部的行星與當前行星絕對值相等
                    stack.pop()  # 彈出堆疊頂部的行星
                elif not stack or stack[-1] < 0:  # 如果堆疊為空或堆疊頂部的行星向左
                    stack.append(asteroid)  # 將當前行星加入到堆疊中

        return stack  # 返回堆疊中剩下的行星

            
        
"""
1. 設定一個stack，之後在回圈中把所有>0（正向）的全部加進stack
2. 如果沒有的話，就去計算他是否比現在stack裡面元素的絕對值大，結束就停下來

時間複雜度是 O(n)，其中 n 是行星的數量，因為我們遍歷了每個行星且每個行星只會入堆疊或出堆疊一次。
空間複雜度是 O(n)，因為在最壞情況下，所有的行星都會加入到堆疊中。
"""