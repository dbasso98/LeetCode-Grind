from typing import List

def contains_duplicate(nums:List[int]) -> bool:
	seen = {}
	for num in nums:
		if num not in seen:
			seen[num] = True
		else:
			return True
	return False

# O(n) time complexity, O(n) space complexity (at most n elements in the hashtable if there are no duplicates).

# Pattern:
# Use an hash table to store occurrence of an element, if an element has already been added then return True.
