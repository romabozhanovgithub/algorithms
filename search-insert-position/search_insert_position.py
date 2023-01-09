from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    mid = 0
    l = len(nums) - 1
    
    if nums[0] > target:
        return 0
    elif nums[-1] < target:
        return l + 1
    
    while low <= high:
        mid = (high + low) // 2
        
        if nums[mid] < target:
            low = mid + 1
            if mid + 1 <= l and nums[mid + 1] > target:
                return mid + 1
        elif nums[mid] > target:
            high = mid - 1
            if nums[mid - 1] < target:
                return mid
        else:
            return mid
