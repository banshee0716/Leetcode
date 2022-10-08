func threeSumClosest(nums []int, target int) int {
    if len(nums) < 3{
        return -1
    }
    sort.Ints(nums)//先sort方便雙指針操作
    smallestDiff := 1 << 31//32位的最小值
    for i := 0; i < len(nums); i++{
        left, right := i+1, len(nums)-1
        for left < right{
            diff := target-nums[i] - nums[left] - nums[right]
            if diff == 0{
                return target
            }
            if abs (diff) < abs(smallestDiff)|| (abs(diff) == abs(smallestDiff) && diff > smallestDiff){
            //把最小Diff修正回來，有兩個情境，一個是絕對值有差距，一個是絕對值相同但一個是正的差距
                smallestDiff = diff
            }
            if diff > 0{
                left++
            }else{
                right--
            }
        }
    }
    return target-smallestDiff
}
func abs (x int)int{
    if x < 0{
        return -x
    }
    return x
}

//O(n^2)