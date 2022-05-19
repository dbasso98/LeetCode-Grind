from typing import List

def findDuplicate(nums: List[int]) -> int:
    slow , fast = nums[0], nums[nums[0]]
    base = 0
    # first detect the cycle (think the list as a linked one, values contained in the index are the “next” node)
    while fast != slow:
        slow, fast = nums[slow], nums[nums[fast]]
    # now we need to find the duplicated number
    while base != slow:
        base, slow = nums[base], nums[slow]
    return base

# O(n) time complexity and O(1) space complexity.

# Pattern:
# Think the array as a linked list, every node points to the element contained at position k, 
# where k is the value contained by the element of the array. 
# Now detect the cycle and find the first component of the cycle.
