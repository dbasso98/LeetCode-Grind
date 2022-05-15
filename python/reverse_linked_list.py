from typing import Optional

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    while head is not None:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    
    return prev

# This is the iterative one, O(n) time complexity since we need to traverse the entire list, 
# O(1) space complexity since the reversal is done in place.

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head
    rest = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return rest

# This instead is the recursive solution, O(n) time complexity but here we have instead O(n) space complexity (due to the n recursive calls).

# Pattern:
# Store two nodes, previous and currently visited. 
# Then just reverse the list by iteratively making the current node pointing to the previous one 
# (to do so store current.next that will be the next current node).

