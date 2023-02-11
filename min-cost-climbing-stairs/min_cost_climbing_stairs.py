"""
You are given an integer array cost where cost[i] is the cost of ith step on
a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""


from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    """Return the minimum cost to reach the top of the floor."""

    if len(cost) == 2:
        return min(cost)
    for i in range(2, len(cost)):
        cost[i] += min(cost[i - 1], cost[i - 2])
    return min(cost[-1], cost[-2])
