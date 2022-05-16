def binarySearch(nums, target):
	start = 0
	end = len(nums) - 1
	while start <= end:
		middle = start + (end-start)//2
		if nums[middle] == target:
			return middle
		elif nums[middle] < target:
			start = middle + 1
		else:
			end = middle - 1
	return -1

# Pattern:
# Two pointers. Look at the middle of the array, then make a comparison with target and visited value. 
# Move the pointers accordingly.

