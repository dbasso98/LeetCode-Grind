def minCostClimbingStairs(self, cost: List[int]) -> int:
    memo = [0 for _ in range(len(cost))]
    memo[0] = cost[0]
    memo[1] = cost[1]
    for index in range(2, len(cost)):
        memo[index] = min(memo[index-1],memo[index-2]) + cost[index]
        
    return min(memo[-1],memo[-2])

# O(n) time and space complexity.
def minCostClimbingStairs(self, cost: List[int]) -> int:
    memo0 = cost[0]
    memo1 = cost[1]
    for index in range(2, len(cost)):
        curr_res = cost[index]+min(memo0,memo1)
        memo0 = memo1
        memo1 = curr_res
        
    return min(memo0,memo1)

# This one uses O(1) space complexity.

# Pattern:
# Dynamic programming is all about finding a pattern. The idea is that we start either
# from the first or the second step, then we always pick the minimum btw the 2 previously
# computed ones and we sum the actual weight.
