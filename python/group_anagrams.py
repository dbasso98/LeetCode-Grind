def product(self, string : str) -> int:
    result = 1
    for letter in string:
        result *= ord(letter)
    return result
    
def occurrences(self, string : str) -> List[int]:
    result = [0]*26
    for letter in string:
        result[ord(letter)-ord('a')] += 1
    return result


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams_store = {}
    for index, string in enumerate(strs):
        """
        if (self.product(string), len(string)) not in anagrams_store:
            anagrams_store[(self.product(string), len(string))] = [string]
        else:
            anagrams_store[(self.product(string), len(string))].append(string)
        """
        occurr = self.occurrences(string)
        if tuple(occurr) not in anagrams_store:
            anagrams_store[tuple(occurr)] = [string]
        else:
            anagrams_store[tuple(occurr)].append(string)
        
    return list(anagrams_store.values())


# Time complexity and space complexity are O(n*k) where n is the length of strs and k is the maximum length of a string contained in strs.
# We can also count occurrences and then we have the same result.

# Pattern:
# For every word in strs, compute the array of the occurrences and put it in a hashmap that will store every anagram.
