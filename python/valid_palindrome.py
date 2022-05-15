from os import re

def isPalindrome(s : str) -> bool:
    s = re.sub("[^A-Za-z0-9]","",s.lower())
    mid_index = round(len(s)/2)
    for index in range(0, mid_index):
        if s[index] != s[-index-1]:
            return False
    return True

# O(n) time complexity but O(n) space complexity since we are creating a new array of 
# size smaller than n with all special chars excluded and lowercase. 
# An in place solution can be:

def isPalindrome(s : str) -> bool:
    start, end = 0, len(s)-1
    while (start <= end):
        if not s[start].isalnum():
            start += 1
            continue
        elif not s[end].isalnum():
            end -= 1
            continue
        if s[start].lower() != s[end].lower():
            return False
        else:
            start += 1
            end -= 1
    return True

# Now everything is done in place so space complexity is O(1).

# Pattern:
# Use two pointers! One pointing to index 0 and the other to the last character of the string. 
# Then iteratively move both towards the middle position by always checking that they are pointing to the same char.
