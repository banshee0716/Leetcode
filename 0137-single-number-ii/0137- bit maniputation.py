class Solution:
    def singleNumber(self, nums):
        ones = 0  # 用來保存只出現一次的數字的位元
        twos = 0  # 用來保存出現兩次的數字的位元

        for num in nums:
            ones = (ones ^ num) & ~twos  # 使用 XOR 更新 ones，並清除第三次出現的位元
            twos = (twos ^ num) & ~ones  # 使用 XOR 更新 twos，並清除第三次出現的位元

        return ones  # 返回只出現一次的數字


"""

這個解法使用了兩個變量 ones 和 twos 來分別表示出現一次和兩次的數字的位元。
在遍歷每一個數字時，我們使用 XOR 運算符來更新這兩個變量。
我們需要注意的是，當一個位元第三次出現時，我們需要將它從 ones 和 twos 中清除，這是通過使用 AND 運算符和 NOT 運算符來實現的。


時間複雜度為 O(n)，其中 n 是數組的長度，因為我們需要遍歷數組一次。
空間複雜度為 O(1)，因為我們只使用了兩個變量來保存中間結果，並沒有使用到與輸入規模相關的額外空間。
"""
