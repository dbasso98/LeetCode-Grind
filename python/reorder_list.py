def reorderList(head : Optional[ListNode]) -> None:
	fast = slow = head
	while fast.next and fast.next.next:
		slow = slow.next
		fast = fast.next.next
	# now slow is at the middle of the list
	# let’s revert the second part of the list
	prev, curr = None, slow.next
	while curr:
		next_node = curr.next
		curr.next = prev
		prev = curr
		curr = next_node
	slow.next = None
	# now we have to merge the two lists (that are unsorted)
	while prev:
		next_head = head.next
		head.next = prev
		head = prev
		prev = next_head

# Pattern:
# 3 steps here, first find the middle of the list, then revert the second half and finally merge the two linked lists by alternating positions.
