class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {} # sorted string : list of anagrams

        for s in strs:
            s_sorted = "".join(sorted(s))

            if s_sorted in hash_map:
                hash_map[s_sorted].append(s)
            else:
                hash_map[s_sorted] = [s]
        
        result = []

        for l in hash_map.values():
            result.append(l)

        return result