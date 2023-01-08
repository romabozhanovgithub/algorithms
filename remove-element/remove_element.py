from typing import List


def removeElement(nums: List[int], val: int) -> int:
    k = 0
    for i in nums:
        if i == val:
            k += 1
    
    for i in range(k):
        nums.remove(val)
        nums.append(None)
        
    return len(nums) - k
