"""
Given the root of a binary tree, return the zigzag level order
traversal of its nodes' values. (i.e., from left to right, then
right to left for the next level and alternate between).
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    queue = [root]
    result = []
    zigzag = 0

    while queue:
        level = []
        zigzag += 1

        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if zigzag % 2 == 0:
            result.append(level[::-1])
        else:
            result.append(level)
    return result
