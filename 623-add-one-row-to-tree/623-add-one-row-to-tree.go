/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func addOneRow(root *TreeNode, v int, d int) *TreeNode {
    
	// handle base case , when we have to add new row is root itself
    if d == 1 {
       return &TreeNode{v,root,nil}
    }
    
    return addNode(root, v, 1, d-1)
}

func addNode(node *TreeNode,v,curr,d int) *TreeNode {
    if node == nil{
        return nil
    }
    if curr == d{//到了指定的層數
        node.Left = &TreeNode{v,node.Left,nil}
        node.Right = &TreeNode{v,nil,node.Right}
        return node 
        //把那層節點弄出兩顆node之後，把剩下的接上去。
    }
    node.Left = addNode(node.Left, v, curr+1, d)
    node.Right = addNode(node.Right, v, curr+1, d)
    return node
}