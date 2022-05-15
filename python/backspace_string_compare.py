def backspaceCompare(s: str, t: str) -> bool:
    resulting_s = []
    resulting_t = []
    for el in s:
        if el is '#':
            if resulting_s:
                resulting_s.pop()
            else:
                continue
        else:
            resulting_s.append(el)
    for el in t:
        if el is '#':
            if resulting_t:
                resulting_t.pop()
            else:
                continue
        else:
            resulting_t.append(el)
    
    return resulting_t == resulting_s

# We can create a function for the duplicated code.
# Time complexity is O(len(s)+len(t)) since we need to scan all elements of the strings 
# and do append or pop operations (which take constant time).
# Space complexity overall is same, because it might be the case that we add all the elements to the stacks if no # appear.

def backspaceCompare(s: str, t: str) -> bool:
    i, j = len(s), len(t)
    while i >= 0 and j >= 0:
        skipper = 1
        while skipper > 0:
            i -= 1
            skipper += 1 if s[i] is '#' and i >= 0 else -1
        skipper = 1
        while skipper > 0:
            j -= 1
            skipper += 1 if t[j] is '#' and j >= 0 else -1
        if i >= 0 and j >= 0 and s[i] != t[j]:
            return False

    return i<0 and j<0

# Pattern:
# Either use a stack to store the letters and pop when encountering a #, 
# or use two pointers, and start by the end of the word to scan both words.
