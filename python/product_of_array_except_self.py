from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    products = [nums[0]]
    reversed_products = [nums[-1]]
    for index in range(1, len(nums)):
        products.append(products[-1]*nums[index])
        reversed_products.append(reversed_products[-1]*nums[-(index+1)])
    reversed_products = reversed_products[::-1]
    answer = [reversed_products[1]]
    for index in range(1, len(nums) - 1):
        answer.append(products[index - 1]*reversed_products[index+1])
    answer.append(products[-2])
    return answer

# O(n) time complexity, but O(n) space complexity, can be for sure improved.
# Follow up is to reduce space complexity to O(1), let’s see:

def productExceptSelf(nums: List[int]) -> List[int]:
	answer = [1] * len(nums)
	actual_product = 1
	reversed_product = 1
	for index in range(0,len(nums)):
		answer[index] *= actual_product
		answer[-(index+1)] *= reversed_product
		actual_product *= nums[index]
		reversed_product *= nums[-(index+1)]
	return answer

# Now space complexity is O(1)!

# Pattern:
# Initialize one array of ones, by avoiding to immediately multiply the 1st and last element 
# and then multiplying in both forward and reverse direction the ones array by ith and -ith element we get the result.
