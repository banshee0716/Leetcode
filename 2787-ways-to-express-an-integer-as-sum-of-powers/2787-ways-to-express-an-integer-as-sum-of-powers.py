class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        # 初始化用來儲存計算結果的字典
        memo = {}

        # 定義動態規劃函數
        def dp(num, index):
            if num == 0:
                # 如果剩餘數字為0，表示已找到一種有效組合
                return 1
            elif num < 0 or index > n or index**x > num:
                # 如果剩餘數字小於0，或當前次方數大於n或大於剩餘數字，則此次方數無法產生有效組合
                return 0
            elif (num, index) in memo:
                # 如果已經計算過這個組合，則直接返回結果
                return memo[(num, index)]
            else:
                # 如果這是新的組合，則計算組合數量並存入字典
                memo[(num, index)] = dp(num - (index**x), index + 1) + dp(num, index + 1)
                return memo[(num, index)]
        
        # 調用動態規劃函數並返回結果，結果需要取模以防止數字過大
        return dp(n, 1) % (10**9 + 7)
