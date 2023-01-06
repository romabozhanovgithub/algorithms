from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        
        d = {}
        
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
