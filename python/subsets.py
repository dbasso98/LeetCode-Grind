def subsets(nums: List[int]) -> List[List[int]]:
	subsets = [[]]
	for num in nums:
		subsets += [subset+[num] for subset in subsets]
	return subsets

# Time complexity is O(n*2^n) and space is O(2^n).

# To do this with backtracking we had to think about the possible decision tree. Basically at each step we decide whether to include or not the ith number in the subset of possible solutions.

def subsets(nums: List[int]) -> List[List[int]]:
	result = []
	subset = []
	def dfs(index):
		if index >= len(nums):
			result.append(subset.copy())
			return
		# decided to include the current number
		subset.append(nums[index])
		dfs(index+1)
		# decided to not include it
		subset.pop()
		dfs(index+1)
	dfs(0)
	return result

# Pattern:
# All possible combinations means recursion. Still we can do it iteratively by adding one at a time the i-th number 
# and keeping all the previously computed combinations in the resulting array.
