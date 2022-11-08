/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getDecimalValue(head *ListNode) int {
    out := 0
    for head != nil{
        out = (out*2) +head.Val
        head = head. Next
    }
    return out
}