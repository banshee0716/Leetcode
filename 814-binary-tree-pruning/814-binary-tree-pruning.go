/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func pruneTree(root *TreeNode) *TreeNode {
    if root == nil{
        return nil
    }
    left := pruneTree(root.Left)
    right := pruneTree(root.Right)
    root.Left = left
    root.Right = right
    if left == nil && right == nil{
        if root.Val == 0{
            return nil
        }
    }
    return root
}