def addTwoNumbers(l1, l2):
	carry = 0
	head = result = ListNode()
	while l1 or l2:
		if l1 and l2:
		sum = l1.val + l2.val + carry
		l1, l2 = l1.next, l2.next
	elif l1:
		sum = l1.val + carry
		l1 = l1.next
	else:
		sum = l2.val + carry
		l2 = l2.next
		res, carry = sum%10, sum//10
		result.next = ListNode(val=res)
		result = result.next
	if carry != 0:
		result.next = ListNode(val=carry)
	return head.next

# Or

def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    carry = 0
    head = result = ListNode()
    while l1 or l2 or carry:
        first = l1.val if l1 else 0
        second = l2.val if l2 else 0
        sum = first + second + carry
        res, carry = sum%10, sum//10
        result.next = ListNode(val=res)
        result = result.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return head.next

# Still O(max(length of l1 or l2)) time and space complexity.
		
# Pattern:
# We just have to pay attention until either one of the two lists exist or 
# if the carry is != 0. The remaining part is pretty simple.
