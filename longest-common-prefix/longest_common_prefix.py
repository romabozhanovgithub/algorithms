from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    res = ""
    
    for i in range(len(strs[0])):
        for j in range(len(strs)):
            if len(strs[j]) - 1 >= i:
                if strs[0][i] != strs[j][i]:  
                    return res
                continue
            return res
        res += strs[0][i]
    return res
