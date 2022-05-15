from typing import List

def contains_duplicate(nums:List[int], k:int) -> bool:
	seen = {}
	for index, num in enumerate(nums):
		if num in seen and index - seen[num] <= k:
			return True
		seen[num] = index
	return False


# O(n) time complexity, O(n) space complexity at most. We don’t need the abs since we are always looking at previous positions (not next ones).

# Pattern:
# Use an hash table to store the position of a number in the array. Then if it is already present and the difference between the actual number and the stored one is inside the k range return True.
