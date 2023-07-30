class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(h >= target for h in hours)
       
        """
某公司有n名員工，編號從0到n-1。每個員工i在公司工作了hours[i]個小時。

公司要求每位員工至少工作目標時間。

給您一個長度為 n 的非負整數小時的 0 索引數組和一個非負整數目標。

返回表示至少工作了目標時間的員工人數的整數。
        """