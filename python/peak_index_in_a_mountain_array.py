def peakIndexInMountainArray(arr: List[int]) -> int:
	for i in range (1,len(arr)):
		if arr[i-1] < arr[i] and arr[i]>arr[i+1]:
			return i
	return None

# O(n) time complexity and O(1) space complexity. To get an O(logn) tc?

def peakIndexInMountainArray(arr: List[int]) -> int:
	start, end = 0, len(arr)-1
	while start < end:
		middle = (start+end)//2
		if arr[middle] < arr[middle+1]:
			start = middle + 1
		else:
			end = middle
	return start

# O(logn) complexity.

# Pattern:
# Binary search babyyyyy. We do the binary search based on the fact 
# whether the middle point lies in one part or another of the mountain. 
# Finally we will get to the peak.
