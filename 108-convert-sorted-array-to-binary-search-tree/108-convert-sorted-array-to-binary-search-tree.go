/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sortedArrayToBST(nums []int) *TreeNode {
    if len(nums) == 0{
        return nil
    }
    mid := (len(nums)-1)/2
    node := &TreeNode{} //創建treenode結構的節點
    node.Val = nums[mid]
    node.Left = sortedArrayToBST(nums[:mid])
    node.Right = sortedArrayToBST(nums[mid+1:])
    
    return node
}