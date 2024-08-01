/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func middleNode(head *ListNode) *ListNode {

//     fast, slow := head, head
    
//     for fast != nil && fast.Next != nil {
//         slow = slow.Next
//         fast = fast.Next.Next
//     }
    
//     return slow
    
// 2nd ...
    
    tmp := [100]*ListNode{}
    count := 0
    
    for head != nil {
        tmp[count] = head
        head = head.Next
        count ++
    }
    
    return tmp[count/2]
}