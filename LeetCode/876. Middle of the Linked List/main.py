# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        
        # Move fast two steps and slow one step at a time
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # When fast reaches the end, slow will be at the middle
        return slow