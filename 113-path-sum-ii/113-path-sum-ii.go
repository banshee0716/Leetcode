/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func pathSum(root *TreeNode, sum int) [][]int {
	res, path := [][]int{}, []int{}
	var helper func(*TreeNode, int)

	helper = func(node *TreeNode, sum int) {
		if node != nil {
			// Add the current node value to the path
			path = append(path, node.Val)
			if node.Left == nil && node.Right == nil && node.Val == sum {
				// Create a copy so changes to path variable will not affect res
				tmp := make([]int, len(path))
				copy(tmp, path)
				res = append(res, tmp)
			}
			helper(node.Left, sum-node.Val)
			helper(node.Right, sum-node.Val)
			// Remove the node from path after processing it
			path = path[0 : len(path)-1]
		}
	}

	helper(root, sum)
	return res
}