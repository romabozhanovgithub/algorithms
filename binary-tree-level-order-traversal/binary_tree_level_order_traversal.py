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
        # return an empty list if the root is None
        return []

    # result list to store the values at each level
    result: List[List[int]] = []

    def helper(node: TreeNode, level: int):
        """
        Helper function to traverse the tree in a pre-order fashion
        """

        # if we haven't encountered this level before, add a new list for it
        if len(result) == level:
            result.append([])

        # add the current node's value to the current level list
        result[level].append(node.val)

        if node.left:
            # if there is a left child, traverse it recursively, increasing the level by 1
            helper(node.left, level + 1)
        if node.right:
            # if there is a right child, traverse it recursively, increasing the level by 1
            helper(node.right, level + 1)

    # call the helper function with the root node and starting level 0
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
