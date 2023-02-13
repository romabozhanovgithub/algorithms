"""
Given an array of strings words and an integer k,
return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest.
Sort the words with the same frequency by their lexicographical order.
"""


from typing import List


def topKFrequent(words: List[str], k: int) -> List[str]:
    d = {}
    for word in words:
        if word not in d:
            d[word] = 0
        d[word] += 1

    l = list(d.items())
    l.sort(key=lambda x: (-x[1], x[0]))
    return [i[0] for i in l[:k]]
