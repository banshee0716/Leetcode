func kthSmallest(matrix [][]int, k int) int {
    ret := make([]int,0)
    for i := 0; i < len(matrix); i++ {
        for j := 0; j < len(matrix[0]); j++{
            ret = append(ret, matrix[i][j])
        }
    }
    sort.Ints(ret)
    return ret[k-1]
}