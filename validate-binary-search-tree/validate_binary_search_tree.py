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
