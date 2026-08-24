class Solution:
    def intToRoman(self, num: int) -> str:
        map = {
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
        }

        result = ""
        for symbol in map:
            count = num // map[symbol]
            result += symbol * count
            num %= map[symbol]
        
        return result
