/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getDecimalValue(head *ListNode) int {
    var out int	
    for head != nil{
        out <<= 1
        out |= head.Val
        head = head. Next
    }
    return out
}