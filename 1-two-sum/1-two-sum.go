func twoSum(nums []int, target int) []int {
    index_map := make(map[int]int)
    for i,v:= range nums{
        j, ok := index_map[-v]
        index_map[v - target] = i
        if ok{
            return []int{j,i}
        }
    }
    return []int{}
}