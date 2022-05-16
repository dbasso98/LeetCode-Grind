def characterReplacement(s: str, k: int) -> int:
    left = max_length = 0
    count = {}
    for right in range(len(s)):
        if s[right] not in count:
            count[s[right]] = 1
        else:
            count[s[right]] += 1
        if (right-left+1)-max(count.values()) > k:
            count[s[left]] -= 1
            left += 1
        max_length = max(max_length,right-left+1)
    return max_length

# O(n) time compleity and O(26) ---> O(1) space complexity.

# Pattern:
# Sliding window, record occurrences of every char inside the window, if the number of elements that can be modified becomes greater than k decrease by one the occurrence of the character and increase by one the start pointer. Otherwise just compute the new length of the window.
