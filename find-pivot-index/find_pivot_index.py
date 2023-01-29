from typing import List


def pivotIndex(nums: List[int]) -> int:
    nums_sum = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        if left_sum == (nums_sum - left_sum - nums[i]):
            return i
        left_sum += nums[i]
    return -1