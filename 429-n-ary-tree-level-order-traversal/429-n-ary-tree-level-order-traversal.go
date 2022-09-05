/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func levelOrder(root *Node) [][]int {
    var result [][]int
    
    if root == nil { 
        return result 
    }
    
    var queue []*Node
    queue = append(queue, root)
    
    for len(queue) > 0 {
        length := len(queue)
        
        var levelNodes []int
        
        for i := 0; i < length; i++ {
            levelNodes = append(levelNodes, queue[i].Val)
            
            for _, child := range queue[i].Children {
                if child != nil {
                    queue = append(queue, child)
                }
            }
        }
        
        result = append(result, levelNodes)
        
        if len(queue) == length {
            break
        }
        
        queue = queue[length:]
    }

    return result
}
