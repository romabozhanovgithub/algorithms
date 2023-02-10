def fibV1Recursive(n: int) -> int:
    if n <= 1:
        return n
    return fibV1Recursive(n - 1) + fibV1Recursive(n - 2)


def fibV2Iterative(n: int) -> int:
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b
