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


def preorder(root: Node) -> List[int]:
    pass

