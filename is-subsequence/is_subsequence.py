def isSubsequence(s: str, t: str) -> bool:
    if len(s) > len(t):
        return False
    elif len(s) == 0:
        return True

    match = 0
    for i in range(len(t)):
        if s[match] == t[i]:
            match += 1
        if match == len(s):
            return True
    return False
