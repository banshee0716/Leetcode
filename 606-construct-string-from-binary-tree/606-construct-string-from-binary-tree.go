/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func tree2str(root *TreeNode) string {
    if root == nil{
        return ""
    }
    left, right := "", ""
    if root.Left != nil{
        left = "(" + tree2str(root.Left) + ")"
    }
    if root.Right != nil{
        left = "(" + tree2str(root.Left) + ")"
        right = "(" + tree2str(root.Right) + ")"
    }
    
    return fmt.Sprintf("%v", root.Val) + left + right
}