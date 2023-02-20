"""
You are given a sorted array consisting of only integers where
every element appears exactly twice, except for one element which
appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.
"""

from typing import List


def singleNonDuplicateV1(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    low = 0
    high = -1
    while low <= high:
        if nums[low] != nums[low + 1]:
            return nums[low]
        elif nums[high] != nums[high -  1]:
            return nums[high]
        low += 2
        high -= 2
    return -1
