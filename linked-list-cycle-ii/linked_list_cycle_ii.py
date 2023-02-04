from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    - Slow moves 1 step at a time, fast moves 2 steps at a time.
    - When slow and fast meet each other, they must be on the cycle:
        - x denotes the length of the linked list before starting the circle
        - y denotes the distance from the start of the cycle to where slow and fast met
        - C denotes the length of the cycle
        - When they meet, slow traveled (x + y) steps while fast traveled 2 * (x + y) steps,
        and the extra distance (x + y) must be a multiple of the circle length C:
            - note that x, y, C are all lengths or the number of steps need to move.
            - head, slow, fast are pointers.
            - head moves x steps and arrives at the start of the cycle.
    - So we have x + y = N * C, let slow continue to travel from y and after x more steps,
    slow will return to the start of the cycle.
    - At the same time, according to the definition of x, head will also reach the start of
    the cycle after moving x steps.
    - So if head and slow start to move at the same time, they will meet at the start of the
    cycle, that is the answer


    - Let the Fast and Slow meet.
    - Calculate the length of the cycle from that point (keep increasing Fast untill it meets with Slow again and count), assume the length is C.
    - In a separate loop, from the beggining, give Fast a head start of length C.
    - Loop until fast and slow meet and they will meet at the start of the cycle. Because Fast was cycle length ahead.

    If you see carefully in the solution which OP provided here, when Fast and Slow meet,
    Slow has covered, distance x+y and Fast has covered distance (x+C+y). This means that
    Fast has covered C distance more than Slow. Which is same the point as having a head
    start of C from the Slow. Which is how the obvious solution works hence this works


    Time: O(n)
    Space: O(1)
    """

    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            break
    else:
        return None  # if not (fast and fast.next): return None
        
    while head != slow:
        head, slow = head.next, slow.next
    return head
