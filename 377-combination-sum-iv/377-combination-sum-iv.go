func combinationSum4(nums []int, target int) int {
    
    // look-up table
    combinationCount := make(map[int]int)
    
    // --------------------------------------------------
    
    // function variable
    var dfs func(int)int
    
    dfs = func(wanted int) int{
        
        // base cases:
        if wanted < 0{
            // stop condition for negative number
            return 0
        }else if wanted == 0{
            // stop condition for perfect match
            return 1
        }
        
        if count, exist := combinationCount[wanted]; exist == true{
            // quick response by look-up table
            return count
        }
        
        // general cases
        count := 0
        
        for _, number := range nums{
            
            nextWanted := wanted - number
            
            count += dfs( nextWanted )
            
        }
        
        combinationCount[wanted] = count
        return count
    }
    // --------------------------------------------------
    
    
    return dfs(target)
}