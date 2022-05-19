def countBits(self, n: int) -> List[int]:
    result = [0]*(n+1)
    for i in range (1,n+1):
        if i%2 == 0:
            result[i] = result[i//2]
        else:
            result[i] = result[i-1] + 1
    return result

# O(n) time complexity and O(1) space complexity.

# Pattern:
# For every power of 2 the number of ones will be 1. We can use memoization to store this concept. 
# For the other numbers instead we notice that the number of ones is the same as for the previous number plus one.
