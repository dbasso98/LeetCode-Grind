def maxSubArray(nums: List[int]) -> int:
    current_sum = best_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(current_sum+num, num)
        if best_sum < current_sum:
            best_sum = current_sum
    return best_sum

# O(n) time complexity and O(1) space complexity.

# Pattern:
# Kinda sliding window problem. We have to keep track of the best sum we 
# achieved at the i-th index. To compute that we have to compare the actual
# sum with the next number in the array and then update accordingly.
