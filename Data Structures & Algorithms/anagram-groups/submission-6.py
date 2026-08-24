class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} # sorted string: list of anagrams

        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
        
        result = []
        for l in anagrams.values():
            result.append(l)
        
        return result