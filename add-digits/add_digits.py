def addDigits(num: int) -> int:
    while num > 9:
        num = num // 10 + num % 10
        
    return num
