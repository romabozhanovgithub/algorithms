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


def preorderV1Recursive(root: Node) -> List[int]:
    res = []
        
    def get_preorder(root: Node, res: List[int]) -> None:
        if root:
            res.append(root.val)
            if root.children:
                for child in root.children:
                    get_preorder(child, res)
    
    get_preorder(root, res)
    return res


def preorderV2Iterative(root: Node) -> List[int]:
        if root is None:
            return []

        stack = [root]
        output = []

        # Till there is element in stack the loop runs
        while stack:
            #pop the last element from the stack and store it into temp
            temp = stack.pop()

            # append the value of temp to output
            output.append(temp.val)

            # add the children of the temp into the stack in reverse order
            # children of 1 = [3,2,4], if not reveresed then 4 will be popped out first from the stack.
            # if reversed then stack = [4,2,3]. Here 3 will pop out first
            # This continues till the stack is empty
            if temp.children:
                stack.extend(temp.children[::-1])
        return output
