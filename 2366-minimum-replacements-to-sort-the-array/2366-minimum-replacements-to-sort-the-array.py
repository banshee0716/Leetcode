class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        # 初始化操作數為 0 和動態上界 prev_bound
        operations = 0
        prev_bound = nums[-1]

        # 從倒數第二個元素開始，向前遍歷陣列
        for num in reversed(nums[:-1]):
            # 計算需要多少次操作將 num 分解為小於等於 prev_bound 的數字
            # 使用巧妙的公式來處理 num 能否被 prev_bound 整除的情況
            no_of_times = (num + prev_bound - 1) // prev_bound
            # 累計操作次數
            operations += no_of_times - 1  # -1 是因為其中一個替換的數字將佔據原來的位置
            # 更新 prev_bound
            prev_bound = num // no_of_times  # 確保下一次迭代中我們以最優的方式替換數字

        return operations


        
        
        
        """
給定一個 0 索引的整數數組 nums。在一次操作中，您可以將數組中的任何元素替換為任意兩個與其相加的元素。

例如，考慮 nums = [5,6,7]。在一次操作中，我們可以將 nums[1] 替換為 2 和 4，並將 nums 轉換為 [5,2,4,7]。
返回使數組按非降序排序的最少操作數。

解題思路
初始化一個變數 res 用於計算所需的最少操作數。
從陣列的最後一個元素開始，使用一個變數 prev_bound 來跟蹤當前考慮的數字必須被分解成小於或等於 prev_bound 的數字。
逐個遍歷陣列中的其他數字，計算將每個數字分解成小於或等於 prev_bound 的數字所需的最少操作數。


時間複雜度：O(n)，其中 n 是數字陣列的長度。我們只需要遍歷一次陣列。
空間複雜度：O(1)，除了輸入和一些常數變數外，我們沒有使用任何額外的空間。

"""