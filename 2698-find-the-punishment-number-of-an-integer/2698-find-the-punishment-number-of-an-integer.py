class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        for i in range(1, n+1):
            x = i**2
            p = str(x)
            if self.check(0, p, i):
                ans += x
        return ans
    
        
    def check(self, idx, p, target):
        if idx == len(p):
            return target == 0
        if target < 0:
            return False
        for i in range(idx, len(p)):
            x = p[idx:i + 1]
            y = int(x)
            if self.check(i + 1, p, target - y):
                return True
        return False
        
        
"""
給定一個正整數n，返回n的懲罰數。

n 的懲罰數定義為所有整數 i 的平方和，使得：

    1 <= i <= n
    i * i 的十進製表示可以劃分為連續的子串，使得這些子串的整數值之和等於 i。
"""