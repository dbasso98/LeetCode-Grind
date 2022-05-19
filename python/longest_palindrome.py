def longestPalindrome(s: str) -> int:
    occurrences = {}
    for letter in s:
        occurrences[letter] = occurrences.get(letter,0) + 1
    length = 0
    at_least_one_element_remaining = False
    for key, occurr in occurrences.items():
        if occurr%2 == 0:
            length += occurr
        else:
            length += occurr-1
            at_least_one_element_remaining = True

    return length if not at_least_one_element_remaining else length+1

# O(n) and O(n) space complexity.

# Pattern:
# Basically we have to take care of the odd occurrences. First compute overall occurrences as usual. 
# Then, we’re gonna add to the palindrome all the even occurrences and all the odd 
# ones (always subtracting by 1 to make them even) and then if at least one odd occurrence has been added we can sum 1 to the result.
