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


def longestPalindrome(s: str) -> int:
    """
    For each letter, say it occurs v times. We know we have v // 2 * 2 letters
    that can be partnered for sure. For example, if we have 'aaaaa', then we
    could have 'aaaa' partnered, which is 5 // 2 * 2 = 4 letters partnered.

    At the end, if there was any v % 2 == 1, then that letter could have been
    a unique center. Otherwise, every letter was partnered. To perform this
    check, we will check for v % 2 == 1 and ans % 2 == 0, the latter meaning
    we haven't yet added a unique center to the answer.

    In other words:
        If we have an odd number of letters partnered, then we can add one
        unique center to our answer. Otherwise, we cannot.
        Before loop ends, we will add all odd numbers to the pairs and
        if there is still a unique center, existing odd numbers, we will
        add 1 to the answer. But we can add unique center only once, that's
        why we check if unpaired_chars exists, if it does, we add 1 to the
        answer, otherwise we don't.

    Time: O(n)
    Space: O(1)
    """

    pairs = 0
    unpaired_chars = set()
    
    for char in s:
        if char in unpaired_chars:
            pairs += 1
            unpaired_chars.remove(char)
        else:
            unpaired_chars.add(char)
    
    return pairs * 2 + 1 if unpaired_chars else pairs * 2
