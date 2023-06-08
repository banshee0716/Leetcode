class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = bisect_left(nums, 0)
        pos = len(nums) - bisect_right(nums, 0 )
        return max(neg, pos)
        #二分搜尋找到負數的邊界跟正數的邊界，如果找到位置的話再來比較兩者間的距離