def helper(self, nums, remainder, result):
    if len(nums) == 0:
        result.append(remainder)
        return
    for i in range(len(nums)):
        self.helper(nums[:i]+nums[i+1:],remainder+[nums[i]], result)	

def permute(self, nums: List[int]) -> List[List[int]]:
	result = []
	self.helper(nums,[],result)
	return result

# Complexity is O(n!).

# Pattern:
# Backtracking, so write a decision tree. The idea is to iteratively 
# subdivide nums in subarrays by adding one at a time the i-th element 
# to the remainder and removing it from nums (that contains the numbers 
# that have not been placed in remainder yet). 

