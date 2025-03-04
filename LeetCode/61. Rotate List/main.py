# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find the length of the linked list
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        # Step 2: Calculate the effective number of rotations
        k = k % length
        if k == 0:
            return head  # No rotation needed if k % length is 0
        
        # Step 3: Make the list circular by connecting the tail to the head
        current.next = head
        
        # Step 4: Find the new tail (the node at position n - k % n - 1)
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
        
        # Step 5: Find the new head (the node after the new tail)
        new_head = new_tail.next
        new_tail.next = None  # Break the circular link to finish the rotation
        
        return new_head