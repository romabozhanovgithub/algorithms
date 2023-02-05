from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    return sorted(map(lambda x: x**2, nums))
