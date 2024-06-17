import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(math.sqrt(c))
        
        while a <= b:
            cur = a * a + b * b
            if cur == c:
                return True
            elif cur < c:
                a += 1
            else:
                b -= 1
        
        return False


    """
解題思路：

遍歷所有可能的a值：從0遍歷到sqrt(c)，因為a和b的範圍都應在0到sqrt(c)之間。
計算b的值：對於每個a值，計算b = sqrt(c - a^2)。如果c - a^2是完全平方數，則b應該是整數。
檢查b是否為整數：如果b的整數部分與b相等，即b == int(b)，則表示找到了合適的a和b，返回True。
如果遍歷完沒有找到：如果所有可能的a都不能找到對應的整數b，則返回False。

時間複雜度：O(√c)，其中c是給定的數。這是因為需要遍歷從0到√c的所有可能值。
空間複雜度：O(1)，算法只使用了固定數量的額外空間。
    """