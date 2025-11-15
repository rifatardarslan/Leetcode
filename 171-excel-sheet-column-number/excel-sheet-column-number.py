class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = 0

        for title in columnTitle:
            value = alphabet.index(title) + 1 
            result = result * 26 + value

        return result