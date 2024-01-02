from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # 統計元素出現次數
        um = {}
        for i in nums:
            um[i] = um.get(i, 0) + 1
        
        ans = []  # 最終結果
        # 構建二維數組
        while um:
            temp = []  # 臨時數組
            to_erase = []  # 需要刪除的鍵
            for f, s in um.items():
                temp.append(f)
                s -= 1
                if s == 0:
                    to_erase.append(f)
                um[f] = s
            ans.append(temp)
            for i in to_erase:
                del um[i]  # 刪除出現次數為0的鍵
        return ans

# 使用black格式化後的代碼與上述代碼在格式上已經符合標準

    
"""
統計元素出現次數：
使用一個字典 um 來記錄每個元素在數組 nums 中的出現次數。

構建二維數組：
持續從字典 um 中取出元素直到字典變為空。每次迭代中，將字典中的所有鍵添加到一個臨時數組 temp 中，並減少這些鍵的出現次數。如果某個鍵的出現次數降至0，則將其從字典中刪除。

返回結果：
將每次迭代得到的臨時數組 temp 添加到最終結果 ans 中，然後返回 ans。


時間複雜度分析：
統計元素出現次數的時間複雜度為 O(n)，其中 n 為數組 nums 的長度。
構建二維數組的時間複雜度為 O(m * k)，其中 m 為數組 nums 中不同元素的數量，k 為每次迭代中字典中元素的個數。在最壞情況下，k 可以接近 n。
總的時間複雜度為 O(n + m * k)，但由於 k 在大多數情況下會小於 n，因此總時間複雜度更接近 O(n)。

空間複雜度分析：
使用了額外的空間來存儲元素出現次數的字典和最終的二維數組，空間複雜度為 O(n)。
"""