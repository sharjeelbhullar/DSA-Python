# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # Temporarily store the next node
            curr.next = prev       # Reverse the current node's pointer
            prev = curr            # Move prev to current
            curr = next_node       # Move curr to next node
        
        # At the end, prev will be the new head
        return prev