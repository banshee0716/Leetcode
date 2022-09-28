/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    dummy := &ListNode {-1, head}
    cur, prev := dummy, dummy
    for cur.Next != nil{
        if n <= 0 {
            prev = prev.Next
        }
        cur = cur.Next
        n -= 1
    }
    nthNode := prev.Next
    prev.Next = nthNode.Next
    
    return dummy.Next
}