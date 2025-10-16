class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        set_arr = set(arr)
        counts = []
        
        for i in set_arr:
            freq = arr.count(i)
            if freq in counts:
                return False
            else:
                counts.append(freq)
                
        return True
            
