from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNodeV1(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Put every node into an array A in order. Then the middle node
    is just A[A.length // 2], since we can retrieve each node by
    index. We can initialize the array to be of length 100,
    as we're told in the problem description that the input
    contains between 1 and 100 nodes

    Time: O(n)
    Space: O(n)
    """
    
    lst = []
    while head is not None:
        lst.append(head)
        head = head.next
    
    return lst[len(lst) // 2]


def middleNodeV2(head: ListNode) -> ListNode:
    """
    When traversing the list with a pointer slow, make another pointer
    fast that traverses twice as fast. When fast reaches the end of the
    list, slow must be in the middle

    Time: O(n)
    Space: O(1)
    """

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
