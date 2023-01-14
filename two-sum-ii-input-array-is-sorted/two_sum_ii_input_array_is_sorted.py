from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    if len(numbers) <= 2:
        return [1, 2]
    start = 0
    end = len(numbers) - 1
    while end >= start:
        if numbers[start] + numbers[end] > target:
            end -= 1
        elif numbers[start] + numbers[end] < target:
            start += 1
        else:
            return [start + 1, end + 1]
