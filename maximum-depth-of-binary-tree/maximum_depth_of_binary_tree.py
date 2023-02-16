"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along
the longest path from the root node down to the farthest leaf node.
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepthV1Recursive(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + max(maxDepthV1Recursive(root.left), maxDepthV1Recursive(root.right))
