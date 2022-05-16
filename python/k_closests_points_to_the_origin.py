import math, heapq

def distance(self, a:List[int]) -> float:
     return math.sqrt(a[0]*a[0]+a[1]*a[1])
        
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    heap = []
    for coords in points:
        heap.append(self.distance(coords),coords)
    heapq.heapify(heap)
    result = []
    while k > 0:
        result.append(heapq.heappop(heap)[1])
        k -= 1
    return result 

# Time complexity is O(n+klogn) and space complexity is O(n+k) (we can also drop the math.sqrt to speed-up computations)

# Pattern:
# K-something, then use a heap! In this case we use a minheap to store the tuple of distance and coords of k closest points.
