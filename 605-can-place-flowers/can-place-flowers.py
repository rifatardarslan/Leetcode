from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        result = 0
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
                left_empty = (i == 0) or (flowerbed[i-1] == 0)
                right_empty = (i == length-1) or (flowerbed[i+1] == 0)
                
                if left_empty and right_empty:
                    flowerbed[i] = 1 
                    result += 1
            if result >= n: 
                return True
        
        return result >= n
