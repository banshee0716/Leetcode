/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func isPalindrome(head *ListNode) bool {
    slow, fast := head, head
    for fast != nil && fast.Next != nil{
        slow = slow.Next
        fast = fast.Next.Next
    }
    // skip central node if length of linked list is odd number
    if fast != nil{
        slow = slow.Next
    }
     // Reverse the linkage of right half of linked list
    tail := reverseLinkedList(slow)
    for tail != nil{
        if tail.Val != head.Val{
            return false
        }
        head, tail = head.Next, tail.Next
    }
    return true
}

func reverseLinkedList(node *ListNode) *ListNode{
    var pre *ListNode = nil
    var cur *ListNode = node
    for cur != nil{
        nextHop := cur.Next
        cur.Next = pre
        pre = cur
        cur = nextHop
    }
    return pre
}