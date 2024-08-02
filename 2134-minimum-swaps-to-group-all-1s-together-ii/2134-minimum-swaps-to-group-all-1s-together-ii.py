class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = nums.count(1)
        mx = cnt = sum(nums[:k])
        n = len(nums)
        
        for i in range(k, n+k):
            cnt += nums[i%n]
            cnt -= nums[(i - k + n) % n]
            mx = max(mx, cnt)
            
        return k - mx
        
        
    
    
    """
交換被定義為在數組中佔據兩個不同的位置並交換其中的值。

循環數組被定義為我們認為第一個元素和最後一個元素相鄰的陣列。

給定一個二進位循環數組 nums，傳回將數組中任意位置的所有 1 組合在一起所需的最小交換次數。
    """