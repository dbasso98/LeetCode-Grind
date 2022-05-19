def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

# O(n) time complexity and O(1) space complexity.

# Pattern:
# Two pointers, make slow start at distance n from fast and then 
# just remove the node pointed by slow.next. Note, if fast has 
# reached the end after n steps then this means that you have to remove the first element.
