class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_index = 0  
        t_len = len(t)

        for char in s:  
            found = False
            for j in range(t_index, t_len):
                if t[j] == char:
                    t_index = j + 1
                    found = True
                    break
            if not found:
                return False

        return True
