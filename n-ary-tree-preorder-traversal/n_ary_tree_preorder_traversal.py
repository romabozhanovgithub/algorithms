"""
N-ary Tree Preorder Traversal

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
"""


from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def preorderV1(root: Node) -> List[int]:
    res = []
        
    def get_preorder(root: Node, res: List[int]) -> None:
        if root:
            res.append(root.val)
            if root.children:
                for child in root.children:
                    get_preorder(child, res)
    
    get_preorder(root, res)
    return res
