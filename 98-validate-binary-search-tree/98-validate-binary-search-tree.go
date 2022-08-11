/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isValidBST(root *TreeNode) bool {
    return DoisValidBST(root, nil, nil)
}


func DoisValidBST(root, min, max *TreeNode) bool{
    /*if n == nil {
        return true
    }
    if min != nil && n.Val <= min.Val {
        return false
    }
    if max != nil && n.Val >= max.Val {
        return false
    }
    return DoisValidBST(n.Left, min, n) && DoisValidBST(n.Right, n, max)
    */
    if root == nil{
        return true
    }
    if min != nil && root.Val <= min.Val{
        return false
    }
    if max != nil && root.Val >= max.Val{
        return false
    }
    return DoisValidBST(root.Left, min, root) && DoisValidBST(root.Right, root, max)
}