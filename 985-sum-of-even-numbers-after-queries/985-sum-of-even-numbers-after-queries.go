func sumEvenAfterQueries(nums []int, queries [][]int) []int {
    evenSum := 0
    for _, val := range(nums) {
        if val %2 == 0{
            evenSum += val
        }
    }
    ans := make([]int, len(queries))
    for i, q := range(queries){
        val, idx := q[0], q[1]
        if nums[idx] % 2 == 0 {
            evenSum -= nums[idx]
        }
        // in-place update nums
        nums[idx] += val
        // check if we need to update evenSum for the new value
        if nums[idx] % 2 == 0 {
            evenSum += nums[idx]
        }
        // then we have evenSum after this query, push it to ans 
        ans[i] = evenSum
    }
    return ans
}