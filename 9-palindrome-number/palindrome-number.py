class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x < 10:
            return True
        
        reversedNum = 0
        orig = x

        while x != 0:
            digit = x % 10
            reversedNum = reversedNum * 10 + digit
            x //= 10

        return orig == reversedNum
