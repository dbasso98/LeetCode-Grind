def binary_search(self, row : List[int], target: int) -> bool:
	start, end = 0, len(row)
	while start < end:
		middle = (start + end)//2
		if row[middle] > target:
			end = middle
		elif row[middle] < target:
			start = middle + 1
		else:
			return True
	return False

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
	start, end = 0, len(matrix)
	columns = len(matrix[0])
	while start < end:
		middle = (start + end)//2
		if target >= matrix[middle][0]:
			if target <= matrix[middle][columns-1]:
				return self.binary_search(matrix[middle], target)
			else:
				start = middle + 1
		else:
			end = middle
	return False

# O(logn+logm) time complexity (nxm matrix) and O(1) space.

# Pattern:
# Do a binary search first on rows, and the targeted column.
			
