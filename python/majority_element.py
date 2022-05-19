def majorityElement(nums: List[int]) -> int:
	occurrences = {num:0 for num in nums}
	threshold = len(nums)//2
	for num in nums:
		occurrences[num] += 1
		if occurrences[num] > threshold:
			return num
	return None

# O(n) space and time complexity. How to get O(1) space complexity?
# We have to use Moore-Boyle voting algorithm:

def majorityElement(self, nums: List[int]) -> int:
    count = 1
    result = nums[0]
    for i in range(1,len(nums)):
        if nums[i] != result:
            count -= 1
            if count == 0:
                result = nums[i]
                count = 1
        else:
            count += 1
    return result

# Pattern:
# Use a hashmap to count occurrences or Moore-Boyle algorithm,
# i.e. keep track of the element with most occurrences iteratively 
# by using a counter variable and another one to store the actual most common value.
