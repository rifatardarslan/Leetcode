class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        set1 = set(word1)
        set2 = set(word2)

        if len(word1) != len(word2):
            return False

        if set1 != set2:
            return False

        freq1 = [word1.count(c) for c in set1]
        freq2 = [word2.count(c) for c in set2]

        return sorted(freq1) == sorted(freq2)
