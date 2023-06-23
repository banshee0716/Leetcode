class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        l = []  # 用於存儲 num 的因數
        for i in range(1, int(num ** 0.5) + 1):  # 迭代到 num 的平方根
            if num % i == 0:  # 如果 i 是 num 的因數
                l.extend([i, num // i])  # 添加 i 和 num//i 到因數列表

        # 計算因數的和（通過 set 去除重複的因數），並與 num 進行比較
        return sum(set(l)) - num == num
    
"""
這個程式碼的時間複雜度為 O(sqrt(n))，因為我們只需要迭代到數字的平方根就能找到所有的因數。這是因為對於每個因數 i，num//i 也是 num 的因數。

空間複雜度為 O(sqrt(n))，在最壞情況下，我們可能需要存儲所有因數（例如，對於一個完全平方數，它的所有因數數量最多）。
"""