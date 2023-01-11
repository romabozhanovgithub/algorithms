def lengthOfLastWord(s: str) -> int:
    k = -1
    for i in range(-1, -(len(s) + 1), -1):
        if s[i].isspace():
            if k != -1:
                return k
        else:
            if k == -1:
                k = 0
            k += 1
    return k
