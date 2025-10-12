from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = {}
        operations = 0

        for num in nums:
            complement = k - num
            if complement in count and count[complement] > 0:
                operations += 1
                count[complement] -= 1
            else:
                count[num] = count.get(num, 0) + 1

        return operations
