"""
You are given an array of integers stones where stones[i] is the weight
of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest
two stones and smash them together. Suppose the heaviest two stones have
weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has
new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left,
return 0.
"""


from typing import List


def lastStoneWeightSortAndInsertV1(stones: List[int]) -> int:
    """
    Sort stones and insert them back into the list
    """

    while len(stones) > 1:
        stones.sort()
        y = stones.pop()
        x = stones.pop()
        if x != y:
            stones.append(y - x)
    return stones[0] if stones else 0


def lastStoneWeightSortAndInsertV2(stones: List[int]) -> int:
    stones.sort()

    while stones:
        y = stones.pop()
        if not stones:
            return y
        x = stones.pop()
        if x != y:
            stones.append(y - x)
            stones.sort()
    return 0


def lastStoneWeightHeap(stones: List[int]) -> int:
    """
    Use a heap to keep track of the heaviest stone
    """
    import heapq

    stones = [-stone for stone in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        y = heapq.heappop(stones)
        x = heapq.heappop(stones)
        if x != y:
            heapq.heappush(stones, y - x)
    return -stones[0] if stones else 0
