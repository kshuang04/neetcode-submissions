class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for string in strs:
            sorted_str = "".join(sorted(string))

            if sorted_str not in hash_map:
                hash_map[sorted_str] = [string]
            else:
                hash_map[sorted_str].append(string)
        
        return list(hash_map.values())