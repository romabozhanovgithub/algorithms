"""
You are given a string s and an integer k. You can choose any character of
the string and change it to any other uppercase English character. You can
perform this operation at most k times.

Return the length of the longest substring containing the same letter you
can get after performing the above operations
"""

def characterReplacement(s: str, k: int) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    if len(s) <= k:
        return len(s)
    max_count = 0
    max_length = 0
    start = 0
    end = 0
    char_count = {}
    while end < len(s):
        char_count[s[end]] = char_count.get(s[end], 0) + 1
        max_count = max(max_count, char_count[s[end]])
        while end - start + 1 - max_count > k:
            char_count[s[start]] -= 1
            start += 1
        max_length = max(max_length, end - start + 1)
        end += 1
    return max_length
