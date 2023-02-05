"""
Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderV1Recursive(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    result = []

    def helper(node, level):
        if len(result) == level:
            result.append([])

        result[level].append(node.val)

        if node.left:
            helper(node.left, level + 1)
        if node.right:
            helper(node.right, level + 1)

    helper(root, 0)
    return result


def levelOrderV2Iterative(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    queue = [root]
    result = []
    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)
    return result
