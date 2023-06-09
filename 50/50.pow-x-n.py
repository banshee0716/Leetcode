#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#


# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 基本條件的判斷
        if not n:
            return 1
        if n < 0:
            # 如果 n 是負的，我們可以將其變為正並將 x 轉為 1/x，使問題變為求 (1/x)^(-n)
            return 1 / self.myPow(x, -n)
        if n % 2:
            # 如果 n 是奇數，我們可以將其變為 n-1，並將結果乘以 x
            return x * self.myPow(x, n - 1)
        # 如果 n 是偶數，我們可以將其變為 n/2，並將 x 變為 x*x
        return self.myPow(x * x, n / 2)


"""
解題思路：
這題的解法是使用快速冪的概念來解決，即分治法的應用。
對於任何一個數的 n 次方，可以將其分解為 (x^2)^(n/2)
這樣可以將原本需要計算 n 次的乘法減半，達到加速運算的效果。
"""

"""
時間複雜度：
這個算法的時間複雜度是 O(log n)，這是因為每次遞迴時，我們都將 n 的值減半。因此，這個遞迴過程會遞迴 log(n) 次。

空間複雜度：
這個算法的空間複雜度也是 O(log n)，這是因為我們使用了遞迴，遞迴的深度是 log(n)，每次遞迴都需要一些額外的空間。
"""
# @lc code=end
