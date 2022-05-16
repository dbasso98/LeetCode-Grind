def climbStairs(n: int) -> int:
    result = 1
    prev = 0
    for _ in range(n-1):
        prev, result = result, result+prev
    return result

# O(n) time complexity and O(1) space complexity.
