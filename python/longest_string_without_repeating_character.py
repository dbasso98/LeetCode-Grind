def lengthOfLongestSubstring(s: str) -> int:
    window = {}
    start = maxLength = 0
    for i, letter in enumerate(s):
        if letter in window and start <= window[letter]:
            start = window[letter] + 1
        else:
            maxLength = max(maxLength, i - start + 1)
            window[letter] = i        
    return maxLength

# O(n) time and O(k) space complexity, if k is the max size of the window.

# Pattern:
# Sliding window, if the char has not been seen inside the window then we just increase its size and add the letter to the window. 
# Otherwise we move our window by putting the start right after the second last occurrence of the repeated char.

