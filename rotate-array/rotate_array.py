from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    l = len(nums)
    k = k % l
    nums[:]=nums[l-k:]+nums[:l-k]
