class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
        sList =list(s)
        result = 0

        for i in range(len(sList)):
            if i + 1 < len(sList) and dictionary[sList[i]] < dictionary[sList[i + 1]]:
                result -= dictionary[sList[i]]
            else:
                result += dictionary[sList[i]] 
        
        return result
