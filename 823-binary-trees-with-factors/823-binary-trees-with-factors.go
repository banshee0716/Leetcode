import (
    "math"
    "sort"
)

func numFactoredBinaryTrees(arr []int) int {
    
    
    
    // map
    // key: root node value
    // value: number of binary tree
    dp := make( map[int]int) 
    
    constant := (int)(math.Pow(10, 9) + 7)
    
    // keep A sorted in ascending order
    sort.Ints(arr)
    
    // scan each possible root node value
    for i, curNum := range arr{
        
        // Case 1: cur_num as root with child nodes
        
        // scan each potential child node value    
        for j := 0 ; j < i ; j+=1 {
            
            factor := arr[j]
            
            quotient, remainder := curNum / factor, curNum % factor
            
            // current (factor, quotient) pair are feasible to be child nodes 
            if remainder == 0{
                dp[curNum] += dp[factor] * dp[quotient]
            }
            
        }
        
        
        // Case 2: cur_num as root without child nodes
        dp[curNum] += 1
        
    }
    
    
    totalCount := 0
    for _, count := range dp{
        totalCount += count
    }
    
    return totalCount % constant
}