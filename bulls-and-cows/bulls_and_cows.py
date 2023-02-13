"""
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what
the number is. When your friend makes a guess, you provide a hint
with the following info:
    The number of "bulls", which are digits in the guess that are
in the correct position.
    The number of "cows", which are digits in the guess that are in
your secret number but are located in the wrong position. Specifically,
the non-bull digits in the guess that could be rearranged such that they
become bulls.

Given the secret number secret and your friend's guess guess, return the hint
for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is
the number of cows. Note that both secret and guess may contain duplicate digits.
"""


def getHint(secret: str, guess: str) -> str:
    """
    >>> getHint("1807", "7810")
    '1A3B'
    >>> getHint("1123", "0111")
    '1A1B'
    >>> getHint("1", "0")
    '0A0B'
    >>> getHint("1", "1")
    '1A0B'
    """
    
    bulls = 0
    cows = 0
    secret_dict = {}
    guess_dict = {}
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
        else:
            secret_dict[secret[i]] = secret_dict.get(secret[i], 0) + 1
            guess_dict[guess[i]] = guess_dict.get(guess[i], 0) + 1
    for key in guess_dict:
        if key in secret_dict:
            cows += min(guess_dict[key], secret_dict[key])
    return f"{bulls}A{cows}B"
