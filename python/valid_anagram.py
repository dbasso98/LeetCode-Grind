def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    letters = {}
    for letter in s:
        if letter in letters:
                letters[letter] += 1
        else:
            letter = 0
        for letter in t:
            if letter in letters:
                letters[letter] -= 1
            else:
                return False
        for letter, occurrence in letters.items():
            if occurrence != 0:
                return False	
    return True

# Time complexity is O(n) and space complexity is O(1) since the size of the hashmap can be at most 26 (n. of letters in the alphabet).

# Pattern:
# Store every char occurrence of s in a hashmap and then decrease by one the value 
# if the letter is also present in t, then if any of the values of the hashmap is != 0, 
# t and s are not anagrams.

