"""
Given two strings s and p, return an array of all the start indices
of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of
a different word or phrase, typically using all the original letters
exactly once.
"""


from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    # sliding window -> substring with same set of freq of chars
    ans = []
    # cnt_s: store frequency of characters in s
    # cnt_p: store frequency of characters in p
    cnt_s, cnt_p = [0] * 26, [0] * 26
    n, m = len(s), len(p)
    j = 0
    # count frequency of characters in p
    for x in p:
        cnt_p[ord(x) - ord('a')] += 1
    for i in range(n):
        # add s[j] to the window if the window is not full
        while j < n and j - i + 1 <= m:
            cnt_s[ord(s[j]) - ord('a')] += 1
            j += 1
        # check if both frequency matches
        if cnt_s == cnt_p:
            # i is the starting index of the window
            ans.append(i)
        # remove the leftmost element from the window
        cnt_s[ord(s[i]) - ord('a')] -= 1
    return ans
