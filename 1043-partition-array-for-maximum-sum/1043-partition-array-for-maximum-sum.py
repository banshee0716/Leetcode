from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)  # 數組的長度
        dp = [0] * (n + 1)  # 動態規劃表初始化
        
        for i in range(n):
            curMax = curSum = 0
            
            # 從i開始向前看k個元素
            for j in range(i, max(-1, i - k), -1):
                curMax = max(curMax, arr[j])  # 更新區間內的最大值
                cur = curMax * (i - j + 1) + dp[j]  # 計算當前分割的總和
                curSum = max(curSum, cur)  # 更新最大總和
            
            dp[i + 1] = curSum  # 更新動態規劃表
        
        return dp[-1]  # 返回最大總和

    
    
    """
給定一個整數陣列 arr，將陣列分成長度最多為 k 的（連續）子陣列。分區後，每個子數組的值都會變更為該子數組的最大值。

傳回給定數組分區後的最大和。產生測試案例以使答案適合 32 位元整數。


LeetCode 1043題「分割數組以得到最大和」的目標是給定一個整數數組arr和一個整數k，要求通過將數組分割成一些（可能的大小不一）子數組，使得每個子數組中最大的元素的和最大化，且每個子數組的長度不超過k。返回完成分割後的最大和。

解題思路
1. 動態規劃：
    -定義一個動態規劃表dp，其中dp[i]表示考慮到arr的前i個元素時，能夠獲得的最大和。dp[0]初始化為0。

2. 遍歷數組：
    -從左到右遍歷數組arr，對於每個位置i，考慮最後一個分割區間的可能長度，從1到k。

3. 更新最大值：
    -在考慮到位置i並且最後一個分割區間長度為某個固定值時，計算該分割方式下的總和，並更新dp[i+1]。

4. 返回結果：
    -dp[n]即為整個數組在分割後能獲得的最大和。
    
時間複雜度
    -遍歷數組arr的時間複雜度為O(n)。
    -對於數組中的每個元素，向前看最多k個元素以更新動態規劃表，因此內層循環的總時間複雜度為O(kn)。
    -總的時間複雜度為O(kn)。

空間複雜度
    -使用了一個額外的動態規劃表dp，其長度為n+1，因此空間複雜度為O(n)。
    """