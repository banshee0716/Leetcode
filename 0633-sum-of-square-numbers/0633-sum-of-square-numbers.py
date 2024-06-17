import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # 遍歷可能的a值，範圍是從0到根號c
        for a in range(int(math.sqrt(c)) + 1):
            # 計算b的值為c - a^2的平方根
            b = math.sqrt(c - a * a)
            # 檢查b是否為整數，如果b的整數部分和自身相等，則b是整數
            if b == int(b):
                return True  # 如果b是整數，說明找到了合適的a和b
        return False  # 如果遍歷完所有a都沒有找到合適的b，返回False
