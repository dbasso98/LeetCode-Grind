from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    complement_ = {}
    for index, num in enumerate(nums):
        complement = target-num
        if complement in complement_:
            return [index, complement_[complement]]
        else:
            complement_[num] = index
            
    return None

# O(n) time complexity, O(n) space complexity

# Pattern:
# Use an hash table to lookup for the complementary of the number placed in the i-th position of the original array. 
# If still the complementary has not been added, then add it to the hash table and as a value put the index equal to the i-th position.
