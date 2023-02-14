"""
Given two strings s and t, return true if they are equal when both are typed
into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""


def backspaceCompare(s: str, t: str) -> bool:
    s = list(s)
    t = list(t)
    i = 0
    while i < len(s):
        if s[i] == "#":
            if i == 0:
                s.pop(i)
            else:
                s.pop(i)
                s.pop(i - 1)
                i -= 1
        else:
            i += 1
    i = 0
    while i < len(t):
        if t[i] == "#":
            if i == 0:
                t.pop(i)
            else:
                t.pop(i)
                t.pop(i - 1)
                i -= 1
        else:
            i += 1
    return s == t
