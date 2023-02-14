"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside
the square brackets is being repeated exactly k times. Note that k is
guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra
white spaces, square brackets are well-formed, etc. Furthermore, you may
assume that the original data does not contain any digits and that digits
are only for those repeat numbers, k. For example, there will not be input
like 3a or 2[4].

The test cases are generated so that the length of the output will never
exceed 105.
"""


def decodeStringV1Recursive(s: str) -> str:
    res = ""
    i = 0
    while i < len(s):
        if s[i].isdigit():
            j = i + 1
            while s[j].isdigit():
                j += 1
            k = int(s[i:j])
            i = j + 1
            cnt = 1
            j = i
            while cnt > 0:
                if s[j] == "[":
                    cnt += 1
                elif s[j] == "]":
                    cnt -= 1
                j += 1
            res += k * decodeStringV1Recursive(s[i:j - 1])
            i = j
        else:
            res += s[i]
            i += 1
    return res


def decodeStringV2Iterative(s: str) -> str:
    stack = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            j = i + 1
            while s[j].isdigit():
                j += 1
            stack.append(int(s[i:j]))
            i = j
        elif s[i] == "[":
            stack.append("[")
            i += 1
        elif s[i] == "]":
            tmp = ""
            while stack[-1] != "[":
                tmp = stack.pop() + tmp
            stack.pop()
            k = stack.pop()
            stack.append(k * tmp)
            i += 1
        else:
            stack.append(s[i])
            i += 1
    return "".join(stack)
