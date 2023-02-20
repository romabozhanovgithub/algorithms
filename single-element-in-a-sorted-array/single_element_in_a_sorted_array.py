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


def singleNonDuplicateV2(nums: List[int]) -> int:
    # Initialize left and right bounds for binary search
    l, r = 0, len(nums) // 2 
    ans = -1
    
    # Binary search loop
    while l <= r: 
        # Calculate the middle between left and right bound
        mid = (l + r) // 2
        # Multiply the middle by 2 as each pair is represented by 2 elements in the array
        idx = mid * 2
        
        # If the selection is outside of the number of elements in the array or if the current element does not equal it's pair
        if idx + 1 >= len(nums) or nums[idx] != nums[idx + 1]:
            # Decrease the right bound
            r = mid - 1
            # Set the ans to the value at the index
            ans = nums[idx]
        # The current element equals it's pair
        else:
            # Increase the left bound
            l = mid + 1
    # Return ans
    return ans
    
