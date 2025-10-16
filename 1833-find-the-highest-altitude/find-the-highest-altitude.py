class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height = 0
        max_height = 0
        
        for i in gain:
            height += i          
            max_height = max(max_height, height)  
        
        return max_height
