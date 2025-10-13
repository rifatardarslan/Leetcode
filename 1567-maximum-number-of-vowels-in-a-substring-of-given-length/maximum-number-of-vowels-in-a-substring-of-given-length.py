class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"} 
        max_sum = 0
        window_sum = 0

        for i in range(k):
            if s[i] in vowels:
                window_sum += 1
        max_sum = window_sum

        for i in range(k, len(s)):
            if s[i - k] in vowels:   
                window_sum -= 1
            if s[i] in vowels:       
                window_sum += 1
            max_sum = max(max_sum, window_sum)

        return max_sum
