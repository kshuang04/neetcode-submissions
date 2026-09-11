class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            encoded_str = ""
            for c in s:
                encoded_str += chr(ord(c) + 1)
            result += str(len(s)) + "#" + encoded_str

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            encoded_str = s[j + 1: j + 1 + length]

            decoded_str = ""
            for c in encoded_str:
                decoded_str += chr(ord(c) - 1)

            result.append(decoded_str)

            i = j + 1 + length
        
        return result