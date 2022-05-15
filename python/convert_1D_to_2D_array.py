from typing import List

def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
	return [original[i*n:(i+1)*n] for i in range(m)] if len(original) == m*n else []

# O(m*n) time complexity, O(m*n) space complexity since we have to allocate that space for the 2D array.

# Pattern:
# Just create a 2D array from a 1D array as explained in the description by using a for loop.
