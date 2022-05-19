def canConstruct(ransomNote: str, magazine: str) -> bool:
	ransomNote_occurr = {letter:0 for letter in ransomNote}
	for letter in ransomNote:
		ransomNote_occurr[letter] += 1
	for letter in magazine:
		if letter in ransomNote_occurr:
			ransomNote_occurr[letter] -= 1
	return all([value <= 0 for _, value in ransomNote_occurr.items()])

# Time complexity is O(n) to build first dict, then O(n+m) for the 2 for loops and finally O(n) to get the result, so overall is O(n+m). Space complexity is O(n). n is len(ransomNote) and m is len(magazine). Faster:

def canConstruct(ransomNote: str, magazine: str) -> bool:
    for letter in set(ransomNote):
        if ransomNote.count(letter) > magazine.count(letter):
            return False
    return True

# Pattern:
# Just use hashmap to store occurrences and make proper comparisons.
