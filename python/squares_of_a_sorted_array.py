def sortedSquares(nums: List[int]) -> List[int]:
    result = [0]*len(nums)
    left, right = 0, len(nums)-1
    current_index = len(nums)-1
    while left <= right:
        if abs(nums[left]) >= abs(nums[right]):
            result[current_index] = nums[left]**2
            left += 1
        else:
            result[current_index] = nums[right]**2
            right -= 1
        current_index -= 1
    return result

# Time complexity is O(n) and space complexity is O(n).

# Pattern:
# Two pointers, one starting from the beginning and the other from the end. 
# Always compare absolute values and properly place the elements in the resulting array.
