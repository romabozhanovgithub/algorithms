from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBSTV1Recursive(root: Optional[TreeNode]) -> bool:
    def dfs(node, upper, lower):
        if not node:
            return True
        elif node.val >= upper or node.val <= lower:
            return False
        else:
            return dfs(node.left, node.val, lower) and dfs(node.right, upper, node.val)
    return dfs(root, float('inf'), float('-inf'))


def isValidBSTV2Iterative(root: Optional[TreeNode]) -> bool:
    stack = [(root, float('inf'), float('-inf'))]
    while stack:
        node, upper, lower = stack.pop()
        if not node:
            continue
        elif node.val >= upper or node.val <= lower:
            return False
        else:
            stack.append((node.left, node.val, lower))
            stack.append((node.right, upper, node.val))
    return True
