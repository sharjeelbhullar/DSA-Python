from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            # Sort the word and use the sorted word as the key
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)

        # The result is the values of the hashmap, which are the anagram groups
        return list(anagram_map.values())