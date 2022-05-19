def threeSum(self, nums: List[int]) -> List[List[int]]:
    n = len(nums)
    if n < 3:
        return []
    nums.sort()
    result = []
    for i in range(n-2):
        start, end = i+1, n-1
        while start < end:
            sum = nums[i]+nums[start]+nums[end]
            if sum > 0:
                end -= 1
            elif sum < 0:
                start += 1
            else:
                result.append([nums[i],nums[start],nums[end]])
                while start < end and nums[start]==nums[start+1]:
                    start += 1
                while start < end and nums[end]==nums[end-1]:
                    end -= 1
                start+=1
                end-=1
    return result

# Time complexity is O(n^2) while space complexity is O(n) or O(1) since we are sorting the array.

# Pattern:
# Sort the array and then use two pointers! We’re going to iterate through the 
# entire array and use the two pointers on the second part of the array to find 
# the values that summed all together are equal to 0. Pay attention to avoid 
# duplicate triplets by ignoring repeated values.
