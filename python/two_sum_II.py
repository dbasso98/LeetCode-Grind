def twoSum(self, numbers: List[int], target: int) -> List[int]:
    end = len(numbers)-1
    start = 0
    diff = target - numbers[end]
    while end > 0 and numbers[end-1] >= diff:
        while numbers[start] <= diff:
            if numbers[end] + numbers[start] == target:
                return [start+1, end+1]
            else:
                start += 1
        end -= 1
        diff = target - numbers[end]
    return None

# Better but still there is O(n) possible time complexity.

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    end = len(numbers)-1
    start = 0
    while start < end:
        res = numbers[start]+numbers[end]
        if res == target:
            return [start+1,end+1]
        if res > target:
            end -= 1
        else:
            start += 1

# Pattern:
# Two pointers, one starts at index 0 and the other one at the end of the array.
# Since the input is ordered we can compare the sum of numbers pointed by the 
# pointers with the target and then move one of the pointers accordingly.
