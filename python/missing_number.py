from typing import List

def missing_number(nums:List[int]) -> int:
	return sum(range(len(nums)+1)) - sum(nums)

# O(n) time complexity since the sum of n numbers is done in O(n) time, 
# space complexity is O(n) since we are constructing a list using range(max_num+1). 
# To avoid that, we know that the sum of n numbers is n*(n+1)/2. 
# Then the space complexity is reduced to O(1)

def missing_number(nums:List[int]) -> int:
	return len(nums)*(len(nums)+1)//2 - sum(nums)

# Pattern:
# Sum all the values in the array and subtract the result to the sum of 1,len(nums)+1 numbers.

