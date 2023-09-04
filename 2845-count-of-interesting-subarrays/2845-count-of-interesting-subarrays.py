from collections import defaultdict
from typing import List

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        # 初始化數字的長度和前綴和
        n = len(nums)
        prefix = [0] * (n + 1)

        # 計算前綴和
        for i in range(n):
            prefix[i + 1] = prefix[i] + (nums[i] % modulo == k)

        # 使用哈希表記錄每個模結果的出現次數
        count = defaultdict(int)
        ans = 0

        # 遍歷前綴和，計算答案
        for i in range(n + 1):
            j = prefix[i] - k
            ans += count[j % modulo]
            count[prefix[i] % modulo] += 1

        return ans

    """
解題思路
1. 前綴和 (Prefix Sum) 計算：首先，為了計算子陣列的模數，我們會先計算一個前綴和的陣列 prefix。這個 prefix[i] 代表從 nums[0] 到 nums[i-1] 中數字模 modulo 為 k 的數目。
2. 哈希表 (Hashmap) 計數：使用一個哈希表 count 來記錄每個前綴和模 modulo 的結果出現的次數。
3. 計算答案：遍歷前綴和陣列 prefix，每次從哈希表 count 中找到符合條件的前綴和，累加到答案 ans 中，並更新哈希表的計數。

時間複雜度: 因為我們遍歷了 nums 一次來計算前綴和，再遍歷前綴和陣列一次來計算答案，所以總時間複雜度為 O(n)，其中 n 是 nums 的長度。

空間複雜度: 我們使用了一個長度為 n+1 的前綴和陣列和一個哈希表來記錄每個模結果的出現次數，所以空間複雜度為 O(n)。
    """