from typing import Optional

def hasCycle(head : Optional[ListNode]) -> bool:
    visited = {}
    while head:
        if head in visited:
            return True
        else:
            visited[head] = True
            head = head.next
    return False

# This has O(n) time complexity and O(n) space complexity since we are allocating a new hashtable.
# How to get O(1) space complexity?

def hasCycle(head : Optional[ListNode]) -> bool:
	slow = fast = head # starting from head
	while fast and fast.next: # until we point to None
		slow = slow.next
		fast = fast.next.next
		if fast is slow:
			return True
	return False

# In this way we have O(1) space complexity.

# Pattern:
# Use two pointers, one slow that is moving one position at a time, the other fast that moves 2 positions at a time. If they meet, then return the element pointed by one of the two, otherwise if fast has reached the end of the array then no there are no cycles.
