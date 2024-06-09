from collections import defaultdict
from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # 初始化答案和前綴和
        res, prefix = 0, 0
        
        # 初始化餘數的頻率哈希表，並先設定餘數為0的頻率為1
        remainderFq = defaultdict(int)
        remainderFq[0] = 1

        # 遍歷每個數字
        for n in nums:
            # 計算前綴和
            prefix += n
            
            # 計算前綴和的餘數
            remainder = prefix % k
            
            # 將該餘數出現次數累加到答案中
            res += remainderFq[remainder]
            
            # 更新該餘數的頻率
            remainderFq[remainder] += 1

        # 返回答案
        return res
    