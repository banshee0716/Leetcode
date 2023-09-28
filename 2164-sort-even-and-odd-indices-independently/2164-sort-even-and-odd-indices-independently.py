class Solution:
	def sortEvenOdd(self, nums: List[int]) -> List[int]:
		n = len(nums)
		for i in range(0,n,2):
			for j in range(i+2,n,2):
				if nums[i] > nums[j]:
					nums[i],nums[j] = nums[j], nums[i]

		for i in range(1,n,2):
			for j in range(i+2,n,2):
				if nums[i] < nums[j]:
					nums[i],nums[j] = nums[j], nums[i]
		return nums