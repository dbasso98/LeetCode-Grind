from typing import Optional

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
   head = result = ListNode()
   while list1 and list2:
      if list1.val <= list2.val:
         result.next = list1
         list1 = list1.next
      else:
         result.next = list2
         list2 = list2.next
      result = result.next
   result.next = list1 or list2
   return head.next

# O(n) time complexity (where n is the total number of elements of the linked lists), O(1) space complexity.

# Pattern:
# Important, use an empty dummy node to avoid dealing with Nones et al.
# Merge the lists iteratively by comparing current value in each one of those. 
# Iterate until one of the two lists ends, then append the one left (using or operator).
