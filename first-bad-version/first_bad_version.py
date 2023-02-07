def isBadVersion(version: int) -> bool:
    pass


def firstBadVersion(n: int) -> int:
    start = 0
    end = n
    mid = 0

    while start < end:
        mid = (start + end) // 2
        if isBadVersion(mid):
            end = mid
        else:
            start = mid + 1
    return start
