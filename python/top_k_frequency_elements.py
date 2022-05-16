import heapq
from collections import Counter

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    occurrencies = {num: 0 for num in nums}
    for num in nums:
        occurrencies[num] += 1
    heap = [(-value,key) for key, value in occurrencies.items()]
    heapq.heapify(heap)
    result = []
    while k > 0:
        result.append(heapq.heappop(heap)[1])
        k -= 1
    return result

# O(n) to build the hashmap, O(n) to build the maxheap, O(klogn) to extract
# the results ---> O(n+klogn) time complexity. O(n) space complexity.
# To do everything in linear time we can use bucket sort!

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    bucket_arr = [[] for i in range(len(nums)+1)]
    for num, value in count.items():
        bucket_arr[value].append(num)
    result = []
    for bucket in bucket_arr[::-1]:
        for el in bucket:
            result.append(el)
            if len(result) == k:
                return result

# Pattern:
# K something, use a heap! Otherwise what we can do is to use Bucket sort in which the 
# auxiliary array contains elements with the same frequency, then extract last k elements.
