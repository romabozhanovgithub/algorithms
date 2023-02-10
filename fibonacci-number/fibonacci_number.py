def fibV1Recursive(n: int) -> int:
    if n <= 1:
        return n
    return fibV1Recursive(n - 1) + fibV1Recursive(n - 2)
