"""
Given the root of a Binary Search Tree (BST), return the minimum
difference between the values of any two different nodes in the tree.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDiffInBSTV1Recursive(root: Optional[TreeNode]) -> int:
    res = [float("inf"), -1] # [min, prev]

    def minDiffInBST(root: Optional[TreeNode], res) -> int:
        if root.left:
            minDiffInBST(root.left, res)
        if res[1] != -1:
            res[0] = min(res[0], root.val - res[1])
        res[1] = root.val
        if root.right:
            minDiffInBST(root.right, res)
        return res[0]
    return minDiffInBST(root, res)


def minDiffInBSTV2Iterative(root: Optional[TreeNode]) -> int:
    res = [float("inf"), -1] # [min, prev]
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if res[1] != -1:
            res[0] = min(res[0], root.val - res[1])
        res[1] = root.val
        root = root.right
    return res[0]
