class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            # Sort the string to use as a key — all anagrams sort to the same key
            key = ''.join(sorted(s))
            groups[key].append(s)
        return list(groups.values())