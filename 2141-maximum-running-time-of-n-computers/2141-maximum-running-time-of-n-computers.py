class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 0, sum(batteries)//n+1
        
        def check(time):
            return sum(min(time,b) for b in batteries) >= n*time
            
        while left < right:
            mid = left + (right - left)//2
            if check(mid):
                left = mid + 1
            else:
                right = mid 
                
        return left-1
        #同時運行所有 n 台計算機的最大分鐘數。
        
        
"""
你有n台電腦。給定整數 n 和一個 0 索引的整數數組電池，其中第 i 個電池可以讓計算機運行電池 [i] 分鐘。您有興趣使用給定的電池同時運行所有 n 台計算機。

最初，您最多可以在每台計算機中插入一塊電池。此後，在任意整數時刻，您可以從計算機中取出電池並插入另一塊電池任意次數。插入的電池可以是全新電池，也可以是另一台計算機的電池。您可能會認為移除和插入過程不需要時間。

請注意，電池不能充電。

返回可以同時運行所有 n 台計算機的最大分鐘數。
"""