func checkSubarraySum(nums []int, k int) bool {
    //keep a map with the first index of the end of prefix that has mod x
    //m[x] = the first index of the end of the prefix array that has the sum % k = x
    m := map[int]int{}
    m[0] = -1
    n := len(nums)
    prefixSum := 0
    for i := 0; i < n; i++ {
        prefixSum += nums[i]
        cur := prefixSum % k
        if idx, ok := m[cur]; ok {
            if i - idx > 1 {
                return true
            }
        } else {
            m[cur] = i
        }
    }
    return false
}