from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: "ListNode" = next


def reverseListIterativeV1(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head
    linked_list = []
    node = head
    while node is not None:
        linked_list.append(node)
        node = node.next
    for i in range(1, len(linked_list)):
        linked_list[-i].next = linked_list[-i - 1]
    linked_list[0].next = None
    return linked_list[-1]


def reverseListIterativeV2(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    temp = head
    while temp:
        # store the next node
        next = temp.next
        # reverse the direction of temp node's next pointer
        temp.next = prev
        # set prev node to temp node
        prev = temp
        # set temp node to next node
        temp = next

    # return the prev node which is now the head of the reversed linked list
    return prev


def reverseListRecursive(head: Optional[ListNode]) -> Optional[ListNode]:
    def dfs(node: ListNode, prev: ListNode):
        # if the next node is None, it means the node is the last node of the linked list
        if node.next == None:
            # reverse the direction of node's next pointer
            node.next = prev
            # return the node
            return node
        # store the next node
        next = node.next
        # reverse the direction of node's next pointer
        node.next = prev
        # call the dfs function recursively with next node and node
        return dfs(next, node)

    if head == None:
        return None
    # return the result of dfs function which is now the head of the reversed linked list
    return dfs(head, None)
