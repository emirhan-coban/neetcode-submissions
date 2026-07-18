class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for kelime in strs:
            anahtar = ''.join(sorted(kelime))
            if anahtar not in groups:
                groups[anahtar] = []
            groups[anahtar].append(kelime)
        return list(groups.values())