/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func averageOfLevels(root *TreeNode) []float64 {
    if root == nil{
        return []float64{}
    }
    curLevelQ := []*TreeNode{root}//計算每階層數量
    averagePerLevel := []float64{}//返回的結果，每階層如何
    for len(curLevelQ) != 0{
        
        nextLevelQ := []*TreeNode{}
        curLevelSum := 0.0
        
        for _, node:= range curLevelQ{
        
            // update current level summation
            if node != nil{
                curLevelSum += float64(node.Val)
            }
            if node.Left != nil{
                nextLevelQ = append(nextLevelQ, node.Left)
            }
            if node.Right != nil{
                nextLevelQ = append(nextLevelQ, node.Right)
            }
        }
        curAvg := curLevelSum / float64(len(curLevelQ))
        averagePerLevel = append(averagePerLevel,curAvg)
        curLevelQ = nextLevelQ
    }
    return averagePerLevel
}