class Solution:
    def intToRoman(self, num: int) -> str:
        char_map = { # symbol : value
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        };

        result = ""
        for symbol in char_map:
            value = char_map[symbol]
            count = num // value
            if count:
                result += symbol * count
                num %= value
        
        return result
