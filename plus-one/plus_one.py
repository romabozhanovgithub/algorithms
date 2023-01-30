from typing import List


def plusOne(digits: List[int]) -> List[int]:
    if digits[-1] < 9:
        digits[-1] += 1
        return digits

    for i in range(1, len(digits) + 1):
        if digits[-i] < 9:
            digits[-i] += 1
            return digits
        else:
            if -i == -len(digits):
                digits[-i] = 1
                digits.append(0)
                return digits
            digits[-i] = 0
