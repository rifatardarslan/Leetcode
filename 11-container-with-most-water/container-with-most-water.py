from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        low = 0
        high = len(height) - 1

        while low < high:
            distance = high - low
            min_height = min(height[low], height[high])
            area = min_height * distance
            max_area = max(max_area, area)

            if height[low] < height[high]:
                low += 1
            else:
                high -= 1

        return max_area
