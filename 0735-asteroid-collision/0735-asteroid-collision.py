class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if not stack or asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                    stack.pop()
                if stack and stack[-1] == abs(asteroid):
                    stack.pop()
                else:
                    if not stack or stack[-1] < 0:
                        stack.append(asteroid)
                
        return stack
            
        

"""
1. 我們得到一個整數數組 asteroids ，代表一行中的小行星。
2. 對於每顆小行星，絕對值代表其大小，符號代表其方向（正值表示向右，負值表示向左）。每顆小行星都以相同的速度移動。
3. 找出所有碰撞後小行星的狀態。如果兩顆小行星相遇，較小的一顆就會爆炸。如果兩者大小相同，則兩者都會爆炸。朝同一方向移動的兩顆小行星永遠不會相遇。     
"""
"""
1. 設定一個stack，之後在回圈中把所有>0（正向）的全部加進stack
2. 如果沒有的話，就去計算他是否比現在stack裡面元素的絕對值大，結束就停下來
"""