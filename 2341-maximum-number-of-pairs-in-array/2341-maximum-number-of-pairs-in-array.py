class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cur = Counter(nums)
        print(cur)
        ans = [0, 0]
        for v in cur.values():
            ans[0] += v // 2
            ans[1] += v % 2
            
        return ans
    
"""
給定一個 0 索引的整數數組 nums。在一項操作中，您可以執行以下操作：
    - 在 nums 中選擇兩個相等的整數。
    - 從 nums 中刪除兩個整數，形成一對。
    
對 nums 執行盡可能多次的操作。

返回大小為 2 的 0 索引整數數組答案，其中答案 [0] 是形成的pair的數量，答案 [1] 是執行盡可能多次操作後 nums 中剩餘整數的數量。

solution：
不用特別講吧，去計算它的值之後，Ans[0]是他成對的數量，ans[1]是他剩餘不能成對的，之後直接返回
"""