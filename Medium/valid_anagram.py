from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)  # Initialize defaultdict with list
        res = []
        for s in strs:
            sk = tuple(sorted(s))  # Sort characters in the string and use as key
            hm[sk].append(s)       # Append the string to the list for this key
        for value in hm.values():
            res.append(value)      # Collect all anagram groups
        return res
