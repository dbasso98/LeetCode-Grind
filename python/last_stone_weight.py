import heapq

def exist_left_root_child(self, stones):
    return len(stones) > 1
    
def lastStoneWeight(self, stones: List[int]) -> int:
    stones = [-el for el in stones]
    heapq.heapify(stones)
    while self.exist_left_root_child(stones):
        s1 = heapq.heappop(stones)
        s2 = heapq.heappop(stones)
        if s1 != s2:
            heapq.heappush(stones,s1-s2)
    return 0 if not stones else -stones[0]

# Time complexity is O(nlogn) while space complexity is O(n).

# Pattern:
# Build a maxheap from the input array, then until there are 
# at least 2 stones smash them (popping the 2 values) 
# and then add the resulting value to the maxheap.
