import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        if nums:
            self.build_heap(nums)
            
    def build_heap(self, nums):
        heapq.heapify(nums)
        self.heap = nums
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

# Time complexity to build the heap is O(n) thanks to heapify, 
# then when we perform add the time complexity is logn for the push and O(1)
# for the while loop (since it gets executed at most once and pop_min costs O(logk), 
# we keep heap always of size k)---> The overall time complexity is O(N) to construct the heap, O(nlogn) for trimming the size of the heap, O(M*logk) for the add, if add is done M times .
# Space complexity is O(n) since we create a heap of size n.

# Pattern:
# Build a min heap of size k and keep that size even when adding elements. 
# To always get the kth min element when adding just return it (it is the root).
