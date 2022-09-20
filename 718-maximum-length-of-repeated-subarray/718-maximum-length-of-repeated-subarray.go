func findLength(A []int, B []int) int {
    ans := 0
    memo := make([][]int,len(A)+1)
    for i := range (memo){
        memo[i] = make([]int, len(B)+1)
    }
    for i := len(A)-1; i > -1; i--{
        for j := len(B)-1; j > -1; j--{
            if A[i] == B[j]{
                memo[i][j] = memo[i+1][j+1] + 1
                if ans < memo[i][j]{
                    ans = memo[i][j]
                }
            }
        }
    }
    
    return ans
}