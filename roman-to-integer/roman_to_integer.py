def romanToInt(s: str) -> int:
    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    prev = s[-1]
    res = romans[prev]
    
    for i in range(-2, -(len(s) + 1), -1):
        if romans[s[i]] < romans[prev]:
            res -= romans[s[i]]
            continue    
        
        res += romans[s[i]]
        prev = s[i]
        
    return res
