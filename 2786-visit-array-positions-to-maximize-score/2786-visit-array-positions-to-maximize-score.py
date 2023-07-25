class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        even_score = nums[0] - (x if nums[0] % 2 else 0)
        odd_score = nums[0] - (0 if nums[0] % 2 else x)
        
        for i in range(1, len(nums)):
            if nums[i] % 2:
                odd_score, even_score = nums[i] + max(odd_score, even_score - x), even_score
            else:
                odd_score, even_score = odd_score, nums[i] + max(even_score, odd_score - x)
                
        return max(even_score, odd_score)
        
        
        
"""
給定一個 0 索引的整數數組 nums 和一個正整數 x。

您最初位於數組中的位置 0，您可以根據以下規則訪問其他位置：

    - 如果您當前處於位置 i，那麼您可以移動到任意位置 j，使得 i < j。
    - 對於您訪問的每個位置 i，您將獲得 nums[i] 分數。
    - 如果你從位置 i 移動到位置 j 並且 nums[i] 和 nums[j] 的奇偶性不同，那麼你會失去 x 的分數。
返回您可以獲得的最高總分。

請注意，最初您有 nums[0] 點。

一個動態規劃的問題，可以把系統中的狀態轉化成奇數和偶數的兩個狀態，滾動計算
我們首先將 Even_score 和 odd_score 初始化為第一個數字的分數，必要時考慮成本“x”。
然後，對於數組中的每個數字，我們根據其奇偶性更新相應的分數。
    -如果數字是奇數，我們通過將當前數字與 odd_score 和 Even_score - x 的最大值相加來更新 odd_score。
    -如果是偶數，我們類似地更新even_score。
最後，我們返回even_score和odd_score中的最大值作為我們可以獲得的最大總分。

https://www.youtube.com/watch?v=jLnWQe4Hzps&feature=youtu.be&ab_channel=vanAmsen
"""