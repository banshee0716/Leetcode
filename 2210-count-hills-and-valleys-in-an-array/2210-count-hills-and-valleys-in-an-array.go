func countHillValley(nums []int) int {
    var l ,res, idx int = len(nums), 0, 1
    for idx < l - 1{
		if nums[idx] == nums[idx - 1]{
			idx++
			continue
		}
		var right int = idx + 1
		for right < l && nums[right] == nums[idx]{
			right++
		}
		if right >= l{
			break
		}
		if (nums[idx] > nums[idx - 1] && nums[idx] > nums[right]) || (nums[idx] < nums[idx - 1] && nums[idx] < nums[right]){
			res++
		}
		idx = right
	}
	return res
}