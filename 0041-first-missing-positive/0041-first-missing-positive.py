class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Function to swap elements in the array
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
        
        n = len(nums)
        
        # Place each positive integer i at index i-1 if possible
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                swap(nums, i, nums[i] - 1)
        
        # Find the first missing positive integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all positive integers from 1 to n are present, return n + 1
        return n + 1

        
    
    """
給定一個未排序的整數數組 nums。傳回 nums 中不存在的最小正整數。
您必須實作一個在 O(n) 時間內運作並使用 O(1) 輔助空間的演算法。


解題思路
這道題的關鍵是將每個正整數i放到數組索引i-1的位置上，然後遍歷數組，第一個數字不符合nums[i] == i + 1條件的索引i+1，就是缺失的最小正整數。

1. 元素交換：定義一個swap函數，用於交換數組中的兩個元素。

2. 數組重排：遍歷數組nums，對於每個元素nums[i]，如果其值在1到n（n是數組長度）之間，且nums[i]不在其應該在的位置上（即nums[i] != nums[nums[i] - 1]），則將其與nums[nums[i] - 1]交換。

3. 尋找缺失的正數：再次遍歷數組，找到第一個nums[i] != i + 1的位置，則i + 1是缺失的最小正數。

4. 處理邊界情況：如果數組中包含1到n的所有正整數，則缺失的最小正數是n + 1。

時間複雜度分析
    -數組重排的過程中，每個元素最多被交換兩次（一次放到正確位置上，另一次是其它元素被交換時），因此時間複雜度為O(N)。
    -第二次遍歷查找缺失的最小正數的時間複雜度也是O(N)。
    -總的時間複雜度為O(N)。

空間複雜度分析
    -本解法只使用了常數級別的額外空間（用於交換元素），因此空間複雜度為O(1)。
    """