class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pre = nums
        
        for i in range(len(self.pre)-1):
            self.pre[i+1]+=self.pre[i]


    def sumRange(self, left: int, right: int) -> int:
        self.left = left
        self.right = right
        if self.left:
            return self.pre[right]-self.pre[left-1]
        else:
            return self.pre[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)