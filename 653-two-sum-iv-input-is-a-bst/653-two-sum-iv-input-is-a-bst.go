/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findTarget(root *TreeNode, k int) bool {
    return dfs(root, k, map[int]bool{})
}
func dfs(root *TreeNode, k int, m map[int]bool) bool{
    if root == nil{
        return false
    }
    if m[k-root.Val]{
        return true
    }
    m[root.Val] = true
    return dfs(root.Left, k ,m) || dfs(root.Right, k ,m)
}