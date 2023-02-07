from typing import List


def searchV1Recursive(nums: List[int], target: int) -> int:
    def binarySearch(low: int, high: int) -> int:
        if low > high:
            return -1

        mid = (low + high) // 2

        if nums[mid] < target:
            return binarySearch(mid + 1, high)
        elif nums[mid] > target:
            return binarySearch(low, mid - 1)
        else:
            return mid

    return binarySearch(0, len(nums) - 1)


def searchV2Iterative(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid

    return -1
