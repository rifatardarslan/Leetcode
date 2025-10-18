class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        result = []

        def binary_search_first_ge(target):
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if potions[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        for s in spells:
            required = success / s
            idx = binary_search_first_ge(required)
            count = n - idx  
            result.append(count)

        return result
