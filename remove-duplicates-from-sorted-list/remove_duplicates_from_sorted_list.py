from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return head

    prev = head
    curr = head.next
    while curr:
        if curr.val == prev.val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return head
