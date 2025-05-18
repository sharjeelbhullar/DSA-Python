# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy head to simplify edge cases
        dummy = ListNode(0)
        current = head

        while current:
            # At each iteration, prev points to the start of the sorted list
            prev = dummy
            next_node = current.next  # Save the next node

            # Find the correct spot to insert current node
            while prev.next and prev.next.val < current.val:
                prev = prev.next

            # Insert current between prev and prev.next
            current.next = prev.next
            prev.next = current

            # Move to the next node
            current = next_node

        return dummy.next