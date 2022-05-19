def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# O(n) time complexity and O(1) space complexity.

# Pattern:
# Use two pointers, fast and slow, when the faster one reaches the end 
# of the linked list then the slower one will be exactly pointing at the middle of the list.
