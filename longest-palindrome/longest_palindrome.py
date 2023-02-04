def longestPalindrome(s: str) -> int:
    letters = {}
    res = 0
    max_odd = 0
    for i in range(len(s)):
        if s[i] not in letters:
            letters[s[i]] = 0
        letters[s[i]] += 1

    for value in letters.values():
        if value % 2 == 0:
            res += value
        elif value > max_odd:
            if max_odd > 0:
                res += max_odd - 1
            max_odd = value
        else:
            res += value - 1
    res += max_odd
    return res
