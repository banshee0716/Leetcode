class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # 如果 k 為奇數，則直接除以 2
        # 如果 k 為偶數，除以 2 之後減 1，因為中位數不能計算兩次
        if k % 2 == 1:
            additional = k // 2
        else:
            additional = k // 2 - 1

        # 如果需要替換的數字數量大於或等於 n，則不需要替換任何數字
        if additional >= n:
            additional = 0

        # 計算差值，確定我們應該加到被替換的數字上的值
        delta = n - (k - additional) + 1

        # 返回原始數組的總和加上 `additional x delta`
        return n * (n + 1) // 2 + additional * delta


"""

解題思路：

1. 直觀理解
考慮一個序列 nums = [1, 2, 3, 4, 5, 6, 7, 8] 和 k = 8。我們可以觀察到 1+7、2+6 和 3+5 都等於 8。因此，我們應該將 5、6、7 替換為 9、10、11，它們是原始數組中最後一個數字 8 之後的三個數字。接著，我們需要確定的是：(1) 我們應該替換多少個數字，以及 (2) 我們應該使用哪些數字來替換第一步中確定的數字。

2. 方法
確定我們應該替換多少數字 (即，變數 additional)。這可以通過計算和為 k 的對數量來確定。
確定我們應該添加到被替換的數字上的值以得到新的數字 (即，delta)。例如，假設 n=9, k=7，那麼有三對其和等於7的數字：1+6、2+5 和 3+4。這三對中的較大部分的最小數字是4。因此，delta = 9-4+1 = 6。
最終答案可以通過將 additional x delta 加到原始數組的總和上得到。
3. 特殊情況
如果 k 非常大，則應將其設為 0。

時間複雜度：O(1)。該算法只執行了一系列的常數時間操作。

空間複雜度：O(1)。該算法只使用了固定數量的額外空間。
"""
