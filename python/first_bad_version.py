def firstBadVersion(self, n: int) -> int:
    start, end = 1, n
    while start < end:
        middle = (start+end)//2
        if isBadVersion(middle):
            end = middle
        else:
            start = middle + 1
    return start

# O(logn) easy peasy binary search.

# Pattern:
# Just do a binary search depending on the fact that the item in the middle is bad or not.
