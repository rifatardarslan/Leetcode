class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tmp = int(''.join(map(str, digits)))
        
        res = tmp + 1

        res = [int(ch) for ch in str(res)]

        return res