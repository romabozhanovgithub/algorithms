def strStr(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    
    return haystack.find(needle)
